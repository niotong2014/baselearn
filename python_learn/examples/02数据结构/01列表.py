#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Python列表(List)数据结构示例
"""

# 1. 列表创建
print("=== 列表创建 ===")

# 空列表
empty_list = []
print(f"空列表: {empty_list}")

# 不同类型的元素
mixed_list = [1, "hello", 3.14, True, [1, 2, 3]]
print(f"混合类型列表: {mixed_list}")

# 使用list()函数
string_to_list = list("Python")
print(f"字符串转列表: {string_to_list}")

range_to_list = list(range(5))
print(f"range转列表: {range_to_list}")

# 列表推导式
squares = [x**2 for x in range(1, 6)]
print(f"平方列表: {squares}")

even_numbers = [x for x in range(10) if x % 2 == 0]
print(f"偶数列表: {even_numbers}")

# 2. 列表基本操作
print("\n=== 列表基本操作 ===")

fruits = ["苹果", "香蕉", "橙子"]
print(f"原始列表: {fruits}")

# 访问元素
print(f"第一个元素: {fruits[0]}")
print(f"最后一个元素: {fruits[-1]}")
print(f"倒数第二个元素: {fruits[-2]}")

# 切片
print(f"前两个元素: {fruits[0:2]}")
print(f"从第二个元素开始: {fruits[1:]}")
print(f"到倒数第二个元素: {fruits[:-1]}")
print(f"所有元素: {fruits[:]}")

# 列表长度
print(f"列表长度: {len(fruits)}")

# 成员检查
print(f"'苹果'在列表中吗? {'苹果' in fruits}")
print(f"'葡萄'在列表中吗? {'葡萄' in fruits}")

# 3. 列表修改
print("\n=== 列表修改 ===")

numbers = [1, 2, 3, 4, 5]
print(f"原始列表: {numbers}")

# 修改单个元素
numbers[0] = 10
print(f"修改第一个元素: {numbers}")

# 修改切片
numbers[1:3] = [20, 30]
print(f"修改切片: {numbers}")

# 4. 列表方法
print("\n=== 列表方法 ===")

colors = ["红色", "绿色", "蓝色"]
print(f"原始颜色列表: {colors}")

# 添加元素
colors.append("黄色")
print(f"append添加: {colors}")

colors.insert(1, "橙色")
print(f"insert添加: {colors}")

colors.extend(["紫色", "粉色"])
print(f"extend添加: {colors}")

# 删除元素
removed_item = colors.pop()
print(f"pop删除: {colors}, 删除的元素: {removed_item}")

removed_item = colors.pop(2)
print(f"pop删除指定位置: {colors}, 删除的元素: {removed_item}")

#colors.remove("绿色")
#print(f"remove删除: {colors}")

# 查找元素
if "蓝色" in colors:
    index = colors.index("蓝色")
    print(f"'蓝色'的索引: {index}")

# 计数
count_red = colors.count("红色")
print(f"'红色'出现的次数: {count_red}")

# 排序
numbers = [3, 1, 4, 1, 5, 9, 2, 6]
print(f"\n原始数字列表: {numbers}")

numbers.sort()  # 原地排序
print(f"升序排序: {numbers}")

numbers.sort(reverse=True)  # 降序排序
print(f"降序排序: {numbers}")

# 使用sorted()函数（返回新列表）
numbers = [3, 1, 4, 1, 5, 9, 2, 6]
sorted_numbers = sorted(numbers)
print(f"sorted()不改变原列表: {numbers}")
print(f"排序后的新列表: {sorted_numbers}")

# 反转列表
numbers.reverse()
print(f"反转后的列表: {numbers}")

# 5. 列表遍历
print("\n=== 列表遍历 ===")

students = ["张三", "李四", "王五", "赵六"]

# 基本遍历
print("基本遍历:")
for student in students:
    print(student)

# 带索引的遍历
print("\n带索引的遍历:")
for index, student in enumerate(students):
    print(f"{index}: {student}")

# 使用索引遍历
print("\n使用索引遍历:")
for i in range(len(students)):
    print(f"索引{i}: {students[i]}")

# 同时遍历多个列表
scores = [85, 92, 78, 95]
print("\n同时遍历多个列表:")
for student, score in zip(students, scores):
    print(f"{student}: {score}分")

# 6. 二维列表（列表的列表）
print("\n=== 二维列表 ===")

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(f"二维列表: {matrix}")

# 访问二维列表元素
print(f"第一行: {matrix[0]}")
print(f"第一行第二列: {matrix[0][1]}")

# 遍历二维列表
print("\n遍历二维列表:")
for row in matrix:
    for element in row:
        print(element, end=" ")
    print()  # 换行

# 创建二维列表
rows = 3
cols = 4
matrix2d = [[0 for _ in range(cols)] for _ in range(rows)]
print(f"\n创建的二维列表: {matrix2d}")

# 7. 列表的高级操作
print("\n=== 列表的高级操作 ===")

# 列表复制
original = [1, 2, 3]
copy1 = original.copy()  # 浅拷贝
copy2 = original[:]      # 切片拷贝
copy3 = list(original)   # 构造函数拷贝

print(f"原列表: {original}")
print(f"拷贝列表: {copy1}, {copy2}, {copy3}")

# 浅拷贝vs深拷贝
import copy
nested_list = [[1, 2], [3, 4]]
shallow_copy = nested_list.copy()
deep_copy = copy.deepcopy(nested_list)

print(f"\n原嵌套列表: {nested_list}")
shallow_copy[0][0] = 999
print(f"修改浅拷贝后原列表: {nested_list}")
deep_copy[0][0] = 888
print(f"修改深拷贝后原列表: {nested_list}")

# 列表推导式高级用法
print("\n高级列表推导式:")

# 生成字母表
import string
letters = [char for char in string.ascii_lowercase[:10]]
print(f"前10个字母: {letters}")

# 字典转列表
student_dict = {"张三": 85, "李四": 92, "王五": 78}
items = list(student_dict.items())
keys = list(student_dict.keys())
values = list(student_dict.values())
print(f"字典项: {items}")
print(f"键: {keys}")
print(f"值: {values}")

# 8. 列表的实际应用
print("\n=== 列表的实际应用 ===")

def find_average(numbers):
    """计算平均值"""
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)

def find_median(numbers):
    """计算中位数"""
    sorted_nums = sorted(numbers)
    n = len(sorted_nums)
    if n == 0:
        return 0
    elif n % 2 == 1:
        return sorted_nums[n // 2]
    else:
        return (sorted_nums[n // 2 - 1] + sorted_nums[n // 2]) / 2

def find_mode(numbers):
    """计算众数"""
    if not numbers:
        return None

    frequency = {}
    for num in numbers:
        frequency[num] = frequency.get(num, 0) + 1

    max_count = max(frequency.values())
    modes = [num for num, count in frequency.items() if count == max_count]

    return modes[0] if len(modes) == 1 else modes

# 统计数据
test_scores = [85, 92, 78, 85, 90, 88, 92, 85, 78, 90]
print(f"测试分数: {test_scores}")
print(f"平均值: {find_average(test_scores):.2f}")
print(f"中位数: {find_median(test_scores)}")
print(f"众数: {find_mode(test_scores)}")

# 9. 列表算法示例
print("\n=== 列表算法示例 ===")

def bubble_sort(arr):
    """冒泡排序"""
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

def binary_search(arr, target):
    """二分查找"""
    arr.sort()
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1

# 测试算法
unsorted = [64, 34, 25, 12, 22, 11, 90]
print(f"未排序: {unsorted}")
sorted_list = bubble_sort(unsorted.copy())
print(f"冒泡排序: {sorted_list}")

target = 25
index = binary_search(sorted_list, target)
print(f"二分查找{target}: 索引{index}")

# 10. 列表性能注意事项
print("\n=== 列表性能注意事项 ===")

import time

# 测试列表操作性能
def test_performance():
    large_list = list(range(100000))

    # 测试append性能
    start = time.time()
    for i in range(10000):
        large_list.append(i)
    end = time.time()
    print(f"append 10000个元素: {end - start:.4f}秒")

    # 测试insert性能（在开头插入）
    start = time.time()
    for i in range(1000):
        large_list.insert(0, i)
    end = time.time()
    print(f"insert 1000个元素到开头: {end - start:.4f}秒")

print("性能测试（结果可能因机器而异）：")
test_performance()

# 11. 实用列表函数
print("\n=== 实用列表函数 ===")

def remove_duplicates(lst):
    """去除列表中的重复元素"""
    return list(set(lst))

def flatten_list(nested_list):
    """展平嵌套列表"""
    result = []
    for item in nested_list:
        if isinstance(item, list):
            result.extend(flatten_list(item))
        else:
            result.append(item)
    return result

def list_intersection(list1, list2):
    """列表交集"""
    return list(set(list1) & set(list2))

def list_union(list1, list2):
    """列表并集"""
    return list(set(list1) | set(list2))

# 测试实用函数
list1 = [1, 2, 2, 3, 4, 4, 5]
list2 = [4, 5, 6, 7, 8]
nested = [1, [2, [3, 4], 5], [6, 7]]

print(f"原列表: {list1}")
print(f"去重: {remove_duplicates(list1)}")

print(f"嵌套列表: {nested}")
print(f"展平: {flatten_list(nested)}")

print(f"列表1: {list1[:5]}")
print(f"列表2: {list2}")
print(f"交集: {list_intersection(list1[:5], list2)}")
print(f"并集: {list_union(list1[:5], list2)}")

print("\n程序执行完毕！")
