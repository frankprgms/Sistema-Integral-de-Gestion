# Importación de la clase base para la gestión de servicios de usuario
from services.base_user_service import Service 

# Definición del servicio especializado en el alquiler de equipos
class EquipmentRentalService(Service):
    def __init__(self, service_id, service_name, base_fee, quantity, status, 
                 equipment_id, category, physical_condition, is_available, daily_rate):
        
        # Inicialización de clase base
        super().__init__(service_name, service_id, None, base_fee)
        
        # Atributos protegidos (encapsulamiento)
        self._quantity = quantity
        self._service_name = service_name
        self._status = status
        self._equipment_id = equipment_id
        self._category = category
        self._physical_condition = physical_condition
        self._is_available = is_available
        self._daily_rate = daily_rate
        
    # --- Propiedad: name ---
    @property
    def service_name(self):
        return self._service_name

    @service_name.setter
    def service_name(self, value):
        self._service_name = value


    # --- Propiedad: quantity (Días de renta) ---
    @property
    def quantity(self):
        return self._quantity

    @quantity.setter
    def quantity(self, value):
        if value <= 0:
            raise ValueError("La cantidad de días de renta debe ser mayor a cero.")
        self._quantity = value

    # --- Propiedad: status ---
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value

    # --- Propiedad: equipment_id ---
    @property
    def equipment_id(self):
        return self._equipment_id

    @equipment_id.setter
    def equipment_id(self, value):
        self._equipment_id = value

    # --- Propiedad: category ---
    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, value):
        self._category = value

    # --- Propiedad: physical_condition ---
    @property
    def physical_condition(self):
        return self._physical_condition

    @physical_condition.setter
    def physical_condition(self, value):
        self._physical_condition = value

    # --- Propiedad: is_available ---
    @property
    def is_available(self):
        return self._is_available

    @is_available.setter
    def is_available(self, value):
        if not isinstance(value, bool):
            raise TypeError("La disponibilidad debe ser un valor booleano.")
        self._is_available = value

    # --- Propiedad: daily_rate ---
    @property
    def daily_rate(self):
        return self._daily_rate

    @daily_rate.setter
    def daily_rate(self, value):
        if value < 0:
            raise ValueError("La tarifa diaria no puede ser negativa.")
        self._daily_rate = value

    # --- Métodos de lógica ---
    def calculate_total_cost(self):
        # Utiliza las propiedades para el cálculo
        return self.base_fee + (self.daily_rate * self.quantity)

    def describe_service(self):
        return {
            "Service": self.service_name,
            "Equipment_ID": self.equipment_id,
            "Category": self.category,
            "Condition": self.physical_condition,
            "Days": self.quantity,
            "Total": self.calculate_total_cost()
        }

    def validate_parameters(self):
        if not self.is_available or self.physical_condition != "Operativo":
            return False
        
        if self.quantity <= 0 or self.daily_rate < 0:
            return False
            
        return True