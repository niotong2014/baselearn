#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Python函数基础示例
"""

# 1. 函数定义和调用
print("=== 函数定义和调用 ===")

def say_hello():
    """简单的问候函数"""
    print("Hello, Python!")
    print("欢迎学习函数编程")

# 调用函数
say_hello()

# 2. 带参数的函数
print("\n=== 带参数的函数 ===")

def greet(name):
    """向特定的人问候"""
    print(f"Hello, {name}!")

# 调用带参数的函数
greet("张三")
greet("李四")

# 3. 带默认参数的函数
print("\n=== 带默认参数的函数 ===")

def greet_with_default(name="朋友"):
    """带默认参数的问候函数"""
    print(f"Hello, {name}!")

# 使用默认参数
greet_with_default()

# 传入参数
greet_with_default("王五")

# 4. 多个参数
print("\n=== 多个参数 ===")

def introduce(name, age, city):
    """介绍个人信息"""
    print(f"我叫{name}，今年{age}岁，来自{city}")

# 调用多个参数函数
introduce("张三", 25, "北京")

# 使用关键字参数
introduce(age=26, name="李四", city="上海")

# 混合使用位置参数和关键字参数
introduce("王五", city="广州", age=24)

# 5. 返回值
print("\n=== 返回值 ===")

def add(a, b):
    """两个数相加"""
    return a + b

def subtract(a, b):
    """两个数相减"""
    return a - b

# 调用函数并获取返回值
result1 = add(5, 3)
result2 = subtract(10, 4)

print(f"5 + 3 = {result1}")
print(f"10 - 4 = {result2}")

# 返回多个值
def get_rectangle_info(length, width):
    """返回矩形的信息"""
    area = length * width
    perimeter = 2 * (length + width)
    return area, perimeter

# 接收多个返回值
area, perimeter = get_rectangle_info(5, 3)
print(f"长方形面积: {area}, 周长: {perimeter}")

# 将返回值作为元组处理
rectangle_info = get_rectangle_info(6, 4)
print(f"长方形信息: {rectangle_info}")

# 6. 参数类型注解
print("\n=== 参数类型注解 ===")

def calculate_circle_area(radius: float) -> float:
    """计算圆的面积"""
    import math
    return math.pi * radius ** 2

def format_name(first_name: str, last_name: str) -> str:
    """格式化姓名"""
    return f"{last_name}{first_name}"

# 调用带类型注解的函数
circle_area = calculate_circle_area(5.0)
formatted_name = format_name("三", "张")

print(f"半径为5的圆面积: {circle_area:.2f}")
print(f"格式化姓名: {formatted_name}")

# 7. 可变参数
print("\n=== 可变参数 ===")

# *args - 任意数量的位置参数
def sum_numbers(*args):
    """计算任意数量数字的和"""
    print(f"传入的参数: {args}")
    return sum(args)

# 调用可变参数函数
result = sum_numbers(1, 2, 3, 4, 5)
print(f"1+2+3+4+5 = {result}")

result = sum_numbers(10, 20, 30)
print(f"10+20+30 = {result}")

# **kwargs - 任意数量的关键字参数
def print_student_info(**kwargs):
    """打印学生信息"""
    print("学生信息:")
    for key, value in kwargs.items():
        print(f"  {key}: {value}")

# 调用关键字参数函数
print_student_info(name="张三", age=20, grade="A", major="计算机")

# 混合使用普通参数、*args和**kwargs
def complex_function(name, *args, **kwargs):
    """复杂的函数参数示例"""
    print(f"姓名: {name}")
    print(f"其他参数: {args}")
    print(f"关键字参数: {kwargs}")

complex_function("李四", 20, "北京", gender="男", hobby="编程")

# 8. 函数文档字符串
print("\n=== 函数文档字符串 ===")

def factorial(n):
    """
    计算数字的阶乘

    参数:
        n (int): 要计算阶乘的非负整数

    返回:
        int: n的阶乘

    示例:
        >>> factorial(5)
        120

    异常:
        ValueError: 如果n为负数
    """
    if n < 0:
        raise ValueError("n必须是非负整数")
    if n == 0:
        return 1
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

# 查看函数文档
print(factorial.__doc__)

# 使用help()函数
# help(factorial)  # 注释掉避免输出过长

# 调用函数
print(f"5! = {factorial(5)}")

# 9. 函数作为对象
print("\n=== 函数作为对象 ===")

def multiply(a, b):
    return a * b

def apply_operation(func, x, y):
    """应用函数到两个参数"""
    return func(x, y)

# 将函数作为参数传递
result = apply_operation(multiply, 3, 4)
print(f"3 * 4 = {result}")

# 函数列表
operations = [add, subtract, multiply]
numbers = (10, 5)

print("\n函数列表操作:")
for op in operations:
    result = op(*numbers)
    print(f"{op.__name__}{numbers} = {result}")

# 10. 嵌套函数
print("\n=== 嵌套函数 ===")

def outer_function(x):
    """外部函数"""
    def inner_function(y):
        """内部函数"""
        return x + y

    return inner_function

# 创建闭包
add_5 = outer_function(5)
add_10 = outer_function(10)

print(f"5 + 3 = {add_5(3)}")
print(f"10 + 7 = {add_10(7)}")

# 更复杂的嵌套函数
def create_counter():
    """创建计数器"""
    count = 0

    def counter():
        nonlocal count
        count += 1
        return count

    return counter

# 创建多个计数器
counter1 = create_counter()
counter2 = create_counter()

print(f"\n计数器1:")
print(f"  第一次调用: {counter1()}")
print(f"  第二次调用: {counter1()}")
print(f"  第三次调用: {counter1()}")

print(f"计数器2:")
print(f"  第一次调用: {counter2()}")
print(f"  第二次调用: {counter2()}")

# 11. 递归函数
print("\n=== 递归函数 ===")

def fibonacci(n):
    """计算斐波那契数列"""
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

def gcd(a, b):
    """计算最大公约数（欧几里得算法）"""
    if b == 0:
        return a
    return gcd(b, a % b)

# 计算斐波那契数
print(f"斐波那契数列前10项:")
for i in range(10):
    print(f"  F({i}) = {fibonacci(i)}")

# 计算最大公约数
print(f"\n最大公约数:")
print(f"  gcd(48, 18) = {gcd(48, 18)}")
print(f"  gcd(1071, 462) = {gcd(1071, 462)}")

# 12. 高阶函数
print("\n=== 高阶函数 ===")

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# map函数 - 对每个元素应用函数
squares = list(map(lambda x: x**2, numbers))
print(f"原列表: {numbers}")
print(f"平方后: {squares}")

# filter函数 - 过滤元素
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(f"偶数: {even_numbers}")

# reduce函数 - 累积计算
from functools import reduce
product = reduce(lambda x, y: x * y, numbers[0:5])
print(f"前5个数的乘积: {product}")

# 自定义高阶函数
def apply_to_list(lst, func):
    """将函数应用到列表的每个元素"""
    return [func(x) for x in lst]

# 使用自定义高阶函数
def double(x):
    return x * 2

def square(x):
    return x ** 2

doubled = apply_to_list(numbers[:5], double)
squared = apply_to_list(numbers[:5], square)

print(f"\n自定义高阶函数:")
print(f"  双倍: {doubled}")
print(f"  平方: {squared}")

# 13. 函数装饰器（基础）
print("\n=== 函数装饰器（基础） ===")

def simple_decorator(func):
    """简单的装饰器"""
    def wrapper():
        print(f"调用 {func.__name__} 函数之前")
        func()
        print(f"调用 {func.__name__} 函数之后")
    return wrapper

@simple_decorator
def say_goodbye():
    """说再见函数"""
    print("Goodbye!")

# 调用装饰后的函数
say_goodbye()

# 带参数的装饰器
def log_decorator(func):
    """日志装饰器"""
    def wrapper(*args, **kwargs):
        print(f"调用函数: {func.__name__}")
        print(f"参数: args={args}, kwargs={kwargs}")
        result = func(*args, **kwargs)
        print(f"返回值: {result}")
        return result
    return wrapper

@log_decorator
def add_with_logging(a, b):
    """带日志的加法"""
    return a + b

# 调用带日志的函数
result = add_with_logging(5, 3)

# 14. 函数的实际应用
print("\n=== 函数的实际应用 ===")

def calculate_statistics(numbers):
    """计算统计信息"""
    if not numbers:
        return None

    n = len(numbers)
    total = sum(numbers)
    average = total / n

    sorted_numbers = sorted(numbers)
    if n % 2 == 1:
        median = sorted_numbers[n // 2]
    else:
        median = (sorted_numbers[n // 2 - 1] + sorted_numbers[n // 2]) / 2

    return {
        "count": n,
        "sum": total,
        "average": average,
        "median": median,
        "min": min(numbers),
        "max": max(numbers)
    }

# 测试统计函数
test_data = [85, 92, 78, 88, 95, 82, 90]
stats = calculate_statistics(test_data)

print(f"数据: {test_data}")
print("统计信息:")
for key, value in stats.items():
    if isinstance(value, float):
        print(f"  {key}: {value:.2f}")
    else:
        print(f"  {key}: {value}")

# 15. 函数的最佳实践
print("\n=== 函数的最佳实践 ===")

def validate_input(value, min_value=0, max_value=100):
    """验证输入值"""
    if not isinstance(value, (int, float)):
        raise TypeError("值必须是数字")
    if min_value <= value <= max_value:
        return True
    return False

def safe_divide(a, b):
    """安全除法"""
    if b == 0:
        raise ValueError("除数不能为零")
    return a / b

# 测试最佳实践函数
try:
    print(f"验证85: {validate_input(85)}")
    print(f"验证150: {validate_input(150)}")
    # print(f"验证'abc': {validate_input('abc')}")  # 会引发异常

    result = safe_divide(10, 2)
    print(f"10 / 2 = {result}")

    # result = safe_divide(10, 0)  # 会引发异常
except (TypeError, ValueError) as e:
    print(f"错误: {e}")

print("\n程序执行完毕！")