from microbit import *
import radio
class Controller:
    def __init__(self):
        radio.on()
        radio.config(channel=10)
        while (True):
            gesture = accelerometer.current_gesture()
            #self.sendRadio(gesture)
            if (gesture == "up"):
                display.show(Image.ARROW_S)
                radio.send('FORWARD')
            elif (gesture == "down"):
                display.show(Image.ARROW_N)
                radio.send('BACKWARD')
            elif (gesture == "left"):
                display.show(Image.ARROW_W)
                radio.send('LEFT')
            elif (gesture == "right"):
                display.show(Image.ARROW_E)
                radio.send('RIGHT')
            else:
                display.show(Image.DIAMOND)
                radio.send('error')
            sleep(20)
    def getRotation(self):
        return accelerometer.get_x(), accelerometer.get_y(), accelerometer.get_z()
c = Controller()