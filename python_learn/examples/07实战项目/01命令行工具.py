#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Python命令行工具项目示例
"""

import argparse
import sys
import os
import json
import csv
from datetime import datetime
from typing import List, Dict, Any

# 1. 任务管理器类
print("=== 1. 任务管理器类 ===")

class TaskManager:
    """任务管理器"""

    def __init__(self, filename="tasks.json"):
        self.filename = filename
        self.tasks = []
        self.load_tasks()

    def load_tasks(self):
        """加载任务"""
        if os.path.exists(self.filename):
            try:
                with open(self.filename, 'r', encoding='utf-8') as f:
                    self.tasks = json.load(f)
            except (json.JSONDecodeError, FileNotFoundError):
                self.tasks = []

    def save_tasks(self):
        """保存任务"""
        with open(self.filename, 'w', encoding='utf-8') as f:
            json.dump(self.tasks, f, ensure_ascii=False, indent=2)

    def add_task(self, title: str, priority: str = "medium",
                 due_date: str = None, description: str = ""):
        """添加任务"""
        task = {
            "id": len(self.tasks) + 1,
            "title": title,
            "priority": priority,
            "status": "pending",
            "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "due_date": due_date,
            "description": description,
            "completed_at": None
        }
        self.tasks.append(task)
        self.save_tasks()
        return task["id"]

    def complete_task(self, task_id: int):
        """完成任务"""
        for task in self.tasks:
            if task["id"] == task_id:
                task["status"] = "completed"
                task["completed_at"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                self.save_tasks()
                return True
        return False

    def delete_task(self, task_id: int):
        """删除任务"""
        for i, task in enumerate(self.tasks):
            if task["id"] == task_id:
                del self.tasks[i]
                self.save_tasks()
                return True
        return False

    def list_tasks(self, status: str = None, priority: str = None):
        """列出任务"""
        filtered_tasks = self.tasks

        if status:
            filtered_tasks = [t for t in filtered_tasks if t["status"] == status]

        if priority:
            filtered_tasks = [t for t in filtered_tasks if t["priority"] == priority]

        return filtered_tasks

    def get_task_stats(self):
        """获取任务统计"""
        total = len(self.tasks)
        completed = len([t for t in self.tasks if t["status"] == "completed"])
        pending = total - completed

        priorities = {}
        for task in self.tasks:
            pri = task["priority"]
            priorities[pri] = priorities.get(pri, 0) + 1

        return {
            "total": total,
            "completed": completed,
            "pending": pending,
            "completion_rate": (completed / total * 100) if total > 0 else 0,
            "priorities": priorities
        }

    def export_to_csv(self, filename: str):
        """导出到CSV"""
        with open(filename, 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(["ID", "标题", "优先级", "状态", "创建时间", "截止日期", "描述", "完成时间"])

            for task in self.tasks:
                writer.writerow([
                    task["id"],
                    task["title"],
                    task["priority"],
                    task["status"],
                    task["created_at"],
                    task["due_date"] or "",
                    task["description"] or "",
                    task["completed_at"] or ""
                ])

# 2. 命令行接口
print("\n=== 2. 命令行接口 ===")

def create_parser():
    """创建命令行参数解析器"""
    parser = argparse.ArgumentParser(
        description="任务管理命令行工具",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
示例用法:
  python task_cli.py add "学习Python" --priority high
  python task_cli.py list --status pending
  python task_cli.py complete 1
  python task_cli.py stats
  python task_cli.py export --format csv
        """
    )

    subparsers = parser.add_subparsers(dest='command', help='可用命令')

    # 添加任务
    add_parser = subparsers.add_parser('add', help='添加新任务')
    add_parser.add_argument('title', help='任务标题')
    add_parser.add_argument('--priority', choices=['low', 'medium', 'high'],
                           default='medium', help='优先级')
    add_parser.add_argument('--due-date', help='截止日期 (YYYY-MM-DD)')
    add_parser.add_argument('--description', help='任务描述')

    # 列出任务
    list_parser = subparsers.add_parser('list', help='列出任务')
    list_parser.add_argument('--status', choices=['pending', 'completed'],
                           help='按状态过滤')
    list_parser.add_argument('--priority', choices=['low', 'medium', 'high'],
                           help='按优先级过滤')

    # 完成任务
    complete_parser = subparsers.add_parser('complete', help='完成任务')
    complete_parser.add_argument('task_id', type=int, help='任务ID')

    # 删除任务
    delete_parser = subparsers.add_parser('delete', help='删除任务')
    delete_parser.add_argument('task_id', type=int, help='任务ID')

    # 统计信息
    subparsers.add_parser('stats', help='显示统计信息')

    # 导出功能
    export_parser = subparsers.add_parser('export', help='导出任务')
    export_parser.add_argument('--format', choices=['csv', 'json'],
                              default='json', help='导出格式')
    export_parser.add_argument('--filename', help='导出文件名')

    return parser

# 3. 格式化输出工具
print("\n=== 3. 格式化输出工具 ===")

class OutputFormatter:
    """输出格式化工具"""

    @staticmethod
    def print_task_table(tasks):
        """打印任务表格"""
        if not tasks:
            print("没有找到任务")
            return

        # 计算列宽
        headers = ["ID", "标题", "优先级", "状态", "创建时间", "截止日期"]
        col_widths = []

        # 计算标题宽度
        for header in headers:
            col_widths.append(len(header))

        # 计算内容宽度
        for task in tasks:
            values = [
                str(task["id"]),
                task["title"][:20],
                task["priority"],
                task["status"],
                task["created_at"][:10],
                task["due_date"] or ""
            ]

            for i, value in enumerate(values):
                col_widths[i] = max(col_widths[i], len(value))

        # 打印表格
        # 表头
        header_line = " | ".join(headers[i].ljust(col_widths[i]) for i in range(len(headers)))
        print(header_line)
        print("-" * len(header_line))

        # 内容
        for task in tasks:
            values = [
                str(task["id"]),
                task["title"][:20],
                task["priority"],
                task["status"],
                task["created_at"][:10],
                task["due_date"] or ""
            ]

            line = " | ".join(values[i].ljust(col_widths[i]) for i in range(len(values)))
            print(line)

    @staticmethod
    def print_stats(stats):
        """打印统计信息"""
        print("\n=== 任务统计 ===")
        print(f"总任务数: {stats['total']}")
        print(f"已完成: {stats['completed']}")
        print(f"待完成: {stats['pending']}")
        print(f"完成率: {stats['completion_rate']:.1f}%")

        print("\n=== 优先级分布 ===")
        for priority, count in stats['priorities'].items():
            print(f"{priority}: {count}")

# 4. 主程序
print("\n=== 4. 主程序 ===")

def main():
    """主函数"""
    parser = create_parser()
    args = parser.parse_args()

    if not args.command:
        parser.print_help()
        return

    task_manager = TaskManager()
    formatter = OutputFormatter()

    if args.command == 'add':
        task_id = task_manager.add_task(
            title=args.title,
            priority=args.priority,
            due_date=args.due_date,
            description=args.description or ""
        )
        print(f"任务已添加，ID: {task_id}")

    elif args.command == 'list':
        tasks = task_manager.list_tasks(status=args.status, priority=args.priority)
        formatter.print_task_table(tasks)

    elif args.command == 'complete':
        if task_manager.complete_task(args.task_id):
            print(f"任务 {args.task_id} 已完成")
        else:
            print(f"任务 {args.task_id} 不存在")

    elif args.command == 'delete':
        if task_manager.delete_task(args.task_id):
            print(f"任务 {args.task_id} 已删除")
        else:
            print(f"任务 {args.task_id} 不存在")

    elif args.command == 'stats':
        stats = task_manager.get_task_stats()
        formatter.print_stats(stats)

    elif args.command == 'export':
        if args.format == 'csv':
            filename = args.filename or f"tasks_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"
            task_manager.export_to_csv(filename)
            print(f"任务已导出到 {filename}")
        elif args.format == 'json':
            filename = args.filename or f"tasks_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
            with open(filename, 'w', encoding='utf-8') as f:
                json.dump(task_manager.tasks, f, ensure_ascii=False, indent=2)
            print(f"任务已导出到 {filename}")

# 5. 交互式模式
print("\n=== 5. 交互式模式 ===")

def interactive_mode():
    """交互式模式"""
    task_manager = TaskManager()
    formatter = OutputFormatter()

    print("\n=== 任务管理器 - 交互式模式 ===")
    print("输入 'help' 查看可用命令，'quit' 退出")

    while True:
        try:
            command = input("\n> ").strip().lower()

            if command in ['quit', 'exit', 'q']:
                print("再见！")
                break

            elif command == 'help':
                print("""
可用命令:
  add <title>           - 添加任务
  list                   - 列出所有任务
  complete <id>          - 完成任务
  delete <id>            - 删除任务
  stats                  - 显示统计
  clear                  - 清屏
  help                   - 显示帮助
  quit                   - 退出程序
                """)

            elif command == 'clear':
                os.system('cls' if os.name == 'nt' else 'clear')

            elif command == 'stats':
                stats = task_manager.get_task_stats()
                formatter.print_stats(stats)

            elif command == 'list':
                tasks = task_manager.list_tasks()
                formatter.print_task_table(tasks)

            elif command.startswith('add '):
                title = command[4:].strip()
                if title:
                    task_id = task_manager.add_task(title)
                    print(f"任务已添加，ID: {task_id}")
                else:
                    print("请输入任务标题")

            elif command.startswith('complete '):
                try:
                    task_id = int(command[9:].strip())
                    if task_manager.complete_task(task_id):
                        print(f"任务 {task_id} 已完成")
                    else:
                        print(f"任务 {task_id} 不存在")
                except ValueError:
                    print("请输入有效的任务ID")

            elif command.startswith('delete '):
                try:
                    task_id = int(command[7:].strip())
                    if task_manager.delete_task(task_id):
                        print(f"任务 {task_id} 已删除")
                    else:
                        print(f"任务 {task_id} 不存在")
                except ValueError:
                    print("请输入有效的任务ID")

            else:
                print(f"未知命令: {command}，输入 'help' 查看可用命令")

        except KeyboardInterrupt:
            print("\n\n再见！")
            break
        except EOFError:
            print("\n再见！")
            break

# 6. 批处理模式
print("\n=== 6. 批处理模式 ===")

def batch_mode():
    """批处理模式示例"""
    task_manager = TaskManager()

    # 添加示例任务
    sample_tasks = [
        ("学习Python基础", "high", "2024-12-31", "完成Python语法学习"),
        ("编写命令行工具", "medium", "2024-12-15", "创建任务管理CLI"),
        ("阅读《Python编程》", "low", None, "阅读Python编程书籍"),
        ("练习算法题", "medium", None, "每天解决5道算法题"),
        ("参与开源项目", "high", "2024-11-30", "为Python项目贡献代码")
    ]

    print("添加示例任务...")
    for title, priority, due_date, description in sample_tasks:
        task_id = task_manager.add_task(title, priority, due_date, description)
        print(f"添加任务: {title} (ID: {task_id})")

    # 完成一些任务
    print("\n完成任务...")
    task_manager.complete_task(1)
    task_manager.complete_task(3)

    # 显示统计
    print("\n任务统计:")
    formatter = OutputFormatter()
    stats = task_manager.get_task_stats()
    formatter.print_stats(stats)

    # 显示当前任务
    print("\n当前任务:")
    tasks = task_manager.list_tasks(status='pending')
    formatter.print_task_table(tasks)

# 7. 主程序入口
print("\n=== 7. 主程序入口 ===")

if __name__ == "__main__":
    # 处理命令行参数
    if len(sys.argv) > 1:
        main()
    else:
        # 如果没有参数，进入交互式模式
        interactive_mode()

# 8. 使用示例
print("\n=== 8. 使用示例 ===")

print("""
使用说明：

1. 命令行模式：
   python 01命令行工具.py add "学习Python" --priority high --due-date 2024-12-31
   python 01命令行工具.py list --status pending
   python 01命令行工具.py complete 1
   python 01命令行工具.py stats
   python 01命令行工具.py export --format csv

2. 交互式模式：
   python 01命令行工具.py
   然后输入命令进行操作

3. 功能特点：
   - 任务增删改查
   - 优先级管理
   - 状态跟踪
   - 数据持久化
   - 导出功能
   - 统计分析
   - 友好的界面
""")

print("\n程序执行完毕！")