# Importación de la clase base para la gestión de servicios de usuario
from services.base_user_service import Service 

# Definición del servicio especializado en el alquiler de equipos, heredando de la clase Service
class EquipmentRentalService(Service):

    def __init__(self,service_id,client,base_fee,equipment_name,rental_days):

        # Inicialización de la clase base con los datos generales del servicio
        super().__init__(service_name="Equipment Rental",service_id=service_id,client=client,base_fee=base_fee)

        # Definición de propiedades específicas: nombre del equipo y duración del alquiler en días
        self.equipment_name = equipment_name
        self.rental_days = rental_days

    def calculate_total_cost(self):

        # Lógica de cálculo financiero que multiplica la tarifa base por los días y añade un seguro fijo
        insurance_fee = 50

        total_cost = (
            self.base_fee * self.rental_days
        ) + insurance_fee

        return total_cost

    def describe_service(self):

        # Generación de una cadena de texto formateada con el resumen detallado de la transacción y el cliente
        return (
            f"\n--- Equipment Rental Service ---\n"
            f"Service ID: {self.service_id}\n"
            f"Client: {self.client}\n"
            f"Equipment: {self.equipment_name}\n"
            f"Rental Days: {self.rental_days}\n"
            f"Base Fee: ${self.base_fee}\n"
            f"Current Status: {self.status}"
        )

    def validate_parameters(self):

        # Reglas de negocio para asegurar que los días, la tarifa y el nombre del equipo sean valores válidos
        if self.rental_days <= 0:
            raise ValueError(
                "Rental days must be greater than 0."
            )

        if self.base_fee < 0:
            raise ValueError(
                "Base fee cannot be negative."
            )

        if self.equipment_name.strip() == "":
            raise ValueError(
                "Equipment name cannot be empty."
            )

        return True