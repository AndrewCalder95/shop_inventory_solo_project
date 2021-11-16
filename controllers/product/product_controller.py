from flask import Flask, render_template, request, redirect
from flask import Blueprint
from flask.templating import render_template_string
from models.manufacturer import Manufacturer
from models.product import Product
from models.product_series import Product_Series
from repositories import product_series_repository
from repositories import product_repository
from repositories import manufacturer_repository

product_blueprint = Blueprint("product", __name__)


@product_blueprint.route('/edit/add_product', methods=['GET'])
def new_product():
    product_series = product_series_repository.select_all()
    return render_template('edit/add/add_product.html', users=product, all_product_series = product_series)
 
@product_blueprint.route('/edit/add_product', methods = ['POST'])
def add():
    colour = request.form['colour']
    wood = request.form['wood']
    in_stock = request.form['in_stock']
    purchase_cost = request.form['purchase_cost']
    selling_price = request.form['selling_price']
    product_series = product_series_repository.select(request.form["product_series_id"])
    product = Product(colour, wood, in_stock, purchase_cost, selling_price, product_series)
    product_repository.save(product)
    return redirect('/edit/add_product')