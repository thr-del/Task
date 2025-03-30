# HTML学习笔记

## 一.HTML简介

### 1.什么是HTML

- HTML 指的是超文本标记语言: HyperText Markup Language
- HTML 不是一种编程语言，而是一种标记语言

- 标记语言是一套标记标签 

- HTML 使用标记标签来描述网页

### 2.HTML标签

- HTML 标签是由尖括号包围的关键词，比如 <html>

- HTML 标签通常是成对出现的

- 标签对中的第一个标签是开始标签，第二个标签是结束标签

- 开始和结束标签也被称为开放标签和闭合标签

### 3.HTML的网页化结构

![屏幕截图 2025-03-27 162650](C:\Users\Tong\Desktop\屏幕截图 2025-03-27 162650.png)

ps：只有白色的部分才能在网页上显示

## 二. HTML常用标签

###  1.文本标签

- 标题标签

 ```
 <h1>一级标题</h1> 
 <h2>二级标题</h2>
 <h3>三级标题</h3>
 <h4>四级标题</h4>
 <h5>五级标题</h5>
 <h6>六级标题</h6>
 ```

<h1>一级标题</h1>
<h2>二级标题</h2>
<h3>三级标题</h3>
<h4>四级标题</h4>
<h5>五级标题</h5>
<h6>六级标题</h6>

***

- 段落标签

```
<p>我爱geek</p>
```

<p>我爱geek</p>

***

- 注释标签

```
<!--注释内容-->
```

<!--我是geek-->

***



- 换行标签

```
<br>通常用于两端落之间
```

<p>我是geek</p><br><p>现在还不是</p>



***

- 分隔线标签

```
<hr>       等于markdown中的***
```

<p>我是geek</p><hr>



- 加粗

```
<b>内容</b>
```

<b>我是geek</b>

***

- 斜体

```
<i>内容</i>
```

<i>i love geek</i>

***

- 下划线

```
<u>内容</u>
```

<u>我是geek</u>

***

- 删除线

```
<s>内容</s>
```

<s>我不geek</s>

***

- 上标

```
<sup>内容</sup>
```

<p>这是一段话<sup>上标</sup></p>

- 下标

```
<sub>内容</sub>
```

<p>这是一段话<sub>下标</sub></p>



***

### 2. 链接标签

```
<a href="URL">
```

<a href="http://douyin.com">抖音</a>

***

### 3. 列表标签

- 有序列表标签

```
<ol>
    <li>有序列表元素1</li>          
    <li>有序列表元素2</li>
    <li>有序列表元素3</li>
</ol>
```

- 无序列表标签

```
<ul>
    <li>无序列表元素1</li>
    <li>无序列表元素2</li>
    <li>无序列表元素3</li>
</ul>
```

***

### 4. 表格标签

```
<table> 

<thead>                     <thead > 用于定义表格的标题部分<th > 
   <tr>
   <th>表头</th>
   </tr>
 </thead>
 
<tbody>                     <tbody > 用于定义表格的主体部分
    <tr>
    <td>表格</td>
    </tr>                   
    </tbody>
</table>
 
 tr：表示表格的一行。
 td：表示表格的数据单元格。
 th：表示表格的表头单元格。 
 
```



<table>
  <thead>
    <tr>
      <th>列标题1</th>
      <th>列标题2</th>
      <th>列标题3</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>行1，列1</td>
      <td>行1，列2</td>
      <td>行1，列3</td>
    </tr>
    <tr>
      <td>行2，列1</td>
      <td>行2，列2</td>
      <td>行2，列3</td>
    </tr>
  </tbody>
</table>

***

### 5，表单标签

HTML表单用于收集用户的输入信息。

```
<form> </form> 用于创建表单
action 属性定义了表单数据提交的目标 URL，method 属性定义了提交数据的 HTTP
```

```
<lable> </lable> 用于为表单元素添加标签，提高可访问性。
```

```
<input> </input> 元素是最常用的表单元素之一，它可以创建文本输入框、密码框、单选按钮、复选框等。type 属性定义了输入框的类型，id 属性用于关联 <label> 元素，name 属性用于标识表单字段。
```

```
<select> </select> 元素用于创建下拉列表>。
```

```
<option> </option>元素用于定义下拉列表中的选项。
```

#### 文本域

```
<input type="text"> 标签来设定，当用户要在表单中键入字母、数字等内容时，就会用到文本域。

<form>
name:<input type="text" name="name">
</form>
```

<form>
name:<input type="text" name="name">
</form>

#### 密码

```
<input type="password"> 来定义

<form>
Password: <input type="password" name="pwd">
</form>
```

<form>
Password: <input type="password" name="pwd">
</form>

#### 单选按钮

```
input type="radio"> 标签定义了表单的单选框选项

<form>
<input type="radio" name="sex" value="male">男<br>
<input type="radio" name="sex" value="female">女
</form>
```

<form action="">
<input type="radio" name="sex" value="male">男<br>
<input type="radio" name="sex" value="female">女
</form>

#### 复选框

```
<input type="checkbox"> 定义了复选框。复选框可以选取一个或多个选项
```

<form>
    <input type="checkbox" name="geek" value="geek">我喜欢geek
</form>

#### 提交

```
<input type="submit"> 定义了提交按钮。
```

<form><input type="submit" value="提交"></form>

***

### 6. 结构标签

结构标签是用于组织和布局页面内容，但没有明确语义（无法表达页面不同部分的功能和含义）的标签。常见的结构标签有<div>和<span>。

<table>
  <thead>
    <tr>
      <th> </th>
      <th>div</th>
      <th>span</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>默认样式</td>
      <td>为块级显示，会以块的形式占据可用空间</td>
      <td>为行内显示，它不会独占一行，只占据其内容的宽度</td>
    </tr>
    <tr>
      <td>作用</td>
      <td>它适合用于创建页面的大块结构，例如页面的主体区域、容器、布局等。</td>
      <td>它适合用于对文本或其他行内元素进行样式化、标记或包裹</td>
    </tr>
    <tr>
      <td>嵌套关系</td>
      <td>可以容纳其他块级元素和行内元素，包括其他的div和span元素。</td>
      <td>通常被用来包裹文本或其他行内元素，比如用来设置特定文本的样式</td>
      </tr>  
  </tbody>
</table>

***

### 7.结构性标签

结构性标签是不仅用于组织和布局页面内容，且具有明确语义（能表达页面不同部分的功能和含义）的标签。常见的结构性标签有<header>、<footer>、<main>、<aside>、<section>、<article>和<nav>。

```
<header>：定义页面的头部区域，通常包括标题、导航、Logo 等。
<footer>：定义页面的底部区域，通常包括版权信息、社交链接、联系信息等。
<main>：定义页面的主体区域，通常包括页面排除头部、底部和侧边栏的主要内容。
<aside>：定义页面主体内容相关的附加信息，通常包括广告、侧边栏和推荐文章等。
<section>：定义文档的章节或区域，通常表示页面内一个独立的内容模块或功能区块。
<article>：定义页面独立的内容块，通常包括博客文章、新闻报道等可以单独展示的内容。
<nav>：定义页面的导航区域，通常包括用于跳转的导航链接
```

***

### 8. 图片标签

```
<img src"URL” alt"当图片无法显示时的替代">
```

***

## 三.HTML的标签属性

### 1.基本语法

```
<标签 属性1=" "  属性2=" ">内容</标签>
```

### 2.属性介绍

- HTML 属性是定义标签行为和样式的重要工具。

- 属性为元素提供更多的信息。

### 3.基本规则

- 属性名不区分大小写。

- 每个标签都有一个或多个属性。

- 属性永远写在开始标签中。

### 4.常见属性

- id属性

为HTML元素指定唯一的标识符，用于在JavaScript和CSS中对元素进行操作和样式设置。

- class属性

用于为HTML元素指定一个或多个类名，多个类名之间用空格分隔。可以通过CSS选择器根据类名来为元素设置样式，也可以在JavaScript中根据类名来选择和操作一组元素。

- style属性

用于直接在HTML元素上设置样式，其值是CSS样式规则。

- title属性

为元素提供额外的提示信息，当鼠标悬停在元素上时，会显示该提示信息。

- lang属性

用于指定元素内容所使用的语言。

- href属性

主要用于<a>标签，指定链接的目标地址，可以是相对路径、绝对路径或完整的URL。

- src属性

用于<img>等标签，指定图像等资源的来源路径。

- width和height属性

用于设置元素的宽度和高度。

***

## 四.块级元素与行内元素

<table>
  <thead>
    <tr>
      <th> </th>
      <th>块级</th>
      <th>行内</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>显示方式</td>
      <td>独占一行</td>
      <td>与其他内容并排显示</td>
    </tr>
    <tr>
      <td>宽度</td>
      <td>默认占满父容器的宽度</td>
      <td>宽度由内容决定</td>
    </tr>
    <tr>
      <td>嵌套</td>
      <td>可以包含块级元素和行内元素</td>
      <td>只能包含行内元素</td>
      </tr>  
      <tr>
      <td>应用场景</td>
      <td>组织页面布局和分隔内容区域</td>
      <td>为局部内容添加样式或功能</td>
      </tr>
- CSS中，块级元素的默认 display 值是 block,可以通过 display: inline 转换为行内元素。
- CSS中，行内元素的默认 display 值是 inline,可以通过 display: block 转换为块级元素。

















