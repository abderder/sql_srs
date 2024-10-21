# pylint: disable=(missing-module-docstring)

from io import StringIO

import duckdb
import pandas as pd

con = duckdb.connect(database="data/exercises_sql_tables.duckdb", read_only=False)

# -------------------------------------
# LISTES EXERCICES
# -------------------------------------
data = {
    "theme": ["CROSS JOIN", "WINDOW FUNCTION"],
    "exercises_name":["food_and_price","electronic_sales"],
    "tables":[["food","price"],"sales"],
    "last_reviewed":["1970-01-01","1970-01-01"]
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
