"""
Una clase Reserva que integre cliente, servicio, duración y estado,
e implemente confirmación, cancelación y procesamiento con
manejo de excepciones
"""

class Reservation:
    def __init__(self,language,  customer, service, duration=0):
        # Inicialización de atributos privados
        self._customer = customer
        self._language = language
        
        self._service = service
        self._duration = duration
        self._status = "Pending"  # Estado inicial por defecto


    def confirmation(self):
        """Confirma la reserva si el estado actual lo permite."""
        pass

    def cancellation(self):
        """Cancela la reserva y reinicia la duración."""
        pass

    def processing(self, data_reservation):
        """Procesa la reserva con nuevos datos, validando la entrada."""
        pass


    # --- Getters (Propiedades) ---

    @property
    def customer(self):
        return self._customer

    @property
    def service(self):
        return self._service

    @property
    def duration(self):
        return self._duration

    @property
    def status(self):
        return self._status

    # --- Setters ---

    @customer.setter
    def customer(self, value):
        if not value:
            raise ValueError(self._language["errors"]["err_customer_empty"])
        self._customer = value

    @service.setter
    def service(self, value):
        if not value:
            raise ValueError(self._language["errors"]["err_service_empty"])
        self._service = value

    @duration.setter
    def duration(self, value):
        if not isinstance(value, (int, float)) or value < 0:
            raise ValueError(self._language["errors"]["err_duration_invalid"])
        self._duration = value

    @status.setter
    def status(self, value):
        estados_validos = ["Pending", "Confirmed", "Cancelled", "Processing"]
        if value not in estados_validos:
            raise ValueError(f"{self._language['errors']['err_status_invalid']} {estados_validos}")
        self._status = value






