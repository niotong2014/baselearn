#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Python数据分析项目示例
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime, timedelta
import json
import csv
from collections import Counter
import random
from typing import List, Dict, Any, Tuple

# 设置matplotlib中文字体
plt.rcParams['font.sans-serif'] = ['SimHei', 'Arial Unicode MS']
plt.rcParams['axes.unicode_minus'] = False

print("=== Python数据分析项目示例 ===")

# 1. 数据生成器
print("\n=== 1. 数据生成器 ===")

class DataGenerator:
    """销售数据生成器"""

    def __init__(self):
        self.products = [
            {"name": "笔记本电脑", "price": 5999, "category": "电子产品"},
            {"name": "手机", "price": 3999, "category": "电子产品"},
            {"name": "书桌", "price": 899, "category": "家具"},
            {"name": "椅子", "price": 399, "category": "家具"},
            {"name": "Python编程书", "price": 89, "category": "图书"},
            {"name": "数据科学指南", "price": 128, "category": "图书"},
            {"name": "T恤", "price": 99, "category": "服装"},
            {"name": "牛仔裤", "price": 199, "category": "服装"}
        ]

        self.cities = ["北京", "上海", "广州", "深圳", "杭州", "南京", "武汉", "成都"]
        self.customers = ["张三", "李四", "王五", "赵六", "钱七", "孙八", "周九", "吴十"]

    def generate_sales_data(self, num_records: int = 1000,
                            start_date: str = "2024-01-01",
                            end_date: str = "2024-12-31") -> pd.DataFrame:
        """生成销售数据"""
        records = []

        start = datetime.strptime(start_date, "%Y-%m-%d")
        end = datetime.strptime(end_date, "%Y-%m-%d")

        for i in range(num_records):
            # 随机选择产品
            product = random.choice(self.products)

            # 生成销售日期
            days_diff = (end - start).days
            sale_date = start + timedelta(days=random.randint(0, days_diff))

            # 生成销售数量
            quantity = random.randint(1, 10)

            # 生成折扣（0-0.5）
            discount = random.uniform(0, 0.5)

            # 计算总价
            total_price = product["price"] * quantity * (1 - discount)

            record = {
                "订单ID": f"ORD{str(i+1).zfill(6)}",
                "客户姓名": random.choice(self.customers),
                "产品名称": product["name"],
                "产品类别": product["category"],
                "单价": product["price"],
                "数量": quantity,
                "折扣": round(discount, 2),
                "总价": round(total_price, 2),
                "销售日期": sale_date.strftime("%Y-%m-%d"),
                "城市": random.choice(self.cities)
            }
            records.append(record)

        return pd.DataFrame(records)

# 2. 数据分析器
print("\n=== 2. 数据分析器 ===")

class SalesAnalyzer:
    """销售数据分析器"""

    def __init__(self, data: pd.DataFrame):
        self.data = data
        self.data['销售日期'] = pd.to_datetime(self.data['销售日期'])

    def basic_statistics(self) -> Dict[str, Any]:
        """基本统计信息"""
        return {
            "总订单数": len(self.data),
            "总销售额": self.data['总价'].sum(),
            "平均订单金额": self.data['总价'].mean(),
            "最大订单金额": self.data['总价'].max(),
            "最小订单金额": self.data['总价'].min(),
            "总客户数": self.data['客户姓名'].nunique(),
            "总产品数": self.data['产品名称'].nunique()
        }

    def category_analysis(self) -> pd.DataFrame:
        """产品类别分析"""
        category_stats = self.data.groupby('产品类别').agg({
            '总价': ['sum', 'count', 'mean'],
            '数量': 'sum'
        }).round(2)
        category_stats.columns = ['总销售额', '订单数', '平均订单金额', '总数量']
        return category_stats

    def monthly_analysis(self) -> pd.DataFrame:
        """月度销售分析"""
        monthly_data = self.data.copy()
        monthly_data['月份'] = monthly_data['销售日期'].dt.to_period('M')

        monthly_stats = monthly_data.groupby('月份').agg({
            '总价': 'sum',
            '订单ID': 'count',
            '客户姓名': 'nunique'
        }).round(2)
        monthly_stats.columns = ['月销售额', '月订单数', '月客户数']
        return monthly_stats

    def city_analysis(self) -> pd.DataFrame:
        """城市销售分析"""
        city_stats = self.data.groupby('城市').agg({
            '总价': ['sum', 'count', 'mean'],
            '客户姓名': 'nunique'
        }).round(2)
        city_stats.columns = ['城市销售额', '订单数', '平均订单金额', '客户数']
        return city_stats

    def customer_analysis(self) -> pd.DataFrame:
        """客户分析"""
        customer_stats = self.data.groupby('客户姓名').agg({
            '总价': ['sum', 'count', 'mean'],
            '产品名称': 'nunique'
        }).round(2)
        customer_stats.columns = ['客户总消费', '订单数', '平均订单金额', '购买产品种类']
        return customer_stats

    def product_analysis(self) -> pd.DataFrame:
        """产品分析"""
        product_stats = self.data.groupby('产品名称').agg({
            '总价': 'sum',
            '数量': 'sum',
            '订单ID': 'count'
        }).round(2)
        product_stats.columns = ['总销售额', '总销量', '订单数']
        return product_stats.sort_values('总销售额', ascending=False)

    def time_series_analysis(self) -> pd.DataFrame:
        """时间序列分析"""
        daily_sales = self.data.groupby('销售日期')['总价'].sum().reset_index()
        daily_sales.columns = ['日期', '日销售额']
        return daily_sales

# 3. 数据可视化器
print("\n=== 3. 数据可视化器 ===")

class DataVisualizer:
    """数据可视化器"""

    def __init__(self, data: pd.DataFrame, analyzer: SalesAnalyzer):
        self.data = data
        self.analyzer = analyzer

    def plot_category_sales(self, save_path: str = None):
        """绘制类别销售图表"""
        category_data = self.analyzer.category_analysis()

        plt.figure(figsize=(12, 6))
        plt.subplot(1, 2, 1)
        category_data['总销售额'].plot(kind='pie', autopct='%1.1f%%')
        plt.title('各类别销售额占比')
        plt.ylabel('')

        plt.subplot(1, 2, 2)
        category_data['总销售额'].plot(kind='bar')
        plt.title('各类别销售额')
        plt.xlabel('产品类别')
        plt.ylabel('销售额')
        plt.xticks(rotation=45)

        plt.tight_layout()
        if save_path:
            plt.savefig(save_path)
        plt.show()

    def plot_monthly_trend(self, save_path: str = None):
        """绘制月度趋势图"""
        monthly_data = self.analyzer.monthly_analysis()
        monthly_data.index = monthly_data.index.to_timestamp()

        plt.figure(figsize=(12, 6))
        plt.subplot(2, 1, 1)
        monthly_data['月销售额'].plot(kind='line', marker='o')
        plt.title('月度销售额趋势')
        plt.xlabel('月份')
        plt.ylabel('销售额')

        plt.subplot(2, 1, 2)
        monthly_data['月订单数'].plot(kind='bar')
        plt.title('月度订单数')
        plt.xlabel('月份')
        plt.ylabel('订单数')

        plt.tight_layout()
        if save_path:
            plt.savefig(save_path)
        plt.show()

    def plot_city_comparison(self, save_path: str = None):
        """绘制城市对比图"""
        city_data = self.analyzer.city_analysis()

        plt.figure(figsize=(12, 6))
        plt.subplot(1, 2, 1)
        city_data['城市销售额'].plot(kind='bar')
        plt.title('各城市销售额对比')
        plt.xlabel('城市')
        plt.ylabel('销售额')
        plt.xticks(rotation=45)

        plt.subplot(1, 2, 2)
        city_data['客户数'].plot(kind='bar')
        plt.title('各城市客户数对比')
        plt.xlabel('城市')
        plt.ylabel('客户数')
        plt.xticks(rotation=45)

        plt.tight_layout()
        if save_path:
            plt.savefig(save_path)
        plt.show()

    def plot_top_customers(self, top_n: int = 10, save_path: str = None):
        """绘制客户消费排行榜"""
        customer_data = self.analyzer.customer_analysis()
        top_customers = customer_data.sort_values('客户总消费', ascending=False).head(top_n)

        plt.figure(figsize=(10, 6))
        top_customers['客户总消费'].plot(kind='bar')
        plt.title(f'Top {top_n} 客户消费排行')
        plt.xlabel('客户姓名')
        plt.ylabel('总消费金额')
        plt.xticks(rotation=45)

        plt.tight_layout()
        if save_path:
            plt.savefig(save_path)
        plt.show()

    def plot_product_performance(self, save_path: str = None):
        """绘制产品表现图"""
        product_data = self.analyzer.product_analysis().head(10)

        plt.figure(figsize=(12, 6))
        plt.subplot(1, 2, 1)
        product_data['总销售额'].plot(kind='bar')
        plt.title('产品销售额排行')
        plt.xlabel('产品名称')
        plt.ylabel('销售额')
        plt.xticks(rotation=45)

        plt.subplot(1, 2, 2)
        product_data['总销量'].plot(kind='bar')
        plt.title('产品销量排行')
        plt.xlabel('产品名称')
        plt.ylabel('销量')
        plt.xticks(rotation=45)

        plt.tight_layout()
        if save_path:
            plt.savefig(save_path)
        plt.show()

    def plot_correlation_heatmap(self, save_path: str = None):
        """绘制相关性热力图"""
        # 选择数值型数据
        numeric_data = self.data[['单价', '数量', '折扣', '总价']]

        plt.figure(figsize=(8, 6))
        sns.heatmap(numeric_data.corr(), annot=True, cmap='coolwarm', center=0)
        plt.title('数值变量相关性热力图')
        plt.tight_layout()

        if save_path:
            plt.savefig(save_path)
        plt.show()

# 4. 报告生成器
print("\n=== 4. 报告生成器 ===")

class ReportGenerator:
    """报告生成器"""

    def __init__(self, analyzer: SalesAnalyzer, visualizer: DataVisualizer):
        self.analyzer = analyzer
        self.visualizer = visualizer

    def generate_html_report(self, output_file: str = "sales_report.html"):
        """生成HTML报告"""
        html_content = f"""
        <!DOCTYPE html>
        <html>
        <head>
            <title>销售数据分析报告</title>
            <meta charset="utf-8">
            <style>
                body {{ font-family: Arial, sans-serif; margin: 40px; }}
                h1 {{ color: #333; }}
                h2 {{ color: #666; margin-top: 30px; }}
                table {{ border-collapse: collapse; width: 100%; margin: 20px 0; }}
                th, td {{ border: 1px solid #ddd; padding: 12px; text-align: left; }}
                th {{ background-color: #f2f2f2; }}
                .summary {{ background-color: #f9f9f9; padding: 20px; border-radius: 5px; }}
                .metric {{ display: inline-block; margin: 10px; padding: 10px; background-color: #e8f4f8; border-radius: 5px; }}
            </style>
        </head>
        <body>
            <h1>销售数据分析报告</h1>
            <p>生成时间: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}</p>
        """

        # 基本统计信息
        stats = self.analyzer.basic_statistics()
        html_content += """
            <h2>基本统计信息</h2>
            <div class="summary">
        """
        for key, value in stats.items():
            if isinstance(value, (int, float)):
                formatted_value = f"{value:,.2f}" if isinstance(value, float) else f"{value:,}"
            else:
                formatted_value = value
            html_content += f'<div class="metric"><strong>{key}:</strong> {formatted_value}</div>'
        html_content += "</div>"

        # 类别分析
        category_data = self.analyzer.category_analysis()
        html_content += f"""
            <h2>产品类别分析</h2>
            <table>
                <tr>
                    <th>类别</th>
                    <th>总销售额</th>
                    <th>订单数</th>
                    <th>平均订单金额</th>
                    <th>总数量</th>
                </tr>
        """
        for index, row in category_data.iterrows():
            html_content += f"""
                <tr>
                    <td>{index}</td>
                    <td>{row['总销售额']:,.2f}</td>
                    <td>{row['订单数']}</td>
                    <td>{row['平均订单金额']:,.2f}</td>
                    <td>{row['总数量']}</td>
                </tr>
            """
        html_content += "</table>"

        # 城市分析
        city_data = self.analyzer.city_analysis()
        html_content += f"""
            <h2>城市销售分析</h2>
            <table>
                <tr>
                    <th>城市</th>
                    <th>销售额</th>
                    <th>订单数</th>
                    <th>平均订单金额</th>
                    <th>客户数</th>
                </tr>
        """
        for index, row in city_data.iterrows():
            html_content += f"""
                <tr>
                    <td>{index}</td>
                    <td>{row['城市销售额']:,.2f}</td>
                    <td>{row['订单数']}</td>
                    <td>{row['平均订单金额']:,.2f}</td>
                    <td>{row['客户数']}</td>
                </tr>
            """
        html_content += "</table>"

        html_content += """
        </body>
        </html>
        """

        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(html_content)
        print(f"HTML报告已生成: {output_file}")

    def generate_csv_report(self, output_file: str = "sales_report.csv"):
        """生成CSV报告"""
        # 合并所有分析数据
        all_data = []

        # 基本统计
        stats = self.analyzer.basic_statistics()
        for key, value in stats.items():
            all_data.append({"类型": "基本统计", "指标": key, "值": value})

        # 类别数据
        category_data = self.analyzer.category_analysis()
        for index, row in category_data.iterrows():
            for col in category_data.columns:
                all_data.append({
                    "类型": "类别分析",
                    "指标": f"{index}-{col}",
                    "值": row[col]
                })

        # 写入CSV
        with open(output_file, 'w', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=['类型', '指标', '值'])
            writer.writeheader()
            writer.writerows(all_data)

        print(f"CSV报告已生成: {output_file}")

# 5. 主程序
print("\n=== 5. 主程序 ===")

def main():
    """主分析程序"""
    print("开始数据分析...")

    # 1. 生成数据
    generator = DataGenerator()
    data = generator.generate_sales_data(num_records=500)
    print(f"生成了 {len(data)} 条销售记录")

    # 保存原始数据
    data.to_csv("sales_data.csv", index=False, encoding='utf-8')
    print("原始数据已保存到 sales_data.csv")

    # 2. 创建分析器
    analyzer = SalesAnalyzer(data)

    # 3. 分析数据
    print("\n=== 基本统计信息 ===")
    stats = analyzer.basic_statistics()
    for key, value in stats.items():
        if isinstance(value, (int, float)):
            formatted_value = f"{value:,.2f}" if isinstance(value, float) else f"{value:,}"
        else:
            formatted_value = value
        print(f"{key}: {formatted_value}")

    print("\n=== 产品类别分析 ===")
    category_data = analyzer.category_analysis()
    print(category_data)

    print("\n=== 月度销售分析 ===")
    monthly_data = analyzer.monthly_analysis()
    print(monthly_data.head())

    print("\n=== 城市销售分析 ===")
    city_data = analyzer.city_analysis()
    print(city_data)

    print("\n=== 客户分析 ===")
    customer_data = analyzer.customer_analysis()
    print(customer_data.sort_values('客户总消费', ascending=False).head(10))

    print("\n=== 产品分析 ===")
    product_data = analyzer.product_analysis()
    print(product_data.head(10))

    # 4. 创建可视化
    print("\n生成可视化图表...")
    visualizer = DataVisualizer(data, analyzer)

    # 生成图表
    visualizer.plot_category_sales("category_sales.png")
    visualizer.plot_monthly_trend("monthly_trend.png")
    visualizer.plot_city_comparison("city_comparison.png")
    visualizer.plot_top_customers(10, "top_customers.png")
    visualizer.plot_product_performance("product_performance.png")
    visualizer.plot_correlation_heatmap("correlation_heatmap.png")

    # 5. 生成报告
    print("\n生成报告...")
    report_generator = ReportGenerator(analyzer, visualizer)
    report_generator.generate_html_report("sales_analysis_report.html")
    report_generator.generate_csv_report("sales_analysis_report.csv")

    print("\n数据分析完成！")
    print("生成的文件:")
    print("- sales_data.csv (原始数据)")
    print("- sales_analysis_report.html (HTML报告)")
    print("- sales_analysis_report.csv (CSV报告)")
    print("- 多个PNG格式的图表文件")

# 6. 交互式分析
print("\n=== 6. 交互式分析 ===")

def interactive_analysis():
    """交互式数据分析"""
    print("=== 交互式数据分析模式 ===")

    # 生成数据
    generator = DataGenerator()
    data = generator.generate_sales_data(num_records=200)
    analyzer = SalesAnalyzer(data)

    while True:
        print("\n可用分析选项:")
        print("1. 基本统计")
        print("2. 类别分析")
        print("3. 月度分析")
        print("4. 城市分析")
        print("5. 客户分析")
        print("6. 产品分析")
        print("7. 生成图表")
        print("8. 退出")

        choice = input("\n请选择分析类型 (1-8): ").strip()

        if choice == '1':
            stats = analyzer.basic_statistics()
            print("\n基本统计信息:")
            for key, value in stats.items():
                if isinstance(value, (int, float)):
                    formatted_value = f"{value:,.2f}" if isinstance(value, float) else f"{value:,}"
                else:
                    formatted_value = value
                print(f"  {key}: {formatted_value}")

        elif choice == '2':
            print("\n类别分析:")
            print(analyzer.category_analysis())

        elif choice == '3':
            print("\n月度分析:")
            print(analyzer.monthly_analysis())

        elif choice == '4':
            print("\n城市分析:")
            print(analyzer.city_analysis())

        elif choice == '5':
            print("\n客户分析 (Top 10):")
            customer_data = analyzer.customer_analysis()
            print(customer_data.sort_values('客户总消费', ascending=False).head(10))

        elif choice == '6':
            print("\n产品分析 (Top 10):")
            print(analyzer.product_analysis().head(10))

        elif choice == '7':
            visualizer = DataVisualizer(data, analyzer)
            print("\n生成图表中...")
            visualizer.plot_category_sales()
            visualizer.plot_monthly_trend()
            visualizer.plot_city_comparison()
            visualizer.plot_top_customers(10)

        elif choice == '8':
            print("退出交互式分析")
            break

        else:
            print("无效选择，请重试")

# 程序入口
if __name__ == "__main__":
    # 检查是否安装了必要的库
    required_libraries = ['pandas', 'numpy', 'matplotlib', 'seaborn']
    missing_libraries = []

    for lib in required_libraries:
        try:
            __import__(lib)
        except ImportError:
            missing_libraries.append(lib)

    if missing_libraries:
        print(f"缺少必要的库: {', '.join(missing_libraries)}")
        print("请运行以下命令安装:")
        print(f"pip install {' '.join(missing_libraries)}")
        print("\n运行完整分析示例:")
        main()
    else:
        print("库检查通过，开始分析...")
        # 取消注释以下行来运行完整分析
        # main()

        # 运行交互式分析
        interactive_analysis()

print("\n程序执行完毕！")