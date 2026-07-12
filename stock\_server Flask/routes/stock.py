from flask import Blueprint, request, jsonify
import db

stock_bp = Blueprint("stock", __name__)

# 药品入库
@stock_bp.route("/api/stock/add", methods=["POST"])
def stock_add():
    data = request.get_json()
    name = data.get("drug_name")
    num = data.get("num")
    batch = data.get("batch")
    if not all([name, num, batch]) or int(num) <= 0:
        return jsonify({"code":-1, "msg":"参数非法"}), 400
    db.db_execute("INSERT INTO drug_stock(drug_name,stock_num,batch_no) VALUES (?,?,?)", (name, num, batch))
    return jsonify({"code":0, "msg":"入库成功"})

# 库存查询
@stock_bp.route("/api/stock/query", methods=["GET"])
def stock_query():
    num = request.args.get("num", 0, type=int)
    if num < 0:
        return jsonify({"code":-1, "msg":"数量不能为负"}), 400
    data = db.db_execute("SELECT * FROM drug_stock WHERE stock_num >= ?", (num,))
    return jsonify({"code":0, "data":data})
