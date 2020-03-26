#! /usr/bin/env make

init-dev:		## 初始化开发环境
	./init.sh

install-dev:	## 开发依赖的包
	source venv/bin/activate && \
	pip install -r requirements.dev.txt

install: 		## 运行依赖
	pip install -r requirements.txt



.PHONY: help
.DEFAULT_GOAL := help

# Ref: https://marmelab.com/blog/2016/02/29/auto-documented-makefile.html
help:
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'