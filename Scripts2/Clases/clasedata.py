import pymysql

class SQL:

    def select(self,host,port,user,passwd,db):

        conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='udelas', db='ventas')

        cur = conn.cursor()
        cur.execute("SELECT * FROM facturas")
        datos=cur
        cur.close()
        conn.close()
        return datos

    def insertar(self,host,port,user,passwd,db):
        pass

    def actualizar(self,host,port,user,passwd,db):
        pass
    def eliminar(self,host,port,user,passwd,db):
        pass
