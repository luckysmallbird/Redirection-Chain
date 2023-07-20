from flask import *

app = Flask(__name__)

@app.route('/')
def main():
    html_file_path = './static/main.html'
    return send_file(html_file_path)

@app.route('/redirect.js')
def redirect():
    html_file_path = './static/redirect.html'
    return send_file(html_file_path)

@app.route('/file_download')
def file():
    html_file_path = './download/download.html'
    return send_file(html_file_path)

@app.route('/Chrome_update')
def chrome():
    html_file_path = './download/danger.txt'
    return send_file(html_file_path , as_attachment=True)

# flask run --host=0.0.0.0 --port=80