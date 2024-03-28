
import sys
sys.path.append('/Users/camus/Desktop/banco')
import conexion as con
from model.usuario import Usuario


class HistorialData():
     
    def buscarPorFecha(self,fechaDesde, fechaHasta,tipo,documento):
       # def buscarPorFecha(self, fechaDesde,FechaHasta,tipo,documento):
        self.db = con.Conexion().conectar()
        self.cursor = self.db.cursor()
        sql = """SELECT DISTINCT * FROM depositos AS d INNER JOIN transferencias AS t ON t.documento = d.documento AND t.tipo = d.tipo AND (DATE(t.fecha_registro) >= ? AND DATE(t.fecha_registro) <= ?) WHERE t.tipo = ? AND t.documento = ?"""

       # res = self.cursor.execute(sql, (tipo, documento))
        res = self.cursor.execute(sql, (fechaDesde, fechaHasta, tipo, documento))
        busqueda = res.fetchall()
       
       
        return busqueda

      
