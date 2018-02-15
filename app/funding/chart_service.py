from app.database.cache import get_from_cache, add_to_cache
from app.database.database import execute_query


def get_funding_aggregated_by_state(start_year, end_year, states):
    query = get_query(start_year, end_year, states)
    data = get_from_cache(query)
    print("DB Query: " + query)

    if data is None:
        data = execute_query(query)
        add_to_cache(query, data)

    return collect_by_state(data)


def collect_by_state(data):
    states = {}

    for year in data:
        fips = year['fips']

        if fips not in states:
            states[fips] = {}

        for key, value in year.items():
            if key == 'fips':
                continue

            if key in states[fips]:
                states[fips][key].append(value)
            else:
                states[fips][key] = []

    return states


def get_query(start_year, end_year, states):
    fips = ''

    for i, state in enumerate(states):
        fips += f'\'{state}\''
        if i < (len(states) - 1):
            fips += ','

    return f'''
        SELECT *
        FROM FundingAndBirthRatesPerState
        WHERE "year" >= {start_year}
        AND "year" <= {end_year}
        AND "fips" IN ({fips})
        ORDER BY "fips", "year";
    '''
