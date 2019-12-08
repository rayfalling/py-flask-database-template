import json

from application import db
from application.model import Meals


def import_from_json(json_file: str):
    with open(json_file, "r", encoding="utf-8") as f:
        sql_list = json.load(f)

    for item in sql_list:
        single = Meals(name=item["name"], category=item["category"])
        # single.id = item["id"]
        db.session.merge(single)

    db.session.commit()
