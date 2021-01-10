# import thư viện chuẩn

# import thư viện ngoài
from flask import Flask

# import thư viện trong
from boitoan.route import boi_toan

app = Flask(__name__)

# register blueprint
app.register_blueprint(boi_toan)


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5003, debug=True)
