from application import db
from sqlalchemy import exc
from application.model import User


def query_user_exist(username):
    result = db.session.query(User).filter_by(username=username).all()
    if len(result) == 0:
        return False
    return True


def register_user(username, password):
    if not query_user_exist(username=username):
        user = User(username=username, password=password)
        try:
            db.session.add(user)
            db.session.commit()
        except exc.SQLAlchemyError:
            return False
    return True


def login(username, password):
    result = db.session.query(User).filter_by(username=username, password=password).all()
    print(result)
    if len(result) == 0:
        return False
    return True
