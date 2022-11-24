import psycopg2
# from config import host, user, password, db_name
#
# try:
# connection = psycopg2.connect(
#     host=host,
#     user=user,
#     password=password,
#     datebase=db_name
# )
# except Exception as _ex:
#     print('[INFO] Error while working with Postgresql', _ex)
# finally:
#     if connection:
#         connection.close()
#         print('[INFO] PostgreSQL connection closed')


import psycopg2

con = psycopg2.connect(
  database="netology_db",
  user="postgres",
  password="124012",
  host="127.0.0.1",
  port="5432"
)

print("Database opened successfully")
# cur = con.cursor()
# cur.execute('''CREATE TABLE STUDENT
#      (ADMISSION INT PRIMARY KEY NOT NULL,
#      NAME TEXT NOT NULL,
#      AGE INT NOT NULL,
#      COURSE CHAR(50),
#      DEPARTMENT CHAR(50));''')
#
# print('Table created successfully')
# con.commit()
# con.close()

with con.cursor() as cur:
    # cur.execute('''
    # DROP TABLE homework;
    # DROP TABLE course;
    # ''')

    # СОЗДАНИЕ ТАБЛИЦ
    cur.execute('''
        CREATE TABLE IF NOT EXISTS course(
            id SERIAL PRIMARY KEY,
            name VARCHAR(40) UNIQUE
        );
        ''')
    cur.execute('''
        CREATE TABLE IF NOT EXISTS homework(
            id serial PRIMARY KEY,
            number INTEGER NOT NULL,
            description TEXT NOT NULL,
            course_id INTEGER NOT NULL REFERENCES course(id)
        );
        ''')
    con.commit()

    # cur.execute('''
    #     INSERT INTO course(name) VALUES ('Python');
    #     ''')
    # con.commit()

    # cur.execute('''
    #     INSERT INTO course(name) VALUES('Java') RETURNING id, name;
    #     ''')
    # print(cur.fetchone())
    # cur.execute('''
    #     INSERT INTO homework(number, description, course_id) VALUES(1, 'простое дз', 1);
    #     ''')
    # con.commit()

    cur.execute('''
        SELECT * FROM course;
        ''')
    print('fetchall', cur.fetchall())

    cur.execute(''' 
            SELECT * FROM course;
            ''')
    print(cur.fetchone())

    cur.execute(''' 
        SELECT * FROM course;
        ''')
    print(cur.fetchmany(3))
con.close()