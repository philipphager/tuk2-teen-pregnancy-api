from app.database.cache import get_from_cache, add_to_cache
from app.database.database import execute_query


def get_teen_pregnancy_world_wide(start_year, end_year, countries):
    query = get_query(start_year, end_year, countries)
    data = get_from_cache(query)
    print("DB Query: " + query)

    if data is None:
        data = execute_query(query)
        add_to_cache(query, data)

    return data


def get_query(start_year, end_year, countries):
    return f'''
        SELECT * 
        FROM TeenRatesWorldwide
        WHERE "Year" >= TO_DATE('{start_year}', 'YYYY')
        AND "Year" <= TO_DATE('{end_year}', 'YYYY')
    '''
