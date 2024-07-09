import psycopg2

db_params = {
    'database': 'postgres',
    'user': 'postgres',
    'password': '2209',
    'host': 'localhost',
    'port': 5432
}

class DBConnect:
    def __init__(self, db_params):
        self.db_params = db_params

    def __enter__(self):
        self.conn = psycopg2.connect(**self.db_params)
        self.cur = self.conn.cursor()
        return self.conn, self.cur

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.conn:
            self.conn.close()

        if self.cur:
            self.cur.close()

class Book:
    def __init__(self, conn, cur):
        self.conn = conn
        self.cur = cur

    def create(self, title, author):
        insert_query = f"INSERT INTO book (title, author) VALUES ('{title}', '{author}')"
        self.cur.execute(insert_query)
        self.conn.commit()

    def read(self):
        select_query = "SELECT * FROM book"
        self.cur.execute(select_query)
        rows = self.cur.fetchall()
        for row in rows:
            print(row)

    def update(self, book_id, new_description):
        update_query = f"UPDATE book SET description = '{new_description}' WHERE id = {book_id}"
        self.cur.execute(update_query)
        self.conn.commit()

    def delete(self, book_id):
        delete_query = f"DELETE FROM book WHERE id = {book_id}"
        self.cur.execute(delete_query)
        self.conn.commit()

with DBConnect(db_params) as (conn, cur):
    book_manager = Book(conn, cur)
    book_manager.create('Python Programming', 'Guido van Rossum')
    book_manager.read()
    book_manager.update(1, 'Introduction to Python Programming')
    book_manager.read()
    book_manager.delete(1)
    book_manager.read()
print("Amallar muvaffaqiyatli bajargan!")
