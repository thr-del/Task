# Python爬虫基础

##  一.步骤解析

#### 1.获取网页内容

- 通过代码给服务器发送请求==>返回网页上的内容

- ***所需知识：1.HTTP：通过发送HTTP请求来获得网页内容***

  ​                   ***2.Requests库（或urllib库） :用Python代码发送HTTP请求***

  ​                  ***3.Selenium：自动化日常 Web任务，抓取动态页面***

#### 2.解析网页内容

- 对网页内容进行解析==>提取想要的数据

- ***所需知识：1.HTML：发送请求后所得内容通常为HTML格式***

  ​                   ***2.Beautiful Soup库 :解析获得的HTML内容，提取我们真正想要的信息***

#### 3.储存或分析数据(取决于具体需求)

- 储存：例：为了收集数据==>把数据储存进数据库。
- 分析数据：例：为了分析数据趋势==>把数据做成可视化列表。

***

## 二.HTTP

#### 1.定义：HTTP(超文本传输协议)：是一种客户端和服务器之间的请求-响应协议。

#### 2.HTTP请求

以下以一个完整的HTTP请求为例：

~~~
POST/user/info HTTP/1.1              请求行

Host:www.example.com
User-Agent:curl/7.77.0               请求头
Accpet:*/*

{
"username":"童汇然",
"email":"baymax_0820@qq.com"         请求体
}
~~~

#####  (1) 请求行

~~~
POST/user/info HTTP/1.1     
POST:方法类型
/user/info：资源路径
HTTP/1.1：协议版本
~~~

**方法类型(主要)**

- GET：主要用于获得数据

  - 安全：会对服务器上的数据进行修改。

  - 幂等：多次请求的结果相同。

  - 请求参数通常为**查询参数（通过URL的查询字符串传递）**。

    ~~~
    GET /search?query=Python&sort=popular HTTP/1.1    
    Host: www.example.com
    ~~~

- POST:主要用于创建数据

  - 不是幂等方法，多次请求可能会导致不同的结果（例如多次提交表单）。

  - 请求参数通常为**请求体参数（数据通常包含在请求体中）**。

    ~~~
    POST /submit HTTP/1.1
    Host: www.example.com
    Content-Type: application/x-www-form-urlencoded
    Content-Length: 27
    
    name=John&age=30
    
    ~~~

- PUT：主要用于更新现有数据。
  - 幂等。
  - 请求参数通常为**请求体参数（数据通常包含在请求体中）**。
- DELETE：主要用于删除数据。
  - 幂等。

*补充*：

请求参数分为：

1.查询参数：是URL的一部分，位于路径之后，以?开始，后面跟着一系列的键值对，键值对之间用&分隔。

2.请求体参数:通常用于POST、PUT和PATCH请求，因为这些方法需要向服务器提交数据。

3.路径参数：用于标识特定的资源，例如获取、更新或删除某个资源。通常以 / 分隔，例如  /users/123  ，其中123是路径参数。

**资源路径**

- 指明了你要访问服务器的哪个资源。
- 例：www.douban.com/movie/top250 中/movie/top250就是我们要找的资源路径。

- 有时后面会加上查询参数。

##### (2) 请求头(包含一些给服务器的信息)

**Host(主机域名)**

- 主机域名结合请求行里的资源路径可以得到一个完整的网址，例：www.douban.com

**User-Agent(用于告知服务器客户端信息)**

- 例：User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36    从中能获得的信息有：
  - 浏览器：Chrome
  - 版本：91.0.4472.124
  - 操作系统：Windows 10

- 如何查看User-Agent：打开浏览器的开发者工具（通常可以通过按F12或右键点击页面并选择“检查”来打开），在“网络”（Network）标签页中，查看请求的“请求头”（Request Headers）部分。记得刷新。

- 爬虫可以伪装成普通浏览器的User-Agent，以避免被服务器屏蔽。

**Accept(告诉服务器客户端想要接受的数据类型)**

例：

- 接受HTML： text/html
- 接受JSON：  application/json
- 接受HTML和JSON:  text/html,application/json
- 接受任意类型：* / *

##### （3）请求体

- 通常用于POST、PUT请求，因为这些方法需要向服务器提交数据。
- 请求体可以包含多种格式的数据，具体取决于请求头中的 Content-Type。
  -  application/x-www-form-urlencoded：键值对形式，类似于查询字符串。
  -  application/json：JSON格式，适合复杂数据结构。
  -  multipart/form-data ：用于文件上传，支持文件和文本数据的混合。
  -  text/plain：纯文本格式。

#### 3.HTTP响应

例：

~~~
HTTP/1.1 200 OK                                状态行

Date:Sun,1 Jun 2025 00:00:00 GMT               响应头
Content-Type:text/html;charset=utf-8

<!DOCTYPE html>
...                                            响应体
</html>
~~~

##### （1）状态行

~~~
HTTP/1.1 200 OK
HTTP/1.1 协议版本
200      状态码
OK       状态消息
~~~

常见的状态码和状态消息如图：

<img src="C:\Users\Tong\Downloads/IMG_6914(20250713-102307).PNG" alt="IMG_6914(20250713-102307)" style="zoom:40%;" />

##### （2）响应头

~~~
Date:Sun,1 Jun 2025 00:00:00 GMT              
Content-Type:text/html;charset=utf-8

Date：生成响应的日期和时间
Content—Type：text/html：返回内容类型：返回html的文本
charset=utf-8：编码格式
~~~

##### （3）响应体

- 服务器想给客户端的数据内容。

***



##  三、Requests库

#### 1.requests库入门

- 在python中，我们用requests库进行网络请求、获取网页数据。
- 常见的爬虫一般分为两类：
  - HTML型：requests.get ()  -->  response.text
  - Json型：requests.post()  -->  response.json

#### 2.导入requests库

~~~python
import requests
~~~

#### 3.参看请求方式

- 打开浏览器，选择一个网页，右键“检查”，点击*网络*，刷新页面。
- 点击需要请求的网址。
- 查看标头。

<img src="C:\Users\Tong\Pictures\Screenshots\屏幕截图 2025-07-13 160050.png" alt="屏幕截图 2025-07-13 160050" style="zoom:50%;" />

#### 4.发送Get请求

- get基本语法：*requests.get(url, params=None，**kwargs)*

  - url：获取页面的url链接。

  - params：指在url中增加的参数。

  - **kwargs：指控制访问的参数，常用的包括headers(请求头)。

    

- **发送简单请求**

~~~python
import requests
r = requests.get (https://www.iqiyi.com/) 
print(r)
~~~

结果是<response  [200]>,说明请求成功。



- **发送带headers的请求**

我们尝试请求豆瓣首页

~~~
import requests
r = requests.get (https://www.douban.com/) 
print(r)
~~~

结果是<response  [418]>,说明请求失败。 为什么？

*绝大多数网站都具备一定的反爬能力，禁止爬虫大量地访问网站，以免给网站服务器带来压力。在爬虫中进行requests请求，很多时候，都需要添加请求头，不然服务器会认为是非法的请求，从而拒绝你的访问。*

~~~
import requests
r = requests.get (https://www.douban.com/) 
print(r.request.headers)   #添加请求头
~~~

但注意：headers中有一个属性为User-Agent。User-Agent告诉HTTP服务器，客户端使用的操作系统和浏览器的名称和版本，这是一个身份标识。**但如上述代码：requests库进行爬虫的User-Agent是'python-requests'，网站通过识别请求头中User-Agent信息来判断是爬虫访问网站，所以会请求失败。**

因此就需要重构User-Agent，将其**伪装成“浏览器”访问网站。**

如何伪装？：和上述查看请求方式一样，在标头界面的最底端有一个User-Agent：Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36 Edg/138.0.0.0。这是浏览器的身份标识。

![屏幕截图 2025-07-13 164036](C:\Users\Tong\Pictures\Screenshots\屏幕截图 2025-07-13 164036.png)

~~~python
import requests

headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36 Edg/138.0.0.0'
}

r = requests.get (https://www.douban.com/) 
print(r.request.headers=headers) #把定义的headers赋值给headers
~~~

结果是<response  [200]>,说明请求成功。

- **获取响应数据**
  - r.text:字符串类型的数据，一般网页数据为文本类用此属性。
  - r.content:二进制类型的数据，一般网页数据为文件时用此属性。
  - r.json:json数据解码，一般网页数据为json格式用此属性。

~~~
import requests
r = requests.get (https://www.douban.com/) 
print(r.text)
~~~

r.text乱码问题的解决

原因：计算机有不同的编码方式：ASCII编码、GBK编码、UTF-8编码。出现乱码的原因是用以一种错误的编码方式去解析语言。



![屏幕截图 2025-07-14 143135](C:\Users\Tong\Pictures\Screenshots\屏幕截图 2025-07-14 143135.png)



例：一般来说，在一个网站的标头中content-type中有charset字段，如charset=utf-8，此时用utf-8编码方式。

但在这个网站中：标头下的content-type中没有charset字段，则python默认为ISO-8859-1编码模式，无法解析中文，造成乱码。

解决方法:

```
r.encoding:请求头中的字符编码：没有就默认ISO-8859-1
r.apparent_encoding:猜测相应正文中的字符编码
```

方法一：

~~~
import requests
r = requests.get (https://www.douban.com/) 
r.encoding = "utf-8"
print(r.text)
~~~

方法二：

~~~
import requests
r = requests.get (https://www.douban.com/) 
r.encoding = r.apparent_encoding
print(r.text)
~~~

***

## 四. urllib入门

#### 1.用途

- 和Requests库一样用于处理与URL相关的操作，包括发送HTTP请求、解析 URL 等。
  - urllib.request:用于发送HTTP请求，获取网络资源。
  - urllib.parse:用于解析和构造URL。
  - urllib.error :用于处理urllib.request模块可能抛出的异常。

#### 2.和Requests库的关系

- requests内部使用urllib来处理底层的 HTTP 请求。
- requests提供了更高级的接口，简化了 urllib的使用。

- 使用 urllib ：不需要额外安装库，适合对性能要求极高的场景。但代码冗长。
- 使用requests ：适用于大多数需要发送 HTTP 请求的场景，代码简洁，功能丰富。

#### 3.基本用法

- **导入**

~~~
import urllib.request
import urllib.parse
~~~

- **发送GET请求**

构造请求：

~~~
url = "http://example.com"
response = urllib.request.urlopen(url)
~~~

读取响应内容：

~~~
data = response.read()
print(data）
~~~

添加请求头：通过urllib.request.Request()添加自定义请求头。

~~~
import urllib.request


url = "http://example.com"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}
req = urllib.request.Request(url, headers=headers)
response = urllib.request.urlopen(req)

data = response.read()
print(data)
~~~

## 五. BeautifulSoup库入门

#### 1.用途

- 一个用于解析HTML文档的Python库，适合进行Web数据抓取和解析，可以轻松地提取和操作HTML文档中的数据。

#### 2. 基本用法

例：以下是一个从一个网页https://www.example.com解析出来的HTML文档，

~~~、
<!DOCTYPE html>
<html>
<head>
    <title>示例页面</title>
</head>
<body>
    <h1>欢迎来到我的网站</h1>
    <p>这是一个示例段落。</p>
    <ul>
        <li>列表项1</li>
        <li>列表项2</li>
        <li>列表项3</li>
    </ul>
    <a href="https://www.example.com">链接</a>
</body>
</html>

~~~

如何用BeautifulSoup库得到想要的数据;

- **导入BeautifulSoup库**

~~~python
from bs4 import BeautifulSoup #从bs4模块中导入BeautifulSoup类
~~~

- **创建BeautifulSoup对象**

***基本格式***

~~~python
soup = BeautifulSoup(解析对象,解析器)
~~~

解析对象：是BeautifulSoup 需要解析的HTML内容。它可以是一个字符串，也可以是一个文件对象。

~~~
字符串：
response = requests.get(url)
html_doc = response.text

soup = BeautifulSoup(html_doc, 'lxml')
~~~

~~~
文件对象:
with open('example.html', 'r') as file:
    html_doc = file.read()

soup = BeautifulSoup(html_doc, 'html.parser')
~~~

解析器：是BeautifulSoup用来解析HTML的工具，常见的有以下几种。

(1)html.parser :纯python实现，不需要额外安装库。适合解析简单的HTML文档。速度较慢，容错性较低。

(2) lxml:需要安装lxml库。能够处理不规范的HTML文档。速度较快，容错性高。

(3) html5lib：需要安装html5lib库。能够处理不规范的HTML文档。速度较慢，容错性高。

以下是一个https://www.example.com的文档创建的完整BeautifulSoup对象

~~~python
import requests
from bs4 import BeautifulSoup

url = 'https://www.example.com'
response = requests.get(url)
html_doc = response.text

soup = BeautifulSoup(html_doc, 'html.parser')
~~~

- BeautifulSoup常见用法

  - 获取标题

    ~~~
    # 获取<title>标签的内容
    title = soup.title.text
    print(f"页面标题: {title}")
    
    运行结果：
    页面标题: 示例页面
    ~~~

  -  获取段落

    ~~~
    # 获取所有的<p>标签
    paragraphs = soup.find_all('p')
    for p in paragraphs:
        print(p.text)
    
    运行结果：
    这是一个示例段落。
    ~~~

  - 获取列表项

    ~~~
    # 获取所有的<li>标签
    list_items = soup.find_all('li')
    for item in list_items:
        print(item.text)
    
    运行结果：
    列表项1
    列表项2
    列表项3
    ~~~

  - 获取特定属性

    ~~~
    # 获取所有<a>标签
    links = soup.find_all('a')
    for link in links:
        print(link['href'])
    
    运行结果：
    https://www.example.com
    ~~~

  - 使用CSS选择器

    ~~~
    # 使用CSS选择器查找所有列表项
    list_items = soup.select('ul li')
    for item in list_items:
        print(item.text)
    
    运行结果：
    列表项1
    列表项2
    列表项3
    ~~~

  - 提取数据并保存

    ~~~
    # 提取所有列表项并保存到列表
    list_items = [item.text for item in soup.find_all('li')]
    print(list_items)
    
    运行结果：
    ['列表项1', '列表项2', '列表项3']
    ~~~

***

## 六.  Selenium入门

#### 1.用途

- 可以模拟用户操作（如点击、输入、滚动等）。
- 用于抓取动态生成的内容，例如通过 JavaScript 渲染的页面。
- 用于自动化日常 Web 任务，如自动登录、数据抓取、表单提交等。

#### 2.基本用法

- **导入**：从 Selenium 库中导入webdriver模块，使得你可以在代码中使用webdriver提供的功能来控制和操作 Web 浏览器。(ps: webdriver提供了创建和管理浏览器驱动程序的功能，支持多种浏览器，用于自动化测试和 Web 数据抓取。)

  ~~~
  from selenium import webdriver
  ~~~

- **初始化**：以Edge浏览器为例,初始化webdriver

  ~~~
  driver = webdriver.Edge()
  ~~~

- **打开网页**

  ~~~
  driver.get("https://www.example.com") #打开指定的网页
  ~~~

- **查找元素**

1.通过 ID 查找元素

~~~
element = driver.find_element("id", "element_id")
~~~

例:

~~~
search_box = driver.find_element("id", "kw") #查找搜索框
search_box.send_keys("geek") #send_keys：这是 WebElement 提供的一个方法，用于向元素发送键盘输入。
~~~

2.通过名称查找元素

~~~
element = driver.find_element("name", "element_name")
~~~

例：

~~~
search_button = driver.find_element("name", "geek")  #查找搜索按钮
search_button.click() #点击搜索按钮，执行搜索操作。
~~~

3.通过 CSS 选择器查找元素

~~~
element = driver.find_element("css selector", "css_selector")
~~~

例：

~~~
button = driver.find_element("css selector", "#myButton") #通过 CSS 选择器查找按钮
button.click()
~~~

- **页面操作**

1.设置窗口大小

~~~
driver.set_window_size(width, height) 
~~~

例：

~~~
driver.set_window_size(1920, 1080) #设置窗口大小为 1920x1080
~~~

2.最大/小化窗口

~~~
driver.maximize_window() # 最大化窗口
driver.minimize_window() # 最小化窗口
~~~

3.全屏窗口

~~~
driver.fullscreen_window() # 全屏窗口
~~~

- **等待页面加载**

使用 Selenium 进行自动化操作时，等待页面加载是一个常见的需求。Selenium 提供了两种主要的等待机制：隐式等待和显式等待。

1.**区别**：用**等待用餐比喻**来解释。假设你去餐厅吃饭，

你告诉服务员：“我最多等10分钟，不管菜有没有上齐，10分钟后我就要开始吃。” 这就是**隐式等待**。你设置了一个固定的时间，不管菜有没有准备好，时间到了就开始下一步操作。如果菜在10分钟内上齐了，你就可以开始吃；如果10分钟内菜没上齐，你会感到不耐烦并开始抱怨（抛出异常）。

你告诉服务员：“我要等我的肉完全熟透了再开始吃，不管需要多长时间。” 这就是**显式等待**。 你没有设置一个固定的时间，而是等待一个特定的条件。

2.**对比**：

隐式等待：

优点：简单，设置一次后对所有操作生效。

缺点：不够灵活，如果页面加载时间比设置的时间短，也会等待固定时间；如果页面加载时间比设置的时间长，就会抛出异常。

适用场景：适合页面加载时间比较稳定，元素查找操作不多的场景。

显式等待：

优点：灵活，可以根据具体的条件动态调整等待时间。

 缺点：需要更多的代码来实现，稍微复杂一些。

适用场景：适合页面加载时间不稳定，需要等待特定条件出现的场景。

3.**代码模式**

1.隐式等待

~~~
driver.implicitly_wait(seconds) # 设置隐式等待时间为 seconds 秒
~~~

例·：

~~~
driver.implicitly_wait(10)
~~~

2.显式等待

~~~PY
from selenium.webdriver.common.by import By
# By是一个模块，提供了多种定位元素的方式，如By.ID,可以使用这些定位方式来查找页面元素。
from selenium.webdriver.support.ui import WebDriverWait
# 导入WebDriverWait，可以帮助我们等待页面上的某个元素出现。
from selenium.webdriver.support import expected_conditions as EC
# 导入了expected_conditions并将其简称为EC，提供了一些预定义的条件，这些条件可以用来告诉 WebDriverWait等待什么。比如，你可以等待某个元素出现、某个元素可见、某个元素可点击等。


wait = WebDriverWait(driver, timeout)
#创建一个WebDriverWait对象，让它等待页面上的某个条件出现
element = wait.until(EC.presence_of_element_located((By.ID, "element_id")))
#在指定的timeout时间内，等待页面中出现id为element_id的元素。如果在timeout时间内找到了该元素，则将该元素赋值给变量element；如果时间到了还没有找到该元素，则报错。
~~~

- **页面导航**

1.前进和后退

~~~
driver.get("https://www.example.com")# 打开一个新的页面
driver.back() # 后退到上一个页面
driver.forward() # 前进到下一个页面
~~~

- 关闭浏览器

~~~python
driver.quit()# 关闭浏览器
~~~

接下来是一个完整的Selenium在Edge浏览器进行网页抓取和操作的代码

~~~py
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Edge()# 初始化 Edge WebDriver

driver.get("https://www.example.com")# 打开指定的网页

# 查找元素并操作
element = driver.find_element(By.ID, "element_id")
element.send_keys("example text")

# 点击按钮
button = driver.find_element(By.ID, "button_id")
button.click()

driver.implicitly_wait(10)# 等待页面加载

# 获取页面标题
title = driver.title
print(title)

# 获取页面源码
html_content = driver.page_source
print(html_content)

driver.quit()# 关闭浏览器
~~~



