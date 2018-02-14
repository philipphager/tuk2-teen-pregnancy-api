import os

from app import create_app
from app.database.database import get_db

config_name = os.getenv('CONFIG')
app = create_app(config_name)

if __name__ == '__main__':
    if config_name == 'DEVELOPMENT':
        host = '127.0.0.1'
        port = 5000
    else:
        host = '0.0.0.0'
        port = 80

    app.run(host=host, port=port)
    # Connect to database at least one to avoid cold start
    get_db()
