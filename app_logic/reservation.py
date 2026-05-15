"""
Una clase Reserva que integre cliente, servicio, duración y estado,
e implemente confirmación, cancelación y procesamiento con
manejo de excepciones
"""
class Reservation:
    def __init__(self, reservation_id, customer_id, main_event_date, payment_method, logs_folder):
        self.reservation_id = reservation_id
        self.customer_id = customer_id
        self.main_event_date = main_event_date
        self.payment_method = payment_method
        
        # Atributo privado para el manejo de logs
        self.__logs_folder = logs_folder
        
        self.services_list = []
        self.global_status = "Pending"
        self.total_amount = 0.0

    def add_service(self, service_instance):
        try:
            if service_instance.validate_parameters():
                self.services_list.append(service_instance)
                self.calculate_grand_total()
                return True
            else:
                error = f"ERROR [Validation]: Parametros invalidos en {service_instance.service_name} (ID: {service_instance.service_id})"
                self.__logs_folder.save(error, error)
                return False
        except Exception as e:
            error = f"CRITICAL ERROR [AddService]: No se pudo agregar el servicio. Detalle: {e}"
            self.__logs_folder.save(error, error)
            return False

    def confirm_reservation(self):
        try:
            if not self.services_list:
                raise ValueError("No se puede confirmar una reserva sin servicios.")
            
            self.global_status = "Confirmed"
            # Lógica para cambiar estado a todos los servicios internos
            for service in self.services_list:
                service.change_status("Confirmed")
            return True
        except Exception as e:
            error = f"CRITICAL ERROR [Confirm]: Fallo al confirmar reserva {self.reservation_id}. Detalle: {e}"
            self.__logs_folder.save(error, error)
            return False

    def cancel_reservation(self):
        try:
            self.global_status = "Cancelled"
            for service in self.services_list:
                service.change_status("Cancelled")
            return True
        except Exception as e:
            error = f"CRITICAL ERROR [Cancel]: Fallo al cancelar reserva {self.reservation_id}. Detalle: {e}"
            self.__logs_folder.save(error, error)
            return False

    def process_payment(self):
        try:
            if self.total_amount <= 0:
                raise ArithmeticError("El monto total debe ser mayor a cero para procesar pago.")
            
            self.global_status = "Paid"
            return True
        except Exception as e:
            error = f"CRITICAL ERROR [Payment]: Error en procesamiento de pago {self.reservation_id}. Detalle: {e}"
            self.__logs_folder.save(error, error)
            return False

    def calculate_grand_total(self):
        try:
            self.total_amount = sum(s.calculate_total_cost() for s in self.services_list)
            return self.total_amount
        except Exception as e:
            error = f"CRITICAL ERROR [TotalCalculation]: Fallo en calculo de montos. Detalle: {e}"
            self.__logs_folder.save(error, error)
            return 0.0
