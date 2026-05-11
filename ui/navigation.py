from app_logic import reservation
from ui.main_shell import MainShell
from ui.modules.room_reservation_view import RoomReservationView as rrv
from ui.modules.create_customers import CreateCustomerView as ccv
import customtkinter as ctk

# Clase encargada de la lógica de navegación y cambio de vistas dentro del Shell principal
class Navigation(MainShell):

    def __init__(self, parent, language, current_theme, file_manager, current_lang):
        # Inicialización de la navegación heredando del contenedor principal y guardando configuraciones de idioma y archivos
        super().__init__(parent, language, current_theme)

        self.texts = language
        self.theme = current_theme
        self.file_manager = file_manager
        self.current_lang = current_lang

        # Llamada para generar la botonera de navegación
        self.agg_buttons()

    def agg_buttons(self):
        # Definición de la lista de botones con sus etiquetas traducidas y sus funciones correspondientes
        buttons_data = [
            (self.texts.get("nav_btn_room_reserv", "room reservation"), self.show_room_reservation),
            (self.texts.get("nav_btn_equipment_rental", "equipment rental"), self.show_equipment_rental),
            (self.texts.get("nav_btn_create_customers", "create customers"), self.show_create_customers),
            (self.texts.get("nav_btn_specialized_consultancies", "specialized consultancies"), self.show_specialized_consultancies)
        ]

        self.sidebar_buttons = []

        # Creación dinámica y empaquetado de los botones en la barra lateral (sidebar)
        for text, command in buttons_data:
            btn = ctk.CTkButton(
                self.sidebar,
                text=text,
                font=("Helvetica", 11, "bold"),
                fg_color=self.theme["primary_color"],
                text_color=self.theme["text_main"],
                hover_color=self.theme.get("primary_hover"),
                corner_radius=8,
                command=command
            )

            btn.pack(
                fill="x",
                padx=20,
                pady=10
            )

            self.sidebar_buttons.append(btn)

    def show_room_reservation(self):
        # Lógica para limpiar el contenido actual y desplegar el módulo de reserva de salas
        print("room reservation.")
        self.clear_content()
        self.reserv_view = rrv(
            parent=self.content_frame,
            current_theme=self.theme,
            language=self.texts,
            file_manager=self.file_manager
        )
        self.reserv_view.pack(fill="both", expand=True)

    def show_equipment_rental(self):
        # Marcador de posición para el módulo de alquiler de equipos
        print("equipment rental")

    def show_specialized_consultancies(self):
        # Marcador de posición para el módulo de consultorías especializadas
        print("specialized consultancies")

    def show_create_customers(self):
        # Lógica para limpiar el contenido actual y desplegar el módulo de gestión/creación de clientes
        print("create customers")
        self.clear_content()
        self.create_customers = ccv(
            parent=self.content_frame,
            current_theme=self.theme,
            language=self.texts,
            file_manager=self.file_manager
        )
        self.create_customers.pack(fill="both", expand=True)

    def clear_content(self):
        # Método para vaciar el panel central antes de cargar una nueva vista
        for widget in self.content_frame.winfo_children():
            widget.destroy()