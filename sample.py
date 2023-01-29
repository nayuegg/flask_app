#必要なモジュールのインポート
from flask import Flask

#　Flask をインスタンス化
app = Flask(__name__)

# ルートディレクトリ（URLに最初にアクセスしたときに表示されるところ）にアクセスがあった時の処理
@app.route('/') 
def hello():
    return 'Hello World!'

# エントリーポイントを設定ーSample.pyが直接実行された場合
if __name__ == '__main__':
    app.run()

#kの後コントロールCでローカルサーバから出る