import json

import requests

BASE_URL = "http://localhost:8000"

# get a list of customers
response = requests.get(BASE_URL + "/customers", params={"skip": 30, "limit": 10})
customers = json.loads(response.content)

print(customers)

# get the details of the first customer
response = requests.get(BASE_URL + f"/customers/{customers[0]['id']}")
customer_details = json.loads(response.content)

print(customer_details)

# get the rentals for this customer
response = requests.get(BASE_URL + f"/customers/{customer_details['id']}/rentals", params={"skip": 0, "limit": 10})
rentals = json.loads(response.content)

print(rentals)

# list the available films
response = requests.get(BASE_URL + f"/available_films", params={"skip": 0, "limit": 10})
available_films = json.loads(response.content)

print(available_films)

# get the details of a specific film
response = requests.get(BASE_URL + f"/films/{available_films[0]['id']}", params={"skip": 0, "limit": 10})
film_details = json.loads(response.content)

print(film_details)

# get the previous renters of a specific film
response = requests.get(BASE_URL + f"/films/{available_films[0]['id']}/renters", params={"skip": 0, "limit": 10})
renters = json.loads(response.content)

print(renters)
