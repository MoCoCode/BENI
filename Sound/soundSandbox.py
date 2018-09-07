# Sandbox for testing pwm audio

#import time.sleep function
from __future__ import division
import time

#import servo module
import Adafruit_PCA9685

# Uncomment to enable debug output.
#import logging
#logging.basicConfig(level=logging.DEBUG)

# Initialise the PCA9685 using the default address (0x40).
pwm = Adafruit_PCA9685.PCA9685()

# Set frequency (between 40 and 1000 Hz)
pwm.set_pwm_freq(250)

# Define channels
speaker = 15

# Turns off speaker pin
def stop():
        pwm.set_pwm(speaker, 0, 4096)

# Plays sound for 0.01 or more seconds at a given pulse width
# Set third variable to 'hold' to hold tone indefinitely 
def note(seconds, width, hold=stop):
	pwm.set_pwm(speaker, 0, width)
	time.sleep(seconds)
	if hold == stop:
		stop()

# Define various vocalizations
def chirp():
	note(0.05, 450)

def doubleChirp():
	note(0.08, 3930)
	time.sleep(0.02)
	note(0.06, 700)

def happyChirp():
	note(0.1, 700)
	time.sleep(0.04)
	note(0.05, 3400)
	time.sleep(0.06)
	note(0.18, 500)

def grumble():
	note(0.07, 400)
	note(0.07, 600)
	note(0.09, 350)
	note(0.06, 200)
	note(0.07, 1000)

# Execute

grumble()
time.sleep(1)

doubleChirp()
time.sleep(1)

happyChirp()

# Turn off pin
pwm.set_pwm(speaker, 0, 4096)
