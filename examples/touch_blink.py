import mraa
import time
print(mraa.getVersion())

led = mraa.Gpio(31)
led.dir(mraa.DIR_OUT)
led.write(0)

time_delay = 3
touch = mraa.Gpio(29)
touch.dir(mraa.DIR_IN)
toggle = False

while True:
    touchButton = int(touch.read())
    if(touchButton == 1):
        print("touch!")
        print("touch   " + str(touchButton) + "  led " + str(led.read()))
        toggle = not toggle
        time.sleep(time_delay)
        if toggle:
            led.write(1)
        else:
            led.write(0)
