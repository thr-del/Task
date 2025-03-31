# js学习笔记

## 一。js介绍

JS（JavaScript）是一种轻量级、解释型、面向对象的脚本语言，同时也是一种编程语言。

**基本用途**

- **客户端脚本：**用于在用户浏览器中执行，实现动态效果和用户交互。

- **网页开发：**与HTML和CSS协同工作，使网页具有更强的交互性和动态性。

- **后端开发：**使用Node.js,JavaScript也可以在服务器端运行，实现服务器端应用的开发。

**导入方式**

- 内联式:在HTML文档中直接嵌入JS代码，CSS代码是放在style标签内，而JS代码是放在head部分或body部分的script标签内。

- 外部连接：把JS代码，单独保存外部文件中，通过script标签的src属性引入HTML文档。

## 二.js相关语法

### 1. var（函数作用域）
```javascript
function demoVar() {
  var num = 10;
  if (true) {
    var num = 20;  // 覆盖外部的num
  }
  console.log(num); // 输出：20
}
demoVar();
```

### 2. let（块级作用域）
```javascript
function demoLet() {
  let num = 10;
  if (true) {
    let num = 20;  // 独立的num
  }
  console.log(num); // 输出：10
}
demoLet();
```

### 3. const（常量）
```javascript
const PI = 3.14;
// PI = 3.1415; // 报错！常量不可修改

const colors = ["red"];
colors.push("blue"); // 允许修改数组内容
console.log(colors); // 输出：["red", "blue"]
```

---

## 二、条件语句

### 1. if-else
```javascript
let age = 18;

if (age >= 18) {
  console.log("成年人");
} else {
  console.log("未成年人");
}
// 输出：成年人
```

### 2. else if
```javascript
let score = 85;

if (score >= 90) {
  console.log("优秀");
} else if (score >= 60) {
  console.log("及格");  // 输出：及格
} else {
  console.log("不及格");
}
```

---

## 三、循环语句

### 1. for循环
```javascript
for (let i = 1; i <= 3; i++) {
  console.log(i); 
}
// 输出：1 2 3
```

### 2. while循环
```javascript
let count = 3;
while (count > 0) {
  console.log(count);
  count--;
}
// 输出：3 2 1
```

### 3. break 和 continue
```javascript
// break跳出循环
for (let i = 1; i <= 5; i++) {
  if (i === 3) break;
  console.log(i);  // 输出：1 2
}

// continue跳过当前循环
for (let i = 1; i <= 5; i++) {
  if (i === 3) continue;
  console.log(i);  // 输出：1 2 4 5
}
```

---

## 

## 三.js数据类型

- **undefined和null**  
  - `undefined` 是一种未定义的状态，表示变量声明但未赋值。对象属性不存在、函数无返回值等情况。  
  - `null` 是一种明确的空值，表示变量被手动赋值为空，或用于占位表示没有对象值。

---

#### 通信理解：
- **undefined**：还没准备好（可能还会有值）。  
- **null**：明确地没有值（我就是空）。

---

### Number和Boolean

|              | Number                                    | Boolean                         |
| ------------ | ----------------------------------------- | ------------------------------- |
| **定义**     | 表示数值类型，包括整数和浮点数。          | 表示逻辑值：`true` 和 `false`。 |
| **特殊值**   | NaN、Infinity、-Infinity                  | false、true                     |
| **常用方法** | `toFixed()`、`parseInt()`、`parseFloat()` | 逻辑运算符：`&&`、`||`、`!`     |
| **应用场景** | 数学运算、格式化数值、数据转换等。        | 条件判断、逻辑控制。            |

```
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Document</title>
    <script>
    //String,Number,Boolean,null,undifined
        const username = "John";
        const age = 30;
        const rate = 4.5;
        const isCool = true;
        const x = null;
        const y = undefined;
        let z;
        
        console.log(typeof username);
        console.log(typeof age);
        console.log(typeof rate);
        console.log(typeof isCool);
        console.log(typeof x);
        console.log(typeof y);
        console.log(typeof z);
    </script>
</head>
<body>

</body>
</html>
```

- **字符串 **

```
<!DOCTYPE html>
<html>
<body>
<script>
// 基础字符串示例
const text = "   Hello JavaScript!   ";

// 常用基础方法演示
console.log("原始字符串:", text);
console.log("长度:", text.length);          // 获取长度
console.log("去空格:", text.trim());        // 去除首尾空格
console.log("大写:", text.toUpperCase());  // 转大写
console.log("小写:", text.toLowerCase());  // 转小写
console.log("截取2-7:", text.substring(2, 7)); // 截取部分
console.log("替换:", text.replace("JavaScript", "World")); // 替换内容
console.log("分割:", "apple,banana,grape".split(",")); // 拆分为数组
</script>
</body>
</html>
```

- **函数**

```
function function_name(参数1，参数2，参数3，...){//参数可以不写，表示不传参
    //函数体，执行这里的代码
    return 返回值;//可选，返回值
}
```

- 数组

数组内部可以储存许多元素

在同一个数组中，每个元素都可以是不同数据类型

const声明的数组内部的元素是可以被部分修改的

```
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Document</title>
    <script>
    //数组的内置方法
    const numbers = new Array(1,2,3,4,5);
    console.log(numbers);

    const fruits = ["apples","oranges","pears",10,true];
    fruits[5] = "grapes";
    fruits.push("mangos");//数组末尾添加一个元素
    fruits.unshift("strawberries");//数组头部添加一个元素
    fruits.pop();//删除数组末尾的元素
    console.log(Array.isArray(fruits))//判断一个变量是否是数组
    console.log(fruits.indexOf("oranges"));//得到特定元素的索引
    console.log(fruits);
    console.log(fruits[0]);//访问数组中的特定元素
    </script>
</head>
<body>

</body>
</html>
```

- JS对象

```
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Document</title>
    <script>
        //对象
    const person = {
        firstName: "John",
        lastName: "Doe",
        age: 30,
        hobbies: ["music","movies","sports"],
        address: {
        street: "50 main st",
        city: "Boston",
        state: "MA", 
        },
    };
    console.log(person);
    console.log(person.firstName,person.lastName);
    console.log(person.hobbies[1]);
    console.log(person.address.city);

    const{ firstName, 
    lastName,
    address:{ city }, 
    } = person;

    console.log(city);


    person.email = "john@gmail.com";

    console.log(person);
    </script>
</head>
<body>

</body>
</html>
```

### 四.js和html、css的关系

## 三者的协作关系
| 技术     | 依赖关系                                                     |
| -------- | ------------------------------------------------------------ |
| **HTML** | CSS 和 JS 的基础，提供操作目标和内容结构。                   |
| **CSS**  | 依赖 HTML 的结构，通过选择器定位元素并添加样式。             |
| **JS**   | 依赖 HTML 和 CSS，通过 DOM 和事件机制实现交互，动态修改内容和样式。 |

---

## 协作示例
```html
<!-- HTML -->
<button id="btn">点击变色</button>
<div id="box"></div>
```

```css
/* CSS */
#box {
  width: 100px;
  height: 100px;
  background-color: blue;
}
```

```javascript
// JavaScript
document.getElementById("btn").addEventListener("click", () => {
  const box = document.getElementById("box");
  box.style.backgroundColor = "red"; // 修改 CSS
  box.textContent = "已变色！";       // 修改 HTML
});
```

---

## 比喻总结
| 技术     | 比喻       | 作用           |
| -------- | ---------- | -------------- |
| **HTML** | 骨架       | 定义结构       |
| **CSS**  | 皮肤与装饰 | 美化外观       |
| **JS**   | 大脑与肌肉 | 控制行为与交互 |

---

**总结**：三者各司其职，共同构建现代 Web 应用。  
- **HTML** 是内容的基础，  
- **CSS** 负责视觉呈现，  
- **JS** 赋予动态能力