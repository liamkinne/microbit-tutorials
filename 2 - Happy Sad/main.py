# Remember we will always need this at the start of every file
from microbit import *

# While loops are a way of repeating code while a condition is met. True is always True so this code will loop forever.

# Notice that the code we want to loop is indented. This indentation is how python knows what we want in the while loop.

while True:
	display.show(Image.HAPPY) # show a happy image on the display
	sleep(1000) # wait for a second
	display.show(Image.SAD) # show a sad image on the display
	sleep(1000) # wait for a second

# When we use 'Image.HAPPY' or 'Image.SAD' we are using a pre-defined image thats part of the microbit Image module.
