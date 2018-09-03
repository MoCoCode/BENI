# Walk Forward

from __future__ import division
import time

import Adafruit_PCA9685

# Uncomment to enable debug output.
#import logging
#logging.basicConfig(level=logging.DEBUG)

# Initialise the PCA9685 using the default address (0x40).
pwm = Adafruit_PCA9685.PCA9685()

# Set pwm frequency (between 40 and 1000 Hz, 60 recommended for sevos)
pwm.set_pwm_freq(60)

# Define servo channels by limb segment 
# (left/right, front/back, upper/lower)

LFU = 0
LFl = 1
LBU = 2
LBL = 3
RFU = 4
RFL = 5
RBU = 6
RBL = 7



