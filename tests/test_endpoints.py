
def test_list_customers(app):

    response = app.get('/customers', params={"skip": 0, "limit": 10})

    assert response.status_code == 200

    customers = response.json()

    assert len(customers) == 10
    assert customers[0] == {
        "id": 1,
        "first_name": "MARY",
        "last_name": "SMITH",
    }


def test_get_customer(app):

    response = app.get('/customers/1')

    assert response.status_code == 200

    customer = response.json()

    assert customer == {
        "id": 1,
        "first_name": "MARY",
        "last_name": "SMITH",
        "address": "1913 Hanoi Way",
        "city": "Sasebo",
        "country": "Japan",
        "district": "Nagasaki",
        "phone": "28303384290",
    }


def test_get_customer_rentals(app):

    response = app.get('/customers/1/rentals', params={"skip": 0, "limit": 10})

    assert response.status_code == 200

    rentals = response.json()

    assert len(rentals) == 10
    assert rentals[0] == {
        "rental_date": "2005-06-15T00:54:12",
        "days_rented": 8,
        "cost": 5.99,
    }


def test_list_available_films(app):

    response = app.get('/available_films', params={"skip": 0, "limit": 10})

    assert response.status_code == 200

    available_films = response.json()

    assert len(available_films) == 10
    assert available_films[0] == {
        "id": 2,
        "title": "ACE GOLDFINGER",
        "category": "Horror",
        "description": "A Astounding Epistle of a Database Administrator And a Explorer who must Find a Car in Ancient China",
        "rating": "G",
        "rental_duration": "3",
    }


def test_get_film_details(app):

    response = app.get('/films/1')

    assert response.status_code == 200

    film = response.json()

    actors = film.pop("actors")

    assert film == {
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
            "Behind the Scenes",
        ],
    }

    assert len(actors) == 10
    assert actors[0] == {
        "first_name": "PENELOPE",
        "last_name": "GUINESS",
        "actor_id": 1,
    }


def test_get_film_renters(app):

    response = app.get('/films/1/renters', params={"skip": 0, "limit": 10})

    assert response.status_code == 200

    renters = response.json()

    assert len(renters) == 10
    assert renters[0] == {
        "id": 8,
        "first_name": "SUSAN",
        "last_name": "WILSON",
    }
