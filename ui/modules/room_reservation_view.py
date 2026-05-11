import customtkinter as ctk

# Clase para la vista de reserva de salas que hereda de CTkFrame para integrarse en el panel de contenido
class RoomReservationView(ctk.CTkFrame):
    def __init__(self, parent, current_theme, language, file_manager):
        # Inicialización del componente cargando las preferencias de tema, idioma y gestor de archivos
        super().__init__(parent)
        self.texts = language
        self.theme = current_theme
