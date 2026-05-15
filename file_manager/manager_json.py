from file_manager.LogHandler import LogHandler
import json
import os

class ManagerJson:
    def __init__(self, folder,logs_folder):
        # Atributo privado para proteger la ruta base de datos
        self.__folder = folder
        self.__logs_folder = logs_folder
        # Garantiza la existencia del directorio de persistencia desde la instanciación
        os.makedirs(self.__folder, exist_ok=True)

    def __get_path(self, file_name):
        """ Método privado para centralizar la construcción de rutas de archivos """
        return os.path.join(self.__folder, f"{file_name}.json")

    def save(self, file_name, data):
        """ 
        Serializa un objeto de Python a un archivo JSON físico.
        Utiliza codificación UTF-8 para evitar problemas con caracteres especiales.
        """
        path = self.__get_path(file_name)
        try:
            with open(path, 'w', encoding='utf-8') as f:
                # indent=4: Genera un archivo legible para auditoría manual
                # ensure_ascii=False: Permite el guardado nativo de tildes y eñes
                json.dump(data, f, indent=4, ensure_ascii=False)
            return True
        except Exception as e:
            error=(f"CRITICAL ERROR [Save]: No se pudo escribir {file_name}. Detalle: {e}")
            self.logs_folder.save(error,error)
            return False

    def update_data(self, file_name, section, key, value):
        """
        Realiza una actualización granular dentro de una sección específica del JSON.
        Carga el estado actual, modifica la clave solicitada y vuelve a persistir.
        """
        current_data = self.load(file_name, default={})
        
        # Validación y creación de la sección si no existe en el esquema actual
        if section not in current_data:
            current_data[section] = {}
            
        current_data[section][key] = value
        
        # Persistencia de la modificación
        return self.save(file_name, current_data)

    def update(self, file_name, new_data):
        """
        Realiza una fusión (merge) masiva de datos.
        Soporta diccionarios (update) y listas (extend), manteniendo la coherencia del tipo.
        """
        current_data = self.load(file_name, default={})
        
        if isinstance(current_data, dict) and isinstance(new_data, dict):
            current_data.update(new_data)
        elif isinstance(current_data, list) and isinstance(new_data, list):
            current_data.extend(new_data)
        else:
            error=("ERROR: Los tipos de datos no coinciden para fusionar.")
            self.__logs_folder.save("error",error)
            return False
            
        return self.save(file_name, current_data)

    def load(self, file_name, default=None):
        """
        Deserializa un archivo JSON. 
        Si el archivo no existe o está corrupto, retorna el valor por defecto
        para evitar rupturas en el flujo de la aplicación.
        """
        path = self.__get_path(file_name)
        
        # Verificación de existencia previa a la lectura
        if not os.path.exists(path):
            error=(f"WARNING: Archivo {file_name}.json no encontrado. Usando default.")
            self.__logs_folder.save("error",error)
            return default
            
        try:
            with open(path, 'r', encoding='utf-8') as f:
                return json.load(f)
        except json.JSONDecodeError:
            # Captura errores de sintaxis en el archivo JSON
            error=(f"CRITICAL ERROR [Load]: Archivo {file_name}.json corrupto.")
            self.__logs_folder.save("error",error)
            return default