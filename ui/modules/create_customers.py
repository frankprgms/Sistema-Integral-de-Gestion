import customtkinter as ctk
from tkinter import ttk
from app_logic.customer import cliente

# Clase principal para la vista de creacion de clientes basada en un marco de CustomTkinter
class CreateCustomerView(ctk.CTkFrame):

    def __init__(self, parent, current_theme, language, file_manager,customers_list):
        # Inicializacion del componente con el tema visual y configuracion de idiomas
        super().__init__(parent, fg_color=current_theme["bg_window"])

        self.texts = language
        self.theme = current_theme
        self.customers_list = customers_list

        # Ejecucion de la configuracion de la interfaz de usuario
        self._setup_ui()

    def _setup_ui(self):
        # Configuracion de la cuadricula principal y el titulo de la vista
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(4, weight=1)

        self.title_label = ctk.CTkLabel(
            self,
            text=self.texts.get("crt_customer_title", "CREATE CUSTOMER"),
            font=("Helvetica", self.theme["font_title_size"], "bold"),
            text_color=self.theme["text_main"]
        )
        self.title_label.grid(row=0, column=0, pady=(20, 10))

        # Creacion del contenedor principal para el formulario de datos
        self.form_frame = ctk.CTkFrame(
            self,
            fg_color=self.theme["bg_container"],
            border_width=1,
            border_color=self.theme["primary_color"],
            corner_radius=12
        )
        self.form_frame.grid(row=1, column=0, padx=20, pady=10, sticky="nsew")
        self.form_frame.grid_columnconfigure(0, weight=1)
        self.form_frame.grid_columnconfigure(1, weight=1)

        # Definicion de los campos de entrada de texto (Nombre, ID, Documento, etc.)
        self._create_field(row=0, column=0, label=self.texts.get("crt_customer_name", "Name"))
        self.entry_name = self.current_entry

        self._create_field(row=0, column=1, label=self.texts.get("crt_customer_customer_id", "Customer ID"))
        self.entry_customer_id = self.current_entry

        self._create_field(row=1, column=0, label=self.texts.get("crt_customer_document", "Document"))
        self.entry_document = self.current_entry

        self._create_field(row=1, column=1, label=self.texts.get("crt_customer_email", "Email"))
        self.entry_email = self.current_entry

        self._create_field(row=2, column=0, label=self.texts.get("crt_customer_phone", "Phone"))
        self.entry_phone = self.current_entry

        self._create_field(row=2, column=1, label=self.texts.get("crt_customer_address", "Address"))
        self.entry_address = self.current_entry

        # Configuracion del interruptor (switch) para el estado activo/inactivo del cliente
        self.state_container = ctk.CTkFrame(
            self.form_frame,
            fg_color=self.theme["bg_window"],
            border_width=1,
            border_color=self.theme["primary_color"],
            corner_radius=10
        )
        self.state_container.grid(row=3, column=0, padx=15, pady=15, sticky="ew")

        self.state_label = ctk.CTkLabel(
            self.state_container,
            text=self.texts.get("crt_customer_state", "Active"),
            text_color=self.theme["text_secondary"],
            anchor="w"
        )
        self.state_label.pack(anchor="w", padx=12, pady=(10, 0))

        self.state_switch = ctk.CTkSwitch(
            self.state_container,
            text="",
            progress_color=self.theme["primary_color"]
        )
        self.state_switch.pack(anchor="w", padx=12, pady=(5, 10))

        # Configuracion del menu desplegable (combobox) para el tipo de membresia
        self.membership_container = ctk.CTkFrame(
            self.form_frame,
            fg_color=self.theme["bg_window"],
            border_width=1,
            border_color=self.theme["primary_color"],
            corner_radius=10
        )
        self.membership_container.grid(row=3, column=1, padx=15, pady=15, sticky="ew")

        self.membership_label = ctk.CTkLabel(
            self.membership_container,
            text=self.texts.get("crt_customer_membership", "Membership"),
            text_color=self.theme["text_main"],
            anchor="w"
        )
        self.membership_label.pack(anchor="w", padx=12, pady=(10, 5))

        self.membership_combo = ctk.CTkComboBox(
            self.membership_container,
            text_color=self.theme["text_secondary"],
            values=["Basic", "Premium", "Gold", "VIP"],
            fg_color=self.theme["bg_container"],
            border_color=self.theme["border_color"],
            button_color=self.theme["primary_color"],
            dropdown_fg_color=self.theme["bg_container"]
        )
        self.membership_combo.pack(fill="x", padx=12, pady=(0, 10))

        # Etiqueta para mostrar mensajes de error o informativos
        self.message_label = ctk.CTkLabel(
            self,
            text="",
            text_color=self.theme["error"],
            font=("Helvetica", self.theme["font_body_size"])
        )
        self.message_label.grid(row=2, column=0, pady=(5, 10))

        # Contenedor y botones de accion (Crear y Limpiar)
        self.button_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.button_frame.grid(row=3, column=0, pady=10)

        self.create_button = ctk.CTkButton(
            self.button_frame,
            text=self.texts.get("crt_customer_create_btn", "Create Customer"),
            fg_color=self.theme["primary_color"],
            hover_color=self.theme["contrast"],
            text_color=self.theme["text_main"],
            command=self.print_customer_data
        )
        self.create_button.pack(side="left", padx=10)

        self.clear_button = ctk.CTkButton(
            self.button_frame,
            text=self.texts.get("crt_customer_clear_btn", "Clear"),
            fg_color=self.theme["border_color"],
            hover_color=self.theme["primary_color"],
            text_color=self.theme["text_main"],
            command=self.clear_fields
        )
        self.clear_button.pack(side="left", padx=10)

        # Configuracion de la tabla (Treeview) para visualizar los clientes registrados
        self.table_container = ctk.CTkFrame(
            self,
            fg_color=self.theme["bg_container"],
            border_width=1,
            border_color=self.theme["border_color"],
            corner_radius=12
        )
        self.table_container.grid(row=4, column=0, padx=20, pady=(10, 20), sticky="nsew")
        self.table_container.grid_rowconfigure(0, weight=1)
        self.table_container.grid_columnconfigure(0, weight=1)

        self.columns = self.texts.get("crt_customer_colms", ["active","name", "customer id", "document", "email", "phone","address", "membership" ])

        self.customer_table = ttk.Treeview(
            self.table_container,
            columns=self.columns,
            show="headings"
        )

        for column in self.columns:
            self.customer_table.heading(column, text=column.upper())
            self.customer_table.column(column, width=120, anchor="center")

        self.customer_table.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)

    # Metodo auxiliar para generar dinimicamente campos de texto con etiqueta
    def _create_field(self, row, column, label):
        container = ctk.CTkFrame(
            self.form_frame,
            fg_color=self.theme["bg_window"],
            border_width=1,
            border_color=self.theme["border_color"],
            corner_radius=10
        )
        container.grid(row=row, column=column, padx=15, pady=15, sticky="ew")
        container.grid_columnconfigure(0, weight=1)

        field_label = ctk.CTkLabel(
            container,
            text=label,
            text_color=self.theme["text_secondary"],
            anchor="w"
        )
        field_label.grid(row=0, column=0, padx=12, pady=(10, 5), sticky="w")

        self.current_entry = ctk.CTkEntry(
            container,
            height=38,
            fg_color=self.theme["bg_container"],
            border_color=self.theme["border_color"],
            text_color=self.theme["text_main"]
        )
        self.current_entry.grid(row=1, column=0, padx=12, pady=(0, 10), sticky="ew")

    # Recopila la informacion de todos los campos y la imprime en consola
    def validate_correct_parameters(self):
        if not self.entry_name.get(): 
            message = self.texts["crt_customer_empty_field"].format(self.columns [1])
            self.show_message(message)
            return 0
            
        if not self.entry_customer_id.get(): 
            message = self.texts["crt_customer_empty_field"].format(self.columns [2])
            
            self.show_message(message)
            return 0
        
        if not self.entry_document.get(): 
            message = self.texts["crt_customer_empty_field"].format(self.columns [3])
            self.show_message(message)
            return 0
        
        if not self.entry_email.get(): 
            message = self.texts["crt_customer_empty_field"].format(self.columns [4])
            self.show_message(message)
            return 0
        if not self.entry_phone.get(): 
            message = self.texts["crt_customer_empty_field"].format(self.columns [5])
            self.entry_phone.delete(0, "end")
            self.show_message(message)
            return 0   
        if not self.entry_address.get(): 
            message = self.texts["crt_customer_empty_field"].format(self.columns [6])
            self.show_message(message)
            return 0
        if not self.membership_combo.get(): 
            message = self.texts["crt_customer_empty_field"].format(self.columns [7])
            self.show_message(message)
            return 0
        
        if self.entry_name.get().isdigit():
            message = self.texts["crt_customer_numbers_field"].format(self.columns [2])
            self.show_message(message)
            self.entry_name.delete(0, "end")
            return 0
        
        if self.entry_document.get().isalpha():
            message = self.texts["crt_customer_letters_field"].format(self.columns [3])
            self.show_message(message)
            self.entry_document.delete(0, "end")
            return 0
        if not "@" in self.entry_email.get():
            message = self.texts["crt_customer_symbol_field"].format(self.columns [4])
            self.show_message(message)
            self.entry_email.delete(0, "end")
            return 0
        if self.entry_phone.get().isalpha():
            message = self.texts["crt_customer_letters_field"].format(self.columns [5])
            self.show_message(message)
            self.entry_phone.delete(0, "end")
            return 0
        self.show_message("")
        return 1
    def print_customer_data(self):
        
        if(self.validate_correct_parameters()==0):
            print("error de datos")
            return
        else:
            print("complete parametros")
                
            data = {
                
                "name": self.entry_name.get(),
                "customer_id": self.entry_customer_id.get(),
                "document": self.entry_document.get(),
                "email": self.entry_email.get(),
                "phone": self.entry_phone.get(),
                "address": self.entry_address.get(),
                "state": self.state_switch.get(),
                "membership": self.membership_combo.get()
            }
            Customer=cliente(data=data)
            
            self.customers_list.append(Customer)
            self.refresh_table()
            
        
        

    # Restablece todos los campos del formulario a sus valores predeterminados
    def clear_fields(self):
        self.entry_name.delete(0, "end")
        self.entry_customer_id.delete(0, "end")
        self.entry_document.delete(0, "end")
        self.entry_email.delete(0, "end")
        self.entry_phone.delete(0, "end")
        self.entry_address.delete(0, "end")
        self.membership_combo.set("")
        self.state_switch.deselect()
        self.message_label.configure(text="")
        for item in self.customer_table.get_children():
            self.customer_table.delete(item)

    # Actualiza la etiqueta de mensaje para mostrar informacion al usuario
    def show_message(self, text):
        self.message_label.configure(text=text)
    def refresh_table(self):
        # 1. Limpiar todos los datos actuales de la tabla
        for item in self.customer_table.get_children():
            self.customer_table.delete(item)

        # 2. Insertar los datos actualizados
        for customer in self.customers_list:
            self.customer_table.insert("", "end", values=(
                "Activo" if customer._state else "Inactivo",
                customer.name,
                customer.customer_id,
                customer.document,
                customer.email,
                customer.phone,
                customer.address,
                customer.membership
            ))