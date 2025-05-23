# Python 学习总结

## 一、Python基础语法

### 1. 基本数据类型
字符串(str)
整数(int) 
浮点数(float)
布尔值(bool)

### 2. 运算符
**算术运算符**  
+ - * / // % **

**比较运算符**  
== != > < >= <=

**逻辑运算符**  
and or not

**运算符优先级**  
1. or < and < not  
2. 逻辑运算 < 比较运算 < 数值运算

## 二、数据结构

### 1. 列表(List)
**切片规则**  
左闭右开区间

**常用方法**  
增：append(), extend(), insert()  
删：remove(), pop(), clear()  
改：sort(), reverse()  
查：count(), index(), index(x,start,end)  

**特殊操作**  
加法：列表拼接  
乘法：重复列表元素  

### 2. 嵌套列表
使用for循环访问嵌套列表
使用循环创建二维列表

### 3. 拷贝机制
**浅拷贝**  
只拷贝外层对象
套部分拷贝引用
方法：copy.copy()

**深拷贝**  
完全独立拷贝所有层级
方法：copy.deepcopy()

### 4. 列表推导式
**基本结构**  
1. [expression for target in iterable]  
2. [expression for target in iterable if condition]


## 三、流程控制

```python
### 1. 分支结构

# 单分支
if condition:
    statements

# 多分支 
if condition1:
    statements1
elif condition2:
    statements2
else:
    statements3

### 2. 循环
continue:只跳出本轮循环

break：跳出整个循环

1.while

while condition:

else:

2.for(迭代)

for i in 范围：

range()——生成一个数字序列，左开右闭

用法：range(stop)   range(start,stop)   range(start,stop,step) 

无论哪种用法参数必须是整数
```
## 四、模块
模块的导入：import 模块名

使用：x.模块名




