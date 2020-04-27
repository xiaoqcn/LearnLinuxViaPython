#! /usr/bin/env make

init-dev:		## 初始化开发环境
	./init.sh

install-dev:	## 开发依赖的包
	source venv/bin/activate && \
	pip install -r requirements.dev.txt

install: 		## 运行依赖
	pip install -r requirements.txt

e1:		## demo1
	python3 -m learn_epoll.demo_01

e2:		## demo2
	python3 -m learn_epoll.demo_psutil

e3:		## demo3
	python3 -m learn_epoll.demo_simple

e5:		## multi process
	nohup python3 -m learn_epoll.multi_process 1>>1.txt 2>>2.txt &

e5s:	## 停止
	cat ~/demo.pid|xargs kill -15



.PHONY: help
.DEFAULT_GOAL := help

# Ref: https://marmelab.com/blog/2016/02/29/auto-documented-makefile.html
help:
	@grep -E '^[a-zA-Z1-9_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'