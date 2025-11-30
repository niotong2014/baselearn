#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Python变量和数据类型示例
"""

# 1. 数字类型
print("=== 数字类型 ===")

# 整数
age = 25
temperature = -10
big_number = 999999999999999999

print(f"年龄: {age}, 类型: {type(age)}")
print(f"温度: {temperature}, 类型: {type(temperature)}")
print(f"大数: {big_number}, 类型: {type(big_number)}")

# 浮点数
pi = 3.14159
height = 1.75
scientific = 1.5e10

print(f"圆周率: {pi}, 类型: {type(pi)}")
print(f"身高: {height}, 类型: {type(height)}")
print(f"科学计数法: {scientific}, 类型: {type(scientific)}")

# 复数
complex_num = 3 + 4j
print(f"复数: {complex_num}, 类型: {type(complex_num)}")

# 2. 字符串类型
print("\n=== 字符串类型 ===")

# 单引号、双引号、三引号
name = '张三'
sentence = "Python是一门伟大的语言"
paragraph = """这是一个多行字符串
可以包含多行内容
非常适合长文本"""

print(f"姓名: {name}")
print(f"句子: {sentence}")
print(f"段落: {paragraph}")

# 字符串操作
full_name = "李四"
greeting = "你好"
message = greeting + ", " + full_name + "!"
print(f"字符串拼接: {message}")

# 字符串格式化
age = 30
formatted_str = f"姓名: {full_name}, 年龄: {age}"
print(f"格式化字符串: {formatted_str}")

# 字符串方法
text = "Hello, Python World!"
print(f"大写: {text.upper()}")
print(f"小写: {text.lower()}")
print(f"长度: {len(text)}")
print(f"分割: {text.split(',')}")
print(f"替换: {text.replace('Python', 'Java')}")

# 3. 布尔类型
print("\n=== 布尔类型 ===")

is_student = True
is_teacher = False
is_empty = None

print(f"是学生: {is_student}, 类型: {type(is_student)}")
print(f"是老师: {is_teacher}, 类型: {type(is_teacher)}")
print(f"为空: {is_empty}, 类型: {type(is_empty)}")

# 布尔运算
print(f"True and False: {True and False}")
print(f"True or False: {True or False}")
print(f"not True: {not True}")

# 4. 类型转换
print("\n=== 类型转换 ===")

# 数字转换
num_str = "42"
int_num = int(num_str)
float_num = float(num_str)
str_num = str(int_num)

print(f"字符串'{num_str}'转整数: {int_num}")
print(f"字符串'{num_str}'转浮点数: {float_num}")
print(f"整数{int_num}转字符串: '{str_num}'")

# 布尔值转换
print(f"bool(0): {bool(0)}")
print(f"bool(1): {bool(1)}")
print(f"bool(''): {bool('')}")
print(f"bool('hello'): {bool('hello')}")

# 5. 变量赋值和交换
print("\n=== 变量赋值和交换 ===")

a = 10
b = 20
print(f"交换前: a = {a}, b = {b}")

# 交换变量值
a, b = b, a
print(f"交换后: a = {a}, b = {b}")

# 多重赋值
x = y = z = 100
print(f"多重赋值: x = {x}, y = {y}, z = {z}")

# 多个变量同时赋值
first, second, third = 1, 2, 3
print(f"多个变量赋值: first = {first}, second = {second}, third = {third}")

# 6. 查看变量信息
print("\n=== 查看变量信息 ===")

variables = [age, pi, name, is_student, complex_num]
for var in variables:
    print(f"值: {var}, 类型: {type(var)}, ID: {id(var)}")

# 7. 删除变量
print("\n=== 删除变量 ===")

temp_var = "临时变量"
print(f"删除前: temp_var = {temp_var}")
del temp_var
try:
    print(f"删除后: temp_var = {temp_var}")
except NameError:
    print("变量temp_var已被删除")

# 8. 常量约定（Python中没有真正的常量）
print("\n=== 常量约定 ===")

# 全大写的变量名表示常量（约定俗成）
MAX_SIZE = 100
PI_VALUE = 3.14159
APP_NAME = "Python学习程序"

print(f"最大尺寸: {MAX_SIZE}")
print(f"圆周率: {PI_VALUE}")
print(f"应用名称: {APP_NAME}")

# 注意：这些值仍然可以被修改
MAX_SIZE = 200
print(f"修改后的最大尺寸: {MAX_SIZE}")

print("\n程序执行完毕！")