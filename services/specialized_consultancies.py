# Importación de la clase base para la gestión de servicios de usuario
from services.base_user_service import Service 


class SpecializedConsultanciesService(Service):
    def __init__(self, service_id, service_name, base_fee, duration, status, 
                specialist_id, category, level_multiplier, availability, modality):
        
        # Inicialización de todos los parámetros de la clase base Service
        super().__init__(service_name, service_id, None, base_fee)
        self.duration = duration
        self.status = status
        
        # Parámetros específicos de consultoría especializada
        self.specialist_id = specialist_id
        self._service_name = service_name
        self.category = category
        self.level_multiplier = level_multiplier
        self.availability = availability
        self.modality = modality

    def calculate_total_cost(self):
        # Multiplica tarifa por horas/cantidad y aplica el multiplicador de nivel
        return (self.base_fee * self.duration) * self.level_multiplier

    def describe_service(self):
        return {
            "Service": self.service_name,
            "Specialist_ID": self.specialist_id,
            "Category": self.category,
            "Date": self.availability,
            "Mode": self.modality,
            "Status": self.status,
            "Total": self.calculate_total_cost()
        }

    def validate_parameters(self):
        # Valida que los multiplicadores y cantidades sean lógicos
        if self.duration <= 0 or self.level_multiplier <= 0:
            return False
        
        if not self.specialist_id or not self.scheduled_datetime:
            return False
            
        return True

    
    # --- Propiedad: name ---
    @property
    def service_name(self):
        return self._service_name

    @service_name.setter
    def service_name(self, value):
        self._service_name = value


    # --- Propiedad: duration ---
    @property
    def duration(self):
        return self._duration

    @duration.setter
    def duration(self, value):
        if value <= 0:
            raise ValueError("La duración debe ser mayor a cero.")
        self._duration = value

    # --- Propiedad: status ---
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value

    # --- Propiedad: specialist_id ---
    @property
    def specialist_id(self):
        return self._specialist_id

    @specialist_id.setter
    def specialist_id(self, value):
        self._specialist_id = value

    # --- Propiedad: category ---
    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, value):
        self._category = value

    # --- Propiedad: level_multiplier ---
    @property
    def level_multiplier(self):
        return self._level_multiplier

    @level_multiplier.setter
    def level_multiplier(self, value):
        
        self._level_multiplier = value

    # --- Propiedad: availability ---
    @property
    def availability(self):
        return self._availability

    @availability.setter
    def availability(self, value):
        self._availability = value

    # --- Propiedad: modality ---
    @property
    def modality(self):
        return self._modality

    @modality.setter
    def modality(self, value):
        self._modality = value




