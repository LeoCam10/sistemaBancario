import sqlite3
 
class Conexion():
    def __init__(self):
        try: 
            self.con = sqlite3.connect('banco.db')
            self.crear_tablas()
        except Exception as e:
            print(e)

    def crear_tablas(self):
        sql_create_tabla = """ CREATE TABLE IF NOT EXISTS usuarios
          (id INTEGER PRIMARY KEY AUTOINCREMENT, nombre TEXT, usuario TEXT UNIQUE, clave TEXT)"""
        cur = self.con.cursor()
        cur.execute(sql_create_tabla)
        cur.close()
        self.crear_admin()

    def crear_admin(self):
        try:   
            cur = self.con.cursor()
            # Verificar si el usuario "admin" ya existe
            cur.execute("SELECT * FROM usuarios WHERE usuario=?", ("admin",))
            existing_user = cur.fetchone()
            if existing_user:
                print("El usuario 'admin' ya está registrado.")
            else:
                # Insertar el usuario "admin" solo si no existe
                sql_insert = """INSERT INTO usuarios (nombre, usuario, clave) VALUES (?, ?, ?)"""
                cur.execute(sql_insert, ("administrador", "admin", "admin1606"))
                self.con.commit()
                print("Se ha creado el usuario 'admin' correctamente.")
        except Exception as e:
             print("Error al crear el usuario 'admin':", e)
        finally:
             cur.close()

    def conectar (self):
         return self.con 
con = Conexion()

