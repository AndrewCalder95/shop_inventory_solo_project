from flask import Flask, render_template
from repositories import product_repository
from repositories import product_series_repository 

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/inventory')
def inventory():
    products = product_repository.select_all()
    return render_template("main_inventory.html", products = products)

@app.route('/edit')
def edit():
    return render_template("edit/edit.html")