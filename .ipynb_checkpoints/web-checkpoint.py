import os
import eval
from flask import Flask, render_template, request, redirect, url_for
app = Flask(__name__)
UPLOAD_FOLDER = './static/uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
DEFAULT_DATA = [{'label':0, 'name':'金正恩', 'rate':'?'},
               {'label':1, 'name':'黒電話', 'rate':'?'},
               {'label':2, 'name':'その他', 'rate':'?'}]
DEFAULT_PIC = "default.jpg"
 
# 普通に開いたとき
@app.route('/')
def hello():
    html = render_template('index.html',filename=DEFAULT_PIC, data=DEFAULT_DATA)
    return html


# 画像をアップロードしたとき
@app.route('/post', methods=['GET', 'POST'])
def uploads_file():
    if request.method == 'POST':
        if request.files['file']:
            file = request.files['file']
            img_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
            file.save(img_path)
            result = eval.evaluation(img_path) 
            html = render_template('index.html',filename=file.filename, data=result)
        else:
            html = render_template('index.html',filename=DEFAULT_PIC, data=DEFAULT_DATA)
        return html
    else:
        return redirect(url_for('index'))      

if __name__ == "__main__":
    app.run()
    