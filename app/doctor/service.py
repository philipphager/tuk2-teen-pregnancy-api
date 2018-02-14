from app.database.cache import get_from_cache, add_to_cache
from app.database.database import execute_query


def get_doctor_visit_count(start_year, end_year, is_male, is_female):
    query = get_query(start_year, end_year, is_male, is_female)
    doctor_visit_count = get_from_cache(query)
    print("DB Query: " + query)

    if doctor_visit_count is None:
        doctor_visit_count = execute_query(query)
        add_to_cache(query, doctor_visit_count)

    return doctor_visit_count


def get_doctor_visit_count_relative_to_state(start_year, end_year, is_male, is_female):
    query = get_relative_query(start_year, end_year, is_male, is_female)
    doctor_visit_count = get_from_cache(query)
    print("DB Query: " + query)

    if doctor_visit_count is None:
        doctor_visit_count = execute_query(query)
        add_to_cache(query, doctor_visit_count)

    return doctor_visit_count


def get_query(start_year, end_year, is_male, is_female):
    genders = '\' \''

    if is_male:
        genders += ',\'M\''

    if is_female:
        genders += ',\'F\''

    return f'''
        SELECT "State"."Name", Count(*)
        FROM "State" 
        LEFT JOIN Patient ON "State"."State" = Patient."State"
        JOIN Transcript ON Patient."PatientGuid" = Transcript."PatientGuid"
        WHERE Patient."Gender" IN ({genders})
        AND Transcript."VisitYear" >= {start_year}
        AND Transcript."VisitYear" <= {end_year}
        GROUP BY Patient."State", "State"."Name";
    '''


def get_relative_query(start_year, end_year, is_male, is_female):
    genders = '\' \''

    if is_male:
        genders += ',\'M\''

    if is_female:
        genders += ',\'F\''

    return f'''
        SELECT "State"."Name", (Count(*) / "State"."Population") * 1000
        FROM "State" 
        LEFT JOIN Patient ON "State"."State" = Patient."State"
        JOIN Transcript ON Patient."PatientGuid" = Transcript."PatientGuid"
        WHERE Patient."Gender" IN ({genders})
        AND Transcript."VisitYear" >= {start_year}
        AND Transcript."VisitYear" <= {end_year}
        GROUP BY Patient."State", "State"."Name", "State"."Population";
    '''
