# Thu vien standard

# ThirdParty
from flask import Blueprint, jsonify, request

# Thu vien ben trong

# Blueprintのインスタンス生成
boitoan = Blueprint("boitoan", __name__)

# làm thế nào để định nghĩa POST, GET


# app decorator
@boitoan.route('/boitoan/', methods=('GET', 'POST'))
def boi_toan():
    if request.method == 'POST':
        ret = _post_boi_toan(request)
    elif request.method == 'GET':
        ret = _get_boi_toan()

    return ret


# Module: function noi bo nen them _(protect), __(private)
def _post_boi_toan(req):
    # Nhận thông tin năm và xử lý
    # Query Parameter
    # Body (Json) {"man": 1998}
    body = req.json
    print("body = {}".format(body))

    year_of_man = body.get("man")
    print("year_of_man = {}".format(year_of_man))

    if year_of_man == 1998:
        return "HOA"
    else:
        return "OTHER"


def _get_boi_toan(req):
    return "OK"