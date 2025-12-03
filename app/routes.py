from flask import Blueprint

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return '<h1>Welcome!</h1><p>This is the Main Index page</p>'

@main.route('/trucks')
def trucks():
    return "<h1>Truck list goes here</h1>"

@main.route('/drivers')
def drivers():
    return "<h1>Driver list goes here</h1>"