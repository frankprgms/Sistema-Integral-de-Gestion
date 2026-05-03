import customtkinter as ctk
from app_logic.reservation import Reservation

class WelcomeView(ctk.CTk):
    """
    Clase para la vista de bienvenida del sistema.
    Maneja la selección dinámica de idioma y temas visuales.
    """
    def __init__(self, file_manager):
        super().__init__()

        # --- CONFIG GLOBAL CTK ---
        

        # --- DATOS Y CONFIGURACIÓN BASE ---
        # Se inyecta la dependencia del gestor de archivos para cargar recursos
        self._file_manager = file_manager
        self._all_languages = file_manager.load("language")
        self._all_themes = file_manager.load("themes")
        

        # Extracción de llaves para navegación técnica (independiente de la traducción)
        self._lang_keys = list(self._all_languages.keys())
        self._theme_keys = list(self._all_themes.keys())
        
        # Estado inicial del sistema: primer idioma y primer tema de la lista
        self._current_theme_index = 0
        self._current_lang = self._lang_keys[0] 
        
        # Carga inicial de diccionarios de texto y colores
        self._texts = self._all_languages.get(self._current_lang, {})
        self._theme = self._all_themes[self._theme_keys[self._current_theme_index]]

        # --- CONFIGURACIÓN DE VENTANA ---
        window_width, window_height = 500, 620
        
        # Lógica de centrado en pantalla basada en la resolución del monitor
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        x = (screen_width // 2) - (window_width // 2)
        y = (screen_height // 2) - (window_height // 2)

        self.geometry(f"{window_width}x{window_height}+{x}+{y}")
        self.resizable(False, False) # Bloqueo de redimensión para mantener diseño

        # --- GRID ROOT (CENTRADO TOTAL) ---
        # Se configura el grid del root para que el contenedor principal flote en el centro
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        # --- CONTENEDOR PRINCIPAL ---
        # CTkFrame que agrupa todos los elementos visuales
        self._main_container = ctk.CTkFrame(
            self,
            corner_radius=15, # Estética moderna redondeada
            border_width=1
        )
        self._main_container.grid(
            row=0,
            column=0,
            padx=50,
            pady=50,
            sticky="nsew" # Permite que el frame se expanda dentro de sus límites
        )

        # Inicialización de componentes y aplicación de estilos
        self._setup_ui()
        self._update_visuals()

    def _setup_ui(self):
        """Construye la jerarquía de widgets dentro del contenedor principal."""
        
        # --- TÍTULO ---
        self._lbl_header = ctk.CTkLabel(
            self._main_container, 
            wraplength=300, # Evita que textos largos rompan el diseño
            justify="center"
        )
        self._lbl_header.pack(padx=20, pady=(40, 5), anchor="center")

        # --- SUBTÍTULO ---
        self._lbl_subtitle = ctk.CTkLabel(
            self._main_container,
            justify="center"
        )
        self._lbl_subtitle.pack(padx=20, pady=(0, 40), anchor="center")

        # --- SELECTOR DE IDIOMA ---
        self._lbl_lang_info = ctk.CTkLabel(self._main_container)
        self._lbl_lang_info.pack(padx=20, pady=(10, 5), anchor="center")

        lang_options = self._texts.get("languages", [])
        self._lang_combo = ctk.CTkComboBox(
            self._main_container,
            values=lang_options,
            command=self._on_language_change, # Callback al cambiar selección
            width=220,
            justify="center"
        )
        self._lang_combo.pack(padx=20, pady=10, anchor="center")

        # --- PAGINADOR DE TEMAS ---
        # Frame interno para organizar botones de navegación y nombre del tema
        self._theme_frame = ctk.CTkFrame(self._main_container, fg_color="transparent")
        self._theme_frame.pack(padx=20, pady=30, anchor="center")

        # Botón anterior tema
        self._btn_prev_theme = ctk.CTkButton(
            self._theme_frame,
            text="<",
            command=lambda: self._change_theme(-1),
            width=40,
            height=40,
            corner_radius=20 # Forma circular
        )
        self._btn_prev_theme.pack(side="left", padx=15)

        # Etiqueta indicadora del tema actual
        self._lbl_theme_name = ctk.CTkLabel(
            self._theme_frame,
            width=100,
            font=("Helvetica", 11, "bold")
        )
        self._lbl_theme_name.pack(side="left")

        # Botón siguiente tema
        self._btn_next_theme = ctk.CTkButton(
            self._theme_frame,
            text=">",
            command=lambda: self._change_theme(1),
            width=40,
            height=40,
            corner_radius=20
        )
        self._btn_next_theme.pack(side="left", padx=15)

        # --- BOTÓN PRINCIPAL ---
        self._btn_enter = ctk.CTkButton(
            self._main_container,
            width=240,
            height=45,
            corner_radius=8,
            command=self._start_system
        )
        self._btn_enter.pack(padx=20, pady=(60, 20), anchor="center")

        # --- FOOTER ---
        self._lbl_footer = ctk.CTkLabel(self._main_container)
        self._lbl_footer.pack(side="bottom", pady=20, anchor="center")


    def _update_visuals(self):
        """Sincroniza el tema y el idioma con todos los widgets de la interfaz."""
        
        # Recarga de diccionarios según el estado actual
        self._texts = self._all_languages.get(self._current_lang, {})
        self._theme = self._all_themes[self._theme_keys[self._current_theme_index]]

        # Configuración dinámica de fuentes basadas en el tema cargado
        f_body = ("Helvetica", self._theme.get("font_body_size", 11))
        f_footer = ("Helvetica", 8)
        new_title = self._texts.get("header","SIGER")
        f_title = ("Helvetica", self._theme.get("font_title_size", 18), "bold")

        # Aplicación de colores globales de ventana y título
        self.configure(fg_color=self._theme["bg_window"])
        self.title(new_title)

        # Estilo del contenedor central
        self._main_container.configure(
            fg_color=self._theme["bg_container"],
            border_color=self._theme["border_color"]
        )

        # Mapeo de widgets para actualización masiva de fuentes y colores
        # Formato: (widget, llave_diccionario_texto, estilo_fuente, llave_color_tema)
        components = [
            (self._lbl_header, "header", f_title, "text_main"),
            (self._lbl_subtitle, "subtitle_welcome_screen", f_body, "text_secondary"),
            (self._lbl_lang_info, "label_lang_welcome_screen", f_body, "text_main"),
            (self._lbl_footer, "footer", f_footer, "text_secondary"),
            (self._lbl_theme_name, None, f_body, "text_main")
        ]

        for widget, key, font_style, color_key in components:
            widget.configure(
                font=font_style,
                text_color=self._theme[color_key]
            )
            # Solo actualiza el texto si existe una llave asociada
            if key:
                widget.configure(text=self._texts.get(key, "N/A"))

        # Refresco visual del paginador de temas
        self._lbl_theme_name.configure(text=self._theme["name"].upper())
        
        # Botones de navegación (comparten color primario del tema)
        for btn in [self._btn_prev_theme, self._btn_next_theme]:
            btn.configure(
                fg_color=self._theme["primary_color"],
                hover_color=self._theme.get("primary_hover", self._theme["primary_color"]),
                text_color="white"
            )

        # Configuración del botón de acción principal
        self._btn_enter.configure(
            text=self._texts.get("btn_continue_welcome_screen", "START"),
            fg_color=self._theme["primary_color"],
            text_color="white",
            font=f_body
        )

        # Actualización de opciones del Combobox con nombres de idiomas traducidos
        new_lang_names = self._texts.get("languages", [])
        if new_lang_names:
            self._lang_combo.configure(values=new_lang_names)
            # Mantenemos la selección sincronizada usando el índice técnico
            current_idx = self._lang_keys.index(self._current_lang)
            self._lang_combo.set(new_lang_names[current_idx])

    def _on_language_change(self, selected_value):
        """
        Manejador del evento de cambio de idioma.
        Mapea el nombre seleccionado de nuevo a su llave técnica (id).
        """
        index = self._lang_combo.cget("values").index(selected_value)
        self._current_lang = self._lang_keys[index]
        self._update_visuals()

    def _change_theme(self, direction):
        """
        Navegación cíclica de temas.
        'direction' puede ser 1 (next) o -1 (prev).
        """
        self._current_theme_index = (
            self._current_theme_index + direction
        ) % len(self._theme_keys) # Operación módulo para rotación infinita
        self._update_visuals()

    def _start_system(self):
        """Finaliza el ciclo de vida de la vista de bienvenida."""
        print(f"Configuración finalizada: {self._current_lang} | {self._theme['name']}")
                
        self.destroy()