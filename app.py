from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    # 이 아래 return 부분을 원하는 HTML로 수정하세요.
    return '''
    <html>
        <head>
            <title>My New Page</title>
        </head>
        <body>
            <h1>웹페이지 내용이 바뀌었습니다! ✅</h1>
            <p>이 내용은 app.py 파일을 수정하여 변경되었습니다.</p>
        </body>
    </html>
    '''

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
