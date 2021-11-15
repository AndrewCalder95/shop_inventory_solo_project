from db.run_sql import run_sql

from models.product import Product
from models.product_series import Product_Series
from repositories import product_series_repository


def select_all():
    products = []

    sql = f"SELECT * FROM products"
    results = run_sql(sql)

    for row in results:
        product_series = product_series_repository.select(row['product_series_id'])
        product = Product(row['colour'], row['wood'], row['in_stock'], row['purchase_cost'], row['selling_price'], product_series, row ['id'])
        products.append(product)
    return products

def save(product):
    sql = "INSERT INTO products (colour, wood, in_stock, purchase_cost, selling_price, product_series_id) VALUES (%s, %s, %s, %s, %s, %s) RETURNING *"
    values = [product.colour, product.wood, product.in_stock, product.purchase_cost, product.selling_price, product.product_series.id]
    result = run_sql(sql, values)
    id = result[0]['id']
    product.id = id 
    return product