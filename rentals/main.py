from typing import List

from fastapi import FastAPI, HTTPException
from mongoengine import connect

from . import config, models, schemas

connect(host=config.settings.mongo_uri)

app = FastAPI()


@app.get("/customers", response_model=List[schemas.CustomerList])
def list_customers(skip: int = 0, limit: int = 100):
    customers = list(models.Customer.objects().order_by('id')[skip:(skip+limit)])
    return customers


@app.get("/customers/{customer_id}", response_model=schemas.CustomerDetails)
def get_customer_details(customer_id: int):
    customer = models.Customer.objects(id=customer_id).get()
    if customer:
        return customer
    else:
        raise HTTPException(status_code=404, detail="Customer not found")


@app.get("/customers/{customer_id}/rentals", response_model=List[schemas.Rental])
def list_customer_rentals(customer_id: int, skip: int = 0, limit: int = 100):
    customer = models.Customer.objects(id=customer_id).get()
    if customer:
        return customer.rentals[skip:(skip+limit)]
    else:
        raise HTTPException(status_code=404, detail="Customer not found")


@app.get("/available_films", response_model=List[schemas.FilmList])
def list_available_films(skip: int = 0, limit: int = 100):
    films = models.Film.objects.aggregate([
        {
            "$lookup": {
                "from": models.Customer._get_collection_name(),
                "localField": "_id",
                "foreignField": "rentals.film_id",
                "as": "relation",
            }
        },
        {
            "$match": {
                "relation": {"$size": 0},
            }
        },
        {
            "$skip": skip
        },
        {
            "$limit": limit
        },
        {
            "$project": {"relation": 0}
        },
    ])

    return [models.Film._from_son(film) for film in films]


@app.get("/films/{film_id}", response_model=schemas.FilmDetails)
def get_film_details(film_id: int):
    film = models.Film.objects(id=film_id).get()
    if film:
        return film
    else:
        raise HTTPException(status_code=404, detail="Customer not found")


@app.get("/films/{film_id}/renters", response_model=List[schemas.CustomerList])
def get_film_renters(film_id: int, skip: int = 0, limit: int = 100):
    film = models.Film.objects(id=film_id).get()
    if film:
        return list(models.Customer.objects(rentals__film_id=film.id).order_by('id')[skip:(skip+limit)])
    else:
        raise HTTPException(status_code=404, detail="Customer not found")
