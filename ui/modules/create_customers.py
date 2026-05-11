import customtkinter as ctk
from tkinter import ttk

# Clase principal para la vista de creación de clientes basada en un marco de CustomTkinter
class CreateCustomerView(ctk.CTkFrame):

    def __init__(self, parent, current_theme, language, file_manager):
        # Inicialización del componente con el tema visual y configuración de idiomas
        super().__init__(parent, fg_color=current_theme["bg_window"])

        self.texts = language
        self.theme = current_theme
        self.customers = []

        # Ejecución de la configuración de la interfaz de usuario
        self._setup_ui()

    def _setup_ui(self):
        # Configuración de la cuadrícula principal y el título de la vista
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(4, weight=1)

        self.title_label = ctk.CTkLabel(
            self,
            text=self.texts.get("crt_customer_title", "CREATE CUSTOMER"),
            font=("Helvetica", self.theme["font_title_size"], "bold"),
            text_color=self.theme["text_main"]
        )
        self.title_label.grid(row=0, column=0, pady=(20, 10))

        # Creación del contenedor principal para el formulario de datos
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

        # Definición de los campos de entrada de texto (Nombre, ID, Documento, etc.)
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

        # Configuración del interruptor (switch) para el estado activo/inactivo del cliente
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

        # Configuración del menú desplegable (combobox) para el tipo de membresía
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

        # Contenedor y botones de acción (Crear y Limpiar)
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

        # Configuración de la tabla (Treeview) para visualizar los clientes registrados
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

        columns = self.texts.get("crt_customer_colms", ["active","name", "customer_id", "document", "email", "phone", "membership" ])

        self.customer_table = ttk.Treeview(
            self.table_container,
            columns=columns,
            show="headings"
        )

        for column in columns:
            self.customer_table.heading(column, text=column.upper())
            self.customer_table.column(column, width=120, anchor="center")

        self.customer_table.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)

    # Método auxiliar para generar dinámicamente campos de texto con etiqueta
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

    # Recopila la información de todos los campos y la imprime en consola
    def print_customer_data(self):
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
        print(data)

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

    # Actualiza la etiqueta de mensaje para mostrar información al usuario
    def show_message(self, text):
        self.message_label.configure(text=text)