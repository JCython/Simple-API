from flask import *
import json, time

app = Flask(__name__)

global p1
p1 = "no player"
global p2
p2 = "no player"
@app.route('/', methods=['GET'])
def home():
    return "home"
@app.route('/p1/', methods=['GET'])
def pa():
    a = str(request.args.get('data'))
    global p1
    p1 = a
    return p2
@app.route('/p2/', methods=['GET'])
def pb():
    a = str(request.args.get('data'))
    global p2
    p2 = a
    return p1

#  run app
if __name__ == '__main__':
    app.run(port=7777)
