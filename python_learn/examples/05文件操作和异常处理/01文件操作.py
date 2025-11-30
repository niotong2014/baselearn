#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Python文件操作示例
"""

# 1. 文本文件读写
print("=== 文本文件读写 ===")

# 写入文本文件
with open("sample.txt", "w", encoding="utf-8") as f:
    f.write("这是第一行\n")
    f.write("这是第二行\n")
    f.write("这是第三行\n")

print("文本文件写入完成")

# 读取文本文件
with open("sample.txt", "r", encoding="utf-8") as f:
    content = f.read()
    print(f"文件内容:\n{content}")

# 逐行读取
print("\n逐行读取:")
with open("sample.txt", "r", encoding="utf-8") as f:
    for line_num, line in enumerate(f, 1):
        print(f"第{line_num}行: {line.strip()}")

# 读取所有行到列表
with open("sample.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()
    print(f"\n读取到列表: {lines}")

# 2. 追加模式
print("\n=== 追加模式 ===")

with open("sample.txt", "a", encoding="utf-8") as f:
    f.write("追加的第一行\n")
    f.write("追加的第二行\n")

print("追加内容完成")

# 验证追加内容
with open("sample.txt", "r", encoding="utf-8") as f:
    print(f"追加后的文件内容:\n{f.read()}")

# 3. 二进制文件操作
print("\n=== 二进制文件操作 ===")

# 创建二进制数据
data = b'\x00\x01\x02\x03\x04\x05\x06\x07\x08\x09'

# 写入二进制文件
with open("binary_data.bin", "wb") as f:
    f.write(data)

print("二进制文件写入完成")

# 读取二进制文件
with open("binary_data.bin", "rb") as f:
    read_data = f.read()
    print(f"读取的二进制数据: {read_data}")
    print(f"十六进制表示: {read_data.hex()}")

# 4. 文件路径操作
print("\n=== 文件路径操作 ===")

import os
import pathlib

# 当前工作目录
print(f"当前工作目录: {os.getcwd()}")

# 文件信息
file_path = "sample.txt"
if os.path.exists(file_path):
    print(f"文件存在: {file_path}")
    print(f"文件大小: {os.path.getsize(file_path)} bytes")
    print(f"绝对路径: {os.path.abspath(file_path)}")
    print(f"文件权限: {oct(os.stat(file_path).st_mode)[-3:]}")

# 使用pathlib（推荐）
print("\n使用pathlib:")
path = pathlib.Path("sample.txt")
if path.exists():
    print(f"文件名: {path.name}")
    print(f"文件后缀: {path.suffix}")
    print(f"文件目录: {path.parent}")
    print(f"文件大小: {path.stat().st_size} bytes")

# 5. 目录操作
print("\n=== 目录操作 ===")

# 创建目录
os.makedirs("test_dir/sub_dir", exist_ok=True)
print("目录创建完成")

# 列出目录内容
print(f"当前目录内容: {os.listdir('.')}")
print(f"test_dir内容: {os.listdir('test_dir')}")

# 创建文件并检查
test_file = "test_dir/test_file.txt"
with open(test_file, "w", encoding="utf-8") as f:
    f.write("测试文件内容")

print(f"\n文件 {test_file} 存在: {os.path.exists(test_file)}")

# 删除文件
os.remove(test_file)
print(f"删除文件后存在: {os.path.exists(test_file)}")

# 6. 文件复制和移动
print("\n=== 文件复制和移动 ===")

import shutil

# 复制文件
shutil.copy("sample.txt", "sample_copy.txt")
print("文件复制完成")

# 移动文件（重命名）
if os.path.exists("sample_copy.txt"):
    shutil.move("sample_copy.txt", "sample_renamed.txt")
    print("文件移动/重命名完成")

# 复制目录
shutil.copytree("test_dir", "test_dir_backup")
print("目录复制完成")

# 删除目录
shutil.rmtree("test_dir")
shutil.rmtree("test_dir_backup")
print("目录删除完成")

# 7. 文件系统遍历
print("\n=== 文件系统遍历 ===")

# 创建测试目录结构
os.makedirs("project/src", exist_ok=True)
os.makedirs("project/tests", exist_ok=True)
os.makedirs("project/docs", exist_ok=True)

# 创建一些文件
files_to_create = [
    "project/main.py",
    "project/src/utils.py",
    "project/src/helpers.py",
    "project/tests/test_main.py",
    "project/docs/README.md"
]

for file_path in files_to_create:
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(f"# {os.path.basename(file_path)}\n")

# 遍历目录
print("项目目录结构:")
for root, dirs, files in os.walk("project"):
    level = root.replace("project", "").count(os.sep)
    indent = " " * 2 * level
    print(f"{indent}{os.path.basename(root)}/")
    subindent = " " * 2 * (level + 1)
    for file in files:
        print(f"{subindent}{file}")

# 8. CSV文件操作
print("\n=== CSV文件操作 ===")

import csv

# 创建CSV文件
data = [
    ["姓名", "年龄", "城市"],
    ["张三", 25, "北京"],
    ["李四", 30, "上海"],
    ["王五", 28, "广州"]
]

with open("students.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerows(data)

print("CSV文件写入完成")

# 读取CSV文件
with open("students.csv", "r", encoding="utf-8") as f:
    reader = csv.reader(f)
    print("CSV文件内容:")
    for row in reader:
        print(row)

# 使用DictReader
with open("students.csv", "r", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    print("\n使用DictReader:")
    for row in reader:
        print(f"{row['姓名']}: {row['年龄']}岁, {row['城市']}")

# 9. JSON文件操作
print("\n=== JSON文件操作 ===")

import json

# 创建Python对象
student_data = {
    "name": "张三",
    "age": 25,
    "courses": ["数学", "物理", "化学"],
    "scores": {
        "数学": 85,
        "物理": 90,
        "化学": 88
    },
    "graduated": False
}

# 写入JSON文件
with open("student.json", "w", encoding="utf-8") as f:
    json.dump(student_data, f, ensure_ascii=False, indent=2)

print("JSON文件写入完成")

# 读取JSON文件
with open("student.json", "r", encoding="utf-8") as f:
    loaded_data = json.load(f)
    print("读取的JSON数据:")
    print(json.dumps(loaded_data, ensure_ascii=False, indent=2))

# 10. 配置文件操作
print("\n=== 配置文件操作 ===")

import configparser

# 创建配置文件
config = configparser.ConfigParser()
config["DEFAULT"] = {
    "debug": "True",
    "log_level": "INFO"
}
config["database"] = {
    "host": "localhost",
    "port": "5432",
    "username": "admin",
    "password": "secret"
}
config["server"] = {
    "host": "0.0.0.0",
    "port": "8000",
    "workers": "4"
}

# 写入配置文件
with open("config.ini", "w", encoding="utf-8") as f:
    config.write(f)

print("配置文件写入完成")

# 读取配置文件
config = configparser.ConfigParser()
config.read("config.ini", encoding="utf-8")

print("配置文件内容:")
for section in config.sections():
    print(f"[{section}]")
    for key, value in config[section].items():
        print(f"{key} = {value}")

# 11. 临时文件操作
print("\n=== 临时文件操作 ===")

import tempfile

# 创建临时文件
with tempfile.NamedTemporaryFile(mode='w', delete=False, encoding="utf-8") as f:
    f.write("这是临时文件内容")
    temp_file_name = f.name

print(f"临时文件创建: {temp_file_name}")

# 读取临时文件
with open(temp_file_name, "r", encoding="utf-8") as f:
    print(f"临时文件内容: {f.read()}")

# 手动删除临时文件
os.unlink(temp_file_name)
print(f"临时文件已删除: {not os.path.exists(temp_file_name)}")

# 临时目录
with tempfile.TemporaryDirectory() as temp_dir:
    print(f"临时目录: {temp_dir}")
    temp_file_path = os.path.join(temp_dir, "temp_file.txt")
    with open(temp_file_path, "w", encoding="utf-8") as f:
        f.write("临时目录中的文件")

    # 在临时目录中操作
    if os.path.exists(temp_file_path):
        print("临时目录中的文件存在")

# 临时目录会自动删除

# 12. 文件权限操作
print("\n=== 文件权限操作 ===")

# 创建文件并设置权限
with open("test_permissions.txt", "w") as f:
    f.write("测试文件权限")

# 获取当前权限
current_mode = os.stat("test_permissions.txt").st_mode
print(f"当前权限: {oct(current_mode)[-3:]}")

# 修改权限（只读）
os.chmod("test_permissions.txt", 0o444)
new_mode = os.stat("test_permissions.txt").st_mode
print(f"修改后权限: {oct(new_mode)[-3:]}")

# 尝试写入只读文件
try:
    with open("test_permissions.txt", "w") as f:
        f.write("尝试写入")
    print("写入成功")
except PermissionError as e:
    print(f"写入失败（预期）: {e}")

# 恢复权限并清理
os.chmod("test_permissions.txt", 0o644)
os.remove("test_permissions.txt")
print("文件已清理")

# 13. 文件锁操作
print("\n=== 文件锁操作 ===")

import fcntl

# 创建文件锁示例
lock_file = "file_lock.txt"

with open(lock_file, "w") as f:
    try:
        # 尝试获取排他锁
        fcntl.flock(f, fcntl.LOCK_EX | fcntl.LOCK_NB)
        print("获取文件锁成功")

        # 模拟文件操作
        f.write("文件锁测试内容")
        print("文件写入完成")

    except IOError:
        print("无法获取文件锁，文件可能被其他进程占用")

    finally:
        # 释放锁
        fcntl.flock(f, fcntl.LOCK_UN)
        print("文件锁已释放")

# 清理文件
os.remove(lock_file)

# 14. 高级文件操作
print("\n=== 高级文件操作 ===")

import mmap

# 创建大文件
large_file = "large_file.txt"
with open(large_file, "w", encoding="utf-8") as f:
    for i in range(1000):
        f.write(f"这是第{i+1}行内容\n")

print(f"大文件创建完成，大小: {os.path.getsize(large_file)} bytes")

# 使用内存映射文件
with open(large_file, "r", encoding="utf-8") as f:
    # 创建内存映射
    mm = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)

    # 在内存映射中搜索
    search_term = "第500行"
    pos = mm.find(search_term.encode("utf-8"))

    if pos != -1:
        print(f"找到'{search_term}'在位置: {pos}")

        # 读取该行
        mm.seek(pos)
        line = mm.readline().decode("utf-8")
        print(f"该行内容: {line.strip()}")

    mm.close()

# 15. 文件监控
print("\n=== 文件监控 ===")

import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

# 注意：这需要安装 watchdog 库
# pip install watchdog

class FileChangeHandler(FileSystemEventHandler):
    """文件变化处理器"""

    def on_modified(self, event):
        if not event.is_directory:
            print(f"文件被修改: {event.src_path}")

    def on_created(self, event):
        if not event.is_directory:
            print(f"文件被创建: {event.src_path}")

    def on_deleted(self, event):
        if not event.is_directory:
            print(f"文件被删除: {event.src_path}")

# 简单的文件监控演示（不实际运行）
print("文件监控功能需要watchdog库")
print("安装命令: pip install watchdog")
print("监控可以检测文件的创建、修改、删除等事件")

# 16. 清理示例文件
print("\n=== 清理示例文件 ===")

# 删除创建的文件
files_to_remove = [
    "sample.txt",
    "sample_renamed.txt",
    "binary_data.bin",
    "students.csv",
    "student.json",
    "config.ini",
    "large_file.txt"
]

for file in files_to_remove:
    if os.path.exists(file):
        os.remove(file)
        print(f"已删除: {file}")

# 删除项目目录
if os.path.exists("project"):
    shutil.rmtree("project")
    print("已删除: project/目录")

print("\n程序执行完毕！")