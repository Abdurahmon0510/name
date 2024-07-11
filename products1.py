import requests
import psycopg2

url = "https://dummyjson.com/products"
response = requests.get(url)
data = response.json()
products1 = data['products']


conn = psycopg2.connect(
    dbname="postgres", user="postgres", password="2209", host="localhost", port="5432"
)

cur = conn.cursor()
cur.execute('''
    CREATE TABLE IF NOT EXISTS products1 (
        id SERIAL PRIMARY KEY,
        title   varchar(1000),
        description varchar(1000),
        price NUMERIC(10,2),
        discountPercentage NUMERIC(10,2),
        rating NUMERIC(10,2),
        stock INT,
        category VARCHAR(1000),
        thumbnail VARCHAR(1000),
        images TEXT[],
        weight VARCHAR(1000)
    )
''')

for product in products1:
    cur.execute('''
        INSERT INTO products1 (title, description, price, discountPercentage, rating, stock, category, thumbnail, images, weight)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    ''', (
        product['title'], product['description'], product['price'], product['discountPercentage'],
        product['rating'], product['stock'], product['category'], product['thumbnail'],
        product['images'], product.get('weight', '')
    ))

conn.commit()
conn.close()

print("Ma'lumotlar muvaffaqiyatli saqlandi!")
