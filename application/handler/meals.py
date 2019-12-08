from application import db
from application.model import Meals
from sqlalchemy import exc
import random


def query_all():
    result = db.session.query(Meals).all()
    categories = set([item.category for item in result])
    result_dict = dict()
    for category in categories:
        values = set(map(lambda x: x.name, list(filter(lambda x: x.category == category, result))))
        result_dict[category] = values
    return result_dict


def query_category():
    result = db.session.query(Meals).all()
    categories = set([(item.category, item.category) for item in result])
    return categories


def query_recommend(category):
    result = db.session.query(Meals).filter_by(category=category).all()
    meals = [item.name for item in result]
    random.shuffle(meals)
    return meals[0]


def delete_item(category, name):
    try:
        db.session.query(Meals).filter_by(category=category, name=name).delete()
        db.session.commit()
    except exc.SQLAlchemyError:
        return False
    return True


def query_item(category, name):
    return db.session.query(Meals).filter_by(category=category, name=name)


def update_item(category, name, category_new, name_new):
    try:
        db.session.query(Meals).filter_by(category=category, name=name).update(
            {"category": category_new, "name": name_new})
        db.session.commit()
    except exc.SQLAlchemyError:
        return False
    return True


def add_item(category, name):
    meal = Meals(category=category, name=name)
    try:
        db.session.add(meal)
        db.session.commit()
    except exc.SQLAlchemyError:
        return False
    return True
