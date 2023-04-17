from db.run_sql import run_sql

from models.country import Country
from models.city import City
from models.sight import Sight
from repositories import city_repository

def save(sight):
    sql = "INSERT INTO sights (event, review, city_id) VALUES (%s, %s, %s) RETURNING *"
    values = [sight.event, sight.review, sight.city.id]
    results = run_sql(sql, values)
    id = results[0]['id']
    sight.id = id
    return sight

def select_all():
    sights = []

    sql = "SELECT * FROM sights"
    results = run_sql(sql)

    for row in results:
        city = city_repository.select(row['city_id'])
        sight = Sight(row['event'], row['review'], city, row['id'] )
        sights.append(sight)
    return sights

def select(id):
    sight = None
    sql = "SELECT * FROM sights WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        city = city_repository.select(result['city_id'])
        sight = Sight(result['event'], result['review'], city, result['id'] )
    return sight


def delete_all():
    sql = "DELETE FROM sights"
    run_sql(sql)

def delete(id):
    sql = "DELETE  FROM sights WHERE id = %s"
    values = [id]
    run_sql(sql, values)


def update(sight):
    sql = "UPDATE sights SET (event, review, city) = (%s, %s, %s) WHERE id = %s"
    values = [sight.event, sight.review, sight.city.id, sight.id]
    run_sql(sql, values)
