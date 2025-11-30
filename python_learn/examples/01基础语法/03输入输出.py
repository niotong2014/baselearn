#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Python输入输出示例
"""

# 1. 基本输出
print("=== 基本输出 ===")

print("Hello, World!")
print("Python", "学习", "教程")  # 多个参数，默认用空格分隔
print("Python", "学习", "教程", sep="-")  # 指定分隔符
print("第一行", end=" ")  # 指定结束符，不换行
print("第二行")

# 2. 格式化输出
print("\n=== 格式化输出 ===")

# % 操作符（旧式）
name = "张三"
age = 25
print("姓名: %s, 年龄: %d" % (name, age))

# format() 方法
print("姓名: {}, 年龄: {}".format(name, age))
print("姓名: {0}, 年龄: {1}".format(name, age))
print("姓名: {n}, 年龄: {a}".format(n=name, a=age))

# f-string（推荐，Python 3.6+）
print(f"姓名: {name}, 年龄: {age}")
print(f"{name}明年{age + 1}岁")

# 3. 数字格式化
print("\n=== 数字格式化 ===")

pi = 3.1415926
print(f"默认: {pi}")
print(f"保留2位小数: {pi:.2f}")
print(f"百分比: {pi:.1%}")
print(f"科学计数法: {pi:.2e}")

# 千位分隔符
large_number = 1234567890
print(f"大数字: {large_number}")
print(f"带分隔符: {large_number:,}")

# 对齐和宽度
print(f"左对齐: {name:<10}|")
print(f"右对齐: {name:>10}|")
print(f"居中对齐: {name:^10}|")

# 4. 基本输入
print("\n=== 基本输入 ===")

# input() 函数总是返回字符串
print("请输入您的姓名：")
user_name = input()
print(f"您好, {user_name}!")

# 直接在input中提供提示信息
age_input = input("请输入您的年龄：")
print(f"您输入的年龄是：{age_input}")

# 5. 输入类型转换
print("\n=== 输入类型转换 ===")

try:
    # 字符串转整数
    num1 = int(input("请输入一个整数："))
    print(f"您输入的整数是：{num1}")
    print(f"类型：{type(num1)}")

    # 字符串转浮点数
    num2 = float(input("请输入一个浮点数："))
    print(f"您输入的浮点数是：{num2}")
    print(f"类型：{type(num2)}")

    # 数学运算
    result = num1 + num2
    print(f"两数之和：{result}")

except ValueError as e:
    print(f"输入错误：{e}")

# 6. 安全输入函数
print("\n=== 安全输入函数 ===")

def get_integer_input(prompt):
    """安全地获取整数输入"""
    while True:
        try:
            value = int(input(prompt))
            return value
        except ValueError:
            print("输入无效，请输入一个整数！")

def get_float_input(prompt):
    """安全地获取浮点数输入"""
    while True:
        try:
            value = float(input(prompt))
            return value
        except ValueError:
            print("输入无效，请输入一个数字！")

def get_yes_no_input(prompt):
    """获取是/否输入"""
    while True:
        value = input(prompt).lower()
        if value in ['y', 'yes', '是', 'y']:
            return True
        elif value in ['n', 'no', '否', 'n']:
            return False
        else:
            print("请输入 'y' 或 'n'！")

# 使用安全输入函数
age = get_integer_input("请输入您的年龄：")
height = get_float_input("请输入您的身高（米）：")
is_student = get_yes_no_input("您是学生吗？(y/n): ")

print(f"\n您输入的信息：")
print(f"年龄：{age}岁")
print(f"身高：{height:.2f}米")
print(f"是否学生：{'是' if is_student else '否'}")

# 7. 批量输入示例
print("\n=== 批量输入示例 ===")

def input_scores():
    """输入多个分数"""
    scores = []
    print("请输入学生分数（输入-1结束）：")

    while True:
        score = get_integer_input("分数：")
        if score == -1:
            break
        elif 0 <= score <= 100:
            scores.append(score)
        else:
            print("分数应在0-100之间！")

    return scores

def analyze_scores(scores):
    """分析分数"""
    if not scores:
        print("没有输入有效分数！")
        return

    print(f"\n分数分析结果：")
    print(f"学生人数：{len(scores)}")
    print(f"平均分：{sum(scores) / len(scores):.2f}")
    print(f"最高分：{max(scores)}")
    print(f"最低分：{min(scores)}")
    print(f"及格人数：{len([s for s in scores if s >= 60])}")

# 输入并分析分数
student_scores = input_scores()
analyze_scores(student_scores)

# 8. 文件输入输出
print("\n=== 文件输入输出 ===")

# 写入文件
try:
    with open("output.txt", "w", encoding="utf-8") as file:
        file.write("这是一个输出文件示例\n")
        file.write(f"当前时间：{__import__('datetime').datetime.now()}\n")
        file.write(f"用户信息：{name}, {age}岁, {height:.2f}米\n")
    print("文件写入成功！")
except Exception as e:
    print(f"文件写入错误：{e}")

# 读取文件
try:
    with open("output.txt", "r", encoding="utf-8") as file:
        print("\n文件内容：")
        content = file.read()
        print(content)
except Exception as e:
    print(f"文件读取错误：{e}")

# 9. 标准输出重定向
print("\n=== 标准输出重定向 ===")

import sys

# 保存原始stdout
original_stdout = sys.stdout

try:
    # 将输出重定向到文件
    with open("redirected_output.txt", "w", encoding="utf-8") as f:
        sys.stdout = f
        print("这行内容会被写入文件")
        print("这行也会被写入文件")

    # 恢复标准输出
    sys.stdout = original_stdout
    print("输出已恢复到控制台")

    # 读取重定向的文件
    with open("redirected_output.txt", "r", encoding="utf-8") as f:
        print("\n重定向文件内容：")
        print(f.read())

except Exception as e:
    sys.stdout = original_stdout
    print(f"重定向错误：{e}")

# 10. 交互式菜单程序
print("\n=== 交互式菜单程序 ===")

def show_menu():
    """显示菜单"""
    print("\n" + "="*30)
    print("Python学习程序菜单")
    print("="*30)
    print("1. 计算器")
    print("2. 温度转换")
    print("3. 猜数字游戏")
    print("4. 退出")
    print("="*30)

def calculator():
    """简单计算器"""
    try:
        num1 = get_float_input("输入第一个数：")
        op = input("输入运算符（+、-、*、/）：")
        num2 = get_float_input("输入第二个数：")

        if op == '+':
            result = num1 + num2
        elif op == '-':
            result = num1 - num2
        elif op == '*':
            result = num1 * num2
        elif op == '/':
            if num2 == 0:
                print("错误：除数不能为零！")
                return
            result = num1 / num2
        else:
            print("错误：无效的运算符！")
            return

        print(f"结果：{num1} {op} {num2} = {result}")
    except Exception as e:
        print(f"计算错误：{e}")

def temperature_converter():
    """温度转换器"""
    print("\n温度转换器")
    print("1. 摄氏度转华氏度")
    print("2. 华氏度转摄氏度")

    choice = get_integer_input("选择转换类型（1-2）：")

    if choice == 1:
        celsius = get_float_input("输入摄氏温度：")
        fahrenheit = celsius * 9/5 + 32
        print(f"{celsius}°C = {fahrenheit:.1f}°F")
    elif choice == 2:
        fahrenheit = get_float_input("输入华氏温度：")
        celsius = (fahrenheit - 32) * 5/9
        print(f"{fahrenheit}°F = {celsius:.1f}°C")
    else:
        print("无效选择！")

def guess_number_game():
    """猜数字游戏"""
    import random

    target = random.randint(1, 100)
    attempts = 0

    print("\n猜数字游戏（1-100）")

    while True:
        attempts += 1
        guess = get_integer_input("输入你的猜测：")

        if guess == target:
            print(f"恭喜！你用了{attempts}次猜对了！")
            break
        elif guess < target:
            print("太小了！")
        else:
            print("太大了！")

# 主循环
while True:
    show_menu()
    choice = input("请选择（1-4）：")

    if choice == '1':
        calculator()
    elif choice == '2':
        temperature_converter()
    elif choice == '3':
        guess_number_game()
    elif choice == '4':
        print("感谢使用！")
        break
    else:
        print("无效选择，请重试！")

    input("\n按Enter键继续...")

print("\n程序执行完毕！")