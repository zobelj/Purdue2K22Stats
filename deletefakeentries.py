from sqlalchemy import create_engine
from sqlalchemy.sql import text

with open('db_url.txt', 'r') as f:
    db_url = f.read()
    my_conn = create_engine(db_url)

with my_conn.connect() as con:
    file = open("sql_scripts/delete_fake_entries.sql")
    query = text(file.read())
    rows = con.execute(query)

print("Fake games deleted!")