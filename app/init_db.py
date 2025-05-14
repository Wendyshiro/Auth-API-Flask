from app import create_app
from app.models import db

app = create_app()
with app.app_context():
    db.create_all()
    print("Databases tables created.")

import os 
print("Database path:", os.path.abspath("site.db"))