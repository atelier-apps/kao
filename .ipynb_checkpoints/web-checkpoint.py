import os
from flask import Flask, render_template, request
app = Flask(__name__)
UPLOAD_FOLDER = './static/uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
 
# 普通に開いたとき
@app.route('/')
def hello():
    html = render_template('index.html',filename="default.jpg", data={"kim":"?%","phone":"?%"})
    return html


# 画像をアップロードしたとき
@app.route('/', methods=['POST'])
def uploads_file():
        file = request.files['file']
        if file:
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], file.filename))
            
            
            # ここで判定処理可能
            data={"kim":"","phone":""}
            data["kim"]="80%"
            data["phone"]="20%"
            
            
            html = render_template('index.html',filename=file.filename, data=data)
            return html

        

if __name__ == "__main__":
    app.run()