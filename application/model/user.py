from application import db


class User(db.Model):
    __table_name__ = "user"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    username = db.Column(db.VARCHAR(200), index=True, nullable=False)
    password = db.Column(db.VARCHAR(200), index=True, nullable=False)

    def __init__(self, username: str, password: str):
        self.username = username
        self.password = password

    def __repr__(self):
        return "<User #{}: {} @ {}>".format(
            self.id,
            self.username,
            self.password
        )
