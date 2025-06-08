from models import Product, Customer, Order, session
import random
from datetime import datetime, timedelta

customer_list = [
    Customer(name = "小明", email = "ming@example.com"),
    Customer(name = "小華", email = "hua@example.com"),
    Customer(name = "小美", email = "mei@example.com"),
    Customer(name = "小強", email = "chiang@example.com"),
    Customer(name = "小綠", email = "green@example.com")
]

product_list = [
    Product(name = "耳機", price = 800),
    Product(name = "滑鼠", price = 600),
    Product(name = "鍵盤", price = 1200),
    Product(name = "螢幕", price = 4000),
    Product(name = "音響", price = 2500)
]


def rand_c():
    c = session.query(Customer).all()
    rc = random.choice(c)
    return rc.id

def rand_p():
    p = session.query(Product).all()
    rp = random.choice(p)
    return rp.id

def rq():
    return random.randint(1,5)

#從start到end之前隨機產生datetime
def random_date(start, end):
    delta = end - start
    random_days = random.randint(0, delta.days)
    return start + timedelta(days=random_days)

order_list = []
start_time = datetime(2024,1,1)
end_time = datetime(2024,3,1)

for _ in range(10):
    order = Order(
        customer_id = rand_c(),
        product_id = rand_p(),
        quantity = rq(),
        order_date = random_date(start_time,end_time))
    order_list.append(order)

session.add_all(order_list)
# session.add_all(customer_list)
# session.add_all(product_list)
session.commit()
print("成功插入訂單！")