import mysql.connector
mydb = mysql.connector.connect(host="localhost", user='root', password="Vinay@#23",database="Inventory_Management")
cur=mydb.cursor()


def create():
  manufacture = """CREATE TABLE manufacture (
  manufacture_id INT NOT NULL AUTO_INCREMENT,
  product VARCHAR(50) NOT NULL,
  color varchar(30),
  quantity INT NOT NULL,
  defective BOOLEAN NOT NULL DEFAULT false,
  PRIMARY KEY (manufacture_id)
)"""
  cur.execute(manufacture)

def display():
    
  cur.execute("select * from manufacture")
  fetch = cur.fetchall()
  for i in fetch:
    print(i)

def insert():

  data = """
INSERT INTO manufacture (product,color, quantity, defective)
VALUES ('Toy', "red",1000, false), ('Chair', "green",500, true), ('Table',"yellow" ,200, false), ('Shirt', "red",800, false),('shoes',"black",204,true)
"""
  cur.execute(data)
  mydb.commit()

# main
create()
insert()
display()