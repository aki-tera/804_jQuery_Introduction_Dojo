import datetime
import json
import requests
import sys
import io
import os
import cgi
import cgitb
cgitb.enable(display=1)


def main01():
    # おまじない
    print('Content-type: application/json; charset=UTF-8')
    print("\r\n\r\n")

    with open("log.txt", , encoding="utf-8", mode="w") as f:
        f.write(str(datetime.datetime.now())+":START\n")

        # POSTデータの判定
        if (os.environ['REQUEST_METHOD'] != "POST"):
            f.write(str(datetime.datetime.now())+":METHOD不正\n")
        else:
            f.write(str(datetime.datetime.now())+":METHOD=POST\n")

        # データ取得
        form = cgi.FieldStorage()

        f.write(str(datetime.datetime.now())+":DATA取得\n")
        f.write(str(form)+"\n")

        dict = {"result": "OK", "message": "python is very good!!"}

        # その2：キーが分からない場合
        for key in form.keys():
            variable = str(key)
            value = str(form.getvalue(variable))
            f.write(str(key)+":"+value+"\n")
            dict[variable] = value

        f.write(str(datetime.datetime.now())+":送信\n")

        json_data = json.dumps(dict)

        f.write(str(json_data)+"\n")

        # 今回のpythonサーバの場合は不要
        # print("Content-type: application/json")
        # print("\n\n")

        print(json_data)
        # print('\n')

        f.write(str(datetime.datetime.now())+":END\n")


def main():
    # HTTPのレスポンスヘッダ
    print("Content-type: application/json; charset=UTF-8")
    print("\r\n\r\n")

    # POSTデータの判定
    if (os.environ['REQUEST_METHOD'] != "POST"):
        print("METHOD不正")

    # データ取得
    form = cgi.FieldStorage()

    dict = {"result": "OK", "message": "python is very good!!"}

    for key in form.keys():
        variable = str(key)
        value = str(form.getvalue(variable))
        dict[variable] = value

    json_data = json.dumps(dict)

    print(json_data)
    print("\r\n")


if __name__ == "__main__":

    main01()

    # main()にログ出力する機能付き
    # main01()

    # 入力をstdinを使ってみたパターン
    # main02()


# https://gist.github.com/peace098beat/bb037b5230e5ad612692
# https://max999blog.com/python-requests-get-post-json-data/
# https://note.nkmk.me/python-requests-web-api/
