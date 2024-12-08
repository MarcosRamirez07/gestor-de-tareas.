import sqlite3

class GestorTareas:
    def __init__(self):
        # Conectar a la base de datos (si no existe, se crea automáticamente)
        self.conn = sqlite3.connect('tareas.db')
        self.cursor = self.conn.cursor()
        self.crear_tabla()

    def crear_tabla(self):
        # Crear la tabla de tareas si no existe
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS tareas (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                titulo TEXT NOT NULL,
                descripcion TEXT NOT NULL,
                estado TEXT NOT NULL,
                prioridad TEXT NOT NULL
            )
        ''')
        self.conn.commit()

    def agregar_tarea(self, tarea):
        # Insertar una tarea en la base de datos
        self.cursor.execute('''
            INSERT INTO tareas (titulo, descripcion, estado, prioridad)
            VALUES (?, ?, ?, ?)
        ''', (tarea.titulo, tarea.descripcion, tarea.estado, tarea.prioridad))
        self.conn.commit()

    def listar_tareas(self):
        # Obtener todas las tareas de la base de datos
        self.cursor.execute('SELECT * FROM tareas')
        return self.cursor.fetchall()

    def eliminar_tarea(self, tarea_id):
        # Eliminar tarea por ID
        self.cursor.execute('DELETE FROM tareas WHERE id = ?', (tarea_id,))
        self.conn.commit()

    def modificar_tarea(self, tarea_id, tarea):
        # Modificar tarea por ID
        self.cursor.execute('''
            UPDATE tareas SET titulo = ?, descripcion = ?, estado = ?, prioridad = ?
            WHERE id = ?
        ''', (tarea.titulo, tarea.descripcion, tarea.estado, tarea.prioridad, tarea_id))
        self.conn.commit()

    def cerrar_conexion(self):
        self.conn.close()

    