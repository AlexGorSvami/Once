import psycopg2

def create_table(con):
  cur.execute(''' 
      CREATE TABLE IF NOT EXISTS client(
          id SERIAL PRIMARY KEY,
          name VARCHAR (40) NOT NULL,
          surname VARCHAR (60) NOT NULL,
          email VARCHAR(60) NOT NULL
          );
      ''')
  con.commit()

  cur.execute('''
    CREATE TABLE IF NOT EXISTS phones(
      id SERIAL PRIMARY KEY,
      phone_number VARCHAR(20) UNIQUE,
      client_id INTEGER NOT NULL REFERENCES client(id)
      );
    ''')
  con.commit()

def add_client(con, name, surname, email, phone=None):
  cur.execute('''
  INSERT INTO client (name, surname, email) VALUES(%s, %s, %s);
  ''', (name, surname, email))

def add_phone_number(con, client_id, phone_number):
    cur.execute('''
    INSERT INTO phones(client_id, phone_number) VALUES(%s, %s);
    ''', (client_id, phone_number))

def change_client():
  print('''Чтобы изменть:
        имя - введите 1
        фамилмю - введите 2
        email - введите 3 
        телефон - введите 4''')
  while True:
    command = int(input())
    if command == 1:
      change_id = input('Введите id')
      change_name = input('Введите новое имя')
      cur.execute('''
      UPDATE client SET name=%s WHERE id=%s;
      ''', (change_name, change_id))
      break
    elif command == 2:
      change_id = input('Введите id')
      change_surname = input('Введите фамилию')
      cur.execute('''
      UPDATE client SET surname=%s WHERE id=%s;
      ''', (change_surname, change_id))
      break
    elif command == 3:
      change_id = input('Введите id')
      change_email = input('Введите новый email')
      cur.execute('''
      UPDATE client SET email=%s WHERE id=%s;
      ''', (change_email, change_id))
      break
    elif command == 4:
      change_phonenumber = input('Введите старый номер')
      new_phonenumber = input('Введите новый номер ')
      cur.execute('''
      UPDATE phones SET phone_number=%s WHERE phone_number=%s;
      ''', (new_phonenumber, change_phonenumber))
      break
    else:
      print('Неверная команда, введите правильную команду')


def del_phone_number():
  del_id = input('Введите id клиента')
  del_number = input('Введите номер телефона')
  cur.execute('''
  DELETE FROM phones WHERE id=%s AND phone_number=%s
  ''', (del_id, del_number))

def del_client():
  del_id = input('Введите id клиента')
  del_surname = input('Введите фамилию клиента')
  cur.execute('''
  DELETE FROM phones WHERE id=%s
  ''',(del_id,))
  cur.execute('''
  DELETE FROM client WHERE id=%s AND surname=%s
  ''', (del_id, del_surname))

def find_client(con, name=None, surname=None, email=None, phone_number=None):
  with con.cursor() as cur:
      if phone_number is not None:
        cur.execute('''SELECT name, surname, email, phone_number
                            FROM client c
                            JOIN phones AS p ON c.id = p.client_id
                            WHERE phone_number = %s;
            ''', (phone_number,))
      else:
        cur.execute('''SELECT name, surname, email, phone_number
                            FROM clients c
                            JOIN phones AS p ON c.id = p.client_id
                            WHERE name = %s or surname = %s or email = %s;
            ''', (name, surname, email))
      print(cur.fetchall())

if __name__ == '__main__':
  with psycopg2.connect(database="postgres", user="postgres", password="124012",host="127.0.0.1", port="5432") as con:
    with con.cursor() as cur:
      create_table(con)
      add_client(con, "Valera", "Rebrov", "valera@gmail.com")
      add_client(con, "Vova", "Vetrov", "vetrov1@yandex.ru")
      add_phone_number(con, 1, "89054321256")
      add_phone_number(con, 2, "89512345786")
      change_client()
      del_phone_number()
      del_client()
      find_client(con)

con.close()
