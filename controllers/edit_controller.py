from itertools import product
from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.manufacturer import Manufacturer
from models.product import Product

from models.product_series import Product_Series
from repositories import product_series_repository
from repositories import product_repository

edit_blueprint = Blueprint("tasks", __name__)

@edit_blueprint.route('/edit')
def edit():
    return render_template("edit/edit.html")

@edit_blueprint.route('/edit/add', methods=['GET'])
def new_product():
    product = product_repository.select_all()
    product_series = product_series_repository.select_all()

    return render_template('edit/add.html', users=product, all_product_series = product_series)

# @edit_blueprint.route('/edit/add', methods = ['POST'])
# def add():
#     colour = request.form['colour']
#     wood = request.form['wood']
#     in_stock = request.form['in_stock']
#     purchase_cost = request.form['purchase_cost']
#     selling_price = request.form['selling_price']
#     product_series = product_series_repository.select(request.form["product_series_id"])
#     product = Product(colour, wood, in_stock, purchase_cost, selling_price, product_series)
#     product_repository.save(product)
#     return redirect('/')

# @edit_blueprint.route('/edit/update', methods = ['GET','POST'])
# def update_product():
#     colour = request.form['colour']
#     wood = request.form['wood']
#     in_stock = request.form['in_stock']
#     purchase_cost = request.form['purchase_cost']
#     selling_price = request.form['selling_price']
#     product_series = product_series_repository.select(request.form['user_id'])
#     product = Product(colour, wood, in_stock, purchase_cost, selling_price, product_series)
#     product.save(product)
#     return redirect('/inventory')