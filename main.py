from file_manager.LogHandler import LogHandler


logs_folder= LogHandler("log")
print ("hola mundo")

logs_folder.save("error","prueba error01")

errors=logs_folder.read("error")


print(errors2)

