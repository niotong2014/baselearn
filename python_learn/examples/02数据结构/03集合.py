#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Python集合(Set)数据结构示例
"""

# 1. 集合创建
print("=== 集合创建 ===")

# 空集合（注意：不能使用{}，因为这是空字典）
empty_set = set()
print(f"空集合: {empty_set}")

# 使用大括号创建集合
fruits = {"苹果", "香蕉", "橙子", "苹果"}  # 重复元素会被自动去除
print(f"水果集合: {fruits}")

# 使用set()函数创建
numbers = set([1, 2, 3, 2, 4, 3, 5])
print(f"数字集合: {numbers}")

# 从字符串创建
string_set = set("Hello")
print(f"字符串集合: {string_set}")

# 集合推导式
squares = {x**2 for x in range(1, 6)}
print(f"平方集合: {squares}")

even_numbers = {x for x in range(10) if x % 2 == 0}
print(f"偶数集合: {even_numbers}")

# 2. 集合基本操作
print("\n=== 集合基本操作 ===")

colors = {"红色", "绿色", "蓝色"}
print(f"颜色集合: {colors}")

# 添加元素
colors.add("黄色")
print(f"添加黄色: {colors}")

# 删除元素
colors.remove("绿色")
print(f"删除绿色: {colors}")

# 使用discard()删除（元素不存在不会报错）
colors.discard("紫色")  # 不会报错
colors.discard("蓝色")
print(f"删除蓝色: {colors}")

# 清空集合
colors.clear()
print(f"清空后: {colors}")

# 3. 集合运算
print("\n=== 集合运算 ===")

set_a = {1, 2, 3, 4, 5}
set_b = {4, 5, 6, 7, 8}

print(f"集合A: {set_a}")
print(f"集合B: {set_b}")

# 并集（所有不重复的元素）
union_set = set_a | set_b
union_set_method = set_a.union(set_b)
print(f"并集(|): {union_set}")
print(f"并集(union): {union_set_method}")

# 交集（两个集合都包含的元素）
intersection_set = set_a & set_b
intersection_set_method = set_a.intersection(set_b)
print(f"交集(&): {intersection_set}")
print(f"交集(intersection): {intersection_set_method}")

# 差集（在A中但不在B中的元素）
difference_set = set_a - set_b
difference_set_method = set_a.difference(set_b)
print(f"差集(-): {difference_set}")
print(f"差集(difference): {difference_set_method}")

# 对称差集（只在其中一个集合中出现的元素）
symmetric_diff_set = set_a ^ set_b
symmetric_diff_set_method = set_a.symmetric_difference(set_b)
print(f"对称差集(^): {symmetric_diff_set}")
print(f"对称差集(symmetric_difference): {symmetric_diff_set_method}")

# 4. 集合关系
print("\n=== 集合关系 ===")

set1 = {1, 2, 3}
set2 = {1, 2, 3, 4, 5}
set3 = {1, 2}

print(f"集合1: {set1}")
print(f"集合2: {set2}")
print(f"集合3: {set3}")

# 子集判断
print(f"set1是set2的子集吗? {set1.issubset(set2)}")
print(f"set1 <= set2: {set1 <= set2}")

# 真子集判断
print(f"set1是set2的真子集吗? {set1 < set2}")
print(f"set2是set2的真子集吗? {set2 < set2}")

# 超集判断
print(f"set2是set1的超集吗? {set2.issuperset(set1)}")
print(f"set2 >= set1: {set2 >= set1}")

# 交集判断（两个集合是否有共同元素）
set4 = {1, 2}
set5 = {3, 4}
print(f"set4和set5有交集吗? {set4.isdisjoint(set5)}")

# 5. 集合方法
print("\n=== 集合方法 ===")

students = {"张三", "李四", "王五", "赵六"}

# 复制集合
students_copy = students.copy()
print(f"复制集合: {students_copy}")

# 批量添加
students.update({"钱七", "孙八"})
print(f"批量添加后: {students}")

# 批量删除
students.difference_update({"张三", "李四"})
print(f"批量删除后: {students}")

# 保留交集
students.intersection_update({"王五", "钱七", "周九"})
print(f"保留交集后: {students}")

# 保留差集
original_set = {1, 2, 3, 4, 5}
original_set.difference_update({1, 2})
print(f"保留差集后: {original_set}")

# 保留对称差集
sym_set = {1, 2, 3}
sym_set.symmetric_difference_update({2, 3, 4})
print(f"保留对称差集后: {sym_set}")

# 6. 集合遍历
print("\n=== 集合遍历 ===")

fruits = {"苹果", "香蕉", "橙子", "葡萄"}

# 基本遍历
print("基本遍历:")
for fruit in fruits:
    print(fruit)

# 带索引的遍历
print("\n带索引的遍历:")
for index, fruit in enumerate(fruits, 1):
    print(f"{index}. {fruit}")

# 集合推导式遍历
squares = {x**2 for x in range(1, 6)}
print(f"\n集合推导式结果: {squares}")

# 7. 冻结集合（frozenset）
print("\n=== 冻结集合 ===")

# 创建冻结集合
frozen_set = frozenset([1, 2, 3, 4, 5])
print(f"冻结集合: {frozen_set}")

# 冻结集合是不可变的，不能添加或删除元素
try:
    frozen_set.add(6)
except AttributeError as e:
    print(f"冻结集合添加元素错误: {e}")

# 冻结集合可以作为字典的键
dict_with_frozen_key = {frozenset([1, 2]): "value1", frozenset([3, 4]): "value2"}
print(f"冻结集合作为字典键: {dict_with_frozen_key}")

# 8. 集合的实际应用
print("\n=== 集合的实际应用 ===")

def remove_duplicates(lst):
    """去除列表中的重复元素"""
    return list(set(lst))

def find_common_elements(list1, list2):
    """找出两个列表的共同元素"""
    return list(set(list1) & set(list2))

def find_unique_elements(list1, list2):
    """找出只在其中一个列表中出现的元素"""
    return list(set(list1) ^ set(list2))

def find_unique_to_first(list1, list2):
    """找出只在第一个列表中出现的元素"""
    return list(set(list1) - set(list2))

# 测试集合应用
list1 = [1, 2, 2, 3, 4, 4, 5]
list2 = [4, 5, 5, 6, 7, 8]

print(f"列表1: {list1}")
print(f"列表2: {list2}")
print(f"去重后: {remove_duplicates(list1)}")
print(f"共同元素: {find_common_elements(list1, list2)}")
print(f"只在其中一个列表: {find_unique_elements(list1, list2)}")
print(f"只在第一个列表: {find_unique_to_first(list1, list2)}")

# 9. 集合性能分析
print("\n=== 集合性能分析 ===")

import time

def performance_test():
    """测试集合和列表的性能差异"""

    # 生成测试数据
    data_size = 100000
    search_data = list(range(data_size))
    search_set = set(search_data)
    test_numbers = list(range(0, data_size, data_size // 1000))

    # 测试列表查找
    start = time.time()
    for num in test_numbers:
        result = num in search_data
    end = time.time()
    list_time = end - start

    # 测试集合查找
    start = time.time()
    for num in test_numbers:
        result = num in search_set
    end = time.time()
    set_time = end - start

    print(f"数据大小: {data_size}")
    print(f"查找次数: {len(test_numbers)}")
    print(f"列表查找时间: {list_time:.4f}秒")
    print(f"集合查找时间: {set_time:.4f}秒")
    print(f"集合比列表快 {list_time / set_time:.1f} 倍")

print("性能测试:")
performance_test()

# 10. 高级集合应用
print("\n=== 高级集合应用 ===")

def word_frequency(text):
    """使用集合统计文本中的单词频率"""
    words = text.lower().split()
    unique_words = set(words)
    word_count = {}

    for word in unique_words:
        word_count[word] = words.count(word)

    return word_count

def find_anagrams(word, word_list):
    """找出字谜词"""
    word_sorted = sorted(word.lower())
    anagrams = []

    for w in word_list:
        if len(w) == len(word) and sorted(w.lower()) == word_sorted:
            anagrams.append(w)

    return anagrams

def power_set(s):
    """生成集合的幂集"""
    power_sets = []
    n = len(s)

    for i in range(1 << n):
        subset = set()
        for j in range(n):
            if i & (1 << j):
                subset.add(list(s)[j])
        power_sets.append(subset)

    return power_sets

# 测试高级应用
sample_text = "Python is great Python is useful Python is powerful"
print(f"示例文本: {sample_text}")
freq = word_frequency(sample_text)
print(f"词频统计: {freq}")

word = "listen"
word_list = ["listen", "silent", "enlist", "hello", "world"]
print(f"\n查找 '{word}' 的字谜词:")
anagrams = find_anagrams(word, word_list)
print(f"字谜词: {anagrams}")

test_set = {1, 2}
print(f"\n集合 {test_set} 的幂集:")
power_sets = power_set(test_set)
for subset in power_sets:
    print(subset)

# 11. 集合的数据验证应用
print("\n=== 集合的数据验证应用 ===")

def validate_email(email, valid_domains):
    """验证邮箱域名"""
    domain = email.split('@')[-1] if '@' in email else None
    return domain in valid_domains

def check_permissions(user_roles, required_permissions):
    """检查用户权限"""
    return user_roles.issuperset(required_permissions)

def find_missing_items(available, required):
    """找出缺少的项"""
    return required - available

# 测试数据验证
valid_email_domains = {"gmail.com", "outlook.com", "163.com"}
emails = ["user@gmail.com", "test@outlook.com", "invalid@yahoo.com"]

print("邮箱验证:")
for email in emails:
    is_valid = validate_email(email, valid_email_domains)
    print(f"{email}: {'有效' if is_valid else '无效'}")

user_permissions = {"read", "write", "execute"}
admin_permissions = {"read", "write", "execute", "delete"}

print(f"\n权限检查:")
print(f"用户权限: {user_permissions}")
print(f"需要管理员权限: {admin_permissions}")
print(f"是否有足够权限: {check_permissions(user_permissions, admin_permissions)}")

available_items = {"apple", "banana", "orange"}
required_items = {"apple", "banana", "grape"}

print(f"\n库存检查:")
print(f"可用: {available_items}")
print(f"需要: {required_items}")
print(f"缺少: {find_missing_items(available_items, required_items)}")

# 12. 集合的数学应用
print("\n=== 集合的数学应用 ===")

def set_operations_example():
    """集合运算的数学应用"""

    # 学生的选课情况
    math_students = {"张三", "李四", "王五", "赵六"}
    physics_students = {"李四", "王五", "钱七", "孙八"}
    chemistry_students = {"张三", "钱七", "周九"}

    print("学生选课情况:")
    print(f"数学: {math_students}")
    print(f"物理: {physics_students}")
    print(f"化学: {chemistry_students}")

    # 同时选数学和物理的学生
    math_physics = math_students & physics_students
    print(f"\n同时选数学和物理的学生: {math_physics}")

    # 只选数学的学生
    only_math = math_students - physics_students - chemistry_students
    print(f"只选数学的学生: {only_math}")

    # 至少选一门课的学生
    all_students = math_students | physics_students | chemistry_students
    print(f"所有选课学生: {all_students}")

    # 选了多门课的学生
    multi_course = (math_students & physics_students) | \
                   (math_students & chemistry_students) | \
                   (physics_students & chemistry_students)
    print(f"选多门课的学生: {multi_course}")

    # 没有选任何课的学生
    all_possible = {"张三", "李四", "王五", "赵六", "钱七", "孙八", "周九", "吴十"}
    no_course = all_possible - all_students
    print(f"没有选课的学生: {no_course}")

set_operations_example()

print("\n程序执行完毕！")