import psycopg2

# PostgreSQL ma'lumotlar ombori bilan ulanish
conn = psycopg2.connect(
    dbname="users",
    user="postgres",
    password="0102",
    host="localhost",
    port="5432"
)

# Ma'lumotlar omborini ishlatish uchun kursor yaratish
cursor = conn.cursor()

# Foydalanuvchilar jadvalini yaratish (agar mavjud emas bo'lsa)
cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id SERIAL PRIMARY KEY,
        user_id INTEGER,
        username TEXT,
        first_name TEXT,
        last_name TEXT
    )
''')

# Yangi foydalanuvchini qo'shish
def add_user(user_id, username, first_name, last_name):
    cursor.execute('''
        INSERT INTO users (user_id, username, first_name, last_name)
        VALUES (%s, %s, %s, %s)
    ''', (user_id, username, first_name, last_name))
    conn.commit()

# Foydalanuvchi ma'lumotlarini o'qish
def get_user(user_id):
    cursor.execute('SELECT * FROM users WHERE user_id = %s', (user_id,))
    return cursor.fetchone()

def all_users_count():
    cursor.execute('SELECT COUNT(*) FROM users')
    return cursor.fetchone()[0]
def all_users_list():
    cursor.execute('SELECT user_id FROM users')
    print(cursor.fetchall())
    # return cursor.fetchone()

# Ma'lumotlar omborini yopish
def close_db():
    cursor.close()
    conn.close()

# Test qilish
if __name__ == '__main__':
    # Foydalanuvchi qo'shish
    add_user(123456789, 'testuser', 'Test', 'User')

    # Foydalanuvchi ma'lumotlarini o'qish
    user = get_user(123456789)
    print("Foydalanuvchi ma'lumotlari:", user)

    # Ma'lumotlar omborini yopish
    close_db()
