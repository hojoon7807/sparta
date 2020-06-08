from pymongo import MongoClient           # pymongo를 임포트 하기(패키지 인스톨 먼저 해야겠죠?)
from bs4 import BeautifulSoup
import requests
from flask import Flask, render_template, jsonify, request
app = Flask(__name__)


client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.dbsparta                      # 'dbsparta'라는 이름의 db를 만듭니다.

# HTML을 주는 부분


@app.route('/')
def home():
    return render_template('원페이지쇼핑몰.html')


@app.route('/orders', methods=['GET'])
def listing():
    orders = list(db.orders.find({},{'_id':0}))
    return jsonify({'result': 'success', 'orders': orders})

# API 역할을 하는 부분


@app.route('/orders', methods=['POST'])
def order():

    receive_name = request.form['give_name']
    receive_amount = request.form['give_amount']
    receive_address = request.form['give_address']
    receive_call = request.form['give_call']

    order={
    'name':receive_name, 'amount':receive_amount, 'address':receive_address, 'call':receive_call
    }
    db.orders.insert_one(order)
    return jsonify({'result': 'success', 'msg':'주문이 완료되었습니다'})
if __name__ == '__main__':
    app.run('0.0.0.0',port=5000,debug=True)
