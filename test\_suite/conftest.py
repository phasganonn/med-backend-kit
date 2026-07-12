import pytest
import requests

# 全局测试服务地址
@pytest.fixture(scope="session")
def base_url():
    return "http://127.0.0.1:5000/api"

# 统一请求封装
@pytest.fixture(scope="session")
def api_client(base_url):
    class Client:
        def get(self, path, params=None):
            return requests.get(f"{base_url}{path}", params=params)
        def post(self, path, json_data=None):
            return requests.post(f"{base_url}{path}", json=json_data)
    return Client()
