#!/bin/bash

# Parse arguments
CHECK_ONLY=0
if [ "$1" == "--check" ]; then
    CHECK_ONLY=1
fi

# Only activate conda in non-CI environment
if [ -z "$CI" ]; then
    # Activate conda environment
    source ~/anaconda3/etc/profile.d/conda.sh
    conda activate
fi

echo "Checking code format..."

# Check required tools in non-CI environment
if [ -z "$CI" ]; then
    if ! python -c "import black" &> /dev/null; then
        echo "Installing black..."
        conda install -c conda-forge black -y
    fi

    if ! python -c "import isort" &> /dev/null; then
        echo "Installing isort..."
        conda install -c conda-forge isort -y
    fi
fi

# Run format checks/fixes
if [ $CHECK_ONLY -eq 1 ]; then
    echo "Running black check..."
    black --check src/ tests/
    if [ $? -ne 0 ]; then
        echo "Black check failed!"
        exit 1
    fi

    echo "Running isort check..."
    isort --check-only src/ tests/
    if [ $? -ne 0 ]; then
        echo "Isort check failed!"
        exit 1
    fi
else
    echo "Formatting with black..."
    black src/ tests/
    
    echo "Formatting with isort..."
    isort src/ tests/
fi

echo "All done!"
exit 0