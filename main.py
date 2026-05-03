
from file_manager.LogHandler import LogHandler
from file_manager.manager_json import ManagerJson
from ui.welcome_view import WelcomeView
from app_logic.customer import cliente


#cliente1=cliente(customer_id=1,name="frank",document=1010101010,email="email@email.com",phone=1010101010,address="calle 5 a l",state="activo",membership="gold")


""""""
if __name__ == "__main__":
    logs_folder= LogHandler("log")
    file_manager = ManagerJson("data",logs_folder)
    
    app = WelcomeView(file_manager)
    app.mainloop()

