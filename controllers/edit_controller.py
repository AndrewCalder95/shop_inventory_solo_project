from flask import Flask, render_template, request, redirect
from flask import Blueprint

edit_blueprint = Blueprint("tasks", __name__)

@edit_blueprint.route('/edit')
def edit():
    return render_template("edit/edit.html")

@edit_blueprint.route('/edit/add')
def add():
    return render_template("edit/add.html")


