# Blinks the top right RED LED
import board
import digitalio
import analogio
import time

led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT

def main():
    print("hi")
    
    while True:
        led.value = True
        time.sleep(0.2)
        led.value = False
        time.sleep(0.2)
        
main()
