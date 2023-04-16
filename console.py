import pdb
from models.city import City
from models.country import Country

from repositories import city_repository, country_repository

city_repository.delete_all()
country_repository.delete_all()

country_1 = Country("Australia", "Oceania")
country_repository.save(country_1)
country_2 = Country("Portugal", "Europe")
country_repository.save(country_2)

country_repository.select_all()

city_1 = City("Sydney", country_1, True)
city_repository.save(city_1)

city_2 = City("Lisbon", country_2, False)
city_repository.save(city_2)

city_3 = City("Melbourne", country_1, True)
city_repository.save(city_3)

pdb.set_trace()
