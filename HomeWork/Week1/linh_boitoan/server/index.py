# Import standard library

# Import thư viện bên ngoài
from flask import Flask


# Import module/package trong project
from boitoan.route import boi_toan

app = Flask(__name__)

# Register blueprint
app.register_blueprint(boi_toan)


if __name__ == '__main__':
    app.run(host="127.0.0.1", port=8000, debug=True)