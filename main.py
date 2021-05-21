from flask import Flask, request
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import check_password_hash

import users

app = Flask(__name__)
auth = HTTPBasicAuth()


@auth.verify_password
def verify_password_and_routes(username, password):
    rule = request.url_rule
    user_data = users.users.get(username)

    if username in users.users \
            and check_password_hash(user_data['pass'], password) \
            and rule.rule in user_data['routes']:
        return username


@app.route('/')
@auth.login_required
def index():
    return "Hello, {}!".format(auth.current_user())


@app.route('/nbnote_invoice')
@auth.login_required
def nbnote_invoice():
    return "Hello, {}!".format(auth.current_user())


if __name__ == '__main__':
    app.run()
