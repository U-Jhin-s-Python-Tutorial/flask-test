from flask import Flask, request


app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        params = request.args
    elif request.method == 'POST':
        params = request.form
    
    result = ''
    for key, value in params.items():
        result += 'key: ' + key + ', value: ' + value + '\n'
    return result


if __name__ == '__main__':    
    app.run()
