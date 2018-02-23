# Define sensitive configurations that are not pushed to VCS.
DB_URL = ""
DB_PORT = ""
DB_USER = ""
DB_PASSWORD = ""

if not all((DB_URL, DB_PORT, DB_USER, DB_PASSWORD)):
    print("Please add db connection params to env/config.py")
    exit(1)
