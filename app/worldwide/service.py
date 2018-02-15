from app.database.cache import get_from_cache, add_to_cache
from app.database.database import execute_query


def get_teen_pregnancy_world_wide(start_year, end_year, countries):
    query = get_query(start_year, end_year, countries)
    data = get_from_cache(query)
    print("DB Query: " + query)

    if data is None:
        data = execute_query(query)
        add_to_cache(query, data)

    return collect_by_country(data)


def collect_by_country(data):
    countries = {}

    for year in data:
        for key, value in year.items():
            if key in countries:
                countries[key].append(value)
            else:
                countries[key] = []

    return countries


def get_query(start_year, end_year, countries):
    county_selector = ''

    for country in countries:
        county_selector += f'\"{country}\",'

    return f'''
        SELECT
        {county_selector} 
        "Year" as "year"
        FROM "TeenPregnanciesWorldwide"
        WHERE "Year" >= {start_year}
        AND "Year" <= {end_year}
    '''
