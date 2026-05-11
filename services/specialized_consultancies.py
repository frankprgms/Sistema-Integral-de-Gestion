# Importación de la clase base para la gestión de servicios de usuario
from services.base_user_service import Service 


class Specialized_Consultancies(Service):
    def __init__(self,service_id,client,base_fee,equipment_name,rental_days):

        # Inicialización de la clase base con los datos generales del servicio
        super().__init__(service_name="Specialized Consultancies",service_id=service_id,client=client,base_fee=base_fee)

        # Definición de propiedades específicas: nombre del equipo y duración del alquiler en días
        self.equipment_name = equipment_name
        self.rental_days = rental_days




