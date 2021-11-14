from db.run_sql import run_sql

from models.product import Product
from models.product_series import Product_Series
from models.manufacturer import Manufacturer

# def save(manufacturer):
#     sql = "INSERT INTO manufacturers (name) VALUES (%s) RETURNING *"
#     values = [manufacturer.name]
#     results = run_sql(sql, values)
#     id = results[0]['id']
#     manufacturer.id = id
#     return manufacturer


def select(id):
    manufacturer = None
    sql = "SELECT * FROM manufacturers WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        manufacturer = Manufacturer(result['name'], result['id'],)
    return manufacturer