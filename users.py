import psycopg2
from typing import Optional

conn = psycopg2.connect(database='lesson',
                        user='postgres',
                        host='localhost',
                        password='703',
                        port=5432)

cursor = conn.cursor()

create_users_table = '''create table if not exists users(
    id serial primary key,
    name varchar(100) not null,
    email varchar(100) unique not null,
    age int check(age > 0),
    address text
);
'''

cursor.execute(create_users_table)
conn.commit()

class User:
    
    def __init__(self, name: str, email: str, age: Optional[int] = None, address: Optional[str] = None):
        self.name = name
        self.email = email
        self.age = age
        self.address = address
    
    @staticmethod
    def get_users():
        get_users_all = 'select * from users;'
        cursor.execute(get_users_all)
        for user in cursor.fetchall():
            print(user)
    
    @staticmethod
    def get_user(user_id: int):
        get_user_query = 'select * from users where id = %s;'
        cursor.execute(get_user_query, (user_id,))
        user = cursor.fetchone()
        print(user)
    
    def save(self):
        insert_user_query = '''
        insert into users(name, email, age, address)
        values (%s, %s, %s, %s)
        returning id;
        '''
        data = (self.name, self.email, self.age, self.address)
        cursor.execute(insert_user_query, data)
        user_id = cursor.fetchone()[0]
        conn.commit()
        return user_id
    
    @staticmethod
    def delete_user(user_id: int):
        delete_user_query = 'delete from users where id = %s;'
        cursor.execute(delete_user_query, (user_id,))
        conn.commit()
    
    def update_user(self, user_id: int):
        update_user_query = '''
        update users
        set name = %s, email = %s, age = %s, address = %s
        where id = %s;
        '''
        data = (self.name, self.email, self.age, self.address, user_id)
        cursor.execute(update_user_query, data)
        conn.commit()
