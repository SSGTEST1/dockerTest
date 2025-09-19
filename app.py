from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return '<h1>Hello, Docker World!</h1><p>This is a simple web app running inside a Docker container.</p>'

if __name__ == '__main__':
    # 컨테이너 외부에서 접근 가능하도록 host를 '0.0.0.0'으로 설정
    app.run(host='0.0.0.0', port=5000)
