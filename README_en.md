# ipv6-ftp-server

[English](README_en.md) | [简体中文](README.md)

An IPv6-enabled FTP server implementation using `pyftpdlib`.
This project was implemented by Copilot Claude 3.5 Sonnet model under my dictation, with passing tests.

## Project Structure

```
ipv6-ftp-server/
├── src/
│   ├── __init__.py
│   ├── server.py         # Main FTP server entry point
│   └── config/
│       ├── __init__.py
│       └── settings.py   # Server configuration
├── tests/
│   ├── __init__.py
│   └── test_server.py    # Test cases
├── scripts/
│   ├── format_check.bat  # Windows format check script
│   └── format_check.sh   # Linux format check script
├── .github/
│   └── workflows/
│       └── ci.yml        # CI configuration
├── logs/
│   └── .gitkeep
├── requirements.txt      # Project dependencies
├── requirements-dev.txt  # Development dependencies
├── environment.yml      # Conda environment config
├── setup.py            # Package setup config
├── .gitignore
└── README.md           # Project documentation
```

## Installation

Run the following commands in the project root directory:

```bash
# Using pip
pip install -r requirements.txt
pip install -r requirements-dev.txt  # For development environment

# Or using conda
conda env create -f environment.yml
conda activate ipv6-ftp-server
```

## Running the Server

To start the FTP server, run:

```bash
python src/server.py
```

## Running Tests

```bash
# Run all tests
pytest tests/ -v

# Run specific test file
pytest tests/test_server.py -v

# Run specific test case
pytest tests/test_server.py::TestFTPServer::test_add_binary_file -v
```

## Code Format Checking

```bash
# Windows
scripts\format_check.bat --check  # Check only
scripts\format_check.bat         # Auto-fix

# Linux
./scripts/format_check.sh --check  # Check only
./scripts/format_check.sh         # Auto-fix
```

## Configuration

Server address, port, and user authentication details can be configured in `src/config/settings.py`.

## Logging

Server logs will be saved in the `logs` directory. Make sure this directory exists and is tracked by Git.