'''
1.Delete the defective item, e.g., the shirt which was accidentally purchased by the “ORay” store, manufactured on the date ‘01-05-23’.

2.Update the manufacture details of all the red-colored toys which are purchased by the “MyKids” store.

3.Display all the “wooden chair” items that were manufactured before the 1st May 2023. 

4.Display the profit margin amount of the “wooden table” that was sold by the “MyCare” store, manufactured by the “SS Export” company.'''



import mysql.connector
mydb = mysql.connector.connect(host="localhost", user='root', password="Vinay@#23",database="Inventory_Management")
cur=mydb.cursor()

s="DELETE FROM goods WHERE product = 'Shirt' AND manufactured_date = '2023-05-01'"

cur.execute(s)
mydb.commit()

s2="""UPDATE manufacture 
SET  quantity = 500, color = 'Red'
WHERE product = 'Toy' AND color = 'Red'"""
cur.execute(s2)
mydb.commit()


s3 = """SELECT * FROM goods
WHERE product = 'wooden chair' AND manufactured_date < '2023-05-01';
"""
cur.execute(s3)
mydb.commit()


s4="""SELECT sale.sale_amount - purchase.purchase_amount as profit_margin
FROM sale 
JOIN purchase ON sale.purchase_id = purchase.purchase_id 
JOIN goods ON purchase.goods_id = goods.goods_id 
JOIN manufacture ON goods.manufacture_id = manufacture.manufacture_id 
WHERE manufacture.product = 'wooden table' 
AND manufacture.color = 'brown' 
AND purchase.spurchased_by = 'MyCare' 
AND manufacture.date< '2023-05-01';
"""
cur.execute(s4)
mydb.commit()