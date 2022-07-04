from flask import *
import json, time

app = Flask(__name__)

#  home
@app.route('/', methods=['GET'])
def home_page():
    data_set = 'This is the home'

    return data_set



# enter username thing
@app.route('/user/', methods=['GET'])  #  /user/?user=USERNAME
def request_page():
    user_query = str(request.args.get('user'))

    data_set = f'You made the username {user_query}'

    return data_set


#  run app
if __name__ == '__main__':
    app.run(port=7777)
