from flask import Flask, render_template
from models.manufacturer import Manufacturer
from models.product_series import Product_Series
from repositories import product_repository
from repositories import product_series_repository 
from controllers.edit_controller import edit_blueprint
from controllers.manufacturer.manufacturer_controller import manufacturer_blueprint
from controllers.product_series.product_series_controller import product_series_blueprint
from controllers.product.product_controller import product_blueprint
app = Flask(__name__)
app.register_blueprint(edit_blueprint)
app.register_blueprint(manufacturer_blueprint)
app.register_blueprint(product_series_blueprint)
app.register_blueprint(product_blueprint)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/inventory')
def inventory():
    products = product_repository.select_all()
    product_series =  product_series_repository.select_all()
    return render_template("main_inventory.html", products = products, product_series = product_series)

@app.route('/inventory/all')
def all_inventory():
    products = product_repository.select_all()
    product_series =  product_series_repository.select_all()
    return render_template("all_inventory.html", products = products, product_series = product_series)


if __name__ == '__main__':
    app.run(debug=True)