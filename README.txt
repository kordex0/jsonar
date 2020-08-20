
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
>> uvicorn rentals.main:app --reload



USING THE WEBSERVER

I have written up a quick client.py script to emulate a usage of the web server. After turning
on the webserver this can be run and will print out the responses of some calls to the webserver.

The other way to use the webserver is to go to localhost:8000/docs which is an auto-generated
openapi specification of the endpoints, and allows testing of all the endpoints.




TESTING THE WEBSERVER

Testing has been set up with pytest. To run the tests, use this command:
>> pytest tests

The tests assume that the database has been loaded with DVDRentals-customers.json in the customers collection
and DVDRentals-films.json in the films collection





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
    "id": 3,
    "title": "ADAPTATION HOLES",
    "category": "Documentary",
    "description": "A Astounding Reflection of a Lumberjack And a Car who must Sink a Lumberjack in A Baloon Factory",
    "rating": "NC-17",
    "rental_duration": "7"
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


