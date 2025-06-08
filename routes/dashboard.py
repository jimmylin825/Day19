from flask import Blueprint, render_template
from .orders import get_filtered_orders
from utils import get_order_summary

dashboard_bp = Blueprint("dashboard", __name__)

@dashboard_bp.route("/dashboard")
def dashboard():
    orders, customer_name, start_date, end_date, sort_by = get_filtered_orders()
    summary = get_order_summary(orders)
    return render_template("dashboard.html", summary = summary)