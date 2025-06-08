from collections import Counter


def generate_filename(customer_name=None, start_date=None, end_date=None, filetype="csv"):
    filename = "orders"
    if customer_name:
        filename += f"_{customer_name}"
    if start_date and end_date:
        filename += f"_{start_date}_to_{end_date}"
    elif start_date:
        filename += f"after_{start_date}"
    elif end_date:
        filename += f"before_{end_date}"
    return f"{filename}.{filetype}"

#（回傳總數、總金額、平均金額、最熱門商品）
def get_order_summary(orders):
    total_count = len(orders)
    total_amount = 0
    product_counter = Counter()

    for order in orders:
        sub_total = order.quantity * order.product.price
        total_amount += sub_total
        product_counter[order.product.name] += order.quantity

    avg_amount = round(total_amount / total_count, 2) if total_count > 0 else 0
    most_common_product = product_counter.most_common(1)[0][0] if product_counter else "無"

    return {
        "total_count" : total_count,
        "total_amount" : total_amount,
        "avg_amount" : avg_amount,
        "most_common_product" : most_common_product
    }


