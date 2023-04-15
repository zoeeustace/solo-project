from flask import Blueprint, render_template
from repositories import city_repository, country_repository
from models.city import City

cities_blueprint = Blueprint("cities", __name__)

#INDEX
# GET /my-list
@cities_blueprint.route("/my-list")
def my_list():
    all_cities = city_repository.select_all()
    return render_template("my-list/index.html", all_cities=all_cities)

# NEW
# GET /my-list/new
@cities_blueprint.route("/my-list/new")
def add():
    countries = country_repository.select_all()
    return render_template("my-list/new")

# CREATE
# POST /my-list

# SHOW
# GET /my-list/<id>

# EDIT
# GET /my-list/<id>/edit

# UPDATE
# PUT (POST) /my-list/<id>

# DELETE
# DELETE (POST) /my-list/<id>/delete