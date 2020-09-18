import datetime
import json
import requests
import sys
import io
import os
import cgi
import cgitb
cgitb.enable(display=1)


def main02():

    # おまじない
    print('Content-type: text/html; charset=UTF-8')
    print("\r\n\r\n")

    with open("log.txt", mode="w") as f:
        f.write(str(datetime.datetime.now())+":START\n")

        # POSTデータの判定
        if (os.environ['REQUEST_METHOD'] != "POST"):
            f.write(str(datetime.datetime.now())+":METHOD不正\n")
        else:
            f.write(str(datetime.datetime.now())+":METHOD=POST\n")

        # 標準入力で対応する場合
        # 但し連続した文字列になり処理が面倒
        # 例）myname=yamada&mypass=abcde&myclss=level2
        # 通常は辞書形式
        data = sys.stdin.read()
        f.write(str(datetime.datetime.now()) + str(data))


def main01():
    # おまじない
    print('Content-type: text/html; charset=UTF-8')
    print("\r\n\r\n")

    with open("log.txt", mode="w") as f:
        f.write(str(datetime.datetime.now())+":START\n")

        # POSTデータの判定
        if (os.environ['REQUEST_METHOD'] != "POST"):
            f.write(str(datetime.datetime.now())+":METHOD不正\n")
        else:
            f.write(str(datetime.datetime.now())+":METHOD=POST\n")

        # データ取得
        form = cgi.FieldStorage()
        # データを切り分けする場合の方法

        # その1：個別に取り出したいとき
        # form_key = form.getfirst("myname")
        # form_pass = form.getfirst("mypass")

        f.write(str(datetime.datetime.now())+":DATA取得\n")

        # その2：キーが分からない場合
        for key in form.keys():
            variable = str(key)
            value = str(form.getvalue(variable))
            f.write(str(key)+":"+value+"\n")

        f.write(str(datetime.datetime.now())+":送信\n")

        # jsonデータを作成する
        # まずは辞書形式を作ってjson形式に変換する
        dict = {"result": "OK", "message": "python is good!!"}
        json_data = json.dumps(dict)

        f.write(str(json_data)+"\n")

        # 今回のpythonサーバの場合は不要
        # print("Content-type: application/json")
        # print("\n\n")

        print(json_data)
        # print('\n')

        f.write(str(datetime.datetime.now())+":END\n")


def main():
    # おまじない
    print("Content-type: text/html; charset=UTF-8")
    print("\r\n\r\n")

    # POSTデータの判定
    if (os.environ['REQUEST_METHOD'] != "POST"):
        print("METHOD不正")

    # データ取得
    form = cgi.FieldStorage()

    # データを切り分けする場合の方法

    # その1：個別に取り出したいとき
    # form_key = form.getfirst("myname")
    # form_pass = form.getfirst("mypass")

    # データを切り分けする場合の方法
    # その2：キーが分からない場合
    for key in form.keys():
        variable = str(key)
        value = str(form.getvalue(variable))

    # jsonデータを作成する
    # まずは辞書形式を作ってjson形式に変換する
    dict = {"result": "OK", "message": "python is good!!"}
    json_data = json.dumps(dict)

    # 今回のpythonサーバの場合は不要
    # print("Content-type: application/json")
    # print("\n\n")

    print(json_data)
    # print('\n')


if __name__ == "__main__":

    main()

    # main()にログ出力する機能付き
    # main01()

    # 入力をstdinを使ってみたパターン
    # main02()


# https://gist.github.com/peace098beat/bb037b5230e5ad612692
# https://max999blog.com/python-requests-get-post-json-data/
# https://note.nkmk.me/python-requests-web-api/
