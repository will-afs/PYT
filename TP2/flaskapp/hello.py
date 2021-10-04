from flask import Flask, request
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def hello_world():
    print(request.args)
    print(request.form)
    return 'Hello, World!\n\n' # + request.args