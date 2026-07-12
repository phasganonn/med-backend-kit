import time

class TestLog:
    @staticmethod
    def save_error_log(case_name, resp_code, msg):
        """记录接口bug日志，保存到本地txt"""
        timestamp = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        content = f"[{timestamp}] 用例:{case_name} 状态码:{resp_code} 异常:{msg}\n"
        with open("error_log.txt", "a", encoding="utf-8") as f:
            f.write(content)
