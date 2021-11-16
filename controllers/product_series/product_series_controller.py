from flask import Flask, render_template, request, redirect
from flask import Blueprint
from flask.templating import render_template_string
from models.manufacturer import Manufacturer
from models.product import Product
from models.product_series import Product_Series
from repositories import product_series_repository
from repositories import product_repository
from repositories import manufacturer_repository

product_series_blueprint = Blueprint("product_series", __name__)


@product_series_blueprint.route('/edit/add_product_series')
def new_product_series():
    manufacturer = manufacturer_repository.select_all()
    return render_template('edit/add/add_product_series.html', all_manufacturers = manufacturer)

@product_series_blueprint.route('/edit/add_product_series', methods=['POST'])
def add_product_series():
    name = request.form["name"]
    skill_level = request.form["skill_level"]
    manufacturer_id = request.form["manufacturer_id"]
    # pdb.set_trace()
    manufacturer = manufacturer_repository.select(manufacturer_id)
    product_series = Product_Series(name, skill_level, manufacturer)
    product_series_repository.save(product_series)
    return redirect ('/inventory')