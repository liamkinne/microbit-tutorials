from microbit import *
# we're also going to import pythons random number generator
import random

# This creates a list storing all of the answers
answers = [
	"Yes",
	"It is decidedly so",
	"Without a doubt",
	"Outlook good",
	"Better not tell you now",
	"Ask again later",
	"Don't count on it",
	"Outlook not so good",
]

while True:
	if accelerometer.was_gesture("shake"):
		answer = random.choice(answers) # pick a random answer from the list
		display.scroll(answer, wait=True)
	else:
		# Image.TARGET sort of looks like a ball.
		display.show(Image.TARGET)
