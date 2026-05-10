name: Build APK

on:
  push:
    branches:
      - main

env:
  FORCE_JAVASCRIPT_ACTIONS_TO_NODE24: true

jobs:
  build:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout repository
        uses: actions/checkout@v4

      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.11'

      - name: List files (Debug)
        run: |
          echo "Checking directory structure..."
          ls -R

      - name: Install system dependencies
        run: |
          sudo apt update
          sudo apt install -y zip unzip openjdk-17-jdk python3-pip python3-setuptools python3-wheel libffi-dev autoconf automake libtool pkg-config zlib1g-dev libncurses5-dev libncursesw5-dev libtinfo5 cmake

      - name: Install buildozer and cython
        run: |
          pip install --upgrade pip
          pip install "cython<3.0.0"
          pip install buildozer

      - name: Build with Buildozer
        run: |
          # اگر فایل buildozer.spec در ریشه نیست، به پوشه مربوطه برو
          # فرض می‌کنیم فایل‌ها در ریشه هستند، اگر نبود در لاگ LS معلوم می‌شود
          yes | buildozer android debug

      - name: Upload APK
        uses: actions/upload-artifact@v4
        with:
          name: apk
          path: bin/*.apk
