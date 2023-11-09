

import mysql.connector
from sqlalchemy import create_engine
import pandas as pd

# إعداد اتصال MySQL
db_connection = mysql.connector.connect(
    host="localhost",  # استبدل بعنوان الخادم الخاص بك
    user="root",    # استبدل بمعرف المستخدم الخاص بك
    password="",  # استبدل بكلمة المرور الخاصة بك
    database="ecommerce_db"  # استبدل باسم قاعدة البيانات الخاصة بك
)

# إنشاء محرك SQLAlchemy
engine = create_engine("mysql+mysqlconnector://root:@localhost/ecommerce_db")

# استعلام قاعدة البيانات واستخراج البيانات إلى DataFrame
query = """
    SELECT * FROM users
"""
df = pd.read_sql(query, engine)

# إغلاق اتصال MySQL
db_connection.close()

customers_df = pd.DataFrame(df)

customers_df['ValidEmail'] = customers_df['email'].str.contains(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$')
customers_df['Validpassword'] = customers_df['email'].str.contains(r'^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[@#$%^&+=!])(?!.*\s).{8,}$')
customers_df.to_csv('users_analysis.csv', index=False)

