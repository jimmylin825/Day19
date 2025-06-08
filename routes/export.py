# routes/export.py
from flask import Blueprint, Response, send_file
from io import StringIO, BytesIO
from openpyxl import Workbook
import csv
from .orders import get_filtered_orders
from utils import generate_filename

export_bp = Blueprint("export", __name__)

@export_bp.route("/export_csv")
def export_csv():
    orders,customer_name, start_date, end_date, sort_by = get_filtered_orders()
    output = StringIO()
    writer = csv.writer(output)
    writer.writerow(["顧客名稱", "商品名稱", "單價", "數量", "總金額", "訂單日期"])
    for order in orders:
        writer.writerow([
            order.customer.name,
            order.product.name,
            order.product.price,
            order.quantity,
            order.quantity * order.product.price,
            order.order_date.strftime("%Y-%m-%d")
        ])

    filename = generate_filename(customer_name, start_date, end_date, "csv")
    response = Response(output.getvalue(), content_type="text/csv")
    response.headers["Content-Disposition"] = f"attachment; filename={filename}"
    return response

@export_bp.route("/export_excel")
def export_excel():
    orders,customer_name, start_date, end_date, sort_by = get_filtered_orders()
    wb = Workbook()
    ws = wb.active
    ws.title = "訂單報表"

    ws.append(["顧客名稱", "商品名稱", "單價", "數量", "總金額", "訂單日期"])
    total_sum = 0
    for order in orders:
        subtotal = order.quantity * order.product.price
        total_sum += subtotal
        ws.append([
            order.customer.name,
            order.product.name,
            order.product.price,
            order.quantity,
            subtotal,
            order.order_date.strftime("%Y-%m-%d")
        ])
    ws.append(["", "", "","", "總金額", total_sum])


    filename = generate_filename(customer_name, start_date, end_date, "xlsx")
    output = BytesIO()
    wb.save(output)
    output.seek(0)
    return send_file(output, as_attachment=True, download_name=filename,
                     mimetype="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")
