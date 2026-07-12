# med-backend-kit
医药流通系统轻量化后端工具集
整合实习期间开发的自动化接口测试套件 + 库存管理Web业务模块，适配中小型医药企业管理系统快速开发。

## 项目功能
1. pytest自动化接口测试工具：批量校验HTTP接口、自动输出bug日志、预置医药业务测试用例
2. Flask轻量化库存模块：药品入库、出库、库存统计、简单分层架构，可直接嵌入后台管理系统

## 技术栈
Python 3.10 + Flask + pytest + SQLite
基础算法、单元测试、Web接口开发

## 快速启动
1. 安装依赖
pip install -r requirements.txt
2. 启动库存服务
python stock_server/app.py
3. 执行自动化测试
pytest test_suite/test_api.py -v

## 作者信息
谢胜杰 | 安徽工业大学 机器人工程本科
实习项目开源沉淀，适配医药类后端开发实训场景
