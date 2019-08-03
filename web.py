import os
import glob
import string
import random
import psycopg2
import socket
import base64
import requests
import json
import datetime
import urllib.parse
import numpy as np
from psycopg2.extras import DictCursor
from flask import Flask, render_template, request, redirect, url_for
app = Flask(__name__)

# 外部pythonファイル
import eval
import database
import textdef as td

# ファイルのパスワードの桁数
FILE_PASSWORD_DIGIT=4

# デフォルト言語
DEFAULT_LANGUAGE="en"

# バルスフラグ
BARUSU = os.environ.get("BARUSU")

# POST APIのURL
POST_URL = os.environ.get("POST_URL")
# ファイル置き場のURL
STORAGE_URL = os.environ.get("STORAGE_URL")
# アプリのURL
APP_URL = os.environ.get("APP_URL")
# アップロードフォルダ
UPLOAD_FOLDER = './static/uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
# タイトルファイル名
TITLE_IMAGE={"en":"title_en.png","ja":"title.png"}


# 炎上時の破壊処理
@app.route('/barusu', methods=['GET'])
def barusu():
    database.barusu()
    return redirect("/closed")


# 破壊された世界
@app.route('/closed', methods=['GET'])
def acsess_closed_page():
    return render_template('closed.html')


# 普通に開いたとき
@app.route('/k', methods=['GET'])
def acsess_main_page():
    
    # バルス判定
    if database.check_barusu()==True:
        return redirect("/closed")
    
    # クエリパラメータを取得
    language=request.args.get("l")
    if language == None:
        language = DEFAULT_LANGUAGE
    file_id=request.args.get("i")
    
    
    textdef=td.get_textdef(language)
    
    title_image=TITLE_IMAGE.get(language)
    
    if title_image==None:
        title_image=TITLE_IMAGE.get(DEFAULT_LANGUAGE)

    if file_id == None:
        return render_template('index.html',
                               language=language,
                               textdef=textdef,
                               textdef_text=json.dumps(textdef), 
                               title_image=title_image
                              )
    else:
        # データベースからレコードを読み込み
        with database.get_connection() as conn:
            with conn.cursor(cursor_factory=DictCursor) as cur:
                cur.execute("SELECT * FROM images WHERE file_id=%s",(file_id,))
                record=cur.fetchone()
        
        if record==None:
            # データベースに該当レコードがなかったら
            return redirect("/image_missing?l="+language)
        else:
            # 
            result=record["result"]
            result_texts=[];
            for r in result:
                result_texts.append(textdef[r["name"]]+": "+str(r["rate"])+"％")
                
            detail=" / ".join(result_texts)
            
            answer=textdef[result[0]["name"]]
            
            img_path=STORAGE_URL+record["file_id"]
            
            url=urllib.parse.quote(APP_URL+"/k?l="+language+"&i="+record["file_id"])
              
            return render_template('result.html',
                                   language=language,
                                   filepath=img_path, 
                                   detail=detail, 
                                   answer=answer, 
                                   url=url,
                                   textdef=textdef,
                                   textdef_text=json.dumps(textdef), 
                                   title_image=title_image
                                  )



# 画像をアップロードしたとき
@app.route('/post', methods=['POST'])
def uploads_file():
    
    # バルス判定
    if database.check_barusu()==True:
        return redirect("/closed")
    
    language=request.form["language"]
    if language ==None:
        language = DEFAULT_LANGUAGE
    
    if request.files['file']:
        file = request.files['file']
        ip = request.remote_addr;
        user_agent = request.environ['HTTP_USER_AGENT'];
        date=datetime.datetime.today()
        
        with database.get_connection() as conn:
            with conn.cursor(cursor_factory=DictCursor) as cur:
                
                # 一時保存用のIDを得る
                cur.execute("INSERT INTO images (ip,user_agent,created_at) VALUES(%s,%s,%s) RETURNING id;",(ip,json.dumps(user_agent),date))
                record = cur.fetchone()
                id=record["id"]
                
                # 画像を一時保存して解析結果を得る（一時保存しなくても良い方法があるなら、上記のIDを得る処理は下記のDB保存処理と統合したい）
                img_path = os.path.join(app.config['UPLOAD_FOLDER'], str(id))
                file.save(img_path)
                result=eval.evaluation(img_path)
                os.remove(img_path)
                
                 # 画像をストレージに保存
                file.seek(0)
                data=base64.b64encode(file.read())
                headers = {'content-type': 'application/base64'}
                res = requests.post(POST_URL, headers=headers, data=data)
                res_result=json.loads(res.text)
                file_id=res_result["file_id"]
                
                # DBに保存
                cur.execute("UPDATE images SET file_id=%s, result=%s WHERE id=%s;",(file_id,json.dumps(result),id))
            conn.commit()
        
        return redirect("/k?l="+language+"&i="+file_id)
    
    textdef=td.get_textdef(language)
    
    
    title_image=TITLE_IMAGE.get(language)
    if title_image==None:
        title_image=TITLE_IMAGE.get(DEFAULT_LANGUAGE)
    
    html = render_template('index.html',language=language,textdef=textdef,textdef_text=json.dumps(textdef),title_image=title_image)
    return html


# 画像がないとき
@app.route('/image_missing', methods=['GET'])
def acsess_image_missing_page():
    # バルス判定
    if database.check_barusu()==True:
        return redirect("/closed")
    
    language=request.args.get("l")
    textdef=td.get_textdef(language)
    title_image=TITLE_IMAGE.get(language)
    if title_image==None:
        title_image=TITLE_IMAGE.get(DEFAULT_LANGUAGE)
        
    html = render_template('image_missing.html',textdef=textdef,title_image=title_image)
    return html
    

# 管理用
@app.route('/management', methods=['GET'])
def open_managemant_page():
    # バルス判定
    if database.check_barusu()==True:
        return redirect("/closed")
    
    if os.environ.get("MANAGEMENT_CODE") ==request.args.get("management_code"):
        with database.get_connection() as conn:
            with conn.cursor(cursor_factory=DictCursor) as cur:
                cur.execute("SELECT * FROM images;")
                records=cur.fetchall()
        
        html = render_template('management.html', items=records)
    else:
        html = None
    return html


if __name__ == "__main__":
    app.run()
