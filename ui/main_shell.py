import customtkinter as ctk
from tkinter import messagebox

# Clase para la ventana principal del sistema (Shell) que actúa como contenedor de la interfaz
class MainShell(ctk.CTkToplevel):
    def __init__(self, parent, language, current_theme):
        # Inicialización de la ventana, configuración de dimensiones y carga de idiomas y temas
        super().__init__(parent)

        self.texts = language        
        self.theme = current_theme    
        
        self.window_width = 1100
        self.window_height = 700
        
        self.title(self.texts.get("header", "SIGER"))
        self.configure(fg_color=self.theme["bg_window"])
        
        self.sidebar_visible = True

        # Configuración del comportamiento elástico de filas y columnas para el diseño responsivo
        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(0, weight=0)
        self.grid_columnconfigure(1, weight=1)
        
        try:
            self.state('zoomed')  # Windows
        except:
            self.attributes('-zoomed', True)  # Linux
        
        self._setup_ui()
        self._apply_visuals()

        # Gestión del protocolo de cierre de ventana
        self.protocol("WM_DELETE_WINDOW", self.on_closing)

    # Método para calcular la posición central de la ventana según la resolución de la pantalla
    def center_window(self):
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        x = (screen_width // 2) - (self.window_width // 2)
        y = (screen_height // 2) - (self.window_height // 2)
        self.geometry(f"{self.window_width}x{self.window_height}+{x}+{y}")

    def _setup_ui(self):
        # Creación de la barra superior (Header) con el botón de menú y etiqueta de estado
        self.header = ctk.CTkFrame(self, height=65, corner_radius=0, border_width=1)
        self.header.grid(row=0, column=0, columnspan=2, sticky="ew")
        self.header.grid_columnconfigure(1, weight=1)

        self.btn_toggle = ctk.CTkButton(
            self.header, text="☰", width=40, font=("Arial", 20),
            hover_color=self.theme.get("primary_hover"),
            command=self.toggle_sidebar
        )
        self.btn_toggle.grid(row=0, column=0, padx=20, pady=10)

        self.lbl_status = ctk.CTkLabel(self.header, font=("Helvetica", 12, "bold"))
        self.lbl_status.grid(row=0, column=2, padx=25)

        # Creación de la barra lateral (Sidebar) que contiene el botón para cerrar sesión
        self.sidebar = ctk.CTkFrame(self, width=240, corner_radius=0)
        self.sidebar.grid(row=1, column=0, sticky="ns")
        self.sidebar.grid_propagate(False)

        self.btn_logout = ctk.CTkButton(
            self.sidebar, 
            command=self.logout_action
        )
        self.btn_logout.pack(side="bottom", fill="x", padx=20, pady=30)

        # Creación del área principal (Content Frame) donde se desplegará el contenido dinámico
        self.content_frame = ctk.CTkFrame(self, corner_radius=0)
        self.content_frame.grid(row=1, column=1, sticky="nsew", padx=2, pady=2)
        
        self.lbl_info = ctk.CTkLabel(self.content_frame, font=("Helvetica", 14))
        self.lbl_info.pack(expand=True)

    def _apply_visuals(self):
        # Aplicación de colores, fuentes y estilos definidos en el diccionario de temas a los widgets
        bg_win = self.theme["bg_window"]
        bg_cont = self.theme["bg_container"]
        accent = self.theme["primary_color"]
        txt_m = self.theme["text_main"]
        txt_s = self.theme["text_secondary"]
        border = self.theme["border_color"]
        
        self.header.configure(fg_color=bg_cont, border_color=border)
        self.sidebar.configure(fg_color=bg_cont)
        self.content_frame.configure(fg_color=bg_win)

        self.btn_toggle.configure(fg_color="transparent", text_color=accent)
        
        self.lbl_status.configure(
            text=self.texts.get("status_online_dashboard"), 
            text_color=txt_s
        )

        self.btn_logout.configure(
            text=self.texts.get("btn_logout_dashboard"),
            fg_color=accent, text_color="white", font=("Helvetica", 11, "bold")
        )

        self.lbl_info.configure(
            text=self.texts.get("placeholder_main_dashboard",""),
            text_color=txt_s
        )

    # Lógica para ocultar o mostrar la barra lateral al presionar el botón de menú
    def toggle_sidebar(self):
        if self.sidebar_visible:
            self.sidebar.grid_remove()
        else:
            self.sidebar.grid()
        self.sidebar_visible = not self.sidebar_visible

    # Muestra un cuadro de diálogo para confirmar la salida antes de cerrar la sesión
    def logout_action(self):
        title = self.texts.get("msg_confirm_title")
        body = self.texts.get("msg_logout_body")
        if messagebox.askyesno(title, body):
            self.on_closing()

    # Finalización de los procesos de la aplicación y destrucción de la ventana
    def on_closing(self):
        self.quit()
        self.destroy()

    # Inicio del bucle principal de ejecución de la interfaz
    def run(self):
        self.mainloop()