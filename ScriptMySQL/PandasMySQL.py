import pymysql
import defselect
import clasedata2
import pandas as pd
# misdatos=defselect.select(host='localhost', port=3306, user='root', passwd='udelas', db='ventas')
# for row in misdatos:
#         print(row)

miclasedata=clasedata2.SQL()
misdatos=miclasedata.select(host='localhost', port=3306, user='root', passwd='udelas', db='ventas')

dd=list(misdatos)
data=pd.DataFrame(dd,columns = ['IdVendedor', 'NombreVendedor'])
print(data)



print ("Ok")

