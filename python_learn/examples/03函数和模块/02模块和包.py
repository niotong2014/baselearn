#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Python模块和包示例
"""

# 1. 导入标准库模块
print("=== 导入标准库模块 ===")

# 导入整个模块
import math
print(f"圆周率: {math.pi}")
print(f"2的平方根: {math.sqrt(2)}")

# 导入模块的特定函数
from random import randint, choice
print(f"随机整数: {randint(1, 100)}")

# 使用别名
import datetime as dt
now = dt.datetime.now()
print(f"当前时间: {now}")

# 2. 创建自定义模块
print("\n=== 创建自定义模块 ===")

# 创建一个简单的计算器模块
calculator_code = '''
def add(a, b):
    """两个数相加"""
    return a + b

def subtract(a, b):
    """两个数相减"""
    return a - b

def multiply(a, b):
    """两个数相乘"""
    return a * b

def divide(a, b):
    """两个数相除"""
    if b == 0:
        raise ValueError("除数不能为零")
    return a / b

# 模块级别的变量
PI = 3.14159
E = 2.71828

def calculate_circle_area(radius):
    """计算圆的面积"""
    return PI * radius ** 2
'''

# 写入模块文件
with open("calculator.py", "w", encoding="utf-8") as f:
    f.write(calculator_code)

# 导入自定义模块
import calculator

print(f"10 + 5 = {calculator.add(10, 5)}")
print(f"10 - 5 = {calculator.subtract(10, 5)}")
print(f"10 * 5 = {calculator.multiply(10, 5)}")
print(f"10 / 5 = {calculator.divide(10, 5)}")
print(f"圆面积(半径=5): {calculator.calculate_circle_area(5)}")

# 3. 从模块导入特定函数
print("\n=== 从模块导入特定函数 ===")

from calculator import add, subtract, PI

print(f"15 + 25 = {add(15, 25)}")
print(f"15 - 25 = {subtract(15, 25)}")
print(f"模块中的PI: {PI}")

# 4. 创建包
print("\n=== 创建包 ===")

# 创建包目录结构
import os

# 创建工具包
os.makedirs("tools", exist_ok=True)

# 创建__init__.py文件
with open("tools/__init__.py", "w", encoding="utf-8") as f:
    f.write("# 工具包\n")

# 创建字符串工具模块
string_tools_code = '''
def reverse_string(s):
    """反转字符串"""
    return s[::-1]

def count_words(text):
    """统计单词数"""
    return len(text.split())

def capitalize_words(text):
    """单词首字母大写"""
    return ' '.join(word.capitalize() for word in text.split())

def remove_punctuation(text):
    """去除标点符号"""
    import string
    return text.translate(str.maketrans('', '', string.punctuation))
'''

with open("tools/string_tools.py", "w", encoding="utf-8") as f:
    f.write(string_tools_code)

# 创建数字工具模块
number_tools_code = '''
def is_prime(n):
    """检查是否为质数"""
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def fibonacci_sequence(n):
    """生成斐波那契数列"""
    fib = [0, 1]
    for i in range(2, n):
        fib.append(fib[-1] + fib[-2])
    return fib

def factorial(n):
    """计算阶乘"""
    if n < 0:
        raise ValueError("n必须是非负整数")
    if n == 0:
        return 1
    return n * factorial(n - 1)

def factors(n):
    """找出所有因数"""
    return [i for i in range(1, n + 1) if n % i == 0]
'''

with open("tools/number_tools.py", "w", encoding="utf-8") as f:
    f.write(number_tools_code)

# 导入包中的模块
from tools import string_tools, number_tools

# 使用字符串工具
text = "Hello, Python World!"
print(f"原文本: {text}")
print(f"反转: {string_tools.reverse_string(text)}")
print(f"单词数: {string_tools.count_words(text)}")
print(f"首字母大写: {string_tools.capitalize_words(text.lower())}")
print(f"去除标点: {string_tools.remove_punctuation(text)}")

# 使用数字工具
print(f"\n数字工具示例:")
print(f"17是质数吗? {number_tools.is_prime(17)}")
print(f"斐波那契数列前10项: {number_tools.fibonacci_sequence(10)}")
print(f"5的阶乘: {number_tools.factorial(5)}")
print(f"12的因数: {number_tools.factors(12)}")

# 5. 模块搜索路径
print("\n=== 模块搜索路径 ===")

import sys

print("Python搜索路径:")
for i, path in enumerate(sys.path, 1):
    print(f"{i:2d}. {path}")

# 6. 动态导入
print("\n=== 动态导入 ===")

def dynamic_import(module_name):
    """动态导入模块"""
    try:
        module = __import__(module_name)
        return module
    except ImportError as e:
        print(f"无法导入模块 {module_name}: {e}")
        return None

# 动态导入模块
math_module = dynamic_import("math")
if math_module:
    print(f"动态导入成功: {math_module.__name__}")

# 7. 模块重载
print("\n=== 模块重载 ===")

import importlib

# 修改模块内容
modified_calculator = '''
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

# 新增函数
def power(a, b):
    return a ** b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("除数不能为零")
    return a / b

PI = 3.14159
E = 2.71828

def calculate_circle_area(radius):
    return PI * radius ** 2
'''

# 重写模块文件
with open("calculator.py", "w", encoding="utf-8") as f:
    f.write(modified_calculator)

# 重载模块
importlib.reload(calculator)

# 测试新功能
print(f"2的3次方: {calculator.power(2, 3)}")
print(f"5的2次方: {calculator.power(5, 2)}")

# 8. 包的__init__.py
print("\n=== 包的__init__.py ===")

# 更新包的__init__.py文件
init_code = '''
# 工具包的__init__.py

from .string_tools import reverse_string, count_words
from .number_tools import is_prime, fibonacci_sequence

__version__ = "1.0.0"
__author__ = "Python学习项目"

def package_info():
    """返回包信息"""
    return {
        "name": "tools",
        "version": __version__,
        "author": __author__,
        "modules": ["string_tools", "number_tools"]
    }
'''

with open("tools/__init__.py", "w", encoding="utf-8") as f:
    f.write(init_code)

# 重新导入包
importlib.reload(tools)

print(f"包信息: {tools.package_info()}")

# 9. 第三方包管理
print("\n=== 第三方包管理 ===")

# 检查已安装的包
try:
    import numpy as np
    print("NumPy版本:", np.__version__)
except ImportError:
    print("NumPy未安装")

try:
    import requests
    print("Requests版本:", requests.__version__)
except ImportError:
    print("Requests未安装")

# 10. 创建可执行脚本
print("\n=== 创建可执行脚本 ===")

script_code = '''#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
简单的计算器脚本
"""

import sys
from calculator import add, subtract, multiply, divide

def main():
    if len(sys.argv) != 4:
        print("用法: python calc.py <数字1> <操作符> <数字2>")
        sys.exit(1)

    try:
        a = float(sys.argv[1])
        op = sys.argv[2]
        b = float(sys.argv[3])
    except ValueError:
        print("错误：请输入有效的数字")
        sys.exit(1)

    if op == '+':
        result = add(a, b)
    elif op == '-':
        result = subtract(a, b)
    elif op == '*':
        result = multiply(a, b)
    elif op == '/':
        try:
            result = divide(a, b)
        except ValueError as e:
            print(f"错误：{e}")
            sys.exit(1)
    else:
        print("错误：不支持的操作符")
        sys.exit(1)

    print(f"结果: {a} {op} {b} = {result}")

if __name__ == "__main__":
    main()
'''

with open("calc.py", "w", encoding="utf-8") as f:
    f.write(script_code)

# 在Unix-like系统上设置可执行权限
import os
os.chmod("calc.py", 0o755)

print("计算器脚本已创建")
print("使用方法:")
print("  python calc.py 10 + 5")
print("  python calc.py 10 - 5")
print("  python calc.py 10 * 5")
print("  python calc.py 10 / 5")

# 11. 模块的最佳实践
print("\n=== 模块的最佳实践 ===")

# 创建遵循最佳实践的模块
best_practices_module = '''
"""
数学工具模块 - 展示模块最佳实践

这个模块提供了基本的数学运算功能。
遵循PEP 8规范，包含完整的文档字符串和类型注解。
"""

__version__ = "1.0.0"
__author__ = "Python学习项目"

from typing import Union, List

Number = Union[int, float]

def add(a: Number, b: Number) -> Number:
    """
    两个数相加

    Args:
        a: 第一个数
        b: 第二个数

    Returns:
        两个数的和

    Examples:
        >>> add(2, 3)
        5
        >>> add(2.5, 3.5)
        6.0
    """
    return a + b

def multiply(a: Number, b: Number) -> Number:
    """
    两个数相乘

    Args:
        a: 第一个数
        b: 第二个数

    Returns:
        两个数的乘积
    """
    return a * b

def average(numbers: List[Number]) -> float:
    """
    计算数字列表的平均值

    Args:
        numbers: 数字列表

    Returns:
        平均值

    Raises:
        ValueError: 如果列表为空

    Examples:
        >>> average([1, 2, 3, 4, 5])
        3.0
    """
    if not numbers:
        raise ValueError("列表不能为空")
    return sum(numbers) / len(numbers)

# 私有函数（约定俗成）
def _validate_number(n: Number) -> bool:
    """验证是否为有效数字（内部使用）"""
    return isinstance(n, (int, float))

# 模块级别的测试
if __name__ == "__main__":
    # 简单测试
    print(add(2, 3))  # 应该输出 5
    print(multiply(4, 5))  # 应该输出 20
    print(average([1, 2, 3, 4, 5]))  # 应该输出 3.0
'''

with open("math_tools.py", "w", encoding="utf-8") as f:
    f.write(best_practices_module)

# 测试最佳实践模块
import math_tools

print("\n测试最佳实践模块:")
print(f"2 + 3 = {math_tools.add(2, 3)}")
print(f"4 * 5 = {math_tools.multiply(4, 5)}")
print(f"平均数: {math_tools.average([1, 2, 3, 4, 5])}")

# 12. 命名空间包
print("\n=== 命名空间包 ===")

# 创建命名空间包的示例
print("命名空间包允许将一个包分散在多个目录中")
print("这在大型项目中很有用")

# 13. 资源文件访问
print("\n=== 资源文件访问 ===")

import pkgutil
import importlib.util

# 创建资源文件
resource_content = '''这是一个资源文件
用于演示如何访问包内的资源文件
包含一些有用的信息
'''

os.makedirs("tools/resources", exist_ok=True)
with open("tools/resources/data.txt", "w", encoding="utf-8") as f:
    f.write(resource_content)

# 读取资源文件
try:
    with open("tools/resources/data.txt", "r", encoding="utf-8") as f:
        content = f.read()
        print("资源文件内容:")
        print(content)
except FileNotFoundError:
    print("资源文件未找到")

# 14. 清理示例文件
print("\n=== 清理文件 ===")

# 显示创建的文件
created_files = [
    "calculator.py",
    "calc.py",
    "math_tools.py",
    "tools/__init__.py",
    "tools/string_tools.py",
    "tools/number_tools.py",
    "tools/resources/data.txt"
]

print("\n创建的文件:")
for file in created_files:
    if os.path.exists(file):
        size = os.path.getsize(file)
        print(f"  {file} ({size} bytes")

print("\n程序执行完毕！")
print("你可以运行这些示例来学习模块和包的使用")