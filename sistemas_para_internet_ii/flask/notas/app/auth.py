from flask import Blueprint


auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET'])
def login():
    return '<h1>Login</h1>'

@auth.route('/logout', methods=['GET'])
def logout():
    return '<h1>Logout</h1>'

@auth.route('/signup', methods=['GET'])
def signup():
    return '<h1>Signup</h1>'
