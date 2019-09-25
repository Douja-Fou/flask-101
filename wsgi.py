# wsgi.py
from flask import Flask
from flask import jsonify
app = Flask(__name__)
PRODUCTS = [
    { 'id': 1, 'name': 'Skello' },
    { 'id': 2, 'name': 'Socialive.tv' },
    { 'id': 3, 'name': 'news.tv' }]

@app.route('/')
def hello():
    return "Hello World!"

@app.route('/api/v1/products', methods=['GET'])
def products():
    return jsonify(PRODUCTS)

@app.route('/api/v1/products/<int:id>', methods=['GET'])
def products(id):
    return 'PRODUCTS %s' % id
