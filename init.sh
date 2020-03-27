#! /usr/bin/env bash

# pyenv --version || true && git --version || true
# pyenv install # 所有可用版本
# pyenv install 3.6.6
# pip intall --upgrade pip
# pip install virtualenv
# pyenv versions || true && pyenv version || true	# 本地安装版本 && 当前目录版本
pyenv local 3.6.6
virtualenv -p $(pyenv which python3) venv