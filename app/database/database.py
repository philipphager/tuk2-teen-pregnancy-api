import pyhdb

from env.config import DB_URL, DB_PORT, DB_USER, DB_PASSWORD

DB_CONNECTION = None


def connect_db():
    return pyhdb.connect(
        host=DB_URL,
        port=DB_PORT,
        user=DB_USER,
        password=DB_PASSWORD
    )


def get_db():
    global DB_CONNECTION

    if DB_CONNECTION is None:
        DB_CONNECTION = connect_db()
    return DB_CONNECTION


def execute_query(query):
    db = get_db()
    cursor = db.cursor()
    cursor.execute(query)

    description = cursor.description
    columns = [column[0] for column in description]
    rows = cursor.fetchall()
    data = []

    for row in rows:
        o = {}
        for i, column in enumerate(columns):
            o[column] = row[i]
        data.append(o)

    return data


def execute_paginated_query(query, offset, limit):
    db = get_db()
    cursor = db.cursor()
    cursor.execute(query + f' LIMIT {limit} OFFSET {offset}')
    return cursor.fetchall()
