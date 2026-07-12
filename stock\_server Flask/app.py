from flask import Flask
from routes.stock import stock_bp

app = Flask(__name__)
# 注册库存业务蓝图，分层架构拆分代码
app.register_blueprint(stock_bp)

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)
