from abc import ABC, abstractmethod

# Clase Abstracta Base
class Service(ABC):
    """
    Clase abstracta que define todos los servicios del sistema.
    """
    def __init__(self, service_name, service_id, client, base_fee):
        # Inicialización de atributos básicos comunes a cualquier servicio
        self.service_name = service_name
        self.service_id = service_id
        self.client = client
        self.base_fee = base_fee
        self.status = "Pending"  # Estado inicial predeterminado

    @abstractmethod
    def calculate_total_cost(self):
        """Calcula el costo final basado en la lógica de cada servicio."""
        pass

    @abstractmethod
    def describe_service(self):
        """Retorna una descripción detallada del servicio."""
        pass

    @abstractmethod
    def validate_parameters(self):
        """Valida que los datos del servicio sean lógicos y seguros."""
        pass

    def change_status(self, new_status):
        """Método concreto para actualizar el estado del servicio."""
        self.status = new_status
        print(f"Estado de {self.service_name} actualizado a: {new_status}")

   

