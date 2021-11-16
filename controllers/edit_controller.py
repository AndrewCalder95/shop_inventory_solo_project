import pdb
from itertools import product
from flask import Flask, render_template, request, redirect
from flask import Blueprint
from flask.templating import render_template_string
from models.manufacturer import Manufacturer
from models.product import Product
from models.product_series import Product_Series
from repositories import product_series_repository
from repositories import product_repository
from repositories import manufacturer_repository

edit_blueprint = Blueprint("edit", __name__)

@edit_blueprint.route('/edit')
def edit():
    return render_template("edit/edit.html")

@edit_blueprint.route('/edit/add_menu')
def add_menu():
    return render_template("edit/add/add_menu.html")

@edit_blueprint.route('/edit/update')
def pick_a_product():
    products = product_repository.select_all()
    product_series =  product_series_repository.select_all()
    return render_template("edit/update/update_menu.html", products = products, product_series = product_series)

@edit_blueprint.route('/edit/update/<id>')
def view_product(id):
    product = product_repository.select(id)
    return render_template('edit/update/update_product.html', product = product)

@edit_blueprint.route('/edit/update/<id>', methods = ['POST'])
def update_product(id):
    colour = request.form['colour']
    wood = request.form['wood']
    in_stock = request.form['in_stock']
    purchase_cost = request.form['purchase_cost']
    selling_price = request.form['selling_price']
    product_series = product_series_repository.select(request.form["product_series_id"])
    product = Product(colour, wood, in_stock, purchase_cost, selling_price, product_series, id)
    product_repository.update(product)
    return redirect('/edit/update')
