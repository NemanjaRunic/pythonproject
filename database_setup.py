import sqlite3
conn=sqlite3.connect('database2.db')
crsr=conn.cursor()

tab1="""CREATE TABLE trainers (
trainer_id INTEGER PRIMARY KEY,
first_name VARCHAR (30),
second_name VARCHAR (30),
gender CHAR(1),
age INTEGER,
seniority VARCHAR (10));"""

tab2="""CREATE TABLE customers (
customer_id INTEGER PRIMARY KEY,
first_name VARCHAR (30),
second_name VARCHAR (30),
gender CHAR(1),
age INTEGER,
fitness_level VARCHAR(3));"""

tab3="""CREATE TABLE equipment (
eq_id INTEGER PRIMARY KEY,
eq_name VARCHAR (30),
manufacturer VARCHAR (30),
type VARCHAR (20),
weight VARCHAR (15),
color VARCHAR (15));"""

tab4="""CREATE TABLE food_supplement (
sup_id INTEGER PRIMARY KEY,
sup_name VARCHAR (30),
manufacturer VARCHAR (30),
type VARCHAR (20),
weight VARCHAR (15),
cal INTEGER);"""


crsr.execute(tab1)
crsr.execute(tab2)
crsr.execute(tab3)
crsr.execute(tab4)

conn.close()