import pymysql

def obtener_conexion():
    # return pymysql.connect( host='us-cdbr-east-06.cleardb.net',
    #                             user='b2590597ec3463',
    #                             password='f0c1aff1',
    #                             db='heroku_3389e7d80f0e249')
    return pymysql.connect( host='localhost',
                                user='root',
                                password='Sofia1900',
                                db='tesis')

def insertar_modelo(modelo, reclamo, tipo, subtipo,validado):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("INSERT INTO modelos(modelo, reclamo, tipo, subtipo, validado) VALUES (%s, %s, %s, %s,%s)",
                       (modelo, reclamo, tipo, subtipo,validado))
    conexion.commit()
    conexion.close()


def obtener_modelos():
    conexion = obtener_conexion()
    modelos = []
    with conexion.cursor() as cursor:
        cursor.execute("SELECT id, modelo, reclamo, tipo, subtipo, validado FROM modelos")
        modelos = cursor.fetchall()
    conexion.close()
    return modelos

def validar_modelo(id):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
            cursor.execute("UPDATE modelos SET validado = 'SI' WHERE id = %s",
                       (id))      
    conexion.commit()
    conexion.close()

def eliminar_modelo(id):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("DELETE FROM modelos WHERE id = %s", (id,))
    conexion.commit()
    conexion.close()


def obtener_modelo_por_id(id):
    conexion = obtener_conexion()
    modelo = None
    with conexion.cursor() as cursor:
        cursor.execute(
            "SELECT id, modelo, reclamo, tipo, subtipo,validado FROM modelos WHERE id = %s", (id,))
        modelo = cursor.fetchone()
    conexion.close()
    return modelo


def actualizar_modelo(modelo, reclamo, tipo, subtipo, validado, id):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("UPDATE modelos SET modelo = %s, reclamo = %s, tipo = %s, subtipo = %s, validado = %s WHERE id = %s",
                       (modelo, reclamo, tipo, subtipo,validado, id))
    conexion.commit()
    conexion.close()