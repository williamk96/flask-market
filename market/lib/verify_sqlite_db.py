import sqlite3

def verify_sqlite_db(db_file):

    connection = sqlite3.connect(db_file)
    cursor = connection.cursor()
    cursor.execute("pragma schema_version;")