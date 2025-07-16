
from time import sleep
import sys

def isInRange(low,up,quantity):
  if quantity <= up and quantity >= low:
    return True
  return False

def vitals_ok(temperature, pulseRate, spo2):
  if !(isInRange(95,102,temperature)) or (!isInRange(60,100,pulseRate))  or spo2 < 90:
    print('Vitals critical!')
    return False
  return True
