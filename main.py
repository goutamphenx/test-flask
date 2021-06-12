from flask import Flask, app

app = Flask(__name__)


@app.route('/')
def helloWorld():
    print('We are in root')
    return 'Hello world'


@app.route('/home')
def home():
    print('We are in home')
    return 'Welcome to home'


if __name__ == '__main__':
    print('We are in main')
    app.run()
