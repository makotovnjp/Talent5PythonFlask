# 開発環境構築
1. conda create -n FlaskDemo python=3.8
2. conda activate FlaskDemo
3. pip install -r requirements.txt

# サーバー実行
1. python index.py

# サンプルのAPI (POSTMANで試せます)
1.  POST http://127.0.0.1:5000/api/sample/news
    - body (JSON): {"title": "news1"}
    
2. GET http://127.0.0.1:5000/api/sample/news?title=new1
    
