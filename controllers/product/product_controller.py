import pdb
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
    return render_template('edit/add/add_product.html', all_product_series = product_series)
 
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
    return redirect('/edit/add_menu')


@product_blueprint.route('/edit/<id>/update')
def view_product(id):
    product = product_repository.select(id)
    return render_template('edit/update/product.html', product = product)

@product_blueprint.route('/edit/<id>/update', methods = ['POST'])
def update_product(id):
    colour = request.form['colour']
    wood = request.form['wood']
    in_stock = request.form['in_stock']
    purchase_cost = request.form['purchase_cost']
    selling_price = request.form['selling_price']
    product_series = request.form['product_series']
    product = Product(colour, wood, in_stock, purchase_cost, selling_price, product_series, id)
    product_repository.update(product)
    return redirect ('/edit/update')

@product_blueprint.route('/edit/<id>/delete', methods=['POST']) 
def delete_product(id):
    product_repository.delete(id)
    return redirect('/edit/update')