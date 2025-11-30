#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Python迭代器和生成器示例
"""

# 1. 迭代器基础
print("=== 迭代器基础 ===")

# 列表作为可迭代对象
numbers = [1, 2, 3, 4, 5]
print(f"原始列表: {numbers}")

# 创建迭代器
numbers_iter = iter(numbers)

# 使用next()获取元素
print("使用next()获取元素:")
print(f"第一个元素: {next(numbers_iter)}")
print(f"第二个元素: {next(numbers_iter)}")
print(f"第三个元素: {next(numbers_iter)}")

# 使用for循环遍历剩余元素
print("使用for遍历剩余元素:")
for num in numbers_iter:
    print(f"元素: {num}")

# 2. 自定义迭代器
print("\n=== 自定义迭代器 ===")

class CountDown:
    """倒计时迭代器"""
    def __init__(self, start):
        self.start = start

    def __iter__(self):
        return self

    def __next__(self):
        if self.start <= 0:
            raise StopIteration
        current = self.start
        self.start -= 1
        return current

# 使用自定义迭代器
countdown = CountDown(5)
print("倒计时:")
for num in countdown:
    print(f"{num}...")

# 3. 生成器函数
print("\n=== 生成器函数 ===")

def fibonacci_generator(n):
    """斐波那契数列生成器"""
    a, b = 0, 1
    count = 0
    while count < n:
        yield a
        a, b = b, a + b
        count += 1

# 使用生成器
fib = fibonacci_generator(10)
print("斐波那契数列:")
for num in fib:
    print(num, end=" ")
print()

# 4. 生成器表达式
print("\n=== 生成器表达式 ===")

# 列表推导式（一次性生成所有元素）
list_comp = [x**2 for x in range(10)]
print(f"列表推导式: {list_comp}")
print(f"列表推导式类型: {type(list_comp)}")

# 生成器表达式（惰性求值）
gen_exp = (x**2 for x in range(10))
print(f"生成器表达式: {gen_exp}")
print(f"生成器表达式类型: {type(gen_exp)}")

print("遍历生成器表达式:")
for num in gen_exp:
    print(num, end=" ")
print()

# 5. 生成器的高级用法
print("\n=== 生成器的高级用法 ===")

def number_generator():
    """数字生成器"""
    print("生成数字1")
    yield 1
    print("生成数字2")
    yield 2
    print("生成数字3")
    yield 3

def square_generator(gen):
    """平方生成器"""
    for num in gen:
        print(f"计算{num}的平方")
        yield num ** 2

# 生成器管道
numbers = number_generator()
squares = square_generator(numbers)

print("生成器管道:")
for square in squares:
    print(f"结果: {square}")

# 6. 生成器的send()和close()方法
print("\n=== 生成器的send()和close() ===")

def echo_generator():
    """回显生成器"""
    print("生成器启动")
    while True:
        received = yield
        print(f"收到: {received}")
        yield f"回显: {received}"

# 使用send()方法
echo_gen = echo_generator()
next(echo_gen)  # 启动生成器

# 发送数据
result = echo_gen.send("Hello")
print(f"生成器返回: {result}")

result = echo_gen.send("World")
print(f"生成器返回: {result}")

# 关闭生成器
echo_gen.close()
print("生成器已关闭")

# 7. 生成器的throw()方法
print("\n=== 生成器的throw()方法 ===")

def generator_with_exception():
    """可以处理异常的生成器"""
    try:
        while True:
            received = yield
            if received == "error":
                raise ValueError("故意抛出的错误")
            print(f"处理: {received}")
    except ValueError as e:
        print(f"捕获到异常: {e}")
        yield "异常已处理"

# 使用throw()方法
gen = generator_with_exception()
next(gen)  # 启动生成器

# 正常数据
gen.send("数据1")

# 抛出异常
try:
    result = gen.throw(ValueError, "测试异常")
    print(f"异常处理结果: {result}")
except ValueError as e:
    print(f"未捕获的异常: {e}")

# 8. yield from 语法
print("\n=== yield from 语法 ===")

def sub_generator():
    """子生成器"""
    yield "子生成器1"
    yield "子生成器2"

def main_generator():
    """主生成器"""
    yield "主生成器1"
    yield from sub_generator()
    yield "主生成器2"

# 使用yield from
for item in main_generator():
    print(item)

# 9. 迭代器和生成器的性能比较
print("\n=== 迭代器和生成器的性能比较 ===")

import sys
import time

def performance_test():
    """性能测试"""
    n = 1000000

    # 列表内存使用
    start_time = time.time()
    numbers_list = [x**2 for x in range(n)]
    list_time = time.time() - start_time
    list_size = sys.getsizeof(numbers_list)

    # 生成器内存使用
    start_time = time.time()
    numbers_gen = (x**2 for x in range(n))
    gen_time = time.time() - start_time
    gen_size = sys.getsizeof(numbers_gen)

    print(f"列表内存使用: {list_size} bytes")
    print(f"列表创建时间: {list_time:.4f}秒")
    print(f"生成器内存使用: {gen_size} bytes")
    print(f"生成器创建时间: {gen_time:.4f}秒")
    print(f"内存节省: {list_size/gen_size:.1f}倍")

performance_test()

# 10. 无限生成器
print("\n=== 无限生成器 ===")

def prime_generator():
    """质数生成器"""
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    num = 2
    while True:
        if is_prime(num):
            yield num
        num += 1

# 使用无限生成器（只取前10个质数）
primes = prime_generator()
print("前10个质数:")
for i in range(10):
    print(next(primes), end=" ")
print()

# 11. 生成器的实际应用
print("\n=== 生成器的实际应用 ===")

def log_file_reader(filename):
    """日志文件读取器"""
    with open(filename, "r", encoding="utf-8") as file:
        for line in file:
            line = line.strip()
            if line:  # 忽略空行
                yield line

def error_log_filter(log_generator):
    """错误日志过滤器"""
    for line in log_generator:
        if "ERROR" in line:
            yield line

# 创建示例日志文件
log_content = """
2024-01-01 10:00:00 INFO 应用程序启动
2024-01-01 10:01:00 ERROR 连接数据库失败
2024-01-01 10:02:00 INFO 数据处理开始
2024-01-01 10:03:00 ERROR 内存不足
2024-01-01 10:04:00 INFO 操作完成
"""

with open("app.log", "w", encoding="utf-8") as f:
    f.write(log_content)

# 使用生成器处理日志
print("错误日志:")
log_reader = log_file_reader("app.log")
error_filter = error_log_filter(log_reader)

for error in error_filter:
    print(error)

# 12. 生成器的协程应用
print("\n=== 生成器的协程应用 ===")

def data_producer(data_list):
    """数据生产者"""
    for data in data_list:
        print(f"生产者产生数据: {data}")
        yield data

def data_consumer(producer):
    """数据消费者"""
    for data in producer:
        print(f"消费者处理数据: {data}")
        # 模拟处理
        processed = f"processed_{data}"
        print(f"处理结果: {processed}")

# 协程示例
data = ["A", "B", "C"]
producer = data_producer(data)
data_consumer(producer)

# 13. 双向生成器
print("\n=== 双向生成器 ===")

def average_calculator():
    """平均值计算器"""
    total = 0
    count = 0
    while True:
        value = yield total / count if count > 0 else 0
        if value is None:  # 结束信号
            break
        total += value
        count += 1
        print(f"当前平均值: {total / count}")

# 使用双向生成器
avg_calc = average_calculator()
next(avg_calc)  # 启动生成器

# 发送数据计算平均值
avg_calc.send(10)
avg_calc.send(20)
avg_calc.send(30)
avg_calc.send(40)

# 结束计算
try:
    avg_calc.send(None)
except StopIteration:
    print("计算完成")

# 14. 生成器的链式操作
print("\n=== 生成器的链式操作 ===")

def read_lines(filename):
    """读取行"""
    with open(filename, "r", encoding="utf-8") as f:
        for line in f:
            yield line.strip()

def filter_lines(lines, keyword):
    """过滤行"""
    for line in lines:
        if keyword in line:
            yield line

def transform_lines(lines, transform_func):
    """转换行"""
    for line in lines:
        yield transform_func(line)

# 链式操作示例
with open("sample.txt", "w", encoding="utf-8") as f:
    f.write("Hello Python\n")
    f.write("Hello World\n")
    f.write("Python is great\n")
    f.write("World is beautiful\n")

print("链式操作示例:")
lines = read_lines("sample.txt")
filtered = filter_lines(lines, "Hello")
transformed = transform_lines(filtered, lambda x: x.upper())

for line in transformed:
    print(line)

# 15. 生成器与数据流
print("\n=== 生成器与数据流 ===")

def data_stream_generator(data_source, chunk_size=2):
    """数据流生成器"""
    for i in range(0, len(data_source), chunk_size):
        chunk = data_source[i:i + chunk_size]
        print(f"生成数据块: {chunk}")
        yield chunk

def data_processor(stream_generator):
    """数据处理器"""
    for chunk in stream_generator:
        # 处理数据块
        processed = [x * 2 for x in chunk]
        print(f"处理数据块: {processed}")
        yield processed

# 数据流处理
data = list(range(1, 11))
stream = data_stream_generator(data)
processor = data_processor(stream)

print("数据流处理:")
for processed_chunk in processor:
    pass

# 16. 异步生成器（Python 3.6+）
print("\n=== 异步生成器概念 ===")

# 注意：这需要Python 3.6+和异步环境
print("异步生成器基本语法:")
print("""
async def async_generator():
    for i in range(5):
        await asyncio.sleep(1)  # 模拟异步操作
        yield i

async def main():
    async for item in async_generator():
        print(item)
""")

print("异步生成器用于处理IO密集型操作")
print("如网络请求、文件读写等异步任务")

# 17. 清理示例文件
print("\n=== 清理示例文件 ===")

import os

files_to_remove = ["sample.txt", "app.log"]
for file in files_to_remove:
    if os.path.exists(file):
        os.remove(file)
        print(f"已删除: {file}")

print("\n程序执行完毕！")