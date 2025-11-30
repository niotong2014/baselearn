#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Python字典(Dictionary)数据结构示例
"""

# 1. 字典创建
print("=== 字典创建 ===")

# 空字典
empty_dict = {}
print(f"空字典: {empty_dict}")

# 使用键值对
person = {
    "name": "张三",
    "age": 25,
    "city": "北京",
    "is_student": False
}
print(f"人物信息: {person}")

# 使用dict()构造函数
student = dict(name="李四", age=20, grade="A")
print(f"学生信息: {student}")

# 使用列表创建字典
keys = ["a", "b", "c"]
values = [1, 2, 3]
dict_from_lists = dict(zip(keys, values))
print(f"从列表创建: {dict_from_lists}")

# 字典推导式
squares = {x: x**2 for x in range(1, 6)}
print(f"平方字典: {squares}")

even_squares = {x: x**2 for x in range(1, 11) if x % 2 == 0}
print(f"偶数平方字典: {even_squares}")

# 2. 字典基本操作
print("\n=== 字典基本操作 ===")

colors = {
    "red": "红色",
    "green": "绿色",
    "blue": "蓝色"
}
print(f"颜色字典: {colors}")

# 访问值
print(f"red的值: {colors['red']}")

# 使用get()方法（更安全）
print(f"yellow的值: {colors.get('yellow', '未知颜色')}")

# 检查键是否存在
print(f"'green'在字典中吗? {'green' in colors}")
print(f"'yellow'在字典中吗? {'yellow' in colors}")

# 字典长度
print(f"字典长度: {len(colors)}")

# 3. 字典修改
print("\n=== 字典修改 ===")

scores = {"数学": 85, "英语": 90, "语文": 88}
print(f"原始分数: {scores}")

# 添加或修改键值对
scores["物理"] = 92
print(f"添加物理: {scores}")

scores["数学"] = 88  # 修改已有键
print(f"修改数学: {scores}")

# 使用update()更新多个键值对
scores.update({"化学": 87, "生物": 85})
print(f"批量更新: {scores}")

# 4. 删除操作
print("\n=== 删除操作 ===")

inventory = {
    "苹果": 10,
    "香蕉": 15,
    "橙子": 8,
    "葡萄": 20
}
print(f"原始库存: {inventory}")

# 删除指定键
del inventory["橙子"]
print(f"删除橙子: {inventory}")

# 使用pop()删除并返回值
removed_value = inventory.pop("香蕉")
print(f"pop香蕉: {inventory}, 删除的值: {removed_value}")

# 使用popitem()删除并返回最后一个键值对（Python 3.7+）
last_item = inventory.popitem()
print(f"popitem: {inventory}, 删除的项: {last_item}")

# 清空字典
inventory.clear()
print(f"清空后: {inventory}")

# 5. 字典遍历
print("\n=== 字典遍历 ===")

student_grades = {
    "张三": 85,
    "李四": 92,
    "王五": 78,
    "赵六": 88
}

# 遍历键
print("遍历键:")
for name in student_grades.keys():
    print(name)

# 遍历值
print("\n遍历值:")
for grade in student_grades.values():
    print(grade)

# 遍历键值对
print("\n遍历键值对:")
for name, grade in student_grades.items():
    print(f"{name}: {grade}分")

# 使用enumerate
print("\n带索引遍历:")
for index, (name, grade) in enumerate(student_grades.items()):
    print(f"{index + 1}. {name}: {grade}分")

# 6. 字典方法
print("\n=== 字典方法 ===")

config = {
    "host": "localhost",
    "port": 8080,
    "debug": True
}

# 获取所有键
print(f"所有键: {list(config.keys())}")

# 获取所有值
print(f"所有值: {list(config.values())}")

# 获取所有键值对
print(f"所有键值对: {list(config.items())}")

# 设置默认值
default_value = config.setdefault("timeout", 30)
print(f"设置默认值timeout: {config}, 返回值: {default_value}")

# 创建新字典（不存在的键使用默认值）
new_dict = config.fromkeys(["host", "port", "timeout"], "unknown")
print(f"fromkeys创建: {new_dict}")

# 7. 嵌套字典
print("\n=== 嵌套字典 ===")

company = {
    "name": "ABC公司",
    "departments": {
        "技术部": {
            "employees": ["张三", "李四", "王五"],
            "budget": 500000
        },
        "市场部": {
            "employees": ["赵六", "钱七"],
            "budget": 300000
        }
    },
    "location": {
        "city": "北京",
        "address": "朝阳区xxx街xxx号"
    }
}

print(f"公司信息: {company}")

# 访问嵌套字典
print(f"公司名称: {company['name']}")
print(f"技术部员工: {company['departments']['技术部']['employees']}")
print(f"公司地址: {company['location']['city']}")

# 遍历嵌套字典
print("\n遍历嵌套字典:")
for dept_name, dept_info in company["departments"].items():
    print(f"{dept_name}:")
    print(f"  员工: {dept_info['employees']}")
    print(f"  预算: {dept_info['budget']}")

# 8. 字典排序
print("\n=== 字典排序 ===")

unsorted_dict = {"banana": 3, "apple": 1, "orange": 2, "grape": 4}
print(f"未排序字典: {unsorted_dict}")

# 按键排序
sorted_by_key = dict(sorted(unsorted_dict.items()))
print(f"按键排序: {sorted_by_key}")

# 按值排序
sorted_by_value = dict(sorted(unsorted_dict.items(), key=lambda x: x[1]))
print(f"按值排序: {sorted_by_value}")

# 降序排序
sorted_desc = dict(sorted(unsorted_dict.items(), key=lambda x: x[1], reverse=True))
print(f"按值降序排序: {sorted_desc}")

# 9. 字典的实际应用
print("\n=== 字典的实际应用 ===")

def count_words(text):
    """统计词频"""
    words = text.lower().split()
    word_count = {}

    for word in words:
        # 去除标点符号
        word = word.strip(".,!?;:\"'()[]{}")
        word_count[word] = word_count.get(word, 0) + 1

    return word_count

def find_most_common(word_count):
    """找出最常见的词"""
    if not word_count:
        return None, 0

    max_count = max(word_count.values())
    most_common = [word for word, count in word_count.items() if count == max_count]

    return most_common[0] if len(most_common) == 1 else most_common, max_count

# 测试词频统计
sample_text = "Python is a great programming language. Python is versatile and easy to learn. Many developers love Python."
word_count = count_words(sample_text)
most_common_word, count = find_most_common(word_count)

print(f"示例文本: {sample_text}")
print(f"词频统计: {word_count}")
print(f"最常见的词: '{most_common_word}' (出现{count}次)")

# 10. 字典合并
print("\n=== 字典合并 ===")

dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}
dict3 = {"b": 20, "e": 5}  # 有重复的键

# 使用update()（会修改原字典）
merged_dict = dict1.copy()
merged_dict.update(dict2)
print(f"update合并: {merged_dict}")

# 使用**运算符（Python 3.5+）
merged_dict2 = {**dict1, **dict2}
print(f"**运算符合并: {merged_dict2}")

# 处理键冲突（后面的会覆盖前面的）
merged_with_conflict = {**dict1, **dict3}
print(f"处理键冲突: {merged_with_conflict}")

# Python 3.9+ 的合并运算符
# merged_dict3 = dict1 | dict2  # Python 3.9+
# print(f"|运算符合并: {merged_dict3}")

# 11. 字典性能注意事项
print("\n=== 字典性能注意事项 ===")

import time

def test_dict_performance():
    """测试字典性能"""

    # 创建大型字典
    large_dict = {i: f"value_{i}" for i in range(100000)}

    # 测试查找性能
    start = time.time()
    for i in range(1000):
        value = large_dict.get(i * 100)
    end = time.time()
    print(f"字典查找1000次: {end - start:.4f}秒")

    # 测试插入性能
    start = time.time()
    for i in range(10000, 20000):
        large_dict[i] = f"new_value_{i}"
    end = time.time()
    print(f"字典插入10000个元素: {end - start:.4f}秒")

print("字典性能测试:")
test_dict_performance()

# 12. 实用字典函数
print("\n=== 实用字典函数 ===")

def invert_dict(original_dict):
    """反转字典（键值互换）"""
    return {value: key for key, value in original_dict.items()}

def filter_dict(dictionary, condition):
    """过滤字典"""
    return {key: value for key, value in dictionary.items() if condition(key, value)}

def group_by(lst, key_func):
    """按条件分组"""
    groups = {}
    for item in lst:
        key = key_func(item)
        groups[key] = groups.get(key, [])
        groups[key].append(item)
    return groups

# 测试实用函数
original = {"a": 1, "b": 2, "c": 3}
inverted = invert_dict(original)
print(f"原字典: {original}")
print(f"反转字典: {inverted}")

scores = {"张三": 85, "李四": 92, "王五": 78, "赵六": 88}
high_scores = filter_dict(scores, lambda k, v: v >= 85)
print(f"高分学生: {high_scores}")

students = [
    {"name": "张三", "age": 20},
    {"name": "李四", "age": 20},
    {"name": "王五", "age": 21}
]
by_age = group_by(students, lambda x: x["age"])
print(f"按年龄分组: {by_age}")

# 13. 字典vs列表
print("\n=== 字典vs列表 ===")

# 查找性能对比
def search_performance():
    data_size = 100000

    # 创建列表和字典
    search_list = list(range(data_size))
    search_dict = {i: f"value_{i}" for i in range(data_size)}

    # 列表查找
    start = time.time()
    for i in range(1000):
        target = i * 100
        found = target in search_list
    end = time.time()
    list_time = end - start

    # 字典查找
    start = time.time()
    for i in range(1000):
        target = i * 100
        found = target in search_dict
    end = time.time()
    dict_time = end - start

    print(f"列表查找1000次: {list_time:.4f}秒")
    print(f"字典查找1000次: {dict_time:.4f}秒")
    print(f"字典比列表快 {list_time/dict_time:.1f} 倍")

print("查找性能对比:")
search_performance()

print("\n程序执行完毕！")