# 標準ライブラリ

# ThirdPartyのライブラリ
from flask import Flask

# 内部のモジュール、パッケージ
from sample.route import sample


# アプリのインスタンス作成
app = Flask(__name__)

# BluePrint登録
app.register_blueprint(sample)


if __name__ == "__main__":
    # アプリ開始
    app.run(host="127.0.0.1", port=5000, debug=True)
