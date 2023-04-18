from os import name
from flask import Blueprint, render_template, request, redirect
from repositories import city_repository, country_repository, sight_repository
from models.city import City
from models.country import Country
from models.sight import Sight
import pdb

cities_blueprint = Blueprint("cities", __name__)




#INDEX
# GET /my-list
@cities_blueprint.route("/my-list")
def my_list():
    all_cities = city_repository.select_all()
    return render_template("my-list/index.html", all_cities=all_cities)

# countries

# NEW COUNTRY
# GET /my-list/new-country
@cities_blueprint.route("/my-list/new-country")
def add_country():
    countries = country_repository.select_all()
    return render_template("my-list/new-country.html", all_countries=countries)


# CREATE
# POST /my-list/countries
@cities_blueprint.route("/my-list", methods=["POST"])
def create_country():
    name = request.form['country_id']
    country = Country(name)
    all_countries = country_repository.select_all()
    found = False
    for countryElement in all_countries:
        if countryElement.name == country.name:
            found = True
    if found == False:
        country_repository.save(country)
    return redirect("/my-list/new-country")

# EDIT
@cities_blueprint.route("/my-list/<id>/edit-country")
def edit_country(id):
    country=country_repository.select(id)
    return render_template("my-list/edit-country.html", country=country)    


# UPDATE
@cities_blueprint.route("/my-list/<id>/update",methods=["POST"])
def update_country(id):
    name=request.form['country_id']
    country=Country(name, id)
    country_repository.update(country)
    return redirect("/my-list/new-country")


# DELETE
# DELETE (POST) /my-list/<id>/delete
@cities_blueprint.route("/my-list/<id>/delete-country", methods=["POST"])
def delete_country(id):
    country_repository.delete(id)
    return redirect("/my-list")


# cities

# # NEW CITY
# # GET /my-list/new
@cities_blueprint.route("/my-list/new")
def add():
    cities = city_repository.select_all()
    countries = country_repository.select_all()
    return render_template("my-list/new.html", all_cities=cities, all_countries=countries)


# # CREATE
# # POST /my-list
@cities_blueprint.route("/mylist", methods=["POST"])
def create_city():
    name = request.form['city']
    country_id = request.form['country_id']
    visited = request.form['visited']
    country = country_repository.select(country_id)
    city=City(name, country, visited)
    all_cities = city_repository.select_all()
    found = False
    for cityElement in all_cities:
        if cityElement.name == city.name:
            found = True
    if found == False:
        city_repository.save(city)
    return redirect("/my-list")

# SHOW
# GET /my-list/<id>
@cities_blueprint.route("/my-list/<id>")
def show_city(id):
    city=city_repository.select(id)
    return render_template("my-list/show.html", city=city)

# # SHOW
# # GET /my-list/<id>/visited
# @cities_blueprint.route("/my-list/<id>")
# def show_visited():
#     city=city_repository.select_all()
#     return render_template("my-list/visited.html", city=city)

# # SHOW
# # GET /my-list/<id>/not-visited
# @cities_blueprint.route("/my-list/<id>")
# def show_not_visited():
#     city=city_repository.select(id)
#     return render_template("my-list/show.html", city=city)

# EDIT
# GET /my-list/<id>/edit
@cities_blueprint.route("/my-list/<id>/edit")
def edit_city(id):
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
@cities_blueprint.route("/my-list/<id>/delete", methods=["POST"])
def delete_city(id):
    city_repository.delete(id)
    return redirect("/my-list")

# sights

# EDIT
# GET
@cities_blueprint.route("/my-list/<id>/sights/edit")
def edit_sight(id):
    sight=sight_repository.select(id)
    cities=city_repository.select_all
    return render_template("my-list/edit-sights.html", sight=sight, all_cities=cities)  

# UPDATE
# PUT (POST) /my-list/<id>
@cities_blueprint.route("/my-list/<id>/sights/update",methods=["POST"])
def update_sight(id):
    event=request.form['event']
    review=request.form['review']
    city_id=request.form['city_id']
    city=city_repository.select(city_id)
    sight=Sight(event, review, city, id)
    city_repository.update(city)
    return redirect("/my-list/<id>")