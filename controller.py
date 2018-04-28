from microbit import *
#import radio
#import music
while (True):
    gesture = accelerometer.current_gesture();
    if (gesture == "up"):
        display.show(Image.ARROW_N);
    elif (gesture == "down"):
        display.show(Image.ARROW_S);
    eliqxf (gesture == "left"):
        display.show(Image.ARROW_W);
    elif (gesture == "right"):
        display.show(Image.ARROW_E);
    