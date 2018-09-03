# Sandbox for testing servos

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

# Helper function to make setting a servo pulse width simpler.
def set_servo_pulse(channel, pulse):
    pulse_length = 1000000    # 1,000,000 us per second
    pulse_length //= 60       # 60 Hz
    print('{0}us per period'.format(pulse_length))
    pulse_length //= 4096     # 12 bits of resolution
    print('{0}us per bit'.format(pulse_length))
    pulse *= 1000
    pulse //= pulse_length
    pwm.set_pwm(channel, 0, pulse)

# Set frequency
pwm.set_pwm_freq(60)

# Define channel names
LFU = 0
LFL = 1

# Define pulse lengths
servo_min = 150
servo_mid = 375
servo_max = 600

servo_0 = 150
servo_30 = 225
servo_60 = 300
servo_90 = 375
servo_120 = 450
servo_150 = 525
servo_180 = 600

# Move to min then stepwise to max
pwm.set_pwm(LFL, 0, servo_0)
time.sleep(1)
pwm.set_pwm(LFL, 0, servo_30)
time.sleep(1)
pwm.set_pwm(LFL, 0, servo_60)
time.sleep(1)
pwm.set_pwm(LFL, 0, servo_90)
time.sleep(1)
pwm.set_pwm(LFL, 0, servo_120)
time.sleep(1)
pwm.set_pwm(LFL, 0, servo_150)
time.sleep(1)
pwm.set_pwm(LFL, 0, servo_180)
time.sleep(1)

#move back to mid
pwm.set_pwm(LFL, 0, servo_mid)
