#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Python装饰器和元类示例
"""

# 1. 基础装饰器
print("=== 基础装饰器 ===")

def timer_decorator(func):
    """计时装饰器"""
    import time
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"{func.__name__} 执行时间: {end_time - start_time:.4f}秒")
        return result
    return wrapper

def logger_decorator(func):
    """日志装饰器"""
    def wrapper(*args, **kwargs):
        print(f"调用函数: {func.__name__}")
        print(f"参数: args={args}, kwargs={kwargs}")
        result = func(*args, **kwargs)
        print(f"返回值: {result}")
        return result
    return wrapper

# 使用装饰器
@timer_decorator
@logger_decorator
def calculate_sum(n):
    """计算1到n的和"""
    return sum(range(n + 1))

print("计算1到1000000的和:")
result = calculate_sum(1000000)
print(f"结果: {result}")

# 2. 带参数的装饰器
print("\n=== 带参数的装饰器 ===")

def repeat_decorator(times):
    """重复执行装饰器"""
    def decorator(func):
        def wrapper(*args, **kwargs):
            results = []
            for i in range(times):
                print(f"第{i+1}次执行 {func.__name__}")
                result = func(*args, **kwargs)
                results.append(result)
            return results
        return wrapper
    return decorator

def validate_decorator(min_val=None, max_val=None):
    """参数验证装饰器"""
    def decorator(func):
        def wrapper(*args, **kwargs):
            # 验证参数
            for arg in args:
                if min_val is not None and arg < min_val:
                    raise ValueError(f"参数不能小于 {min_val}")
                if max_val is not None and arg > max_val:
                    raise ValueError(f"参数不能大于 {max_val}")
            return func(*args, **kwargs)
        return wrapper
    return decorator

# 使用带参数的装饰器
@repeat_decorator(3)
def greet(name):
    """问候函数"""
    return f"Hello, {name}!"

@validate_decorator(min_val=1, max_val=100)
def process_number(num):
    """处理数字"""
    return num * 2

print("\n重复执行装饰器:")
greetings = greet("Alice")
for i, greeting in enumerate(greetings, 1):
    print(f"第{i}次结果: {greeting}")

print("\n参数验证装饰器:")
try:
    result = process_number(50)
    print(f"处理结果: {result}")
    # result = process_number(0)  # 会引发异常
except ValueError as e:
    print(f"错误: {e}")

# 3. 类装饰器
print("\n=== 类装饰器 ===")

class CountCalls:
    """计数装饰器类"""
    def __init__(self, func):
        self.func = func
        self.call_count = 0

    def __call__(self, *args, **kwargs):
        self.call_count += 1
        print(f"第{self.call_count}次调用 {self.func.__name__}")
        return self.func(*args, **kwargs)

class DebugDecorator:
    """调试装饰器类"""
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        print(f"DEBUG: 调用 {self.func.__name__}")
        print(f"DEBUG: 参数: {args}, {kwargs}")
        try:
            result = self.func(*args, **kwargs)
            print(f"DEBUG: 返回值: {result}")
            return result
        except Exception as e:
            print(f"DEBUG: 异常: {e}")
            raise

# 使用类装饰器
@CountCalls
@DebugDecorator
def calculate_factorial(n):
    """计算阶乘"""
    if n < 0:
        raise ValueError("n不能为负数")
    if n == 0:
        return 1
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

print("\n类装饰器示例:")
result1 = calculate_factorial(5)
result2 = calculate_factorial(3)
print(f"结果: {result1}, {result2}")

# 4. 方法装饰器
print("\n=== 方法装饰器 ===")

def method_timer(method):
    """方法计时装饰器"""
    import time
    def wrapper(self, *args, **kwargs):
        start_time = time.time()
        result = method(self, *args, **kwargs)
        end_time = time.time()
        print(f"{self.__class__.__name__}.{method.__name__} 执行时间: {end_time - start_time:.4f}秒")
        return result
    return wrapper

class DataProcessor:
    """数据处理器类"""
    def __init__(self, data):
        self.data = data

    @method_timer
    def process_data(self):
        """处理数据"""
        import time
        time.sleep(0.1)  # 模拟处理时间
        return [x * 2 for x in self.data]

    @method_timer
    def filter_data(self, threshold):
        """过滤数据"""
        return [x for x in self.data if x > threshold]

# 使用方法装饰器
processor = DataProcessor([1, 2, 3, 4, 5])
processed = processor.process_data()
filtered = processor.filter_data(3)
print(f"处理后数据: {processed}")
print(f"过滤后数据: {filtered}")

# 5. 装饰器链
print("\n=== 装饰器链 ===")

def auth_decorator(func):
    """认证装饰器"""
    def wrapper(*args, **kwargs):
        print("检查认证...")
        # 模拟认证检查
        authenticated = kwargs.get('authenticated', False)
        if not authenticated:
            raise PermissionError("未认证")
        print("认证通过")
        return func(*args, **kwargs)
    return wrapper

def log_decorator(func):
    """日志装饰器"""
    def wrapper(*args, **kwargs):
        print(f"LOG: 执行 {func.__name__}")
        return func(*args, **kwargs)
    return wrapper

def cache_decorator(func):
    """缓存装饰器"""
    cache = {}
    def wrapper(*args, **kwargs):
        key = str(args) + str(kwargs)
        if key in cache:
            print(f"缓存命中: {key}")
            return cache[key]
        print(f"缓存未命中，计算结果: {key}")
        result = func(*args, **kwargs)
        cache[key] = result
        return result
    return wrapper

# 装饰器链
@cache_decorator
@log_decorator
@auth_decorator
def get_user_data(user_id, authenticated=False):
    """获取用户数据"""
    print(f"获取用户 {user_id} 的数据")
    return {"id": user_id, "name": f"User{user_id}"}

print("\n装饰器链示例:")
# 第一次调用（未认证）
try:
    result = get_user_data(1)
except PermissionError as e:
    print(f"错误: {e}")

# 第二次调用（已认证）
result1 = get_user_data(1, authenticated=True)
print(f"结果: {result1}")

# 第三次调用（缓存命中）
result2 = get_user_data(1, authenticated=True)
print(f"结果: {result2}")

# 6. functools.wraps装饰器
print("\n=== functools.wraps装饰器 ===")

import functools

def preserve_metadata_decorator(func):
    """保持原函数元数据的装饰器"""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        """包装器函数"""
        print(f"执行 {func.__name__}")
        return func(*args, **kwargs)
    return wrapper

def without_wraps_decorator(func):
    """不保持原函数元数据的装饰器"""
    def wrapper(*args, **kwargs):
        print(f"执行 {func.__name__}")
        return func(*args, **kwargs)
    return wrapper

# 使用装饰器
@preserve_metadata_decorator
def add(a, b):
    """加法函数"""
    return a + b

@without_wraps_decorator
def subtract(a, b):
    """减法函数"""
    return a - b

print("\n保持元数据:")
print(f"函数名: {add.__name__}")
print(f"文档字符串: {add.__doc__}")
print(f"函数签名: {add.__annotations__}")

print("\n未保持元数据:")
print(f"函数名: {subtract.__name__}")
print(f"文档字符串: {subtract.__doc__}")

# 7. 元类基础
print("\n=== 元类基础 ===")

class Meta(type):
    """自定义元类"""
    def __new__(cls, name, bases, attrs):
        print(f"创建类: {name}")
        print(f"基类: {bases}")
        print(f"属性: {list(attrs.keys())}")

        # 添加新属性
        attrs['created_by'] = 'Meta'
        attrs['version'] = '1.0'

        return super().__new__(cls, name, bases, attrs)

class MyClass(metaclass=Meta):
    """使用元类的类"""
    def __init__(self, value):
        self.value = value

# 使用元类创建的类
instance = MyClass(42)
print(f"\n实例属性: {instance.value}")
print(f"类属性: {MyClass.created_by}, {MyClass.version}")

# 8. 元类应用：单例模式
print("\n=== 元类应用：单例模式 ===")

class SingletonMeta(type):
    """单例元类"""
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]

class SingletonClass(metaclass=SingletonMeta):
    """单例类"""
    def __init__(self, value):
        self.value = value

    def get_value(self):
        return self.value

# 测试单例
singleton1 = SingletonClass("第一次")
singleton2 = SingletonClass("第二次")

print(f"实例1: {id(singleton1)}")
print(f"实例2: {id(singleton2)}")
print(f"是否为同一实例: {singleton1 is singleton2}")
print(f"值: {singleton1.get_value()}")

# 9. 元类应用：属性验证
print("\n=== 元类应用：属性验证 ===")

class ValidateMeta(type):
    """验证元类"""
    def __new__(cls, name, bases, attrs):
        # 查找验证属性
        for attr_name, attr_value in attrs.items():
            if hasattr(attr_value, '__call__') and not attr_name.startswith('_'):
                # 为方法添加验证装饰器
                attrs[attr_name] = cls._add_validation(attr_value)

        return super().__new__(cls, name, bases, attrs)

    @staticmethod
    def _add_validation(func):
        """添加验证装饰器"""
        def wrapper(*args, **kwargs):
            # 验证第一个参数（self）的属性
            if args and hasattr(args[0], '_validate'):
                args[0]._validate()
            return func(*args, **kwargs)
        return wrapper

class ValidatedPerson(metaclass=ValidateMeta):
    """被验证的人员类"""
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def _validate(self):
        """验证方法"""
        if not isinstance(self.name, str):
            raise ValueError("姓名必须是字符串")
        if not isinstance(self.age, int) or self.age < 0:
            raise ValueError("年龄必须是正整数")

    def introduce(self):
        """介绍方法"""
        return f"我叫{self.name}，今年{self.age}岁"

# 测试属性验证
person = ValidatedPerson("张三", 25)
print(f"介绍: {person.introduce()}")

try:
    invalid_person = ValidatedPerson(123, -5)
    invalid_person.introduce()
except ValueError as e:
    print(f"验证错误: {e}")

# 10. 元类应用：ORM风格
print("\n=== 元类应用：ORM风格 ===")

class ORMMeta(type):
    """ORM元类"""
    def __new__(cls, name, bases, attrs):
        # 收集字段信息
        fields = {}
        for attr_name, attr_value in attrs.items():
            if not attr_name.startswith('_') and not hasattr(attr_value, '__call__'):
                fields[attr_name] = attr_value

        # 添加字段信息到类属性
        attrs['_fields'] = fields
        attrs['get_fields'] = lambda self: fields

        return super().__new__(cls, name, bases, attrs)

class Model(metaclass=ORMMeta):
    """模型基类"""
    def __init__(self, **kwargs):
        for field_name, field_value in kwargs.items():
            if field_name in self._fields:
                setattr(self, field_name, field_value)

    def to_dict(self):
        """转换为字典"""
        return {field: getattr(self, field) for field in self._fields}

class User(Model):
    """用户模型"""
    name = str
    age = int
    email = str

# 使用ORM风格类
user = User(name="李四", age=30, email="lisi@example.com")
print(f"用户信息: {user.to_dict()}")
print(f"字段: {user.get_fields()}")

# 11. 描述符协议
print("\n=== 描述符协议 ===")

class ValidatedAttribute:
    """验证属性描述符"""
    def __init__(self, attribute_type, min_value=None, max_value=None):
        self.attribute_type = attribute_type
        self.min_value = min_value
        self.max_value = max_value
        self.name = None

    def __set_name__(self, owner, name):
        self.name = name

    def __get__(self, instance, owner):
        if instance is None:
            return self
        if self.name not in instance.__dict__:
            raise AttributeError(f"'{owner.__name__}' object has no attribute '{self.name}'")
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        if not isinstance(value, self.attribute_type):
            raise TypeError(f"{self.name} 必须是 {self.attribute_type.__name__} 类型")
        if self.min_value is not None and value < self.min_value:
            raise ValueError(f"{self.name} 不能小于 {self.min_value}")
        if self.max_value is not None and value > self.max_value:
            raise ValueError(f"{self.name} 不能大于 {self.max_value}")
        instance.__dict__[self.name] = value

class Product:
    """产品类"""
    price = ValidatedAttribute((int, float), min_value=0)
    stock = ValidatedAttribute(int, min_value=0)
    name = ValidatedAttribute(str)

# 使用描述符
product = Product()
product.name = "iPhone"
product.price = 9999
product.stock = 100

print(f"产品信息: {product.name}, 价格: {product.price}, 库存: {product.stock}")

try:
    product.price = -100  # 会引发异常
except ValueError as e:
    print(f"描述符验证错误: {e}")

# 12. 装饰器工厂
print("\n=== 装饰器工厂 ===")

def create_decorator(prefix="DEBUG"):
    """装饰器工厂"""
    def decorator(func):
        def wrapper(*args, **kwargs):
            print(f"{prefix}: 调用 {func.__name__}")
            return func(*args, **kwargs)
        return wrapper
    return decorator

# 使用装饰器工厂
info_decorator = create_decorator("INFO")
warning_decorator = create_decorator("WARNING")

@info_decorator
def process_data():
    """处理数据"""
    print("数据处理中...")

@warning_decorator
def backup_data():
    """备份数据"""
    print("数据备份中...")

print("\n装饰器工厂示例:")
process_data()
backup_data()

# 13. 上下文装饰器
print("\n=== 上下文装饰器 ===")

from contextlib import contextmanager

@contextmanager
def performance_monitor():
    """性能监控上下文"""
    import time
    start_time = time.time()
    try:
        yield
    finally:
        end_time = time.time()
        print(f"执行时间: {end_time - start_time:.4f}秒")

# 使用上下文装饰器
def intensive_operation():
    """密集操作"""
    with performance_monitor():
        import time
        time.sleep(0.1)
        print("密集操作完成")

print("\n上下文装饰器示例:")
intensive_operation()

# 14. 装饰器最佳实践
print("\n=== 装饰器最佳实践 ===")

def debug_decorator(func):
    """调试装饰器（最佳实践）"""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f"DEBUG: {func.__name__} 开始执行")
        try:
            result = func(*args, **kwargs)
            print(f"DEBUG: {func.__name__} 执行成功")
            return result
        except Exception as e:
            print(f"DEBUG: {func.__name__} 执行失败: {e}")
            raise
    return wrapper

class DatabaseConnection:
    """数据库连接类"""
    def __init__(self, host, port):
        self.host = host
        self.port = port

    @debug_decorator
    def connect(self):
        """连接数据库"""
        print(f"连接到 {self.host}:{self.port}")
        return True

    @debug_decorator
    def query(self, sql):
        """执行查询"""
        print(f"执行查询: {sql}")
        return ["结果1", "结果2", "结果3"]

# 使用最佳实践装饰器
db = DatabaseConnection("localhost", 5432)
db.connect()
results = db.query("SELECT * FROM users")
print(f"查询结果: {results}")

# 15. 装饰器的局限性
print("\n=== 装饰器的局限性 ===")

print("""
装饰器的局限性：
1. 装饰器会改变原函数的元数据（除非使用functools.wraps）
2. 装饰器可能影响函数的可读性
3. 装饰器的调用顺序可能影响结果
4. 装饰器可能导致调试困难
5. 装饰器不能用于重载操作符（如__add__）
""")

# 16. 清理和总结
print("\n=== 清理和总结 ===")

print("""
装饰器和元类的应用场景：

装饰器适合：
- 日志记录
- 性能监控
- 权限验证
- 缓存
- 参数验证
- 重试机制

元类适合：
- ORM框架
- 单例模式
- 属性验证
- 类注册
- 框架设计

选择建议：
- 简单需求使用装饰器
- 复杂类级别控制使用元类
- 优先考虑代码的可读性和维护性
""")

print("\n程序执行完毕！")