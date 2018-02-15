from app.database.cache import get_from_cache, add_to_cache
from app.database.database import execute_query


def get_funding_by_state(year):
    query = get_query(year)
    data = get_from_cache(query)
    print("DB Query: " + query)

    if data is None:
        data = execute_query(query)
        add_to_cache(query, data)

    for d in data:
        d['abstinence rate'] = round(d['abstinence only'] / d['total'], 3) * 100
        d['comprehensive rate'] = round(d['comprehensive sex education'] / d['total'], 3) * 100

    return data


def get_query(year):
    return f'''
        SELECT *
        FROM FundingAndBirthRatesPerState
        WHERE "year" = {year}
        ORDER BY "fips";
    '''
