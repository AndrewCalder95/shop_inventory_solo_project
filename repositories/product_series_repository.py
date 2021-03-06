from db.run_sql import run_sql
from models.manufacturer import Manufacturer

from models.product_series import Product_Series
from models.manufacturer import Manufacturer
from repositories import manufacturer_repository


def select(id):
    product_series = None
    sql = "SELECT * FROM product_series WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        manufacturer = manufacturer_repository.select(result['manufacturer_id'])
        product_series = Product_Series(result['name'], result['skill_level'], manufacturer, result['id'])
    return product_series

def select_all():
    product_series = []

    sql = "SELECT * FROM product_series"
    results = run_sql(sql)

    for row in results:
        manufacturer = manufacturer_repository.select(row['manufacturer_id'])
        individual_product_series = Product_Series(row['name'], row['skill_level'], manufacturer, row['id'])
        product_series.append(individual_product_series)
    return product_series


def save(product_series):
    sql = "INSERT INTO product_series (name, skill_level, manufacturer_id) VALUES (%s, %s, %s) RETURNING *"
    values = [product_series.name, product_series.skill_level, product_series.manufacturer.id]
    results = run_sql(sql, values)
    id = results[0]['id']
    product_series.id = id
    return product_series

def product_series(id):
    sql = "DELETE FROM product_series WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def update(product_series):
    sql = "UPDATE product_series SET (name, skill_level) = (%s, %s) WHERE id = %s"
    values = [product_series.name, product_series.skill_level, product_series.id]
    run_sql(sql, values)   

def delete(id):
    sql = "DELETE FROM product_series WHERE id = %s"
    values = [id]
    run_sql(sql, values)