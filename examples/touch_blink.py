import mraa
import time
print(mraa.getVersion())

green_led = mraa.Gpio(31)
green_led.dir(mraa.DIR_OUT)
green_led.write(0)

yellow_led = mraa.Gpio(33)
yellow_led.dir(mraa.DIR_OUT)
yellow_led.write(0)

led3 = mraa.Gpio(27)
led3.dir(mraa.DIR_OUT)
led3.write(0)

time_delay = 3
touch = mraa.Gpio(29)
touch.dir(mraa.DIR_IN)
toggle = False

while True:
    if(int(touch.read()) == 1):
        print("touch!")
        toggle = not toggle
        was_touched = False
        timeout = time.time() + time_delay
        time.sleep(1)
        if toggle:
            while timeout > time.time():
                if int(touch.read()) == 1:
                    was_touched = True
                    break
            if was_touched:
                toggle = not toggle
                print("reset: clothing used") 
                time.sleep(1)
            elif toggle:
                green_led.write(1)
                print("green")
                timeout = time.time() + time_delay
                time.sleep(1)
                if toggle:
                    while timeout > time.time():
                        if int(touch.read()) == 1:
                            was_touched = True
                            break
                    green_led.write(0)
                    if was_touched:
                        toggle = not toggle
                        print("reset: clothing used") 
                        time.sleep(1)
                    elif toggle: 
                        yellow_led.write(1)
                        print("yellow")
                        timeout = time.time() + time_delay
                        time.sleep(1)
                        if toggle:
                            while timeout > time.time():
                                if int(touch.read()) == 1:
                                    was_touched = True
                                    break
                            yellow_led.write(0)
                            if was_touched:
                                toggle = not toggle
                                print("reset: clothing used")
                                time.sleep(1)
                            elif toggle: 
                                led3.write(1)
                                print("last")
                                #TODO send signal to REST endpoint
        else:
            green_led.write(0)
            yellow_led.write(0)
            led3.write(0)
