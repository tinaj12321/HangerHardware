import mraa
print(mraa.getVersion())

led = mraa.Gpio(31)
led.dir(mraa.DIR_OUT)
led.write(0)

touch = mraa.Gpio(29)
touch.dir(mraa.DIR_IN)

while True:
    touchButton = int(touch.read())
    if(touchButton == 1):
        led.write(1)
    else:
        led.write(0)
    print("touch   " + str(touchButton) + "  led " + str(led.read()))
