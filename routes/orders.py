# routes/orders.py
from flask import Blueprint, render_template, request
from models import session, Order, Customer, Product
from datetime import datetime

orders_bp = Blueprint("orders", __name__)

def get_filtered_orders():
    customer_name = request.args.get("customer")
    start_date = request.args.get("start")
    end_date = request.args.get("end")

    query = session.query(Order)

    if customer_name:
        query = query.join(Order.customer).filter(Customer.name == customer_name)

    if start_date:
        start_dt = datetime.strptime(start_date, "%Y-%m-%d")
        query = query.filter(Order.order_date >= start_dt)

    if end_date:
        end_dt = datetime.strptime(end_date, "%Y-%m-%d")
        query = query.filter(Order.order_date <= end_dt)

    #加入排序功能
    sort_by = request.args.get("sort")
    if sort_by == "amount_desc":
        query = query.join(Order.product).order_by((Order.quantity * Product.price).desc())
    elif sort_by == "amount_asc":
        query = query.join(Order.product).order_by((Order.quantity * Product.price).asc())
    elif sort_by == "date_desc":
        query = query.order_by(Order.order_date.desc())
    elif sort_by == "date_asc":
        query = query.order_by(Order.order_date.asc())

    orders = query.all()
    return orders, customer_name, start_date, end_date, sort_by



@orders_bp.route("/orders")
def show_orders():
    orders, customer_name, start_date, end_date, sort_by = get_filtered_orders()
    return render_template("orders.html", orders=orders)