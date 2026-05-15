# Importación de la clase base para la gestión de servicios de usuario
from services.base_user_service import Service 

class RoomReservationService(Service):
    def __init__(self, service_id, service_name, base_fee, quantity, status, 
                 room_id, room_type, capacity, hourly_rate, is_available):
        
        # Inicialización de clase base
        super().__init__(service_name, service_id, None, base_fee)
        
        # Atributos protegidos
        self._quantity = quantity
        self._service_name = service_name
        self._status = status
        self._room_id = room_id
        self._room_type = room_type
        self._capacity = capacity
        self._hourly_rate = hourly_rate
        self._is_available = is_available

    # --- Propiedad: quantity (Horas de reserva) ---
    @property
    def quantity(self):
        return self._quantity

    @quantity.setter
    def quantity(self, value):
        if value <= 0:
            raise ValueError("La cantidad de horas debe ser mayor a cero.")
        self._quantity = value

    # --- Propiedad: name ---
    @property
    def service_name(self):
        return self._service_name

    @service_name.setter
    def service_name(self, value):
        self._service_name = value

    # --- Propiedad: status ---
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value

    # --- Propiedad: room_id ---
    @property
    def room_id(self):
        return self._room_id

    @room_id.setter
    def room_id(self, value):
        self._room_id = value

    # --- Propiedad: room_type ---
    @property
    def room_type(self):
        return self._room_type

    @room_type.setter
    def room_type(self, value):
        self._room_type = value

    # --- Propiedad: capacity ---
    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self, value):
        if value <= 0:
            raise ValueError("La capacidad debe ser un número positivo.")
        self._capacity = value

    # --- Propiedad: hourly_rate ---
    @property
    def hourly_rate(self):
        return self._hourly_rate

    @hourly_rate.setter
    def hourly_rate(self, value):
        if value < 0:
            raise ValueError("La tarifa por hora no puede ser negativa.")
        self._hourly_rate = value

    # --- Propiedad: is_available ---
    @property
    def is_available(self):
        return self._is_available

    @is_available.setter
    def is_available(self, value):
        if not isinstance(value, bool):
            raise TypeError("El estado de disponibilidad debe ser un valor booleano.")
        self._is_available = value

    # --- Métodos de lógica ---
    def calculate_total_cost(self):
        return self.base_fee + (self.hourly_rate * self.quantity)

    def describe_service(self):
        return {
            "Service": self.service_name,
            "Room_ID": self.room_id,
            "Type": self.room_type,
            "Capacity": self.capacity,
            "Hours": self.quantity,
            "Status": self.status,
            "Total": self.calculate_total_cost()
        }

    def validate_parameters(self):
        if not self.is_available:
            return False
        
        if self.quantity <= 0 or self.hourly_rate <= 0:
            return False
            
        return True