# pylint: disable=(missing-module-docstring)

from io import StringIO

import duckdb
import pandas as pd

con = duckdb.connect(database="data/exercises_sql_tables.duckdb", read_only=False)

# -------------------------------------
# LISTES EXERCICES
# -------------------------------------
data = {
    "theme": ["CROSS JOIN", "WINDOW FUNCTION", "GROUP BY"],
    "exercises_name": [
        ["food_and_price"],
        ["electronic_sales"],
        ["orders_customers", "students_grades"],
    ],
    "tables": [
        [["food", "price"]],
        [["sales"]],
        [["orders", "customers"], ["students", "grades"]],
    ],
    "last_reviewed": [["1970-01-01"], ["1980-01-01"], ["1975-01-01", "1975-01-01"]],
}
memory_state = pd.DataFrame(data)
con.execute("CREATE TABLE IF NOT EXISTS memory_state as SELECT * FROM memory_state")

DATA_FOOD = """food_id,food_name
1,Pizza
2,Burger
3,Sushi
4,Pasta
5,Salad
"""
food = pd.read_csv(StringIO(DATA_FOOD))
con.execute("CREATE TABLE IF NOT EXISTS food as SELECT * FROM food")

# Données Price en format CSV
DATA_PRICE = """food_id,price
1,8.99
2,5.49
3,12.99
4,7.50
6,4.99
"""
price = pd.read_csv(StringIO(DATA_PRICE))
con.execute("CREATE TABLE IF NOT EXISTS price as SELECT * FROM price")

DATA_SALES = """
id,product,category,quantity,price,sales_date
1,Keyboard,Electronics,10,25.50,2024-10-01
2,Mouse,Electronics,20,15.00,2024-10-01
3,Laptop,Electronics,5,1200.00,2024-10-02
4,Chair,Furniture,12,85.00,2024-10-02
5,Desk,Furniture,7,300.00,2024-10-03
6,Headphones,Electronics,15,99.99,2024-10-03
7,Lamp,Furniture,18,45.00,2024-10-04
8,Monitor,Electronics,3,250.00,2024-10-05
9,Table,Furniture,9,400.00,2024-10-05
10,Smartphone,Electronics,25,699.99,2024-10-06
"""
sales = pd.read_csv(StringIO(DATA_SALES))
con.execute("CREATE TABLE IF NOT EXISTS sales as SELECT * FROM sales")


DATA_ORDERS = """
order_id,customer_id,order_date,total_amount
1,101,2024-01-10,250.50
2,102,2024-01-11,125.00
3,103,2024-01-12,300.75
4,101,2024-01-13,80.20
5,104,2024-01-14,200.00
6,102,2024-01-15,150.00
7,103,2024-01-16,400.00
8,101,2024-01-17,90.50
9,104,2024-01-18,120.00
10,102,2024-01-19,300.00
"""
orders = pd.read_csv(StringIO(DATA_ORDERS))
con.execute("CREATE TABLE IF NOT EXISTS orders as SELECT * FROM orders")

DATA_CUSTOMERS = """
customer_id,customer_name,country
101,John Doe,USA
102,Jane Smith,Canada
103,Michael Johnson,UK
104,Sarah Connor,France
"""
customers = pd.read_csv(StringIO(DATA_CUSTOMERS))
con.execute("CREATE TABLE IF NOT EXISTS customers as SELECT * FROM customers")


DATA_STUDENTS = """
student_id,student_name,class
1,John Doe,Maths
2,Jane Smith,Science
3,Michael Johnson,History
4,Sarah Connor,Maths
5,Lisa Brown,Science
"""
students = pd.read_csv(StringIO(DATA_STUDENTS))
con.execute("CREATE TABLE IF NOT EXISTS students as SELECT * FROM students")

DATA_GRADES = """
student_id,student_name,class
1,John Doe,Maths
2,Jane Smith,Science
3,Michael Johnson,History
4,Sarah Connor,Maths
5,Lisa Brown,Science
"""
grades = pd.read_csv(StringIO(DATA_GRADES))
con.execute("CREATE TABLE IF NOT EXISTS grades as SELECT * FROM grades")

con.close()
