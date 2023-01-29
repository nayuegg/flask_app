#coding: utf-8

from flask import Flask, render_template

#appという名前でFlaskをインスタンス化
app = Flask(__name__)

# --- view側の設定 ---
#ルートディレクトリにアクセスした時の挙動
@app.route("/")
#インデックス関数が呼ばれる
def index():
    # return "Hello World!"
    return render_template("index.html")

#エントリーポイントの設定
if __name__ == "__main__":
    app.run()


