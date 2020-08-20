from datetime import datetime
from decimal import Decimal
from typing import List

from pydantic import BaseModel


class CustomerBase(BaseModel):
    id: int
    first_name: str
    last_name: str


class CustomerList(CustomerBase):

    class Config:
        orm_mode = True


class CustomerDetails(CustomerBase):
    address: str = None
    city: str = None
    country: str = None
    district: str = None
    phone: str = None

    class Config:
        orm_mode = True


class Rental(BaseModel):

    film_id: int
    rental_date: datetime
    days_rented: int
    cost: Decimal

    class Config:
        orm_mode = True


class Actor(BaseModel):
    first_name: str
    last_name: str
    actor_id: int

    class Config:
        orm_mode = True


class FilmBase(BaseModel):
    id: int
    title: str
    category: str
    description: str
    rating: str
    rental_duration: str


class FilmList(FilmBase):

    class Config:
        orm_mode = True


class FilmDetails(FilmBase):

    length: str
    replacement_cost: Decimal
    special_features: List[str]

    actors: List[Actor]

    class Config:
        orm_mode = True
