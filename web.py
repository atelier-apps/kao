import os
import glob
import string
import random
import eval
from flask import Flask, render_template, request, redirect, url_for
app = Flask(__name__)
UPLOAD_FOLDER = './static/uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
FILE_NAME_DIGIT=10

# 普通に開いたとき
@app.route('/p', methods=['GET'])
def open():
    q_i=request.args.get("i")
    if q_i != None:
        print("s")
        img_path = os.path.join(app.config['UPLOAD_FOLDER'], q_i)
        result = eval.evaluation(img_path)
        answer=result[0]["name"]
        if os.environ.get("APP_URL") ==None:
            os.environ["APP_URL"] = "dummyURL"
        url=os.environ.get('APP_URL')+"/p?i="+q_i
        detail=""
        result_texts=[];
        for r in result:
            result_texts.append(r["name"]+": "+str(r["rate"])+"％")
        detail=" / ".join(result_texts)    
        html = render_template('result.html',filepath=img_path, detail=detail, answer=answer, url=url)
    else:
        html = render_template('index.html')
    return html

# 管理用
@app.route('/management', methods=['GET'])
def open_managemant_page():
    if os.environ.get("MANAGEMENT_CODE") ==request.args.get("management_code"):
        items=glob.glob(UPLOAD_FOLDER+"/*")
        html = render_template('management.html', items=items)
    else:
        html = None
    return html


# 画像をアップロードしたとき
@app.route('/post', methods=['POST'])
def uploads_file():
    if request.files['file']:
        file = request.files['file']
        filename=get_file_name()
        img_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(img_path)
        return redirect("/p?i="+filename)  
    else:
        html = render_template('index.html')
    return html


def get_file_name():
    dat = string.digits
    name=None
    for i in range(50):
        n="i"+''.join([random.choice(dat) for i in range(FILE_NAME_DIGIT)])
        exist=os.path.exists(os.path.join(app.config['UPLOAD_FOLDER'], n))
        if exist==False:
            name=n
    if name ==None:
        for i in range(FILE_NAME_DIGIT):
            n="i"+i.zfill(FILE_NAME_DIGIT)
            exist=os.path.exists(os.path.join(app.config['UPLOAD_FOLDER'], n))
            if exist==False:
                name=n
    return name

if __name__ == "__main__":
    app.run()
    



