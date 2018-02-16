from microbit import *

# Again we use a while loop to have our code run continuosly. You're going to use these a lot.

# An if statement will run a bit of code if a condition is met. We can also have an optional thing called an else statement which will run if the abouve if statement does not meet is condition.

while True: 
	if button_a.is_pressed():
		display.show(Image.HAPPY)
	else:
		display.show(Image.SAD)

# button_a is another microbit module that we can use. The function is_pressed() will return True if the button is down or False if the button is up. We can also use was_pressed() to figure out if the button has just been pressed. Why don't you try was_pressed() and see what happens?
