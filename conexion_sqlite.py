import sqlite3

class Comunicacion():
    def __init__(self):
        self.conexion = sqlite3.connect('clientes.db')

    def inserta_datos(self, nombre,apellido,  email, telefono):
        cursor = self.conexion.cursor()
        bd =  ''' INSERT INTO datos(NOMBRE,APELLIDO, EMAIL, TELEFONO)
        VALUES ('{}','{}','{}','{}')'''.format(nombre, apellido,  email, telefono)
        cursor.execute(bd)
        self.conexion.commit()
        cursor.close()
    
    def mostrar_datos(self):
        cursor = self.conexion.cursor()
        bd = "SELECT * FROM datos"
        cursor.execute(bd)
        datos = cursor.fetchall()
        return datos

    def elimina_datos(self, nombre):
        cursor = self.conexion.cursor()
        bd = ''' DELETE FROM datos WHERE NOMBRE = '{}' '''.format(nombre)
        cursor.execute(bd)
        self.conexion.commit()
        cursor.close()
    
    def actualiza_datos(self, ID, nombre,apellido, email, telefono):
        cursor = self.conexion.cursor()
        bd = ''' UPDATE datos SET NOMBRE = '{}', APELLIDO = '{}', EMAIL = '{}', TELEFONO = '{}' WHERE ID = '{}' '''.format(nombre, apellido, email,telefono, ID)
        cursor.execute(bd)
        dato = cursor.rowcount
        self.conexion.commit()
        cursor.close()
        return dato
    
