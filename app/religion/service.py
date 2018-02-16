from app.database.cache import get_from_cache, add_to_cache
from app.database.database import execute_query


def get_religiousness_by_state():
    query = get_query()
    data = get_from_cache(query)
    print("DB Query: " + query)

    if data is None:
        data = execute_query(query)
        add_to_cache(query, data)

    return data


def get_query():
    return f'''
        SELECT *
        FROM "Religions2010"
    '''
