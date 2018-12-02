import mraa
import time
from twilio.rest import Client

account_sid = 'AC52b6653b756bcb8853e3a42773bdf15c'
auth_token = 'b6631ae520bf37f5c02de8c00bf3d8ed'
client = Client(account_sid,auth_token)
twilio_num = '+18454456307'
my_num='+19738309712'

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
        welcomeMessage=client.messages.create(
            to=my_num,
            from_=twilio_num,
            body="Something has been hung up here. We're keeping track of your usage :)"
        )
        toggle = not toggle
        was_touched = False
        timeout = time.time() + time_delay
        time.sleep(5)
        if toggle:
            while timeout > time.time():
                if int(touch.read()) == 1:
                    was_touched = True
                    break
            if was_touched:
                messageReset1 = client.messages.create(
                    to=my_num,
                    from_=twilio_num,
                    body="Clothing taken at " + str(time.ctime(int(time.time())))+". You hung this up recently so you must wear this a lot!")
                print("taken from hanger")
                toggle = not toggle
                time.sleep(5)
            elif toggle:
                messageGreen = client.messages.create(
                    to=my_num,
                    from_=twilio_num,
                    body="It's getting into the first week you've left this in the closet... It's currently "+str(time.ctime(int(time.time())))+". You hung this up recently so you must wear this a lot!") 
                green_led.write(1)
                print("green")
                timeout = time.time() + time_delay
                time.sleep(5)
                if toggle:
                    while timeout > time.time():
                        if int(touch.read()) == 1:
                            was_touched = True
                            break
                    green_led.write(0)
                    if was_touched:

                        print("clothing placed on hanger")
                        toggle = not toggle
                        time.sleep(5)
                    elif toggle:
                        yellowMessage=client.messages.create(
                            to=my_num,
                            from_=twilio_num,
                            body="It's now the second week this item hasn't been used. The light will be yellow up until 5 weeks. date is: "+str(time.ctime(int(time.time()))))

                        yellow_led.write(1)
                        print("yellow")
                        timeout = time.time() + time_delay
                        time.sleep(5)
                        if toggle:
                            while timeout > time.time():
                                if int(touch.read()) == 1:
                                    was_touched = True
                                    break
                            yellow_led.write(0)
                            if was_touched:
                                messageReset3 = client.messages.create(
                                    to=my_num,
                                    from_=twilio_num,
                                    body="You wore it between two and five weeks! It hasn't been ages but still don't let this get to the back of the closet. This was removed at "+str(time.ctime(int(time.time()))))

                                toggle = not toggle

                                time.sleep(5)
                            elif toggle: 
                                led3.write(1)
                                purpleMessage=client.messages.create(
                                        to=my_num,
                                        from_=twilio_num,
                                        body="You haven't worn this in more than a month. I'd suggest you wear this more or donate it."+str(time.ctime(int(time.time()))))
        else:
            finalMessage=client.messages.create(
                to=my_num,
                from_=twilio_num,
                body="After a very long time you're wearing it. hopefully you're either wearing it more or donating it. "
            )
            green_led.write(0)
            yellow_led.write(0)
            led3.write(0)
