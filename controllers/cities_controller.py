from os import name
from flask import Blueprint, render_template, request, redirect
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
    cities = city_repository.select_all()
    return render_template("my-list/new.html", all_cities=cities)

# CREATE
# POST /my-list
@cities_blueprint.route("/my-list", methods=["POST"])
def create_city():
    name = request.form['city']
    country_id = request.form['country_id']
    visited = request.form['visited']
    country=country_repository.select(country_id)
    city=City(name, country, visited)
    city_repository.save(city)
    return redirect("/my-list")



                        

# SHOW
# GET /my-list/<id>
@cities_blueprint.route("/my-list/<id>")
def show_city(id):
    city=city_repository.select(id)
    return render_template("my-list/show.html", city=city)

# EDIT
# GET /my-list/<id>/edit
@cities_blueprint.route("/my-list/<id>/edit")
def edit_list(id):
    city=city_repository.select(id)
    countries=country_repository.select_all()
    return render_template("my-list/edit.html", city=city, all_countries=countries)


# UPDATE
# PUT (POST) /my-list/<id>
@cities_blueprint.route("/my-list/<id>",methods=["POST"])
def update_list(id):
    name=request.form['city']
    country_id=request.form['country_id']
    visited=request.form['visited']
    country=country_repository.select(country_id)
    city=City(name,country,visited,id)
    city_repository.update(city)
    return redirect("/my-list")

# DELETE
# DELETE (POST) /my-list/<id>/delete