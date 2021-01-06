# import thư viện chuẩn

# import thư viện cài thêm
from flask import Blueprint, request, jsonify
import http

# import package

sample = Blueprint("sample", __name__)

name = [{"title": "Something"}]


@sample.route('/')
def home():
     return jsonify({'message': "hello, world"})


@sample.route("/boitoan/", methods=['GET', 'POST'])
def cal():
    if request.method == "GET":
        res = _get_boitoan()
    elif request.method == "POST":
        res = _post_boitoan(request)
        print(res.format("year_of_man"))
        print(res.format("year_of_woman"))
    return res


# Calculate function
def _get_boitoan():
    return "ok"

def _post_boitoan(req):
    body = req.json
    print(f"body = {body}")


    year_of_man = body.get("man")
    year_of_woman = body.get("woman")

    if year_of_man == "2000":
        return "Kim"
    else: return "Orther"

    if year_of_woman == "1998":
        return "Hỏa"
    else:
        return "Orther"

    for _ in body:
        return _
