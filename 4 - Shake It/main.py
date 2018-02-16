from microbit import *

# On the micro:bit board, it has a build in accelerometer. This can measure acceleration in 3 directions: x, y, z. It can also recognise gestures which is when the acceleration follows a certain pattern.

while True:
	if accelerometer.was_gesture("shake"):
		display.show(Image.HAPPY)
		sleep(1000) # show the happy face for a second
		display.show(Image.SAD) # go back to being sad :(

# The other gestures on the micro:bit are: up, down, left, right, face up, face down, freefall, 3g, 6g and 8g. Give these a try and see how they are triggered.
