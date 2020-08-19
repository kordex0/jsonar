from datetime import datetime
from decimal import Decimal, ROUND_HALF_UP
from typing import Optional
import mongoengine
import dateutil
from mongoengine import (
    Document, EmbeddedDocument, EmbeddedDocumentField, FloatField, IntField,
    ListField, StringField)


class DateTimeField(mongoengine.DateTimeField):
    def to_python(self, value):
        if isinstance(value, datetime):
            return value
        else:
            try:
                return dateutil.parser.parse(value)
            except Exception:
                return None

    def to_mongo(self, value):
        value = super().to_mongo(value)
        if value:
            return value.isoformat(' ', timespec="milliseconds")
        else:
            return value


class BaseDocument(Document):
    id = IntField(db_field="_id")

    meta = {'abstract': True}


class Payment(EmbeddedDocument):
    _amount = FloatField(db_field="Amount")
    payment_date = DateTimeField(db_field="Payment Date")
    payment_id = IntField(db_field="Payment Id")

    @property
    def amount(self):
        if self._amount:
            return Decimal(self._amount).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
        else:
            return Decimal()

    @amount.setter
    def amount(self, value):
        if isinstance(value, float):
            self._amount = value
        else:
            self._amount = float(value)


class Rental(EmbeddedDocument):
    title = StringField(db_field="Film Title")
    rental_date = DateTimeField(db_field="Rental Date")
    return_date = DateTimeField(db_field="Return Date")
    film_id = IntField(db_field="filmId")
    rental_id = IntField(db_field="rentalId")
    staff_id = IntField(db_field="staffId")

    payments = ListField(EmbeddedDocumentField(Payment), db_field="Payments")

    @property
    def days_rented(self) -> Optional[int]:
        if self.rental_date and self.return_date:
            return (self.return_date - self.rental_date).days
        else:
            return None

    @property
    def cost(self) -> Decimal:
        return sum(payment.amount for payment in self.payments)


class Customer(BaseDocument):

    address = StringField(db_field="Address")
    city = StringField(db_field="City")
    country = StringField(db_field="Country")
    district = StringField(db_field="District")

    first_name = StringField(db_field="First Name")
    last_name = StringField(db_field="Last Name")

    phone = StringField(db_field="Phone")

    rentals = ListField(EmbeddedDocumentField(Rental), db_field="Rentals")

    meta = {'collection': 'customers'}


class Actor(EmbeddedDocument):
    first_name = StringField(db_field="First name")
    last_name = StringField(db_field="Last name")
    actor_id = IntField(db_field="actorId")


class Film(BaseDocument):

    actors = ListField(EmbeddedDocumentField(Actor), db_field="Actors")

    category = StringField(db_field="Category")
    description = StringField(db_field="Description")
    length = StringField(db_field="Length")
    rating = StringField(db_field="Rating")
    rental_duration = StringField(db_field="Rental Duration")
    _replacement_cost = StringField(db_field="Replacement Cost")
    _special_features = StringField(db_field="Special Features")
    title = StringField(db_field="Title")

    @property
    def replacement_cost(self):
        if self._replacement_cost:
            return Decimal(self._replacement_cost).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
        else:
            return Decimal()

    @replacement_cost.setter
    def replacement_cost(self, value):
        if isinstance(value, str):
            self._replacement_cost = value
        else:
            self._replacement_cost = str(value)

    @property
    def special_features(self):
        if self._special_features:
            return [special_feature.strip() for special_feature in self._special_features.split(',') if special_feature.strip()]
        else:
            return []

    @special_features.setter
    def special_features(self, value):
        if isinstance(value, list):
            self._special_features = ','.join(value)
        else:
            self._special_features = value

    meta = {'collection': 'films'}
