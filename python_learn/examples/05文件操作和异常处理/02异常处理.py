#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Python异常处理示例
"""

# 1. 基本异常处理
print("=== 基本异常处理 ===")

def basic_exception_example():
    """基本异常处理示例"""
    try:
        x = 10 / 0
        print(f"结果: {x}")
    except ZeroDivisionError:
        print("错误：除数不能为零")

basic_exception_example()

# 2. 多个异常处理
print("\n=== 多个异常处理 ===")

def multiple_exceptions_example():
    """多个异常处理示例"""
    operations = [
        ("10 / 0", lambda: 10 / 0),
        ("int('abc')", lambda: int('abc')),
        ("[1, 2, 3][5]", lambda: [1, 2, 3][5])
    ]

    for name, operation in operations:
        try:
            result = operation()
            print(f"{name}: {result}")
        except ZeroDivisionError:
            print(f"{name}: 除数不能为零")
        except ValueError:
            print(f"{name}: 值转换错误")
        except IndexError:
            print(f"{name}: 索引超出范围")
        except Exception as e:
            print(f"{name}: 未知错误 - {type(e).__name__}")

multiple_exceptions_example()

# 3. 异常的详细信息
print("\n=== 异常的详细信息 ===")

def exception_details_example():
    """异常详细信息示例"""
    try:
        result = 10 / 0
    except Exception as e:
        print(f"异常类型: {type(e)}")
        print(f"异常信息: {e}")
        print(f"异常参数: {e.args}")
        import traceback
        print(f"堆栈跟踪:")
        traceback.print_exc()

exception_details_example()

# 4. finally子句
print("\n=== finally子句 ===")

def finally_example():
    """finally子句示例"""
    for divisor in [2, 0, 3]:
        try:
            result = 10 / divisor
            print(f"10 / {divisor} = {result}")
        except ZeroDivisionError:
            print(f"10 / {divisor}: 除数不能为零")
        finally:
            print("finally子句总是执行")

finally_example()

# 5. else子句
print("\n=== else子句 ===")

def else_example():
    """else子句示例"""
    for i in range(3):
        try:
            if i == 1:
                raise ValueError("故意抛出异常")
            print(f"操作成功: i = {i}")
        except ValueError as e:
            print(f"捕获异常: {e}")
        else:
            print("没有异常发生")
        finally:
            print("finally子句")

else_example()

# 6. 自定义异常
print("\n=== 自定义异常 ===")

class InsufficientFundsError(Exception):
    """资金不足异常"""
    def __init__(self, balance, amount):
        self.balance = balance
        self.amount = amount
        self.message = f"余额不足: 需要{amount}, 但只有{balance}"
        super().__init__(self.message)

class NegativeAmountError(Exception):
    """负数金额异常"""
    def __init__(self, amount):
        self.amount = amount
        self.message = f"金额不能为负数: {amount}"
        super().__init__(self.message)

class BankAccount:
    """银行账户类"""
    def __init__(self, balance=0):
        self.balance = balance

    def withdraw(self, amount):
        """取款"""
        if amount < 0:
            raise NegativeAmountError(amount)
        if amount > self.balance:
            raise InsufficientFundsError(self.balance, amount)
        self.balance -= amount
        return self.balance

    def deposit(self, amount):
        """存款"""
        if amount < 0:
            raise NegativeAmountError(amount)
        self.balance += amount
        return self.balance

# 测试自定义异常
account = BankAccount(1000)
print(f"初始余额: {account.balance}")

operations = [
    ("存款500", lambda: account.deposit(500)),
    ("取款200", lambda: account.withdraw(200)),
    ("取款2000", lambda: account.withdraw(2000)),
    ("存款-100", lambda: account.deposit(-100))
]

for name, operation in operations:
    try:
        result = operation()
        print(f"{name}: 成功, 余额: {result}")
    except (InsufficientFundsError, NegativeAmountError) as e:
        print(f"{name}: {e}")

# 7. 异常链
print("\n=== 异常链 ===")

class DataProcessingError(Exception):
    """数据处理异常"""
    pass

def process_data(data):
    """处理数据"""
    try:
        if not isinstance(data, list):
            raise TypeError("数据必须是列表类型")
        if len(data) == 0:
            raise ValueError("数据不能为空")
        return [x * 2 for x in data]
    except (TypeError, ValueError) as e:
        raise DataProcessingError(f"数据处理失败: {e}") from e

# 测试异常链
test_cases = [
    [1, 2, 3],       # 正常情况
    "not a list",    # 类型错误
    []               # 空数据
]

for data in test_cases:
    try:
        result = process_data(data)
        print(f"处理成功: {result}")
    except DataProcessingError as e:
        print(f"处理失败: {e}")
        if e.__cause__:
            print(f"  原因: {e.__cause__}")

# 8. 上下文管理器
print("\n=== 上下文管理器 ===")

class FileHandler:
    """文件处理器"""
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.file = None

    def __enter__(self):
        """进入上下文"""
        self.file = open(self.filename, self.mode, encoding="utf-8")
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        """退出上下文"""
        if self.file:
            self.file.close()
        if exc_type is not None:
            print(f"异常发生: {exc_type.__name__}: {exc_val}")
        return True  # 抑制异常

# 使用自定义上下文管理器
with FileHandler("test_context.txt", "w") as f:
    f.write("使用自定义上下文管理器\n")
    # 这里故意出错测试异常处理
    # result = 10 / 0

# 9. 上下文管理器装饰器
from contextlib import contextmanager

@contextmanager
def database_connection():
    """数据库连接上下文管理器"""
    print("连接数据库")
    connection = "database_connection"
    try:
        yield connection
    finally:
        print("关闭数据库连接")

# 使用装饰器创建的上下文管理器
with database_connection() as conn:
    print(f"使用连接: {conn}")

# 10. 异常处理的最佳实践
print("\n=== 异常处理的最佳实践 ===")

class DataValidator:
    """数据验证器"""
    def __init__(self):
        self.errors = []
        self.warnings = []

    def validate_number(self, value, name, min_val=None, max_val=None):
        """验证数字"""
        if not isinstance(value, (int, float)):
            self.errors.append(f"{name}必须是数字")
            return False

        if min_val is not None and value < min_val:
            self.errors.append(f"{name}不能小于{min_val}")
            return False

        if max_val is not None and value > max_val:
            self.errors.append(f"{name}不能大于{max_val}")
            return False

        return True

    def validate_string(self, value, name, min_length=None, max_length=None):
        """验证字符串"""
        if not isinstance(value, str):
            self.errors.append(f"{name}必须是字符串")
            return False

        if min_length is not None and len(value) < min_length:
            self.warnings.append(f"{name}长度小于{min_length}")

        if max_length is not None and len(value) > max_length:
            self.errors.append(f"{name}长度超过{max_length}")
            return False

        return True

    def get_validation_result(self):
        """获取验证结果"""
        return {
            "is_valid": len(self.errors) == 0,
            "errors": self.errors,
            "warnings": self.warnings
        }

# 测试数据验证
validator = DataValidator()
data = {
    "age": 25,
    "score": 105,
    "name": "张三",
    "description": "这是一个很长的描述文本..."
}

validator.validate_number(data["age"], "年龄", min_val=0, max_val=120)
validator.validate_number(data["score"], "分数", min_val=0, max_val=100)
validator.validate_string(data["name"], "姓名", max_length=50)
validator.validate_string(data["description"], "描述", max_length=50)

result = validator.get_validation_result()
print(f"验证结果: {'通过' if result['is_valid'] else '失败'}")
print(f"错误: {result['errors']}")
print(f"警告: {result['warnings']}")

# 11. 异常处理的性能考虑
print("\n=== 异常处理的性能考虑 ===")

import time

def test_exception_performance():
    """测试异常处理性能"""
    iterations = 100000

    # 测试正常情况
    start = time.time()
    for i in range(iterations):
        try:
            x = i + 1
        except:
            pass
    normal_time = time.time() - start

    # 测试异常情况
    start = time.time()
    for i in range(iterations):
        try:
            x = 1 / 0
        except:
            pass
    exception_time = time.time() - start

    print(f"正常情况耗时: {normal_time:.4f}秒")
    print(f"异常情况耗时: {exception_time:.4f}秒")
    print(f"性能差异: {exception_time/normal_time:.1f}倍")

test_exception_performance()

# 12. 断言
print("\n=== 断言 ===")

def calculate_discount(price, discount_percent):
    """计算折扣价格"""
    assert price > 0, "价格必须大于0"
    assert 0 <= discount_percent <= 100, "折扣必须在0-100之间"
    return price * (100 - discount_percent) / 100

# 测试断言
test_cases = [
    (100, 20),    # 正常情况
    (0, 10),      # 价格为0
    (100, 150)    # 折扣超过100
]

for price, discount in test_cases:
    try:
        result = calculate_discount(price, discount)
        print(f"价格{price}, 折扣{discount}%: {result}")
    except AssertionError as e:
        print(f"价格{price}, 折扣{discount}%: 断言失败 - {e}")

# 13. 警告
print("\n=== 警告 ===")

import warnings

def deprecated_function():
    """已弃用的函数"""
    warnings.warn("此函数已弃用，请使用new_function()代替",
                   DeprecationWarning, stacklevel=2)
    return "旧函数的结果"

def new_function():
    """新函数"""
    return "新函数的结果"

# 测试警告
print("调用已弃用的函数:")
result = deprecated_function()
print(f"结果: {result}")

# 14. 日志记录
print("\n=== 日志记录 ===")

import logging

# 配置日志
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('app.log'),
        logging.StreamHandler()
    ]
)

def log_example():
    """日志记录示例"""
    logging.debug("调试信息")
    logging.info("一般信息")
    logging.warning("警告信息")
    logging.error("错误信息")
    logging.critical("严重错误信息")

log_example()

# 15. 全局异常处理
print("\n=== 全局异常处理 ===")

import sys

def handle_exception(exc_type, exc_value, exc_traceback):
    """全局异常处理器"""
    print("=== 全局异常处理器被调用 ===")
    print(f"异常类型: {exc_type.__name__}")
    print(f"异常信息: {exc_value}")
    print("=== 全局异常处理器结束 ===")

# 设置全局异常处理器
sys.excepthook = handle_exception

# 测试全局异常处理
def test_global_exception():
    # 这行代码会触发全局异常处理器
    # result = 10 / 0
    pass

print("全局异常处理已设置")
print("要测试全局异常处理，取消注释上面的除零错误代码")

# 16. 异常处理的实际应用
print("\n=== 异常处理的实际应用 ===")

class NetworkRequest:
    """网络请求模拟器"""
    def __init__(self):
        self.success_rate = 0.7  # 70%成功率
        self.timeout_rate = 0.2  # 20%超时率

    def send_request(self, url, data=None):
        """发送请求"""
        import random

        if random.random() > self.success_rate:
            if random.random() < self.timeout_rate:
                raise TimeoutError(f"请求超时: {url}")
            else:
                raise ConnectionError(f"连接失败: {url}")

        # 模拟成功响应
        return {
            "status": 200,
            "url": url,
            "data": data,
            "response": "success"
        }

def robust_request_handler(request, url, data=None, max_retries=3):
    """健壮的请求处理器"""
    retries = 0
    last_exception = None

    while retries < max_retries:
        try:
            response = request.send_request(url, data)
            print(f"请求成功: {url}")
            return response
        except TimeoutError as e:
            last_exception = e
            retries += 1
            print(f"超时重试 {retries}/{max_retries}: {e}")
        except ConnectionError as e:
            last_exception = e
            retries += 1
            print(f"连接错误重试 {retries}/{max_retries}: {e}")

    print(f"所有重试失败: {last_exception}")
    return None

# 测试健壮请求处理器
request = NetworkRequest()
urls = ["http://example.com/api", "http://test.com/data", "http://api.example.com"]

for url in urls:
    result = robust_request_handler(request, url)
    if result:
        print(f"最终结果: {result}")
    print("-" * 40)

# 17. 资源清理
print("\n=== 资源清理 ===")

class ResourceManager:
    """资源管理器"""
    def __init__(self):
        self.resources = []
        print("资源管理器初始化")

    def acquire_resource(self, resource_name):
        """获取资源"""
        resource = f"Resource_{resource_name}"
        self.resources.append(resource)
        print(f"获取资源: {resource}")
        return resource

    def release_resource(self, resource):
        """释放资源"""
        if resource in self.resources:
            self.resources.remove(resource)
            print(f"释放资源: {resource}")

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        # 清理所有资源
        for resource in self.resources[:]:  # 使用副本避免修改列表
            self.release_resource(resource)
        print("资源清理完成")

# 使用资源管理器
with ResourceManager() as manager:
    resource1 = manager.acquire_resource("Database")
    resource2 = manager.acquire_resource("File")
    # 即使这里发生异常，资源也会被正确清理
    # result = 10 / 0

print("\n程序执行完毕！")