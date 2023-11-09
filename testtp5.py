
import sqlite3

# 1. Establish a connection to the SQLite database
conn = sqlite3.connect('customer_sales.db') 
# 2. Create a cursor object
cursor = conn.cursor()
import pandas as pd
Q_tbl_customers ="SELECT * FROM tbl_customers;"  # Define query for tbl_customers
Q_tbl_sales ="SELECT * FROM tbl_sales;"          # Define query for tbl_sales
Q_tbl_products ="SELECT * FROM tbl_products where Expire_Date   ;"    # Define query for tbl_prodcuts 

tbl_customers_DF =pd.read_sql_query(Q_tbl_customers, conn) # Get tbl_customers as Pandas DataFrame 
tbl_sales_DF =pd.read_sql_query(Q_tbl_sales, conn)  # Get tbl_sales as Pandas DataFrame 
tbl_products_DF =pd.read_sql_query(Q_tbl_products, conn) # Get tbl_products as Pandas DataFrame

tbl_customers_DF.info()