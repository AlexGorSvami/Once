import psycopg2
from config import *

con = psycopg2.connect(
  database="netology_db",
  user="postgres",
  password="124012",
  host="127.0.0.1",
  port="5432"
)
print(' connect OK')

with con.cursor() as cur:
  def create_table():
    cur.execute(''' 
        CREATE TABLE IF NOT EXISTS client(
            id SERIAL PRIMARY KEY,
            name VARCHAR (40) NOT NULL,
            surname VARCHAR (60) NOT NULL,
            email VARCHAR(60) NOT NULL
            );
        ''')
      print('Table client create')
      con.commit()

    cur.execute('''
      CREATE TABLE IF NOT EXISTS phones(
        id SERIAL PRIMARY KEY,
        phone_number VARCHAR(20) UNIQUE,
        clent_id INTEGER NOT NULL REFERENCES client(id)
        );
      ''')
      print('Create phones table')
    con.commit()

def add_client(cur, name, surname, email):
    cur.execute('''
    INSERT INTO client(name, surname, email) VALUES(%s, %s, %s);
    ''', (name, surname, email))

def add_phonenumber(cur, client_id, phonenumber):
    cur.execute('''
    INSERT INTO phones(client_id, phones) VALUES(%s, %s);
    ''', (client_id, phonenumber))
