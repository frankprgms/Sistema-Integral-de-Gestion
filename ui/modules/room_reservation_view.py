import customtkinter as ctk

class RoomReservationView(ctk.CTkFrame):
    def __init__(self, parent, current_theme, language, file_manager, customers_list, equipments_list, consultancies_list, rooms_list):
        # Inicialización con el tema visual
        super().__init__(parent, fg_color=current_theme["bg_window"])
        
        self.texts = language
        self.theme = current_theme
        self.file_manager = file_manager
        
        # Listas de objetos
        self.customers_list = customers_list
        self.rooms_list = rooms_list
        self.equip_list = equipments_list
        self.specialists_list = consultancies_list
        
        # Diccionarios para rastrear variables de la interfaz
        self.check_vars_equip = {} 
        self._setup_ui()

    def _setup_ui(self):
        # Configuración de pesos: las columnas se expanden por igual
        self.grid_columnconfigure((0, 1), weight=1)
        self.grid_rowconfigure(1, weight=0) 

        # 1. Título de la Vista
        self.title_label = ctk.CTkLabel(
            self,
            text=self.texts.get("room_res_title", "GESTIÓN DE RESERVAS"),
            font=("Helvetica", self.theme["font_title_size"], "bold"),
            text_color=self.theme["text_main"]
        )
        self.title_label.grid(row=0, column=0, columnspan=2, pady=(20, 10))

        # 2. Contenedor Principal (Formulario)
        self.form_frame = ctk.CTkFrame(
            self,
            fg_color=self.theme["bg_container"],
            border_width=1,
            border_color=self.theme["primary_color"],
            corner_radius=12
        )
        self.form_frame.grid(row=1, column=0, columnspan=2, padx=20, pady=10, sticky="nsew")
        self.form_frame.grid_columnconfigure((0, 1), weight=1)

        # --- FILA 1: CLIENTE Y SALA ---
        self._create_section_label(self.form_frame, self.texts.get("res_customer_select", "Seleccionar Cliente"), 0, 0)
        customer_info = [f"{c.name} (ID: {c.customer_id})" for c in self.customers_list]
        self.customer_combo = ctk.CTkComboBox(
            self.form_frame, 
            values=customer_info, 
            fg_color=self.theme["bg_window"],
            text_color=self.theme["text_secondary"],
            border_color=self.theme["border_color"]
        )
        self.customer_combo.grid(row=1, column=0, padx=15, pady=(2, 15), sticky="ew")

        self._create_section_label(self.form_frame, self.texts.get("res_room_select", "Seleccionar Sala"), 0, 1)
        room_info = [f"{r.service_name} (Cap: {r.capacity})" for r in self.rooms_list]
        self.room_combo = ctk.CTkComboBox(
            self.form_frame, 
            values=room_info, 
            fg_color=self.theme["bg_window"],
            text_color=self.theme["text_secondary"],
            border_color=self.theme["border_color"]
        )
        self.room_combo.grid(row=1, column=1, padx=15, pady=(2, 15), sticky="ew")

        # --- FILA 2: ESPECIALISTA Y EQUIPOS ---
        self._create_section_label(self.form_frame, self.texts.get("res_spec_select", "Asignar Especialista"), 2, 0)
        spec_info = [s.service_name for s in self.specialists_list]
        self.spec_combo = ctk.CTkComboBox(
            self.form_frame, 
            values=spec_info, 
            fg_color=self.theme["bg_window"],
            text_color=self.theme["text_secondary"],
            border_color=self.theme["border_color"]
        )
        self.spec_combo.grid(row=3, column=0, padx=15, pady=(2, 15), sticky="new")

        self._create_section_label(self.form_frame, self.texts.get("res_equip_extra", "Equipos Adicionales"), 2, 1)
        self.equip_scroll = ctk.CTkScrollableFrame(
            self.form_frame, 
            height=150, 
            fg_color=self.theme["bg_window"],
            border_width=1,
            border_color=self.theme["border_color"]
        )
        self.equip_scroll.grid(row=3, column=1, padx=15, pady=(2, 15), sticky="nsew")

        for equip in self.equip_list:
            var = ctk.BooleanVar()
            cb = ctk.CTkCheckBox(
                self.equip_scroll, 
                text=f"{equip.service_name}",
                variable=var,
                text_color=self.theme["text_main"],
                border_color=self.theme["primary_color"],
                hover_color=self.theme["primary_color"]
            )
            cb.pack(anchor="w", padx=10, pady=5)
            self.check_vars_equip[equip._equipment_id] = var

        # --- FILA 3: ANOTACIONES Y PRIORIDAD (COLOR) ---
        self._create_section_label(self.form_frame, self.texts.get("res_note_system", "Anotación del Sistema"), 4, 0)
        self.note_entry = ctk.CTkEntry(
            self.form_frame, 
            text_color=self.theme["text_secondary"],
            placeholder_text=self.texts.get("res_placeholder_note", "Escriba una nota técnica..."),
            fg_color=self.theme["bg_window"],
            border_color=self.theme["border_color"]
        )
        self.note_entry.grid(row=5, column=0, padx=15, pady=(2, 20), sticky="ew")


        # --- BOTÓN DE ACCIÓN FINAL ---
        self.add_button = ctk.CTkButton(
            self,
            text=self.texts.get("res_btn_add", "Añadir Reserva"),
            font=("Helvetica", 14, "bold"),
            fg_color=self.theme["primary_color"],
            hover_color=self.theme.get("contrast", "#27ae60"),
            height=40,
            command=self.save_reservation_data
        )
        self.add_button.grid(row=2, column=0, columnspan=2, pady=30)

    def _create_section_label(self, parent, text, row, col):
        """Crea etiquetas pegadas al widget inferior usando sticky='sw' y sin pady inferior."""
        label = ctk.CTkLabel(
            parent, 
            text=text, 
            text_color=self.theme["text_secondary"], 
            font=("Helvetica", 12, "bold")
        )
        # pady=(15, 0) -> 15 arriba para separar bloques, 0 abajo para no alejarse del combo
        label.grid(row=row, column=col, padx=15, pady=(15, 0), sticky="sw")

    def save_reservation_data(self):
        selected_equip_ids = [eid for eid, v in self.check_vars_equip.items() if v.get()]
        
        data = {
            "customer_selected": self.customer_combo.get(),
            "room_selected": self.room_combo.get(),
            "specialist_assigned": self.spec_combo.get(),
            "equipment_ids": selected_equip_ids,
            "annotation": self.note_entry.get()
        }
        
        print(">>> RESERVA GENERADA CON ÉXITO:")
        for key, value in data.items():
            print(f"{key.capitalize()}: {value}")