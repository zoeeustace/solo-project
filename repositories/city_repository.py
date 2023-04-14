from db.run_sql import run_sql
from models.city import City
from models.country import Country
import repositories.country_repository as country_repository

def save(city):
    sql = "INSERT INTO cities (name, country_id, visited) VALUES (%s, %s, %s) RETURNING *"
    values = [city.name, city.country.id, city.completed]
    results = run_sql(sql, values)
    id = results[0]['id']
    city.id = id
    return city

def delete_all():
    sql = "DELETE FROM cities"
    run_sql(sql)