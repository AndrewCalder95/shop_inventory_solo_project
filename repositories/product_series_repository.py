from db.run_sql import run_sql

from models.product_series import Product_Series


def select(id):
    product_series = None
    sql = "SELECT * FROM product_series WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        product_series = Product_Series(result['name'], result['skill_level'], result['id'] )
    return product_series

def select_all():
    product_series = []

    sql = f"SELECT * FROM product_series"
    results = run_sql(sql)

    for row in results:
        individual_product_series = Product_Series(row['name'], row['skill_level'], row['manufacturer_id'])
        product_series.append(individual_product_series)
    return product_series