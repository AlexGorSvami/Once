host ='127.0.0.1'
user ='postgres'
password ='124012'
db_name ='netology_db'
port ='5432'

con = psycopg2.connect(
  database="netology_db",
  user="postgres",
  password="124012",
  host="127.0.0.1",
  port="5432"
)
print('OK')