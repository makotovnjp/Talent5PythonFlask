# 標準ライブラリ

# ThirdPartyのライブラリ
from flask import Blueprint, jsonify, request
import http

# 内部のモジュール、パッケージ

# Blueprintのインスタンス生成
sample = Blueprint("sample", __name__)

# Dummyデータ
news = [{"title": "ABC"}]


# **********************************************************************************************************************
# 公開API
# **********************************************************************************************************************
# メソッド指定しないURL
@sample.route("/api/sample/hello")
def hello():
    return jsonify({'message': "hello"})


# ①Get, Post, PUT, DELETEの作り方
# Get Ex
# http://127.0.0.1:5000/api/sample/news?title=news1
# POST
# http://127.0.0.1:5000/api/sample/news
# body = {"title":"DEF"}
# ②EndPointの作り方
@sample.route("/api/sample/news", methods=['GET', 'POST', 'PUT', 'DELETE'])
def api_news():
    if request.method == 'GET':
        res = _api_news_query(request)
    elif request.method == 'POST':
        res = _api_news_post(request)
    elif request.method == 'PUT':
        res = _api_news_put(request)
    elif request.method == 'DELETE':
        res = _api_news_delete(request)
    else:
        raise ValueError("Not Support Method")

    return res


# **********************************************************************************************************************
# 内部関数
# **********************************************************************************************************************
def _api_news_query(req):
    # ③クエリの受け取り方
    query = req.args
    print(query)

    title = query.get('title')
    print(title)

    print(news)

    if title is not None:
        for item in news:
            if title == item["title"]:
                return jsonify(item), http.HTTPStatus.OK

    return jsonify({"message": "Not existed"}), http.HTTPStatus.BAD_REQUEST


def _api_news_post(req):
    # ④ボディパラメータの受け取り方
    body = req.json
    print("body = {}".format(body))
    news.append(body)

    # ⑤レスポンスの返し方
    return jsonify({"message": "post OK"}), http.HTTPStatus.CREATED


def _api_news_put(req):
    return jsonify(news), http.HTTPStatus.OK


def _api_news_delete(req):
    return jsonify(news), http.HTTPStatus.OK



