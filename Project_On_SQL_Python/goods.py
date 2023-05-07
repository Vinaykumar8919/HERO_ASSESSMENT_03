import mysql.connector
mydb = mysql.connector.connect(host="localhost", user='root', password="Vinay@#23",database="Inventory_Management")
cur=mydb.cursor()

def create():
    c='''CREATE TABLE goods (
  goods_id INT NOT NULL,
  product VARCHAR(50) NOT NULL,
  manufactured_date DATE NOT NULL,
  PRIMARY KEY (goods_id)
)'''
    cur.execute(c)

def insert():
    ins="""INSERT INTO goods (goods_id,product, manufactured_date)
VALUES (100,'Toy', '2023-04-15'), (101,'Chair', '2023-05-01'), (102,'Table', '2023-04-20'), (103,'Shirt', '2023-03-28'),(104,'shoe', '2023-04-01')"""
    cur.execute(ins)
    mydb.commit()

def display():
  cur.execute("select * from goods")
  fetch = cur.fetchall()
  for i in fetch:
    print(i)


# main
# create()
insert()
display()