
Tested using Python 3.8



SETUP STEPS


setup virtual environment
>> python -m venv venv
>> source venv/bin/activate


install python requirements
>> pip install -r requirements.txt


setup .env file
>> echo "MONGO_URI=<mongo uri here>" >> .env


my .env file looked like this:
MONGO_URI=mongodb://localhost:27017/rentals




RUNNING THE WEBSERVER

This command will run the webserver:
>> uvicorn rentals.main:app


If you would like to run the webserver and have it reload every
time code changes, you can run:
>>> uvicorn rentals.main:app --reload





ENDPOINTS


Return a list of customers

GET /customers
[
  {
    "id": 1,
    "first_name": "MARY",
    "last_name": "SMITH"
  },
  ...
]


Return the details of a customers (not including their rentals)

GET /customers/{customer_id}
{
  "id": 1,
  "first_name": "MARY",
  "last_name": "SMITH",
  "address": "1913 Hanoi Way",
  "city": "Sasebo",
  "country": "Japan",
  "district": "Nagasaki",
  "phone": "28303384290"
}


Return a list of the movies that a customer has rented

GET /customers/{customer_id}/rentals
[
  {
    "rental_date": "2005-06-15T00:54:12",
    "days_rented": 8,
    "cost": 5.99
  },
  ...
]


Return a list of films that are available for renting

GET /available_films
[
  {
    "id": 2,
    "title": "ACE GOLDFINGER",
    "category": "Horror",
    "description": "A Astounding Epistle of a Database Administrator And a Explorer who must Find a Car in Ancient China",
    "rating": "G",
    "rental_duration": "3"
  },
  ...
]


Returns the details of a film

GET /films/{film_id}
{
  "id": 1,
  "title": "ACADEMY DINOSAUR",
  "category": "Documentary",
  "description": "A Epic Drama of a Feminist And a Mad Scientist who must Battle a Teacher in The Canadian Rockies",
  "rating": "PG",
  "rental_duration": "6",
  "length": "86",
  "replacement_cost": 20.99,
  "special_features": [
    "Deleted Scenes",
    "Behind the Scenes"
  ],
  "actors": [
    {
      "first_name": "PENELOPE",
      "last_name": "GUINESS",
      "actor_id": 1
    },
    ...
  ]
}


Returns a list of the people who have ever rented this film

GET /films/{film_id}/renters
[
  {
    "id": 8,
    "first_name": "SUSAN",
    "last_name": "WILSON"
  },
  ...
]


