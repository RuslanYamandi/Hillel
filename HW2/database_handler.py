import sqlite3


def execute_query(query: str, args=()):
    with sqlite3.connect('chinook.db') as conn:
        cursor = conn.cursor()
        cursor.execute(query, args)
        conn.commit()
        result = cursor.fetchall()
    return result


def format_query_records(records: list):
    return '<br>'.join(str(record) for record in records)