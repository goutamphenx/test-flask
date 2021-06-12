from flask import Flask, app

app = Flask(__name__)


@app.route('/')
def helloWorld():
    return 'Hello world'


@app.route('/home')
def home():
    return 'Welcome to home'


if __name__ == '__main__':
    app.run()
