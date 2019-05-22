#pip install --upgrade pip
#pip install pymysql
#https://pypi.org/project/PyMySQL/
#https://pymysql.readthedocs.io/en/latest/
#https://github.com/PyMySQL/PyMySQL/


import pymysql

conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='udelas', db='ventas')

cur = conn.cursor()
cur.execute("SELECT * FROM facturas")

print(cur.description)
print()

for row in cur:
    print(row)

cur.close()
conn.close()

