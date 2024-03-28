
import sys
sys.path.append('/Users/camus/Desktop/banco')
import conexion as con
import sys
sys.path.append('/Users/camus/Desktop/banco/model')
from movimiento import Transferencia
from datetime import datetime
from model.usuario import Usuario


class TransferenciaData():

    def __init__(self):
        try:
            self.db = con.Conexion().conectar()
            self.cursor = self.db.cursor()
            sql_create_transferencia = """CREATE TABLE IF NOT EXISTS transferencias
            (id INTEGER PRIMARY KEY AUTOINCREMENT, monto NUMERIC, tipo TEXT, documento TEXT, internacional BOOLEAN, dolares BOOLEAN, fecha_registro DATETIME, verificado BOOLEAN, motivo TEXT)"""

            self.cursor.execute(sql_create_transferencia)
            self.db.commit()
            self.cursor.close()
            self.db.close()
            print("Tabla Transferencias creada ") 
        except Exception as ex:
            print("Tabla Transferencias OK ", ex) 
    
    def registrar(self,info: Transferencia):
        fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.db = con.Conexion().conectar()
        self.cursor = self.db.cursor()
        
        self.cursor.execute("""INSERT INTO transferencias (monto, tipo, documento, internacional, dolares, fecha_registro, verificado, motivo) VALUES ("{}", "{}", "{}", "{}", "{}", "{}", "{}", "{}")""".format(info._monto, info._tipo, info._documento, info._internacional, info._dolares, fecha, False, info._motivo))


        self.db.commit()

        if self.cursor.rowcount == 1:
            return True
        else:
            return False
           