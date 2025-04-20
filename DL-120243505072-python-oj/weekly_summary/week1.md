# Python 学习总结

## 一、Python基础语法

### 1.基本数据类型
字符串(str)
整数(int)
浮点数(float)
布尔值(bool)

### 2.运算符
算术运算符：+ - * / // % **
比较运算符：== != > < >= <=
逻辑运算符：and or not
运算符优先级：or<and<not

             逻辑<比较<数值

## 二、结构
### 一、列表：切片--左闭右开
### 二、方法：
1.增:append(),extend(),insert()

2.删:remove(),pop(),clear()

3.改:sort(),reverse()

4.查:count(),index(),index(x,start,end)

4.加法：拼接 

  乘法：重复列表中的元素
### 三、嵌套列表
利用for访问嵌套列表
利用循环创建二维列表

### 四、深拷贝与浅拷贝
浅拷贝只拷贝外层的对象，若包含嵌套拷贝的只能是其引用,即不适用二维以上列表
深拷贝：copy.deepcopy()
浅拷贝:copy.copy()

### 五、列表推导式
结构：
1.expression for target in iterable
2.expression for target in iterable if condition
3.expression for target1 in iterable if condition1
           for target2 in iterable if condition2
           ...
           for targetN in iterable if conditionN

## 三、分支和循环
### 分支结构：
1.if condition:
  else:

2.if condition:
  elif condtion:
  else:

### 循环
continue:只跳出本轮循环
break：跳出整个循环

1.while
while condition:
else:

2.for(迭代)
for i in 范围：
range()——生成一个数字序列，左开右闭
用法：range(stop)  range(start,stop)  range(start,stop,step) 
无论哪种用法参数必须是整数

## 四、模块
模块的导入：import 模块名

使用：x.模块名





