#  Python基础学习

###  一. 命令行模式和Python交互模式

####  1.命令行模式

- 打开方式：在Windows开始菜单选择Terminal（终端）。
- 提示符:     PS C:\>
- 特点：执行一个.py文件只能在命令行模式执行。
- 切换：假定hello.py存储在work目录下。如果你的hello.py存储在其他目录，例如，test目录，则使用cd test。如果要切换到其他盘符，例如切换到D:盘，需要输入D:

####  2.Python交互模式

- 打开方式：命令行模式下敲命令python。（或直接通过开始菜单选择Python 菜单项）
- 提示符： >>>
- 退出：在Python交互模式下输入exit()并回车。
- 特点：直接输入代码，按回车，就可以立刻得到代码执行结果。
- SyntaxError：表示输入的Python代码有语法错误。

***

###  二 .输入和输出

####  1.输出

- 方式：print()在括号中加上字符串。

~~~
例：print('hello, world')
   print('The quick brown fox', 'jumps over', 'the lazy dog')
   【print()函数也可以接受多个字符串，用逗号“,”隔开，就可以连成一串输出】
~~~

#### 2.输入

- 方式：input()

~~~
例：name = input()
   geek
   print(name)
   geek
~~~

***

###  三. Python基本语法

####  1. 缩进表示代码块层次结构（4个空格的缩进）

~~~python
if True:
    print("条件为真")
else:
    print("条件为假")

~~~

对比c语言：通过花括号  {}  来定义代码块，缩进只是一种格式化风格，不影响语法。

~~~c
#include <stdio.h>

int main() {
    if (1) {
        printf("条件为真\n");
    } else {
        printf("条件为假\n");
    }
    return 0;
}

~~~

#### 2.#用来注释

~~~python
#这是一段注释
~~~

#### 3.大小写敏感

~~~python
def myFunction():
    print("这是大写的函数")

def myfunction():
    print("这是小写的函数")

# 调用函数
myFunction()  # 调用大写的函数
myfunction()  # 调用小写的函数

# myFunction 和 myfunction 是两个不同的函数

~~~

***

###  四.数据类型和变量

####  1. 整数

- 可以处理任意大小的整数，包括负整数，写法与数学一致。
- 持用  _  分隔数字，如  10_000_000_000  等同于  10000000000  。

####  2.浮点数

- 科学计数法表示：把10用e替代，1.23x109就是1.23e9，或者12.3e8，0.000012可以写成1.2e-5。

####  3.字符串(基础)

- 定义：使用单引号  '  或双引号  "  括起来的文本。引号本身不是字符串的一部分。

- 嵌套引号： 如果字符串内部包含单引号，可以用双引号括起来，反之亦然。

- 转义字符  \  ：用于表示字符串内部的特殊字符。

  ~~~
  'I\'m \"OK\"!'
  表示I'm "OK"!
  ~~~

- 原始字符串  r '    '  ：在字符串前加  r  ，表示字符串中的内容不进行转义。

  ~~~
  print(r'\\\t\\')
  表示\\\t\\
  ~~~

  

- 多行字符串  '''     '''  :使用三引号  '''  或  """  表示多行字符串。

####  4.布尔值

- 表示：直接用True、False表示布尔值（请注意大小写）。
- and：与运算，只有所有都为True，and运算结果才是True。
- or：或运算，只要其中有一个为True，or运算结果就是True。
- not：非运算，它是一个单目运算符，把True变成False，False变成True。

####  5.空值

- 表示：None。
- 不能理解为0。

####  6.变量

- 变量名：必须是大小写英文、数字和`_`的组合，且不能用数字开头。

- 动态语言：变量可以随时被赋予不同类型的值。(变量的类型是在运行时决定的，而不是在编译时)。

  ~~~python
  a = 10  # a 是一个整数
  print(type(a))  # 输出 <class 'int'>
  
  a = "geek"  # a 现在是一个字符串
  print(type(a))  # 输出 <class 'str'>
  
  a = [1, 2, 3]  # a 现在是一个列表
  print(type(a))  # 输出 <class 'list'>
  
  ~~~

####  7.常量

- 表示：通常用全部大写的变量名表示常量。

  ~~~python
  PI = 3.14159265359
  ~~~

- 除法：有两种。1./：计算结果是浮点数，即使是两个整数恰好整除，结果也是浮点数。2.//：地板除，永远是整数，即使除不尽。

  ~~~python
  9 / 3
  3.0
  10 // 3
  3
  ~~~

  

****

###  五.字符串(进阶)

#### 1. Python 3 中的字符串

- Python 3 的字符串是以 Unicode 编码的，支持多语言字符。

####  2.字符编码与解码

- ord()   函数：获取字符的 Unicode 整数表示。

  ~~~
  例：ord('A')
  65
  ord('中')
  20013
  ~~~

- chr()   函数：将 Unicode 整数转换为对应的字符。

  ~~~
  例：chr(66)
  'B'
  chr(25991)
  '文'
  ~~~

- 十六进制表示：可以用   \u   前缀表示 Unicode 字符。

  ~~~python
  '\u4e2d\u6587'
  '中文'
  ~~~

####  3. 字符串与字节的转换

- str是 Unicode 字符串，bytes是字节序列。
- encode()：将str转换为bytes。
- decode()：将bytes转换为str  。

#### 4.字符串长度计算

- len()函数：计算字符串的字符数。

  ~~~
  例：len('ABC')  # 返回3
  ~~~

- 对于bytes，len()计算字节数。

  ~~~
  例：len(b'ABC')  # 返回3
  ~~~

***

### 六.格式化

#### 1.%操作符

- %s：字符串（可接收任何类型）
- %d：整数
- %f：浮点数
- %.nf：保留n位小数的浮点数

~~~python
name = "小明"
age = 18

print("我叫%s，今年%d岁" % (name, age))
# 输出：我叫小明，今年18岁
~~~

#### 2.format() 方法

- 使用{}作为占位符，通过.format()传递参数
- 按位置索引：{0}、{1}（索引从0开始）
- 按参数名：{name}、{age}

~~~python
city = "北京"
temp = 25

# 按位置
print("{}的温度是{}℃".format(city, temp))
# 输出：北京的温度是25℃

# 按参数名
print("{c}的温度是{t}℃".format(c=city, t=temp))
# 输出：北京的温度是25℃
~~~

#### 3.f-string

- 最简洁直观的方式，在字符串前加f或F，直接在{}中写变量或表达式。

~~~python
x = 5
y = 3

print(f"{x}加{y}等于{x + y}")
# 输出：5加3等于8
~~~

***

### 七.list and tuple

#### 1.list（列表）

- 定义：有序、可变的集合，用[]表示。例：classmates = ['a', 'b', 'c']。
- 基本操作
  - 查：用索引（从0开始，支持负数表示倒数），如classmates[0]（取第一个元素）。
  - 增：append：末尾添加、insert：指定位置插入，如classmates.append('d')。
  - 删：pop()：删除末尾元素、pop(索引)：删除指定位置元素，如classmates.pop(1)。
  - 改：直接给索引赋值，如classmates[1] = 'e'。

#### 2.tuple（元组）

- 有序、不可变的集合，用()表示。例：classmates = ('a', 'b', 'c')。
- 基本操作
  - 查：同list，用索引获取元素，如classmates(0).
  - 不可变：无增、删、改方法，元素一旦确定无法修改。

***

### 八.条件判断

#### 1，条件判断

- 基本结构：根据条件真假执行不同代码，用缩进区分代码块，末尾加冒号:

~~~python
age = 18
if age >= 18:  # 条件为True时执行
    print("成年")
else:  # 条件为False时执行
    print("未成年")
~~~

- 多条件判断：用elif（else if的缩写）处理多个条件，从上到下判断，满足一个后忽略后续。

~~~python
score = 85
if score >= 90:
    print("优秀")
elif score >= 60:  # 前面条件不满足时判断
    print("及格")
else:  # 所有条件都不满足时执行
    print("不及格")
~~~

- 条件简写：非零数值、非空字符串等视为True，否则为False。

~~~python
x = "hello"
if x:  # 字符串非空，条件为True
    print("非空")  # 输出：非空
~~~

***

### 九.match语句

- 作用：针对变量匹配多种情况。类似于c语言中的switch case。
- 基本用法：用**match 变量:**开头，接着用**case 匹配值:**定义匹配项，最后可用**case _:**匹配所有其他情况（仅能放最后）。

~~~python
score = 'B'
match score:
    case 'A':
        print('优秀')
    case 'B':
        print('良好')  # 输出：良好
    case _:
        print('其他')
~~~

- 带条件的匹配：用case 变量 if 条件，满足条件时绑定变量并执行。

~~~~python
age = 8
match age:
    case x if x < 10:
        print(f'小于10岁：{x}') 
    case _:
        print('其他年龄')
~~~~

- 多值匹配：用|分隔多个匹配值，满足其一即匹配。

~~~python
num = 3
match num:
    case 1 | 2 | 3:
        print('1-3之间')  # 输出：1-3之间
    case _:
        print('其他数字')
~~~

***

### 十.循环结构

#### 1.for...in 循环

- 作用：遍历序列，依次处理每个元素。
- 用法：for 变量 in 序列: 循环体

~~~python
names = ['a', 'b', 'c']
for name in names:
    print(f'Hello, {name}!') 
~~~

#### 2.while 循环

- 作用：只要条件满足，就重复执行循环体，直到条件不满足时退出。
- 用法：while 条件: 循环体

~~~python
sum = 0
n = 99
while n > 0:
    sum += n
    n -= 2  # 每次减2（取奇数）
print(sum)  # 输出：2500
~~~

#### 3.循环控制语句

- break：提前退出整个循环。

~~~python
n = 1
while n <= 100:
    if n > 10:
        break 
    print(n)
    n += 1  
~~~

- continue：跳过当前循环的剩余部分，直接开始下一轮循环。

~~~python
n = 0
while n < 10:
    n += 1
    if n % 2 == 0:  
        continue
    print(n)  # 输出1,3,5,7,9
~~~

***

### 十一.dict and set

#### 1.dict（字典）

- 定义：键-值（key-value）存储的无序集合，用{key: value, ...}表示，查找速度极快。例：d = {'a': 95, 'b': 75}
- 基本操作
  - 查：通过key获取value，如d['a']：返回95
  - 增/改：d['a'] = 67（新增或更新key对应的value
  - 删：d.pop('b')（删除指定key及对应的value）

- 特点
  - key必须是不可变对象（如int），list等可变对象不能作为key
  - 无序（存储顺序与插入顺序无关），key不重复

#### 2.set（集合）

- 定义：无序的不重复key集合，无value，用{key1, key2, ...}或set(序列)创建。例：s = {1, 2, 3}
- 基本操作
  - 增：s.add(4)（添加元素，重复添加无效）
  - 删：s.remove(4)（删除指定元素）
  - 集合运算：交集s1 & s2、并集s1 | s2（如s1={1,2}, s2={2,3}，则s1&s2={2}，s1|s2={1,2,3}）

- 特点
  - 元素为不可变对象，无重复元素，无序

***

### 十二、函数基础

#### 1.内置函数

- 定义：提供现成函数可直接调用
- 数据类型相关
  - int()：将其他类型转为整数
  - float()：将其他类型转为浮点数
  - str()：将其他类型转为字符串
  - bool()：判断值的布尔类型（非零/非空为True，否则False）例：print(bool(0))   输出：False，print(bool('abc'))   输出：True

- 数值计算相关
  - abs()：返回绝对值，例：print(abs(-5))   输出：5
  - max()：返回多个参数中的最大值
  - min()：返回多个参数中的最小值
  - sum()：计算可迭代对象的总和

- 序列操作相关
  - len()：返回对象的长度（元素个数）,例:print(len('hello'))   输出：5
  - list()：将可迭代对象转为列表，例：print(list('abc'))   输出：['a', 'b', 'c']
  - tuple()：将可迭代对象转为元组，例：print(tuple([1, 2]))   输出：(1, 2)
  - range()：生成整数序列（常用于循环），例：print(list(range(5)))   输出：[0, 1, 2, 3, 4]

- 其他

  - isinstance()：判断对象是否为指定类型，例：print(isinstance(5, int))    输出：True

  - type()：返回对象的类型，例：print(type(3))    输出：<class 'int'>

  - enumerate()：同时获取元素的索引和值

    ~~~python
    for i, v in enumerate(['a', 'b', 'c']):
        print(i, v)  # 输出：0 a；1 b；2 c
    ~~~

  - zip()：将多个可迭代对象按位置打包成元组

    ~~~python
    a = [1, 2, 3]
    b = ['x', 'y', 'z']
    print(list(zip(a, b)))  # 输出：[(1, 'x'), (2, 'y'), (3, 'z')]
    ~~~

  - map()：对可迭代对象的每个元素应用函数

    ~~~python
    print(list(map(lambda x: x**2, [1, 2, 3])))  # 输出：[1, 4, 9]
    ~~~

  - filter()：筛选出符合条件的元素

    ~~~python
    print(list(filter(lambda x: x % 2 == 0, [1, 2, 3, 4])))  # 输出：[2, 4]
    ~~~

#### 2.自定义函数

- 定义格式：用def关键字，格式为def 函数名(参数): 函数体，返回值用return

~~~python
def my_abs(x):
    if x >= 0:
        return x
    else:
        return -x
print(my_abs(-7))  # 输出：7
~~~

- 空函数：用pass作为占位符

~~~python
def nop():
    pass  # 暂不实现，保证代码可运行
~~~

- 参数检查：用isinstance()验证参数类型

~~~python
def my_abs(x):
    if not isinstance(x, (int, float)):
        raise TypeError("错误类型")
    return x if x >=0 else -x
~~~

- 返回多个值：实际返回元组（tuple），可被多个变量接收。

~~~python
def move(x, y):
    return x+1, y-1  # 返回元组
a, b = move(2, 3)
print(a, b)
~~~

#### 3.函数参数类型

- 位置参数：必须按顺序传入的参数

~~~python
def power(x, n):  # x和n都是位置参数
    return x **n
print(power(2, 3))  # 输出：8
~~~

- 默认参数：可指定默认值，简化调用（必选参数在前，默认参数在后）。

~~~python
def power(x, n=2):  # n默认值为2
    return x** n
print(power(3))  # 输出：9（相当于power(3,2)）
~~~

- 可变参数：参数前加*

~~~python
def calc(*nums):  # nums是可变参数
    sum = 0
    for n in nums:
        sum += n
    return sum
print(calc(1, 2, 3))  # 输出：6
~~~

- 关键字参数：参数前加**

~~~PY
def person(name, **kw):  # kw是关键字参数
    print(name, kw)
person('b', age=18, city='B')  
~~~

- 命名关键字参数：限制关键字参数的名称（需加*分隔，或跟在可变参数后）

~~~python
def person(name, *, city, job):  # city和job是命名关键字参数
    print(name, city, job)
person('b', city='B', job='student') 
~~~

- 参数组合顺序：定义时需按以下顺序：必选参数 → 默认参数 → 可变参数 → 命名关键字参数 → 关键字参数

#### 4.递归函数

- 定义：函数内部调用自身，需有终止条件避免无限递归。

~~~py
def fact(n):  # 计算n的阶乘
    if n == 1:  # 终止条件
        return 1
    return n * fact(n-1)
print(fact(5))  # 输出：120
~~~

***

### 十三.面向对象编程基础

#### 1.类（Class）与实例（Instance）

- 类的定义：类是抽象的模板，描述一类事物的共同属性和行为，用class关键字定义，格式为class 类名(父类):。若没有明确父类，默认继承object（所有类的根类）

~~~py
class Student(object):  # 定义Student类，继承自object
    pass  # 空类，暂未定义属性和方法
~~~

- 实例的创建：实例是类的具体对象，通过类名()创建，每个实例占用独立内存空间

~~~py
bart = Student()  # 创建Student类的实例bart
~~~

- 初始化方法__ init __：实例创建时自动调用，用于绑定属性（类似构造函数）。第一个参数必须是self（代表实例自身），后续参数为实例属性

~~~python
class Student(object):
    def __init__(self, name, score):  # 定义必须传入的属性name和score
        self.name = name  # 给实例绑定name属性
        self.score = score  # 给实例绑定score属性

# 创建实例时必须传入name和score（无需传self）
bart = Student('a', 100)
print(bart.name)  # 输出：a
print(bart.score)  # 输出：100
~~~

#### 2.数据封装

- 概念：将数据的属性和操作数据的逻辑封装在类内部，外部通过调用方法操作数据，无需关心内部实现
- 类的方法：定义在类中的函数，第一个参数必为self，可直接访问实例属性。

~~~python
class Student:
    def __init__(self, name, score):
        self.name, self.score = name, score
    
    def print_score(self):
        print(f"{self.name}'s score is {self.score}")
    
    def get_grade(self):
        return 'A' if self.score >= 90 else 'B' if self.score >= 60 else 'C'

bart = Student('a', 100)
bart.print_score()
print(bart.get_grade())
~~~

#### 3.访问限制

- 目的：防止外部随意修改实例内部状态，保证数据安全性。
- 私有属性定义：属性名以双下划线_ _开头

~~~python
lass Student(object):
    def __init__(self, name, score):
        self.__name = name
        self.__score = score
~~~

- 访问和修改私有属性：通过类内定义的get_xxx（获取）和set_xxx（修改）方法操作，可在方法中添加参数校验。

~~~py
class Student(object):
    def __init__(self, name, score):
        self.__name = name
        self.__score = score
    
    # 获取私有属性name
    def get_name(self):
        return self.__name
    
    # 修改私有属性score（添加范围校验）
    def set_score(self, score):
        if 0 <= score <= 100:  # 确保分数在0-100之间
            self.__score = score
        else:
            raise ValueError("Score must be between 0 and 100")

bart = Student('a', 59)
print(bart.get_name())  # 输出：Bart（通过方法访问）
bart.set_score(80)  # 合法修改
bart.set_score(150)  # 抛出错误：ValueErro
~~~

#### 4.继承与多态

- 继承

  - 概念：子类（Subclass）继承父类（Base Class）的属性和方法，无需重复编写代码，可新增或重写父类方法。

    ~~~python
    # 父类：动物
    class Animal(object):
        def run(self):
            print("Animal is running")
        
        def eat(self):
            print("Animal is eating")
    
    # 子类：狗（继承自动物）
    class Dog(Animal):
        # 重写父类的run方法
        def run(self):
            print("Dog is running")
        
        # 新增子类特有方法
        def bark(self):
            print("Dog is barking")
    ~~~

  - 效果：子类自动拥有父类的方法，若重写则优先调用子类方法

    ~~~
    dog = Dog()
    dog.run()  # 输出：Dog is running（调用重写的方法）
    dog.eat()  # 输出：Animal is eating（继承父类方法）
    dog.bark()  # 输出：Dog is barking（子类特有方法）
    ~~~

- 多态

  - 概念：不同子类的实例调用相同方法时，表现出不同行为；函数可接收父类类型参数，自动适配传入的子类实例

    ~~~python
    # 接收Animal类型参数的函数
    def run_twice(animal):
        animal.run()
        animal.run()
    
    # 传入不同子类实例
    run_twice(Animal())  # 输出：Animal is running（两次）
    run_twice(Dog())     # 输出：Dog is running（两次）
    ~~~

  - 好处：新增子类时，无需修改依赖父类的函数

    ~~~python
    # 新增子类：猫（继承自动物）
    class Cat(Animal):
        def run(self):
            print("Cat is running")
    
    run_twice(Cat())  # 输出：Cat is running（两次），无需修改run_twice函数
    ~~~

- 鸭子类型（动态语言特性）

  - 无需严格继承关系，只要对象有所需方法，即可被使用

    ~~~python
    # 非Animal子类，但有run方法
    class Timer(object):
        def run(self):
            print("Timer starts")
    
    run_twice(Timer())  # 输出：Timer starts（两次），可被run_twice调用
    ~~~

#### 5.对象信息获取

- type()：判断对象的类型

  ~~~python
  print(type(123))  # 输出：<class 'int'>
  ~~~

- isinstance()：判断对象是否为某个类型或其子类的实例

  ~~~python
  print(isinstance(dog, Animal))  # 输出：True（Dog是Animal的子类）
  ~~~

- getattr()/setattr()/hasattr()：动态操作对象的属性和方法

  ~~~python
  obj = Student('Bart', 59)
  print(hasattr(obj, 'name'))  # 输出：True（判断是否有属性）
  setattr(obj, 'age', 8)  # 给obj设置age属性
  print(getattr(obj, 'age'))  # 输出：8（获取属性）
  print(getattr(obj, 'gender', 'unknown'))  # 输出：unknown（属性不存在时返回默认值）
  ~~~

  
