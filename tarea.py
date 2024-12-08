class Tarea:
    def __init__(self, titulo, descripcion, estado="pendiente", prioridad="media"):
        # Inicializa los atributos de la clase
        self.titulo = titulo
        self.descripcion = descripcion
        self.estado = estado
        self.prioridad = prioridad
    
    # Método especial para convertir el objeto en una cadena de texto
    def __str__(self):
        return f"{self.titulo} - {self.estado} - {self.prioridad}"