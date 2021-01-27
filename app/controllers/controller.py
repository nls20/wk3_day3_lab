from flask import render_template
from app import app
from app.models.order_list import orders

@app.route('/orders')
def index():
    return render_template('index.html', title='Home', orders=orders)

@app.route('/orders/<index>')
def order(index):
    order_to_return = orders[int(index)]
    return render_template('order.html', title='Order', order_to_return=order_to_return)

