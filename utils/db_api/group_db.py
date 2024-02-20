import psycopg2

# PostgreSQL ma'lumotlar ombori bilan bog'lanish
conn = psycopg2.connect(
    dbname="users",
    user="postgres",
    password="0102",
    host="localhost",
    port="5432"
)

# Ma'lumotlar omborini ishlatish uchun kursor yaratish
cursor = conn.cursor()

# Guruhlar jadvalini yaratish (agar mavjud emas bo'lsa)
cursor.execute('''
    CREATE TABLE IF NOT EXISTS groups (
        id SERIAL PRIMARY KEY,
        group_id INTEGER,
        group_name TEXT,
        member_count INTEGER
    )
''')

# Yangi guruhni qo'shish
def add_group(group_id, group_name, member_count):
    cursor.execute('''
        INSERT INTO groups (group_id, group_name, member_count)
        VALUES (%s, %s, %s)
    ''', (group_id, group_name, member_count))
    conn.commit()

# Guruhlar ro'yxatini olish
def get_all_groups():
    cursor.execute('SELECT * FROM groups')
    return cursor.fetchall()

# Ma'lumotlar omborini yopish
def close_db():
    cursor.close()
    conn.close()

# Test qilish
if __name__ == '__main__':
    # Guruh qo'shish
    add_group(123456789, 'Test Group', 100)

    # Guruhlar ro'yxatini olish
    groups = get_all_groups()
    print("Guruhlar ro'yxati:", groups)

    # Ma'lumotlar omborini yopish
    close_db()
