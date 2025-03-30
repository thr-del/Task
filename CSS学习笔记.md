# CSS学习笔记

## 1. CSS介绍

- 定义：是一种于用于定义网页外观和布局的样式语言。

- 作用：为页面提供丰富的样式，包括字体、颜色、布局等，让页面更美观、结构更清晰。

- 基本语法：

```
选择器{
	属性1：属性值1；
	属性2：属性值2；
}
```

- 基本规则：

  - 一个选择器的声明中可以包含多条属性。

  - 声明中的每一行属性后需以分号;结尾。

  - 声明中的属性和值以“键值对”的形式出现。

- 导入方式
  - 内联样式
    把CSS样式直接放在HTML标签中，在style属性中直接定义样式。
  - 内部样式表
    在<head>标签中添加<style>标签来定义样式。
  - 外部样式表
    先在外部的CSS文件中定义样式，然后在HTML文档的<head>标签里添加<link>标签，把CSS文件链接到这个HTML文档中。

​              三种导入方式的优先级：内联样式>内部样式表>外部样式表

## 2.CSS选择器

- #### 元素选择器

```
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8" />
    <title>title</title>
    <style>
    h1 {
    color:red;
    }      
    </style>
</head>
<body>
   <h1>这是元素选择器</h1>
</body>
</html>
```

- #### 类选择器

```
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8" />
    <title>title</title>
    <style>
   .highlight {
   background-color:red;
   }
        
    </style>
</head>
<body>
    <h1 class="highlight">这是类选择器</h1>
</body>
</html>
```

- #### ID选择器

```
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8" />
    <title>title</title>
    <style>
   #header {
   font-size=35px;
   } 
    </style>
</head>
<body>
    <h1 id="header">这是ID选择器</h1>
</body>
</html>
```

- #### 通用选择器

```
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8" />
    <title>title</title>
    <style>
   * {
   font-family='KaiTi';
   }
    </style>
</head>
<body>
    <h1 class="highlight">这是类选择器</h1>
    <h2 id="QWE">这是一个通用选择器</h2>
</body>
</html>
```



- #### 子元素选择器

```
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8" />
    <title>title</title>
    <style>
   .father > .son{
    color: #000;
   }

    </style>
</head>
<body>
    <div class="father">
    <p class="son">这是一个子元素选择器</p>
    </div>
</body>
</html>
```

- #### 后代选择器

```
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8" />
    <title>title</title>
    <style>
   .father > .son{
    color: #000;
   }
   
   .father p{
   color:brown;
   font-size:larger;
   }

    </style>
</head>
<body>
    <div class="father">
    <p class="son">这是一个子元素选择器</p>
    <div>
    <p class="grandson">这是一个后代选择器示例</p>
    </div>
    </div>
</body>
</html>
```

- #### 兄弟选择器

```
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8" />
    <title>title</title>
    <style>
    h1 + p {
    background-color:red;
    }
    </style>
</head>
<body>
  <p>这是一个p标签</p>
  <h1>这是一个相邻兄弟选择器示例</h1>
  <p>这是另一个p标签</p>
</body>
</html>
```



- #### 伪类选择器

```
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8" />
    <title>title</title>
    <style>
    #element:hover{
    background-color:red;
    }
    </style>
</head>
<body>
  <h1 id="element">这是一个伪类选择器示例</h1>
</body>
</html>
```



##  3.CSS常见属性

#### 1.布局相关

- **display **

​       控制元素的选择类型

```
.block { display: block; }   /* 块级元素 */
.inline { display: inline; } /* 行内元素 */
.flex { display: flex; }     /* 弹性盒子 */
.grid { display: grid; }     /* 网格布局 */
```

- **position**

​       定义元素的定位方式

```
.relative { position: relative; } /* 相对定位 */
.absolute { position: absolute; } /* 绝对定位 */
.fixed { position: fixed; }       /* 固定定位 */
.sticky { position: sticky; }     /* 粘性定位 */
```

- **flex**

```
.container {
  display: flex;
  justify-content: center; /* 水平对齐 */
  align-items: center;     /* 垂直对齐 */
  gap: 10px;              /* 子项间距 */
}
```

- **grid**

```
.container {
  display: flex;
  justify-content: center; /* 水平对齐 */
  align-items: center;     /* 垂直对齐 */
  gap: 10px;              /* 子项间距 */
}
```

#### 2.盒模型

- **width **/ **height**
  控制元素宽高

```
{ width: 100px; height: 200px; }
```

- **padding** / **margin**

  内边距和外边距

```
.box {
  padding: 10px;          /* 四个方向 */
  margin: 20px auto;      /* 上下20px，左右居中 */
}
```

- **border**

  边框样式

```
.border {
  border: 2px solid #333; /* 宽度、样式、颜色 */
  border-radius: 8px;     /* 圆角 */
}
```

- **box-sizing**

```
.box { box-sizing: border-box; } /* 包含 padding 和 border */
```

#### 3.文本样式

- **font-size/font-family**

  字体大小和类型

```
.text {
  font-size: 16px;
  font-family: Arial, sans-serif;
}
```

- **color**

  颜色

```
.text {
  color: #ff0000;
}
```

- **text-ailgn**

  对齐

```
.text {
  text-align: center;
}
```

- **line-height**

  行高

```
.text{line-height:3.30;}/*3.30倍数行高*/
```

- **text-decoration**

​       文本装饰

```
.link { text-decoration: underline; }
```

#### 4.背景

- **background-color**

  背景颜色

```
.bg-red { background-color: #ff0000; }
```

- **background-image**

  背景图片

```
.hero {
  background-image: url("image.jpg");
  background-size: cover; /* 覆盖整个区域 */
}
```

- **渐变背景**

```
.gradient {
  background: linear-gradient(to right, #ff6b6b, #4ecdc4);
}
```

#### 5.定位与层叠

- **z-index**

  控制层叠顺序

```
.modal { z-index: 999; } /* 置于顶层 */
```

- **top/bottom/right/left**

  定位偏移

```
.tooltip {
  position: absolute;
  top: 10px;
  left: 20px;
}
```

#### 6.其他属性

- **box-shadow**

  盒子阴影

```
.card { box-shadow: 2px 2px 10px rgba(0,0,0,0.1); }
```

****

- **opacity**

  透明度

```
。fade{ opacity:0.5;}
```

## 3. CSS盒子模型

文档中的每个元素都可以被看成是一个矩形的盒子，这个盒子包含了内容（content）、内边距（padding）、文本边框（border）和 外边距（margin）。



![IMG_5214(20250330-012930)](C:\Users\Tong\Downloads/IMG_5214(20250330-012930).PNG)



![IMG_5215(20250330-014014)](C:\Users\Tong\Downloads/IMG_5215(20250330-014014).PNG)

```
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>CSS盒子模型练习</title>
    <style>
        .box {
            width: 200px;        /* 内容区域宽度 */
            height: 150px;       /* 内容区域高度 */
            padding: 25px;       /* 内边距：内容与边框的间距 */
            border: 5px solid #ff6b6b;  /* 边框：宽度 样式 颜色 */
            margin: 30px;        /* 外边距：盒子与其他元素的间距 */
            background-color: #ffe66d;  /* 背景色填充内容+内边距区域 */
            
            box-sizing: content-box; /* 默认值：width=内容宽度 */
        }

        /* 对比不同box-sizing的盒子 */
        .border-box-example {
            box-sizing: border-box;  /* width=内容+padding+border的总和 */
            margin-top: 50px;      /* 外边距叠加效果示例 */
        }
    </style>
</head>
<body>
    <!-- 标准盒子模型 -->
    <div class="box">
        这是一个标准内容盒子
        （200px内容宽 + 25px*2内边距 + 5px*2边框 = 总宽度260px）
    </div>

    <!-- border-box对比盒子 -->
    <div class="box border-box-example">
        使用border-box的盒子
        （总宽度固定为200px，自动调整内容区域）
    </div>
</body>
</html>
```

**练习代码运行结果如图所示：**

![屏幕截图 2025-03-30 074112](C:\Users\Tong\Desktop\屏幕截图 2025-03-30 074112.png)

## 4.CSS布局方式

- **普通布局**

（元素按文档从默认规则从上到下，从左向右排列）

```
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Document</title>
</head>
<body>
    <div>块级元素1</div>
    <div>块级元素2</div>
    <span>行内元素1</span><span>行内元素2</span>
</body>
</html>
```



- **浮动布局**

元素通过 float 属性脱离文档流，实现左右浮动
**浮动的三大特性**

- 脱标：脱离标准流（当元素设置了浮动之后，元素就会脱离标准流的控制移动到指定的位置，浮动的盒子就不再保留原来所占的位置，就像漂浮在空中一样，脱离了原来的地面）。
- 一行显示：顶部对齐（如果多个盒子同时设置了浮动，那么他们就会按照属性值一行内显示，并且顶端对齐排列）。
- 具备行内块元素特性（不管原先是什么模式的元素，添加了浮动之后，都会具有行内块元素相似的特性）。
  浮动和行内块的区别：
  浮动的元素是相互贴靠在一起的，不会有缝隙，如果父级宽度装不下这些浮动的盒子，多出去的盒子就会另起一行，而我们如果使用行内块元素的话，它彼此之间是由缝隙的，不如浮动这么方便。

**浮动的典型应用：**让多个块级元素在同一行内排列显示。

**浮动注意：**浮动是相对于父元素浮动，只会在父元素的内部移动。

**浮动的清除**：常见的清除浮动方式有两种：在浮动元素的父元素中添加overflow属性，指定值为hidden；
伪元素清除法：在浮动标签的父元素添加一个伪元素。

```
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>CSS浮动布局对比示例</title>
    <style>
        /* 基础样式 */
        .container {
            background: #b3e5fc;
            border: 3px solid #1565c0;
            margin: 20px 0;
        }
        .box {
            width: 100px;
            height: 100px;
            padding: 10px;
            color: #fff;
        }
        .left {
            background: #e91e63;
            float: left;
        }
        .right {
            background: #009688;
            float: right;
        }

        /* 清除浮动方法 */
        .method1 { height: 120px; } /* 固定高度法 */
        .method2 { overflow: hidden; } /* overflow法 */
        .method3::after { /* clearfix法 */
            content: "";
            display: table;
            clear: both;
        }
    </style>
</head>
<body>
    <!-- 未清除浮动的示例 -->
    <div class="container">
        <div class="box left">左浮动元素</div>
        <div class="box right">右浮动元素</div>
    </div>
    <p>父容器高度塌陷 → 边框无法包裹浮动元素</p>

    <!-- 方法1：固定高度 -->
    <div class="container method1">
        <div class="box left">左浮动</div>
        <div class="box right">右浮动</div>
    </div>
    <p>方法1：通过固定高度强制撑开容器（不灵活）</p>

    <!-- 方法2：overflow清除 -->
    <div class="container method2">
        <div class="box left">左浮动</div>
        <div class="box right">右浮动</div>
    </div>
    <p>方法2：overflow:hidden 创建BFC（可能裁剪内容）</p>

    <!-- 方法3：clearfix清除 -->
    <div class="container method3">
        <div class="box left">左浮动</div>
        <div class="box right">右浮动</div>
    </div>
    <p>方法3：clearfix伪元素清除（推荐最佳实践）</p>
</body>
</html>
```

**示例效果如图所示：**

![屏幕截图 2025-03-30 083208](C:\Users\Tong\Desktop\屏幕截图 2025-03-30 083208.png)

- **弹性布局**

​    一维布局，灵活实现水平或垂直居中对齐，适合导航栏等场景。

```
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>简单弹性布局</title>
    <style>
        .container {
            display: flex;        /* 启用弹性布局 */
            gap: 10px;           /* 项目间距 */
            background: #e0e0e0;
            padding: 20px;
        }

        .item {
            flex: 1;             /* 等分剩余空间 */
            padding: 30px;
            background: #2196F3;
            color: white;
            text-align: center;
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="item">项目1</div>
        <div class="item">项目2</div>
        <div class="item">项目3</div>
    </div>
</body>
</html>
```



![屏幕截图 2025-03-30 094403](C:\Users\Tong\Desktop\屏幕截图 2025-03-30 094403.png)

- **网格布局**

​    二维布局，可同时精确控制行和列，适合复杂页面设计。

```
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>基础网格布局</title>
    <style>
        .container {
            display: grid;  /* 启用网格布局 */
            grid-template-columns: repeat(3, 1fr); /* 3等宽列 */
            gap: 15px;      /* 网格间隙 */
            padding: 20px;
            background: #f0f0f0;
        }

        .item {
            background: #2196F3;
            color: white;
            padding: 30px;
            text-align: center;
            border-radius: 5px;
        }

        /* 响应式布局：小屏幕时改为2列 */
        @media (max-width: 600px) {
            .container {
                grid-template-columns: repeat(2, 1fr);
            }
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="item">1</div>
        <div class="item">2</div>
        <div class="item">3</div>
        <div class="item">4</div>
        <div class="item">5</div>
        <div class="item">6</div>
    </div>
</body>
</html>
```

![屏幕截图 2025-03-30 094845](C:\Users\Tong\Desktop\屏幕截图 2025-03-30 094845.png)

## 5.CSS定位

定位是使用 CSS的position 属性精确控制元素位置，让元素按照特定模式定位到页面中的某个位置的方法。

常见定位：

- **相对定位：**相对于元素在文档流中的正常位置进行定位。
- **绝对定位**：相对于其最近的已定位的父级元素进行定位，不占据文档流的位置。
- **固定定位**：相对于浏览器窗口进行定位。不占据文档流固定在屏幕上的位置，不随滚动而移动。
- **定位布局与浮动布局优缺点**：浮动布局灵活性高，但不易控制。定位布局控制精准，但不够灵活。

```
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>CSS定位基础示例</title>
    <style>
        /* 基础容器样式 */
        .container {
            height: 200px;
            margin: 50px;
            border: 2px solid #333;
            position: relative; /* 为绝对定位提供参照 */
        }

        /* 定位演示盒子 */
        .box {
            width: 80px;
            height: 80px;
            color: white;
            text-align: center;
            line-height: 80px;
        }

        /* 相对定位 */
        .relative-box {
            background: #e91e63;
            position: relative;
            top: 20px;
            left: 50px;
        }

        /* 绝对定位 */
        .absolute-box {
            background: #2196F3;
            position: absolute;
            bottom: 10px;
            right: 10px;
        }

        /* 固定定位 */
        .fixed-box {
            background: #4CAF50;
            position: fixed;
            top: 20px;
            right: 20px;
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="box relative-box">相对定位</div>
        <div class="box absolute-box">绝对定位</div>
    </div>
    <div class="box fixed-box">固定定位</div>

    <div style="height: 2000px"> <!-- 创建滚动空间 -->
        <p>滚动页面观察固定定位元素的位置</p>
    </div>
</body>
</html>
```







![屏幕截图 2025-03-30 100152](C:\Users\Tong\Desktop\屏幕截图 2025-03-30 100152.png)







