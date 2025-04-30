@echo off
setlocal

:: Parse arguments
set CHECK_ONLY=0
if "%1"=="--check" set CHECK_ONLY=1

echo Checking code format...

:: Activate conda environment
call conda activate

:: Check required tools
python -c "import black" 2>NUL
if errorlevel 1 (
    echo Installing black...
    conda install -c conda-forge black -y
)

python -c "import isort" 2>NUL
if errorlevel 1 (
    echo Installing isort...
    conda install -c conda-forge isort -y
)

:: Run format checks/fixes
if %CHECK_ONLY%==1 (
    echo Running black check...
    black --check src/ tests/
    if errorlevel 1 (
        echo Black check failed!
        exit /b 1
    )

    echo Running isort check...
    isort --check-only src/ tests/
    if errorlevel 1 (
        echo Isort check failed!
        exit /b 1
    )
) else (
    echo Formatting with black...
    black src/ tests/
    
    echo Formatting with isort...
    isort src/ tests/
)

echo All done!
endlocal
exit /b 0