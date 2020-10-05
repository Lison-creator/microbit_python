
from microbit import *


port = "COM7"


msg = uart.read()

while True:
    msg = uart.read()
    if msg:
        display.scroll(msg)



