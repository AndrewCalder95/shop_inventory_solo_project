from flask import Flask, render_template, request, redirect
from flask import Blueprint
from flask.templating import render_template_string
from models.manufacturer import Manufacturer
from models.product import Product
from models.product_series import Product_Series
from repositories import product_series_repository
from repositories import product_repository
from repositories import manufacturer_repository

manufacturer_blueprint = Blueprint("manufacturer", __name__)


@manufacturer_blueprint.route('/edit/add_manufacturer', methods=['GET'])
def new_manufacturer():
    return render_template('edit/add/manufacturer.html')

@manufacturer_blueprint.route('/edit/add_manufacturer', methods=['POST'])
def add_manufacturer():
    name = request.form["name"]
    manufacturer = Manufacturer(name)
    if name != "":
        manufacturer_repository.save(manufacturer)
    return redirect ('/edit/add_menu')

@manufacturer_blueprint.route('/edit/update/manufacturer', methods = ['GET'])
def update_manufacturer():
    manufacturers = manufacturer_repository.select_all()
    return render_template ('edit/update/manufacturer.html', manufacturers = manufacturers)

@manufacturer_blueprint.route('/edit/update/manufacturer', methods = ['POST'])
def deactivate_manufacturer(id):
    manufacturer = manufacturer_repository.select(id)
    manufacturer_repository.mark_deactive(manufacturer)
    return redirect ('/inventory' )