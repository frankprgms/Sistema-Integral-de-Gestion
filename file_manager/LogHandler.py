import os

class LogHandler:
    def __init__(self, folder):
        self.__folder = folder
        os.makedirs(self.__folder, exist_ok=True)

    def __get_path(self, file_name):
        return os.path.join(self.__folder, f"{file_name}.txt")

    def save(self, file_name, data):
        
        path = self.__get_path(file_name)
        try:
            with open(path,"a", encoding='utf-8') as f:
                f.write(data+"\n")
            return True
        except Exception as e:
            error=(f"CRITICAL ERROR [save]: No se pudo escribir {file_name}. Detalle: {e}\n")

            with open("archivo.txt", "a", encoding="utf-8") as f:
                f.write(error)
            return False
    def read(self,file_name):
        path = self.__get_path(file_name)
        """Lee el archivo de errores y devuelve una lista de strings."""
        if not os.path.exists(path):
            return [] # Retorna lista vacía si aún no hay errores registrados
            
        try:
            with open(path, "r", encoding="utf-8") as f:
                # .read().splitlines() elimina los saltos de línea (\n) automáticamente
                return f.read().splitlines()
        except Exception as e:
            error=f"CRITICAL ERROR [get_errors]:No se pudo leer {e}"
            self.save("error", error)
            return []
    def clear_log(self, file_name):
        """Limpia el contenido de un log sin borrar el archivo."""
        path = self.__get_path(file_name)
        if os.path.exists(path):
            open(path, 'w').close() # Al abrirlo en 'w' y cerrar, se vacía
    def get_log_size(self, file_name):
        """Devuelve el tamanio del archivo en bytes."""
        path = self.__get_path(file_name)
        if os.path.exists(path):
            return os.path.getsize(path)
        return 0
    