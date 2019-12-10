from application import db
from application.utils.data_import import import_from_json
from os import path


db.create_all()
print("Importing from json...")
import_from_json(path.join(path.dirname(path.abspath(__file__)), r"candidates.json"))

print("Done! Now serving!")

print("Database initialized.")
