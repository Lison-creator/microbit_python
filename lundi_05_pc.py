import serial
import requests


port = "COM7"
conn = serial.Serial(port,115200)


message = input("Message: ")
print(message)


while True:
    conn.write(message.encode())






#récpérer un msg et l'envoyer via le port usb sur microbit
#microbit scroll du message

