from flask import Flask
from CodeDoc.page import Page

app = Flask(__name__)

@app.route('/')
def main():
    page = Page('pages/documentation/index.html')

    page.SetTitle('This is title')
    page.SetVariable('text', 'This is text')

    return page.GetRenderTemplate()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
