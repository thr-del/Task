# Web指纹基础

**目录：**

一.Web指纹的基本识别方法

二.Web指纹常用识别工具使用

​        (1) WhatWeb

​        (2) Wapplyzer

三.Web指纹识别对漏洞挖掘的意义



## 一.Web指纹的基本识别方法



我把Web指纹识别的过程分为三个阶段，并以一个简单的“查字典”的例子来抽象化这个过程

**起因**：**分析目标Web应用的特征**。（类似于遇到一个不认识的字，你首先要对这个字的偏旁，拼音等特征做一个分析，才能方便自己查字典）

**经过(重点)**：**特征提取与匹配**。（根据分析得到的信息，在字典例挨个对照着查）

**结果**：**识别其使用的CMS（内容管理系统）、框架、插件、服务器类型、版本号等信息**（等你查到了这个字，你才能知道这个字的用法等信息）

PS：等你找到了这个字的用法等信息，你才能知道这个字是否存在使用缺陷（**评估潜在的安全风险和漏洞。**）



#### 1.**起因:分析目标Web应用的特征**

如何分析Web应用的特征？类似于分析人的特征，可以从长相、心灵的多个角度分析一样。Web应用也可以从多个角度进行分析，以下是几个常见的角度：

- **HTTP头分析**

原理：检查HTTP响应头信息来识别服务器软件、内容管理系统（CMS）、Web框架、JavaScript库等。

例：

访问一个使用Nginx服务器的网站，响应头可能包含

~~~
Server: nginx/1.18.0
~~~

使用WordPress网站可能会在响应头中包含

~~~
X-Powered-By: WordPress
~~~

使用Spring框架的Java应用可能会在响应头中包含

~~~
X-Application-Context: spring
~~~

- **内容检索**

原理：内容检索涉及搜索HTML内容中的特定字符串或模式，以识别CMS、框架或其他Web应用。

例：

如果页面源代码中包含此代码，则表明该网站使用WordPress 6.0作为CMS。

~~~
<meta name="generator" content="WordPress 6.0" />
~~~

如果页面源代码中包含上述代码，则表明该网站使用Vue.js 2.6.14作为前端框架。

~~~
<script src="https://cdn.jsdelivr.net/npm/vue@2.6.14/dist/vue.min.js"></script>
~~~

- **文件分析**

原理：检查特定文件的存在和内容，如robots.txt、favicon.ico文件或动态加载的JavaScript文件。

例：

WordPress的默认图标MD5值是固定的，我们计算 favicon.ico文件的MD5值并与之比对，如果匹配，则可能是WordPress网站。

某些前端框架（如Vue.js、React.js）会在JavaScript文件中写入特定的代码片段，可以通过这些片段来识别使用的框架。

- **Cookie分析**

原理：检查HTTP响应中的Set-Cookie头，分析Cookie名称和值，以识别会话管理或用户跟踪机制。

例:

PHPSESSID 是PHP默认的会话管理Cookie名称。通过检测PHPSESSID  ，可以推断网站可能使用了PHP作为后端语言，并且使用了默认的会话管理机制。

~~~
Set-Cookie: PHPSESSID=123456789abcdef; path=/; HttpOnly
~~~

- **网络请求分析**

原理：捕获网络请求和响应，分析请求的URL、参数和响应数据，以识别API端点或服务。

例：

响应内容类型：Content-Type: application/json表明响应数据是JSON格式。

响应数据：返回的JSON数据包含用户信息，表明这是一个用户管理API。

~~~
HTTP/1.1 200 OK
Content-Type: application/json
{
  "users": [
    {"id": 1, "name": "geek"},
    ]
}
~~~

- **服务识别**

原理：识别运行在特定端口上的服务，如SMTP、FTP、SSH、数据库服务等。

例：

发送HTTP请求：连接到目标IP的80端口，发送一个简单的HTTP请求

~~~
GET / HTTP/1.1
Host: example.com
~~~

HTTP服务通常会返回类似以下的响应

~~~
HTTP/1.1 200 OK
Server: Apache/2.4.41 (Ubuntu)
~~~

响应头中包含Server字段，显示服务器软件名称（如   Apache  ）和版本信息。

- **自动化工具**

原理：使用自动化工具如WhatWeb、Wappalyzer等进行指纹识别。

例：

运行whatweb http://example.com，WhatWeb输出识别结果，如WordPress 5.5.3，表明网站使用WordPress 5.5.3作为CMS。



****

#### 2.**经过(重点)**：**特征提取与匹配**。



在上述那个”查字典“的例子中，”字典“本身就是一个巨大的汉字数据库。该数据库存储了大量的汉字即汉字的特征信息。

所以我们要进行特征提取和匹配的核心在于**指纹数据库的构建**：指纹数据库存储了大量Web应用的特征信息。工具通过将目标站点的特征与数据库中的记录进行比对，从而确定其使用的Web技术栈。

以下是一个简单的指纹数据库例子，这个数据库包含三种类型的指纹：HTTP头、HTML内容和文件哈希。

~~~~json
{
  "headers": {
    "nginx": [["Server", "nginx"]],
    "apache": [["Server", "Apache"]],
  },
  "content": {
    "wordpress": ["<!-- WordPress start -->", "<!-- WordPress end -->"],
    "joomla": ["<jdoctype 'script'>jQuery"]
  },
  "hashes": {
    "wordpress_favicon": "md5:d5:1234567890abcdef",
}

~~~~

这个指纹数据库的作用：

(1) HTTP头（headers）指纹：

nginx：识别Nginx服务器的指纹，通过检查HTTP响应头中的Server字段是否包含字符串nginx。

apache：识别Apache服务器的指纹，通过检查Server字段是否包含字符串Apache。

(2) HTML内容（content）指纹：

wordpress：识别WordPress CMS，通过搜索HTML内容中的特定注释<!-- WordPress start -->和<!-- WordPress end -->。

joomla：识别Joomla CMS，通过搜索包含jQuery库的<script>标签。

(3) 文件哈希（hashes）指纹：

wordpress_favicon：识别WordPress网站，通过下载并计算favicon.ico文件的MD5哈希值，与已知的哈希值  md5:d1234567890abcdef匹配。



***

#### 3.**结果**：**识别信息**

Web指纹识别技术通过分析目标Web应用的特征，可以识别以下关键信息：

- CMS（内容管理系统）

定义：用于管理和发布Web内容的软件系统，如WordPress、Joomla、Drupal等。

- 框架

定义：用于构建Web应用的软件框架，如React、Vue.js、Angular、Django、Flask等。

- 服务器类型

定义：运行Web应用的服务器软件，如Apache、Nginx、IIS等。

-  版本号

定义：软件的具体版本信息，如CMS、框架、插件、服务器等的版本号。

- 数据库类型和版本

定义：网站使用的数据库系统，如MySQL、PostgreSQL、MongoDB等。

- 编程语言

定义：用于开发Web应用的编程语言，如PHP、Python、JavaScript、Java等。

- Web服务器配置

定义：Web服务器的配置信息，如HTTP头部、响应代码、错误页面等。

- 会话管理机制

 定义：网站用于管理用户会话的机制，如Cookie、Token等。

***

## 二.Web指纹常用识别工具使用

#### 1.WhatWeb

介绍：一款基于Ruby的Web指纹识别工具，能够识别目标Web应用的CMS类型、框架、服务器版本、插件、脚本语言等关键信息。支持多种识别方式，包括HTTP头、HTML内容、Cookie、URL路径等。

<img src="C:\Users\Tong\Pictures\Screenshots\屏幕截图 2025-07-31 021213.png" alt="屏幕截图 2025-07-31 021213" style="zoom:75%;" />

**基本命令**

~~~
whatweb example.com
~~~

该命令会输出目标站点的基本指纹信息，如CMS类型、服务器、脚本语言、插件等。

举个例子：输入https://www.iqiyi.com会得到以下信息

![屏幕截图 2025-07-31 021731](C:\Users\Tong\Pictures\Screenshots\屏幕截图 2025-07-31 021731.png)

**指定端口扫描**

~~~
whatweb -p 8080 example.com
~~~

用于检测非标准端口（如8080）上的Web服务指纹。

**输出详细信息**

~~~
whatweb -v example.com
~~~

使用 `-v` 参数可以输出更详细的识别结果，包括匹配的插件名称和版本号。

**批量扫描**

~~~
whatweb -i targets.txt
~~~

其中 targets.txt 是一个包含多个域名或IP地址的文本文件，每行一个目标。

**自定义插件（用Ruby写）**

~~~ruby
Plugin.define "MyCMS" do
    match :body, /Powered by MyCMS/
    match :header, /X-Powered-By: MyCMS/
end
~~~

插件通常位于 `/usr/share/whatweb/plugins/` 路径下。每个插件为一个 `.rb` 文件，包含识别逻辑。此代码定义了一个名为 `MyCMS` 的插件，通过HTML内容和HTTP头中的关键字进行匹配。

***

#### 2.Wapplyzer

简介：Wapplyzer 是基于Node.js的Web指纹识别工具，其识别方式与WhatWeb类似，但依赖JSON格式的规则库进行匹配。

**基本使用**

~~~
wapplyzer http://example.com
~~~

该命令会输出目标站点的识别结果，包括使用的CMS、框架、服务器、JavaScript库等。

**输出JSON格式**

~~~
wapplyzer -j http://example.com
~~~

使用 -j 参数可以将结果输出为JSON格式，便于程序解析。

**使用自定义规则**

~~~
wapplyzer -c custom-rules.json http://example.com
~~~

其中 custom-rules.json 是一个自定义的识别规则文件，格式如下：

~~~json
{
    "MyCMS": {
        "url": "/",
        "html": "Powered by MyCMS",
        "headers": {
            "server": "MyCMS"
        }
    }
}
~~~

该规则定义了识别目标是否使用 MyCMS 的HTML关键字和HTTP头信息。

***

## 三.Web指纹识别对漏洞挖掘的意义

还是我刚刚的“查字典”的例子：等你找到了这个字的用法等信息，你才能知道这个字是否存在使用缺陷（**评估潜在的安全风险和漏洞。**）

#### 1.快速找到已知的漏洞

- 通过识别目标系统使用的CMS、框架、插件、服务器等的版本号，可以快速查找这些版本是否存在已知的安全漏洞。

例：如果识别出目标网站使用的是WordPress 5.2.0，而该版本已知存在SQL注入漏洞，那么可以立即针对该漏洞进行进一步的测试。

- 用识别到的版本号在漏洞数据库（比如CVE、NVD）里查找，看看有没有别人已经发现的漏洞。

#### 2.缩小攻击面

- 了解目标系统使用的技术栈（如PHP、MySQL、Apache等），可以缩小攻击面，集中精力挖掘这些技术栈中的已知漏洞。

例·：如果目标网站使用了PHP 7.2.10，而该版本已知存在多个安全漏洞，那么可以专注于这些漏洞的测试。

- 识别目标网站使用的插件和扩展，这些组件往往是安全漏洞的高发区。

####  3.提高漏洞挖掘效率

- Web指纹识别工具（如WhatWeb、Wappalyzer等）可以快速扫描目标网站，提供详细的技术栈信息。

- 过精确的技术栈和版本号识别，减少误报和漏报，提高漏洞挖掘的准确性。