import pymysql
import defselect
import clasedata

# misdatos=defselect.select(host='localhost', port=3306, user='root', passwd='udelas', db='ventas')
# for row in misdatos:
#         print(row)

miclasedata=clasedata.SQL()
misdatos=miclasedata.select(host='localhost', port=3306, user='root', passwd='udelas', db='ventas')
for row in misdatos:
        print(row)

