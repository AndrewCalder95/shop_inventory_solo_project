from flask import Flask, render_template
from repositories import product_repository
from repositories import product_series_repository 
from controllers.edit_controller import edit_blueprint
app = Flask(__name__)
app.register_blueprint(edit_blueprint)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/inventory')
def inventory():
    products = product_repository.select_all()
    return render_template("main_inventory.html", products = products)


if __name__ == '__main__':
    app.run(debug=True)