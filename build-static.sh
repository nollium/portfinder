#!/bin/sh
# Build script for creating static Linux binaries
# This is run inside an Alpine Linux container

set -e

echo "Installing build dependencies..."
apk add --no-cache gcc musl-dev linux-headers libffi-dev openssl-dev zlib-dev bzip2-dev xz-dev git binutils openssl-libs-static zlib-static

echo "Installing Python dependencies..."
python -m pip install --upgrade pip
pip install -r requirements-build.txt
pip install -e .

echo "Setting up static linking environment..."
export LDFLAGS="-static -Wl,-static -static-libgcc"
export CFLAGS="-static"

echo "Building with PyInstaller..."
pyinstaller --clean --distpath=dist portfinder-static.spec

echo "Testing binary..."
chmod +x dist/portfinder
dist/portfinder --help

echo "Checking binary dependencies..."
ldd dist/portfinder 2>&1 | grep -q "not a dynamic executable" && echo "✅ Binary is fully static" || echo "⚠️  Binary has dynamic dependencies"

echo "Binary size:"
ls -lh dist/portfinder