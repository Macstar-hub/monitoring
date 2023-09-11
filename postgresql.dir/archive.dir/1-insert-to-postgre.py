import psycopg2

conn = psycopg2.connect(
    host="localhost",
    port=5432,
    database="statuscode"
)

cursor = conn.cursor()

insert_statement = "INSERT INTO statuscount (url, statuscode, epochtime) VALUES (%s, %s, %s)"

values = ("urla", 200, 10)

cursor.execute(insert_statement, values)

conn.commit()

cursor.close()

conn.close()
