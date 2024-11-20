# import psycopg2
#
# class DataBase:
#     def __init__(self):
#         self.database = psycopg2.connect(
#             database='shop',
#             user='postgres',
#             host='localhost',
#             password='1'
#         )
#
#     def manager(self, sql, *args, commit=False, fetchone=False, fetchall=False):
#         with self.database as db:
#             with db.cursor() as cursor:
#                 cursor.execute(sql, args)
#                 if commit:
#                     result = db.commit()
#                 elif fetchone:
#                     result = cursor.fetchone()
#                 elif fetchall:
#                     result = cursor.fetchall()
#             return result
#
#     def create_table_categories(self):
#         sql = '''CREATE TABLE IF NOT EXISTS categories(
#                     category_id INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
#                     category_name VARCHAR(50) NOT NULL UNIQUE
#                 );'''
#
#         self.manager(sql, commit=True)
#
#     def create_table_products(self):
#         sql = '''CREATE TABLE IF NOT EXISTS products(
#             product_id INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
#             product_name VARCHAR(150) NOT NULL UNIQUE,
#             product_price NUMERIC(7, 2) NOT NULL CHECK(product_price >= 0 AND product_price <= 99999.99),
#             category_id INTEGER REFERENCES categories(category_id)
#         );'''
#         self.manager(sql, commit=True)
#
#     def insert_category(self, category_name):
#         sql = '''INSERT INTO categories(category_name) values (%s) ON CONFLICT DO NOTHING'''
#         self.manager(sql, category_name, commit=True)
#
#     def insert_product(self, product_name, product_price, category_id):
#         sql = '''INSERT INTO products(product_name, product_price, category_id) values
#         (%s, %s, %s) ON CONFLICT DO NOTHING'''
#         self.manager(sql, product_name, product_price, category_id, commit=True)
#
#     def select_products(self):
#         sql = '''select * from products;'''
#         return self.manager(sql, fetchall=True)
#
#
# db = DataBase()
# db.create_table_categories()
# db.create_table_products()
# db.insert_category('Olmalar')
# db.insert_product('Burger mini', 15000, 1)
# print(db.select_products())


# Vazifa____________________________________________________________________

# class DataBase:
#     def __init__(self):
#         self.database = psycopg2.connect(
#             database='Universty',
#             user='postgres',
#             host='localhost',
#             password='1'
#         )
#
#     def manager(self, sql, *args, commit=False, fetchone=False, fetchall=False):
#         with self.database as db:
#             with db.cursor() as cursor:
#                 cursor.execute(sql, args)
#                 if commit:
#                     result = db.commit()
#                 elif fetchone:
#                     result = cursor.fetchone()
#                 elif fetchall:
#                     result = cursor.fetchall()
#
#             return result
#
#     def create_table_students(self):
#         sql = '''
#             create table if not exists students(
#             student_id INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
#             age INTEGER NOT NULL CHECK(age > 0),
#             email VARCHAR(50) UNIQUE NOT NULL
#             );
#         '''
#         self.manager(sql, commit=True)
#
#     def insert_students(self, age, email):
#         sql = '''insert into students(age, email) values
#         (%s, %s) ON CONFLICT DO NOTHING
#         '''
#
#         self.manager(sql, age, email, commit=True)
#
#     def alter_table_students(self):
#         sql = '''alter table students rename to talabalar;'''
#
#         self.manager(sql, commit=True)
#
#     def alter_column_students(self):
#         sql = '''alter table talabalar rename column age to yosh'''
#
#         self.manager(sql, commit=True)
#
#     def update_students(self, yosh, id):
#         sql = '''update talabalar set yosh = (%s) where student_id = (%s);'''
#
#         self.manager(sql, yosh, id,commit=True)
#
#     def delete_students(self, id):
#         sql = '''delete from talabalar where student_id = (%s);'''
#
#         self.manager(sql, id, commit=True)
#
#     def create_table_courses(self):
#         sql = '''
#             create table if not exists courses(
#             course_id INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
#             course_code INTEGER UNIQUE NOT NULL,
#             credits INTEGER CHECK(credits != 1)
#             )
#         '''
#         self.manager(sql, commit=True)
#
#     def insert_courses(self, course_code, credits):
#         sql = '''insert into courses(course_code, credits) values
#         (%s, %s) ON CONFLICT DO NOTHING'''
#
#         self.manager(sql, course_code, credits, commit=True)
#
#
#     def create_table_enrollments(self):
#         sql = '''
#             create table if not exists enrollments(
#             enrollment_id INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
#             student_id INTEGER REFERENCES students(student_id) ON DELETE CASCADE,
#             course_id INTEGER REFERENCES courses(course_id) ON DELETE SET NULL
#             )
#         '''
#         self.manager(sql, commit=True)
#
#     def create_table_teachers(self):
#         sql = '''
#             create table if not exists teachers(
#             teacher_id INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
#             experience_years INTEGER CHECK(experience_years >= 0)
#             )
#         '''
#         self.manager(sql, commit=True)
#
#     def insert_teacher(self, experience_years):
#         sql = '''insert into teachers(experience_years) values
#         (%s) ON CONFLICT DO NOTHING
#         '''
#
#         self.manager(sql, experience_years, commit=True)
#
#     def create_table_course_assignments(self):
#         sql = '''
#             create table if not exists course_assignments(
#             assignment_id INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
#             teacher_id INTEGER REFERENCES teachers(teacher_id) ON DELETE SET DEFAULT,
#             course_id INTEGER REFERENCES courses(course_id) ON DELETE SET NULL
#             )
#         '''
#         self.manager(sql, commit=True)
#
#
# db = DataBase()
# db.create_table_students()
# db.create_table_courses()
# db.create_table_enrollments()
# db.create_table_teachers()
# db.create_table_course_assignments()
# db.insert_students(20, 'ali@gmail.com')
# db.insert_students(19, 'toxir@gmail.com')
# db.insert_students(21, 'sanobar@gmail.com')
# db.insert_students(22, 'sardor@gmail.com')
# db.insert_students(23, 'vali@gmail.com')
# db.insert_students(24, 'botir@gmail.com')
# db.insert_students(25, 'sobir@gmail.com')
# db.insert_courses(1, 10)
# db.insert_courses(2, 11)
# db.insert_courses(3, 12)
# db.insert_teacher(5)
# db.insert_teacher(6)
# # db.alter_table_students()
# # db.alter_column_students()
# db.update_students(33, 1)
# db.update_students(88, 3)
# db.delete_students(1)
