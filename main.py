
from file_manager.LogHandler import LogHandler
from file_manager.manager_json import ManagerJson
from ui.welcome_view import WelcomeView


if __name__ == "__main__":
    logs_folder= LogHandler("log")
    file_manager = ManagerJson("data",logs_folder)
    app = WelcomeView(file_manager)
    app.mainloop()

