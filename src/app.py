from flask import Flask
app = Flask(__name__)

@app.route('/')
def IndexPage():
    return 'Hello World!'

if __name__ == '__main__':
    app.run()