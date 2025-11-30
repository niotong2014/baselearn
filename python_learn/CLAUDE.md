# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## 项目概述

这是一个Python学习代码库，用于学习和实践Python编程。由于是学习项目，代码结构可能会经常变化，包含各种练习、示例和实验性代码。

## 开发环境设置

### 虚拟环境
```bash
# 创建虚拟环境
python -m venv venv

# 激活虚拟环境
# macOS/Linux:
source venv/bin/activate
# Windows:
venv\Scripts\activate

# 停用虚拟环境
deactivate
```

### 依赖管理
```bash
# 安装依赖
pip install -r requirements.txt

# 生成requirements.txt
pip freeze > requirements.txt
```

## Python代码规范

### 运行Python文件
```bash
# 运行单个Python文件
python filename.py

# 运行带有参数的Python文件
python filename.py arg1 arg2

# 使用Python 3
python3 filename.py
```

### 代码检查
```bash
# 使用flake8进行代码检查
flake8 .

# 使用black格式化代码
black .

# 使用isort整理导入
isort .
```

## 测试
```bash
# 运行所有测试
pytest

# 运行特定测试文件
pytest test_specific.py

# 运行带覆盖率的测试
pytest --cov=.

# 运行unittest测试
python -m unittest discover
```

## 项目结构建议

对于学习项目，建议按以下结构组织：
- `exercises/` - 练习题代码
- `examples/` - 示例代码
- `projects/` - 完整项目实践
- `notes/` - 学习笔记
- `utils/` - 通用工具函数

## 学习资源开发

在这个代码库中工作时：
1. 代码注释应该包含学习要点和解释
2. 为学习概念创建清晰的示例
3. 包含足够的文档字符串
4. 使用print语句展示程序执行过程（学习阶段）
5. 创建可交互的代码示例

## Git工作流

```bash
# 初始化Git仓库
git init

# 添加所有文件
git add .

# 提交更改
git commit -m "描述更改"

# 查看状态
git status

# 查看更改
git diff
```

## 常见任务

### 创建新的Python练习
1. 创建新的Python文件，命名清晰描述练习内容
2. 添加必要的注释和文档字符串
3. 包含示例用法和预期输出
4. 如果需要，添加对应的测试文件

### 调试Python代码
```bash
# 使用Python调试器
python -m pdb filename.py

# 或者使用breakpoint()
# 在代码中添加：breakpoint()
```

## 注意事项

1. 这是一个学习环境，代码可能包含故意错误用于调试学习
2. 某些文件可能是为了演示特定概念而创建的
3. 代码可能会频繁修改和重构
4. 优先考虑代码的可读性和教育价值，而不是性能优化