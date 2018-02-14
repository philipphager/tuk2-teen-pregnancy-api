from app.database.cache import get_from_cache, add_to_cache
from app.database.database import execute_query


def get_teen_pregnancy_by_ethnicity(year):
    query = get_query(year)
    data = get_from_cache(query)
    print("DB Query: " + query)

    if data is None:
        data = execute_query(query)
        add_to_cache(query, data)

    return 'TODO'


def get_query(year):
    return f'''
        SELECT "State Code" AS "id", "Year" AS "year", "BirthRate" AS "birthRate"
         FROM BirthsPerYearAndState
         WHERE "Year" = '{year}'
    '''
