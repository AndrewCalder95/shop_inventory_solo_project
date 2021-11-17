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
def update_menu():
    return render_template("edit/add/menu.html")

@edit_blueprint.route('/edit/update/menu')
def add_menu():
    return render_template("edit/update/menu.html")