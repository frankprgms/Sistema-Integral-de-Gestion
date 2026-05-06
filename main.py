
from pathlib import Path
 
from file_manager.LogHandler import LogHandler
from file_manager.manager_json import ManagerJson
from ui.welcome_view import WelcomeView
from app_logic.customer import cliente
 
 
if __name__ == "__main__":
    # Ruta base del proyecto, es decir, la carpeta donde está este archivo main.py
    BASE_DIR = Path(__file__).resolve().parent
 
    # Carpeta donde se guardarán los logs
    logs_folder = LogHandler(str(BASE_DIR / "log"))
 
    # Carpeta donde están los archivos JSON o datos del sistema
    file_manager = ManagerJson(str(BASE_DIR / "data"), logs_folder)
 
    # Se carga la vista principal del sistema
    app = WelcomeView(file_manager)
 
    # Se ejecuta la aplicación
    app.mainloop()