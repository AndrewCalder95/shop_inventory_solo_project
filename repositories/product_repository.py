from db.run_sql import run_sql

from models.product import Product
from repositories import product_series_repository


def select_all():
    products = []

    sql = f"SELECT * FROM products"
    results = run_sql(sql)

    for row in results:
        product_series = product_series_repository.select(row['product_series_id'])
        product = Product(row['colour'], row['wood'], row['in_stock'], row['purchase_cost'], row['selling_cost'], product_series)
        products.append(product)
    return products