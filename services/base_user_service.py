from abc import ABC, abstractmethod

class Service(ABC):
    """
    Clase abstracta base para la gestión de servicios del sistema.
    Define la interfaz obligatoria y los atributos compartidos.
    """
    def __init__(self, service_id, service_name, base_fee, quantity=1):
        # Identificador único del servicio
        self.service_id = service_id
        
        # Nombre descriptivo 
        self.service_name = service_name
        
        # Tarifa base 
        self.base_fee = base_fee
        
        # Cantidad o duración del servicio
        self.quantity = quantity
        
        # Estado inicial por defecto
        self.status = "Pending"

    @abstractmethod
    def calculate_total_cost(self):
        """
        Debe retornar el costo final del servicio.
        Cada subclase implementará sus propios recargos o descuentos.
        """
        pass

    @abstractmethod
    def describe_service(self):
        """
        Debe retornar una cadena de texto o diccionario con los detalles
        específicos del servicio para mostrar al usuario.
        """
        pass

    @abstractmethod
    def validate_parameters(self):
        """
        Debe verificar que los datos ingresados (cantidad, fechas, etc.) 
        sean válidos antes de procesar el servicio.
        """
        pass

    def change_status(self, new_status):
        """
        Método concreto para actualizar el estado del servicio.
        Común para todas las clases hijas.
        """
        valid_statuses = ["Pending", "Active", "Completed", "Cancelled"]
        
        if new_status in valid_statuses:
            self.status = new_status
            print(f"[{self.service_id}] Estado actualizado a: {self.status}")
        else:
            print(f"Error: El estado '{new_status}' no es válido.")

    def apply_discount(self, percentage):
        """
        Método concreto para reducir la tarifa base según un porcentaje (0-100).
        """
        if 0 <= percentage <= 100:
            reduction = self.base_fee * (percentage / 100)
            self.base_fee -= reduction
            print(f"Descuento del {percentage}% aplicado a {self.service_name}.")
        else:
            print("Error: Porcentaje de descuento inválido.")
   

