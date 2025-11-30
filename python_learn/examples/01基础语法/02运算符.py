#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Python运算符示例
"""

# 1. 算术运算符
print("=== 算术运算符 ===")

a = 10
b = 3

print(f"a = {a}, b = {b}")
print(f"加法: a + b = {a + b}")
print(f"减法: a - b = {a - b}")
print(f"乘法: a * b = {a * b}")
print(f"除法: a / b = {a / b}")
print(f"整除: a // b = {a // b}")
print(f"取余: a % b = {a % b}")
print(f"幂运算: a ** b = {a ** b}")

# 2. 赋值运算符
print("\n=== 赋值运算符 ===")

x = 5
print(f"x = {x}")

x += 3  # 等同于 x = x + 3
print(f"x += 3 => x = {x}")

x -= 2  # 等同于 x = x - 2
print(f"x -= 2 => x = {x}")

x *= 4  # 等同于 x = x * 4
print(f"x *= 4 => x = {x}")

x /= 3  # 等同于 x = x / 3
print(f"x /= 3 => x = {x}")

x //= 2  # 等同于 x = x // 2
print(f"x //= 2 => x = {x}")

x %= 3  # 等同于 x = x % 3
print(f"x %= 3 => x = {x}")

x **= 2  # 等同于 x = x ** 2
print(f"x **= 2 => x = {x}")

# 3. 比较运算符
print("\n=== 比较运算符 ===")

p = 10
q = 20
r = 10

print(f"p = {p}, q = {q}, r = {r}")
print(f"p == q: {p == q}")
print(f"p == r: {p == r}")
print(f"p != q: {p != q}")
print(f"p > q: {p > q}")
print(f"p < q: {p < q}")
print(f"p >= r: {p >= r}")
print(f"p <= r: {p <= r}")

# 字符串比较
str1 = "apple"
str2 = "banana"
print(f"'{str1}' > '{str2}': {str1 > str2}")
print(f"'{str1}' < '{str2}': {str1 < str2}")
print(f"'{str1}' == '{str1}': {str1 == str1}")

# 4. 逻辑运算符
print("\n=== 逻辑运算符 ===")

t = True
f = False

print(f"True: {t}, False: {f}")
print(f"t and f: {t and f}")
print(f"t or f: {t or f}")
print(f"not t: {not t}")
print(f"not f: {not f}")

# 短路求值
def func1():
    print("函数1执行")
    return True

def func2():
    print("函数2执行")
    return False

print("\n短路求值示例:")
print("func1() and func2():")
result = func1() and func2()
print(f"结果: {result}")

print("\nfunc2() and func1():")
result = func2() and func1()
print(f"结果: {result}")

# 5. 身份运算符
print("\n=== 身份运算符 ===")

list1 = [1, 2, 3]
list2 = [1, 2, 3]
list3 = list1

print(f"list1 = {list1}")
print(f"list2 = {list2}")
print(f"list3 = {list3}")
print(f"list1 is list2: {list1 is list2}")  # 比较对象标识
print(f"list1 is list3: {list1 is list3}")
print(f"list1 == list2: {list1 == list2}")  # 比较值
print(f"id(list1): {id(list1)}")
print(f"id(list2): {id(list2)}")
print(f"id(list3): {id(list3)}")

# 6. 成员运算符
print("\n=== 成员运算符 ===")

numbers = [1, 2, 3, 4, 5]
text = "Hello Python"

print(f"numbers = {numbers}")
print(f"3 in numbers: {3 in numbers}")
print(f"6 in numbers: {6 in numbers}")
print(f"3 not in numbers: {3 not in numbers}")
print(f"6 not in numbers: {6 not in numbers}")

print(f"text = '{text}'")
print(f"'H' in text: {'H' in text}")
print(f"'h' in text: {'h' in text}")
print(f"'Python' in text: {'Python' in text}")

# 7. 位运算符
print("\n=== 位运算符 ===")

m = 5  # 二进制: 0101
n = 3  # 二进制: 0011

print(f"m = {m} (二进制: {bin(m)})")
print(f"n = {n} (二进制: {bin(n)})")
print(f"m & n (按位与): {m & n} (二进制: {bin(m & n)})")
print(f"m | n (按位或): {m | n} (二进制: {bin(m | n)})")
print(f"m ^ n (按位异或): {m ^ n} (二进制: {bin(m ^ n)})")
print(f"~m (按位取反): {~m} (二进制: {bin(~m)})")
print(f"m << 1 (左移1位): {m << 1} (二进制: {bin(m << 1)})")
print(f"m >> 1 (右移1位): {m >> 1} (二进制: {bin(m >> 1)})")

# 8. 运算符优先级
print("\n=== 运算符优先级示例 ===")

# 演示优先级
result = 2 + 3 * 4
print(f"2 + 3 * 4 = {result}")

# 使用括号改变优先级
result = (2 + 3) * 4
print(f"(2 + 3) * 4 = {result}")

# 复杂表达式
result = 2 + 3 * 4 ** 2 / 2 - 1
print(f"2 + 3 * 4 ** 2 / 2 - 1 = {result}")

# 9. 实际应用示例
print("\n=== 实际应用示例 ===")

# 计算圆的面积和周长
radius = 5
pi = 3.14159
area = pi * radius ** 2
circumference = 2 * pi * radius
print(f"半径为{radius}的圆:")
print(f"面积: {area:.2f}")
print(f"周长: {circumference:.2f}")

# 判断闰年
year = 2024
is_leap_year = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
print(f"{year}年是闰年吗? {is_leap_year}")

# 温度转换
celsius = 25
fahrenheit = celsius * 9/5 + 32
print(f"{celsius}°C = {fahrenheit:.1f}°F")

# 10. 运算符重载示例（简单类）
print("\n=== 运算符重载示例 ===")

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __str__(self):
        return f"Point({self.x}, {self.y})"

p1 = Point(1, 2)
p2 = Point(3, 4)
p3 = p1 + p2
print(f"p1 = {p1}")
print(f"p2 = {p2}")
print(f"p1 + p2 = {p3}")

print("\n程序执行完毕！")
