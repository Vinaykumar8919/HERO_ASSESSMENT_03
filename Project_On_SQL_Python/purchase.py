import mysql.connector
mydb = mysql.connector.connect(host="localhost", user='root', password="Vinay@#23",database="Inventory_Management")
cur=mydb.cursor()

def create():
    c='''CREATE TABLE purchase (
  purchase_id INT NOT NULL AUTO_INCREMENT,
  product VARCHAR(50) NOT NULL,
  purchased_by VARCHAR(50) NOT NULL,
  purchase_amount int NOT NULL,
  purchase_date DATE NOT NULL,
  PRIMARY KEY (purchase_id)
)'''
    cur.execute(c)

def insert():
    ins = '''INSERT INTO purchase (product, purchased_by, purchase_amount, purchase_date)
VALUES ('Toy', 'MyKids', 1500, '2023-04-18'), ('Chair', 'ORay', 300, '2023-05-03'), ('Table', 'MyCare', 1200, '2023-04-25'), ('Shirt', 'FashionHub', 800, '2023-03-30')'''
    cur.execute(ins)
    mydb.commit()


def display():
  cur.execute("select * from purchase")
  fetch = cur.fetchall()
  for i in fetch:
    print(i)

# main
create()
insert()
display()