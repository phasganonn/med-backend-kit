import log_util

def test_stock_add(api_client):
    """药品入库接口测试"""
    data = {"drug_name":"布洛芬", "num":100, "batch":"20260701"}
    res = api_client.post("/stock/add", json_data=data)
    if res.status_code != 200:
        log_util.TestLog.save_error_log("药品入库", res.status_code, res.text)
    assert res.status_code == 200
    assert res.json()["code"] == 0

def test_stock_query(api_client):
    """库存查询边界测试：负数数量"""
    res = api_client.get("/stock/query", params={"num":-10})
    if res.status_code != 400:
        log_util.TestLog.save_error_log("负数库存查询", res.status_code, res.text)
    assert res.status_code == 400
