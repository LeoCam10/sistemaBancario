
import sys
sys.path.append('/Users/camus/Desktop/banco')
import conexion as con
import sys
sys.path.append('/Users/camus/Desktop/banco/model')
from movimiento import DepositoInternacional
from datetime import datetime
from model.usuario import Usuario


class DepositoData():

    def __init__(self):
        try:
            self.db = con.Conexion().conectar()
            self.cursor = self.db.cursor()
            sql_create_deposito = """CREATE TABLE IF NOT EXISTS depositos
            (id INTEGER PRIMARY KEY AUTOINCREMENT,
              monto NUMERIC, 
              tipo TEXT,
                documento TEXT,
                 pnombre TEXT,
                 snombre TEXT,
                 papellido TEXT,
                 sapellido TEXT,
                 sexo TEXT,
                internacional BOOLEAN,
                  dolares BOOLEAN, 
                  fecha_deposito DATETIME,             
                    fecha_nacimiento DATETIME,
                         lugar_nacimiento TEXT,
                           terminos BOOLEAN,
                        motivo TEXT)"""

            self.cursor.execute(sql_create_deposito)
            self.db.commit()
            self.cursor.close()
            self.db.close()
            print("Tabla Deposito creada ") 
        except Exception as ex:
            print("Tabla Deposito OK ", ex) 
    
    def registrar(self,info: DepositoInternacional):
        fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.db = con.Conexion().conectar()
        self.cursor = self.db.cursor()       
        self.cursor.execute("""INSERT INTO depositos (monto, tipo, documento,pnombre, snombre, papellido, sapellido,sexo,  internacional, dolares,fecha_deposito, fecha_nacimiento, lugar_nacimiento,terminos, motivo  ) VALUES ("{}", "{}", "{}", "{}", "{}","{}", "{}", "{}","{}", "{}", "{}", "{}", "{}", "{}", "{}")""".format(info._monto, info._tipo, info._documento, info._nombre1, info._nombre2, info._apellido1, info._apellido2,info._sexo, info._internacional, info._dolares,fecha, info._fechanacimiento,info._lugarnacimiento,info._terminos, info._motivo))
        self.db.commit()
        if self.cursor.rowcount == 1:
            return True
        else:
            return False
           