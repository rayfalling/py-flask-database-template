from application import db


class Meals(db.Model):
    __table_name__ = "meals"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    name = db.Column(db.VARCHAR(200), index=True, nullable=False)
    category = db.Column(db.VARCHAR(200), index=True, nullable=False)

    def __init__(self, name: str, category: str):
        self.name = name
        self.category = category

    def __repr__(self):
        return "<model #{}: {} @ {}>".format(
            self.id,
            self.name,
            self.category
        )
