import mraa
import time
print(mraa.getVersion())

green_led = mraa.Gpio(31)
green_led.dir(mraa.DIR_OUT)
green_led.write(0)

yellow_led = mraa.Gpio(33)
yellow_led.dir(mraa.DIR_OUT)
yellow_led.write(0)

led3 = mraa.Gpio(34)
led3.dir(mraa.DIR_OUT)
led3.write(0)

time_delay = 3
touch = mraa.Gpio(29)
touch.dir(mraa.DIR_IN)
toggle = False

while True:
    touchButton = int(touch.read())
    if(touchButton == 1):
        print("touch!")
        toggle = not toggle
        if toggle:
            time.sleep(time_delay)
            green_led.write(1)
            print("green")
            time.sleep(time_delay)
            green_led.write(0)
            yellow_led.write(1)
            print("yellow")
            time.sleep(time_delay)
            yellow_led.write(0)
            led3.write(1)
            print("last")
            #TODO send signal to REST endpoint
        else:
            time.sleep(time_delay)
            green_led.write(0)
            yellow_led.write(0)
            led3.write(0)
