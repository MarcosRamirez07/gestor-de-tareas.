import tkinter as tk
from tkinter import ttk
from gestor_tareas import GestorTareas
from tarea import Tarea

class Interfaz:
    def __init__(self):
        self.gestor = GestorTareas()  # Crear el gestor de tareas
        self.root = tk.Tk()  # Crear la ventana principal
        self.root.title("Gestor de Tareas")  # Título de la ventana

        # Crear el campo para introducir el título de la tarea
        self.titulo_label = tk.Label(self.root, text="Título:")
        self.titulo_label.pack()

        self.titulo_entry = tk.Entry(self.root)  # Campo donde se escribe el título
        self.titulo_entry.pack()

        # Crear el campo para introducir la descripción de la tarea
        self.descripcion_label = tk.Label(self.root, text="Descripción:")
        self.descripcion_label.pack()

        self.descripcion_entry = tk.Entry(self.root)  # Campo donde se escribe la descripción
        self.descripcion_entry.pack()

        # Crear el botón para añadir una tarea
        self.agregar_boton = tk.Button(self.root, text="Añadir Tarea", command=self.añadir_tarea)
        self.agregar_boton.pack()

        # Crear la lista de tareas que se verá en la ventana
        self.lista_tareas = tk.Listbox(self.root)
        self.lista_tareas.pack()

        # Actualizar la lista con las tareas que ya puedan estar guardadas
        self.actualizar_lista()

    def añadir_tarea(self):
        titulo = self.titulo_entry.get()  # Obtener lo que el usuario escribió en el título
        descripcion = self.descripcion_entry.get()  # Obtener la descripción

        if titulo:  # Asegurarse de que el título no esté vacío
            nueva_tarea = Tarea(titulo, descripcion)  # Crear nueva tarea con título y descripción
            self.gestor.agregar_tarea(nueva_tarea)  # Llamar el método de agregar tarea a la base de datos
            self.actualizar_lista()  # Actualizar la lista de tareas en la interfaz

    def actualizar_lista(self):
        self.lista_tareas.delete(0, tk.END)  # Limpiar la lista
        for tarea in self.gestor.listar_tareas():  # Obtener las tareas desde la base de datos
            tarea_str = f"{tarea[1]} - {tarea[3]} - {tarea[4]}"  # Formato: título - estado - prioridad
            self.lista_tareas.insert(tk.END, tarea_str)  # Mostrar las tareas en la lista

    def iniciar(self):
        self.root.mainloop()  # Iniciar la ventana y empezar a ver todo
