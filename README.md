# ipv6-ftp-server

[English](README_en.md) | 简体中文

这是一个使用 `pyftpdlib` 实现的支持 IPv6 的 FTP 服务器项目。
这个项目是由本人口述，全权交给Copilot Claude 3.5 Sonnet 模型实现的，test可以跑通。

## 项目结构

```
ipv6-ftp-server/
├── src/
│   ├── __init__.py
│   ├── server.py         # FTP 服务器主入口
│   └── config/
│       ├── __init__.py
│       └── settings.py   # 服务器配置文件
├── tests/
│   ├── __init__.py
│   └── test_server.py    # 测试用例
├── scripts/
│   ├── format_check.bat  # Windows 格式检查脚本
│   └── format_check.sh   # Linux 格式检查脚本
├── .github/
│   └── workflows/
│       └── ci.yml        # CI 配置文件
├── logs/
│   └── .gitkeep
├── requirements.txt      # 项目依赖
├── requirements-dev.txt  # 开发依赖
├── environment.yml       # Conda 环境配置
├── setup.py             # 包安装配置
├── .gitignore
└── README.md            # 项目文档
```

## 安装依赖

在项目根目录下运行以下命令以安装所需的依赖：

```bash
# 使用 pip 安装
pip install -r requirements.txt
pip install -r requirements-dev.txt  # 如果需要开发环境

# 或使用 conda 安装
conda env create -f environment.yml
conda activate ipv6-ftp-server
```

## 运行服务器

要启动 FTP 服务器，请运行以下命令：

```bash
python src/server.py
```

## 运行测试

```bash
# 运行所有测试
pytest tests/ -v

# 运行特定测试文件
pytest tests/test_server.py -v

# 运行特定测试用例
pytest tests/test_server.py::TestFTPServer::test_add_binary_file -v
```

## 代码格式检查

```bash
# Windows
scripts\format_check.bat --check  # 只检查格式
scripts\format_check.bat         # 自动修复格式

# Linux
./scripts/format_check.sh --check  # 只检查格式
./scripts/format_check.sh         # 自动修复格式
```

## 配置

在 `src/config/settings.py` 文件中，您可以配置服务器地址、端口和用户认证详细信息。

## 日志

服务器日志将保存在 `logs` 目录中。请确保该目录存在并被 Git 跟踪。