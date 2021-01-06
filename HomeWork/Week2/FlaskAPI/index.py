#import thư viện chuẩn

#import thư viện cài thêm
from flask import Flask

#import package
from src.boitoan import sample


app = Flask(__name__)

#blueprints
app.register_blueprint(sample)

if __name__ == "__main__":
    app.run(host=None, port="5000", debug=True)