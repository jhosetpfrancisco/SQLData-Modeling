import psycopg2

connection = psycopg2.connect('dbname=example')

cursor = connection.cursor()

cursor.execute('DROP TABLE IF EXISTS table2;')

cursor.execute('''
  CREATE TABLE table2 (
    id INTEGER PRIMARY KEY,
    completed BOOLEAN NOT NULL DEFAULT False
  );
''')

cursor.execute('INSERT INTO table2 (id, completed) VALUES (%s, %s);', (1, True))

SQL = 'INSERT INTO table2 (id, completed) VALUES (%(id)s, %(completed)s);'

data = {
  'id': 2,
  'completed': False
}
cursor.execute(SQL, data)

cursor.execute('SELECT * from table2;')
result_all = cursor.fetchall()
print(result_all)

cursor.execute('INSERT INTO table2 (id, completed) VALUES (%s,%s);', (3,True))

cursor.execute('SELECT * from table2;')
result = cursor.fetchone()
print('fetchone ' , result)

result2 = cursor.fetchmany(2)
print('fetchmany ' , result2)

result3 = cursor.fetchone()
print('fetchone ' , result3)

connection.commit()

connection.close()
cursor.close()