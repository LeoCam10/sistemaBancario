
import sys
sys.path.append('/Users/camus/Desktop/banco')
import conexion as con
from model.usuario import Usuario


class CiudadData():
     
    def listarCiudades(self):
        self.db = con.Conexion().conectar()
        self.cursor = self.db.cursor()
        res = self.cursor.execute("SELECT * FROM ciudades order by nombre")
        ciudades = res.fetchall()
        return ciudades

      
