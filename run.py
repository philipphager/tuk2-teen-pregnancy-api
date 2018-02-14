import os

from app import create_app
from app.database.database import get_db

config_name = os.getenv('CONFIG')
app = create_app(config_name)

if __name__ == '__main__':
    app.run()
    # Connect to database at least one to avoid cold start
    get_db()
