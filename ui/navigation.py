from app_logic import reservation
from ui.main_shell import MainShell
from ui.modules.room_reservation_view import RoomReservationView as rrv
from ui.modules.create_customers import CreateCustomerView as ccv
from services.equipment_rental_service import  EquipmentRentalService as ers
from services.specialized_consultancies import  SpecializedConsultanciesService as scs
from services.room_reservation_service import  RoomReservationService as rrs
from app_logic.customer import cliente
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
        self.customers_list = []
        self.equipments_list = []
        self.consultancies_list = []
        self.rooms_list = []

        # Llamada para generar la botonera de navegación
        self.agg_buttons()
        
    def agg_services(self):
        # --- EQUIPOS ---
        self.equipments_list.extend([
            ers(service_id="e1", service_name="Projector", base_fee=1150, quantity=2, status=True, equipment_id=165446558741987, category="Electric", physical_condition=90, is_available=True, daily_rate=200),
            ers(service_id="e2", service_name="Laptop Pro", base_fee=2500, quantity=5, status=True, equipment_id=165446558741988, category="Computing", physical_condition=95, is_available=True, daily_rate=450),
            ers(service_id="e3", service_name="Sound System", base_fee=1800, quantity=3, status=True, equipment_id=165446558741989, category="Audio", physical_condition=85, is_available=True, daily_rate=300),
            ers(service_id="e4", service_name="LED Screen 55'", base_fee=3200, quantity=2, status=True, equipment_id=165446558741990, category="Video", physical_condition=100, is_available=True, daily_rate=600),
            ers(service_id="e5", service_name="Microphone Wireless", base_fee=500, quantity=10, status=True, equipment_id=165446558741991, category="Audio", physical_condition=92, is_available=True, daily_rate=150)
        ])

        # --- CONSULTORÍAS ---
        self.consultancies_list.extend([
            scs(service_id="c1", service_name="Frank Aguila", base_fee=1878, duration=20, status=True, specialist_id="Programacion", category="Tecnologia", level_multiplier="Junior", availability="08-17", modality=4),
            scs(service_id="c2", service_name="franz kafka", base_fee=2500, duration=15, status=True, specialist_id="Ciberseguridad", category="Tecnologia", level_multiplier="Senior", availability="09-18", modality=1),
            scs(service_id="c3", service_name="Marco Polo", base_fee=1200, duration=10, status=True, specialist_id="Marketing", category="Comercial", level_multiplier="Mid", availability="10-14", modality=2),
            scs(service_id="c4", service_name="Sofia Chen", base_fee=3000, duration=40, status=True, specialist_id="Data Science", category="Tecnologia", level_multiplier="Expert", availability="07-15", modality=4),
            scs(service_id="c5", service_name="Lucas Smith", base_fee=1500, duration=12, status=True, specialist_id="UI/UX Design", category="Diseno", level_multiplier="Mid", availability="14-20", modality=3)
        ])

        # --- SALAS ---
        self.rooms_list.extend([
            rrs(service_id="r1", service_name="Sala A", base_fee=15585, quantity=1, status=True, room_id="15424", room_type="Conferencia", capacity=100, hourly_rate="1200", is_available=True),
            rrs(service_id="r2", service_name="Sala B (Lounge)", base_fee=8000, quantity=1, status=True, room_id="15425", room_type="Networking", capacity=30, hourly_rate="600", is_available=True),
            rrs(service_id="r3", service_name="Auditorio Central", base_fee=50000, quantity=1, status=True, room_id="15426", room_type="Auditorio", capacity=500, hourly_rate="4500", is_available=True),
            rrs(service_id="r4", service_name="Coworking", base_fee=2000, quantity=1, status=True, room_id="15427", room_type="Compartido", capacity=15, hourly_rate="200", is_available=True),
            rrs(service_id="r5", service_name="Directorio Ejecutivo", base_fee=12000, quantity=1, status=True, room_id="15428", room_type="Privado", capacity=12, hourly_rate="950", is_available=True)
        ])
        # --- CLIENTES ---
        self.customers_list.extend([
            cliente(data = {"name": "valeria","customer_id": "c1011411","document": 1020304050,"email": "valeria@email.com","phone": 3001234567,"address": "avenida siempre viva 123","state": True,"membership": "premium"}),
            cliente(data = {"name": "marcos","customer_id": "c1011412","document": 9876543210,"email": "marcos@email.com","phone": 3159876543,"address": "carrera 10 # 45 - 20","state": True,"membership": "regular"}),
            cliente(data = {"name": "elena","customer_id": "c1011413","document": 5544332211,"email": "elena@email.com","phone": 3204567890,"address": "calle 100 # 15 - 30","state": False,"membership": "vip"}),
            cliente(data = {"name": "ricardo","customer_id": "c1011414","document": 1122334455,"email": "ricardo@email.com","phone": 3112223344,"address": "diagonal 40 # 2 - 10","state": True,"membership": "gold"}),
            cliente(data = {"name": "sofia","customer_id": "c1011415","document": 6677889900,"email": "sofia@email.com","phone": 3185554433,"address": "transversal 5 # 80","state": True,"membership": "regular"})
        ])
            

    def agg_buttons(self):
        # Definición de la lista de botones con sus etiquetas traducidas y sus funciones correspondientes
        buttons_data = [
            (self.texts.get("nav_btn_room_reserv", "room reservation"), self.show_room_reservation),
            #(self.texts.get("nav_btn_equipment_rental", "equipment rental"), self.show_equipment_rental),
            (self.texts.get("nav_btn_create_customers", "create customers"), self.show_create_customers),
            #(self.texts.get("nav_btn_specialized_consultancies", "specialized consultancies"), self.show_specialized_consultancies)
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
        self.agg_services()
        self.clear_content()
        self.reserv_view = rrv(
            parent=self.content_frame,
            current_theme=self.theme,
            language=self.texts,
            file_manager=self.file_manager,
            customers_list=self.customers_list , 
            equipments_list=self.equipments_list, 
            consultancies_list=self.consultancies_list, 
            rooms_list=self.rooms_list            
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
            file_manager=self.file_manager,
            customers_list=self.customers_list,
            
        )
        self.create_customers.pack(fill="both", expand=True)

    def clear_content(self):
        # Método para vaciar el panel central antes de cargar una nueva vista
        for widget in self.content_frame.winfo_children():
            widget.destroy()