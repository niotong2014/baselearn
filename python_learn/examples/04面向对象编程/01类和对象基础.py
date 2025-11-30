#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Python类和对象基础示例
"""

# 1. 类的基本定义
print("=== 类的基本定义 ===")

class Person:
    """人类"""

    # 类变量（所有实例共享）
    species = "人类"

    # 构造函数
    def __init__(self, name, age):
        """初始化实例"""
        self.name = name  # 实例变量
        self.age = age    # 实例变量

    # 实例方法
    def introduce(self):
        """自我介绍"""
        return f"大家好，我叫{self.name}，今年{self.age}岁"

    # 类方法
    @classmethod
    def get_species(cls):
        """获取物种信息"""
        return cls.species

    # 静态方法
    @staticmethod
    def is_adult(age):
        """判断是否成年"""
        return age >= 18

# 创建实例
person1 = Person("张三", 25)
person2 = Person("李四", 17)

print(f"实例1: {person1.introduce()}")
print(f"实例2: {person2.introduce()}")

# 访问类变量
print(f"物种: {Person.get_species()}")
print(f"张三是成年吗: {Person.is_adult(person1.age)}")
print(f"李四是成年吗: {Person.is_adult(person2.age)}")

# 2. 访问控制
print("\n=== 访问控制 ===")

class BankAccount:
    """银行账户类"""

    def __init__(self, account_number, balance=0):
        self._account_number = account_number  # 受保护属性
        self.__balance = balance  # 私有属性

    def get_balance(self):
        """获取余额"""
        return self.__balance

    def deposit(self, amount):
        """存款"""
        if amount > 0:
            self.__balance += amount
            return True
        return False

    def withdraw(self, amount):
        """取款"""
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            return True
        return False

    def _validate_account(self):
        """验证账户（内部方法）"""
        return len(str(self._account_number)) == 10

# 创建银行账户
account = BankAccount("1234567890", 1000)

print(f"账户余额: {account.get_balance()}")
account.deposit(500)
print(f"存款后余额: {account.get_balance()}")
account.withdraw(200)
print(f"取款后余额: {account.get_balance()}")

# 访问受保护属性（不推荐但可以访问）
print(f"账户号码: {account._account_number}")

# 尝试访问私有属性（会报错）
try:
    print(f"直接访问余额: {account.__balance}")
except AttributeError as e:
    print(f"错误: {e}")

# 3. 属性装饰器
print("\n=== 属性装饰器 ===")

class Temperature:
    """温度类"""

    def __init__(self, celsius=0):
        self._celsius = celsius

    @property
    def celsius(self):
        """获取摄氏温度"""
        return self._celsius

    @celsius.setter
    def celsius(self, value):
        """设置摄氏温度"""
        if -273.15 <= value <= 1000:
            self._celsius = value
        else:
            raise ValueError("温度超出有效范围")

    @property
    def fahrenheit(self):
        """获取华氏温度"""
        return self._celsius * 9/5 + 32

    @fahrenheit.setter
    def fahrenheit(self, value):
        """设置华氏温度"""
        celsius = (value - 32) * 5/9
        self.celsius = celsius

# 使用温度类
temp = Temperature(25)
print(f"摄氏温度: {temp.celsius}°C")
print(f"华氏温度: {temp.fahrenheit:.1f}°F")

# 通过属性设置器修改值
temp.celsius = 30
print(f"修改后摄氏温度: {temp.celsius}°C")
print(f"修改后华氏温度: {temp.fahrenheit:.1f}°F")

# 通过华氏温度设置
temp.fahrenheit = 86
print(f"通过华氏温度设置后: {temp.celsius}°C")

# 4. 继承
print("\n=== 继承 ===")

class Animal:
    """动物基类"""

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def speak(self):
        """发出声音"""
        return "动物发出声音"

    def info(self):
        """获取信息"""
        return f"{self.name}，{self.age}岁"

class Dog(Animal):
    """狗类"""

    def __init__(self, name, age, breed):
        super().__init__(name, age)
        self.breed = breed

    def speak(self):
        """狗叫"""
        return "汪汪！"

    def fetch(self):
        """接飞盘"""
        return f"{self.name}在接飞盘"

class Cat(Animal):
    """猫类"""

    def __init__(self, name, age, color):
        super().__init__(name, age)
        self.color = color

    def speak(self):
        """猫叫"""
        return "喵喵~"

    def climb(self):
        """爬树"""
        return f"{self.color}的{self.name}在爬树"

# 创建实例
dog = Dog("旺财", 3, "金毛")
cat = Cat("咪咪", 2, "白色")

print(f"狗: {dog.info()}")
print(f"狗叫: {dog.speak()}")
print(f"狗接飞盘: {dog.fetch()}")

print(f"\n猫: {cat.info()}")
print(f"猫叫: {cat.speak()}")
print(f"猫爬树: {cat.climb()}")

# 5. 多重继承
print("\n=== 多重继承 ===")

class Flyable:
    """可飞行的特性"""

    def fly(self):
        return "可以飞行"

class Swimmable:
    """可游泳的特性"""

    def swim(self):
        return "可以游泳"

class Duck(Animal, Flyable, Swimmable):
    """鸭子类"""

    def __init__(self, name, age):
        super().__init__(name, age)

    def speak(self):
        return "嘎嘎！"

# 创建鸭子实例
duck = Duck("唐老鸭", 5)
print(f"\n鸭子: {duck.info()}")
print(f"鸭子叫: {duck.speak()}")
print(f"鸭子飞行: {duck.fly()}")
print(f"鸭子游泳: {duck.swim()}")

# 6. 方法重写
print("\n=== 方法重写 ===")

class Shape:
    """图形基类"""

    def area(self):
        """计算面积"""
        return 0

    def perimeter(self):
        """计算周长"""
        return 0

class Rectangle(Shape):
    """矩形类"""

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        """计算矩形面积"""
        return self.width * self.height

    def perimeter(self):
        """计算矩形周长"""
        return 2 * (self.width + self.height)

    def __str__(self):
        return f"矩形({self.width}x{self.height})"

class Circle(Shape):
    """圆形类"""

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        """计算圆面积"""
        import math
        return math.pi * self.radius ** 2

    def perimeter(self):
        """计算圆周长"""
        import math
        return 2 * math.pi * self.radius

    def __str__(self):
        return f"圆形(半径={self.radius})"

# 创建图形实例
rectangle = Rectangle(5, 3)
circle = Circle(4)

print(f"{rectangle}: 面积={rectangle.area()}, 周长={rectangle.perimeter()}")
print(f"{circle}: 面积={circle.area():.2f}, 周长={circle.perimeter():.2f}")

# 7. 抽象基类
print("\n=== 抽象基类 ===")

from abc import ABC, abstractmethod

class Vehicle(ABC):
    """交通工具抽象基类"""

    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    @abstractmethod
    def start_engine(self):
        """启动发动机（抽象方法）"""
        pass

    @abstractmethod
    def stop_engine(self):
        """停止发动机（抽象方法）"""
        pass

    def info(self):
        """获取车辆信息"""
        return f"{self.brand} {self.model}"

class Car(Vehicle):
    """汽车类"""

    def start_engine(self):
        """启动汽车发动机"""
        return f"{self.brand} {self.model}发动机已启动"

    def stop_engine(self):
        """停止汽车发动机"""
        return f"{self.brand} {self.model}发动机已停止"

class Motorcycle(Vehicle):
    """摩托车类"""

    def start_engine(self):
        """启动摩托车发动机"""
        return f"{self.brand} {self.model}摩托车发动机已启动"

    def stop_engine(self):
        """停止摩托车发动机"""
        return f"{self.brand} {self.model}摩托车发动机已停止"

# 创建交通工具实例
car = Car("Toyota", "Camry")
motorcycle = Motorcycle("Honda", "CBR")

print(f"汽车: {car.info()}")
print(car.start_engine())
print(car.stop_engine())

print(f"\n摩托车: {motorcycle.info()}")
print(motorcycle.start_engine())
print(motorcycle.stop_engine())

# 8. 运算符重载
print("\n=== 运算符重载 ===")

class Vector:
    """向量类"""

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        """加法运算符重载"""
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        """减法运算符重载"""
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, scalar):
        """乘法运算符重载"""
        return Vector(self.x * scalar, self.y * scalar)

    def __eq__(self, other):
        """等于运算符重载"""
        return self.x == other.x and self.y == other.y

    def __str__(self):
        """字符串表示"""
        return f"Vector({self.x}, {self.y})"

    def __repr__(self):
        """对象表示"""
        return self.__str__()

# 创建向量实例
v1 = Vector(3, 4)
v2 = Vector(1, 2)
v3 = Vector(3, 4)

print(f"向量1: {v1}")
print(f"向量2: {v2}")
print(f"向量3: {v3}")

print(f"v1 + v2 = {v1 + v2}")
print(f"v1 - v2 = {v1 - v2}")
print(f"v1 * 2 = {v1 * 2}")
print(f"v1 == v2: {v1 == v2}")
print(f"v1 == v3: {v1 == v3}")

# 9. 实例属性和类属性
print("\n=== 实例属性和类属性 ===")

class Employee:
    """员工类"""

    # 类变量
    company = "ABC公司"
    employee_count = 0

    def __init__(self, name, salary):
        # 实例变量
        self.name = name
        self.salary = salary
        self.employee_id = Employee.employee_count + 1

        # 更新类变量
        Employee.employee_count += 1

    @classmethod
    def get_employee_count(cls):
        """获取员工总数"""
        return cls.employee_count

    def display_info(self):
        """显示员工信息"""
        return f"{self.name} (ID: {self.employee_id}), 工资: {self.salary}, 公司: {self.company}"

# 创建员工实例
emp1 = Employee("张三", 5000)
emp2 = Employee("李四", 6000)
emp3 = Employee("王五", 7000)

print(emp1.display_info())
print(emp2.display_info())
print(emp3.display_info())

print(f"\n员工总数: {Employee.get_employee_count()}")
print(f"公司名称: {Employee.company}")

# 修改类变量
Employee.company = "XYZ公司"
print(f"修改后的公司名称: {Employee.company}")
print(emp1.display_info())

# 10. 特殊方法（魔术方法）
print("\n=== 特殊方法（魔术方法） ===")

class Book:
    """书籍类"""

    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def __len__(self):
        """返回页数"""
        return self.pages

    def __getitem__(self, key):
        """支持切片操作"""
        if isinstance(key, slice):
            start = key.start or 0
            stop = key.stop or self.pages
            step = key.step or 1
            return list(range(start, stop, step))
        elif isinstance(key, int):
            return f"第{key+1}页"
        else:
            raise TypeError("无效的索引类型")

    def __contains__(self, item):
        """检查是否包含"""
        return item.lower() in self.title.lower() or item.lower() in self.author.lower()

    def __call__(self, page):
        """使对象可调用"""
        if 1 <= page <= self.pages:
            return f"正在阅读《{self.title}》第{page}页"
        else:
            return "页码超出范围"

# 创建书籍实例
book = Book("Python编程", "张三", 300)

print(f"书籍信息: 《{book.title}》 by {book.author}")
print(f"页数: {len(book)}")

# 切片操作
print(f"前10页: {book[:10]}")
print(f"第5页: {book[4]}")

# 包含检查
print(f"包含'Python': {'Python' in book}")
print(f"包含'张三': {'张三' in book}")

# 调用对象
print(book(50))
print(book(500))

print("\n程序执行完毕！")