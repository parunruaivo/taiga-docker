import os, sys, psycopg2


connectionString = "dbname={{DB_NAME}} user={{DB_USER}} host={{DB_HOST}} password={{DB_PASS}} port={{DB_PORT}}"

print('Checking database connection.')
try:
    conn = psycopg2.connect(connectionString)
    cur = conn.cursor()
    cur.execute("select * from information_schema.tables where table_name=%s", ('django_migrations',))
    exists = bool(cur.rowcount)

    if exists is False:
        print('Database does not appear to be setup.')
        os._exit(2)
except:
    sys.exit(1)

