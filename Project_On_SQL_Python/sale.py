import mysql.connector
mydb = mysql.connector.connect(host="localhost", user='root', password="Vinay@#23",database="Inventory_Management")
cur=mydb.cursor()

def create():
    c='''CREATE TABLE sale (
  sale_id INT NOT NULL AUTO_INCREMENT,
  product VARCHAR(50) NOT NULL,
  sold_by VARCHAR(50) NOT NULL,
  sale_amount int NOT NULL,
  sale_date DATE NOT NULL,
  profit_margin DECIMAL(5, 2) NOT NULL,
  PRIMARY KEY (sale_id)
)'''
    cur.execute(c)

def insert():
    ins = '''INSERT INTO sale (product, sold_by, sale_amount, sale_date, profit_margin)
VALUES ('Toy', 'MyKids', 2000, '2023-04-20', 0.25), ('Chair', 'MyFurnish', 500, '2023-05-05', 0.20), ('Table', 'MyCare', 1800, '2023-04-30', 0.30), ('Shirt', 'FashionHub', 1200, '2023-04-02', 0.50)'''
    cur.execute(ins)
    mydb.commit()


def display():
  cur.execute("select * from sale")
  fetch = cur.fetchall()
  for i in fetch:
    print(i)

# main
create()
insert()
display()