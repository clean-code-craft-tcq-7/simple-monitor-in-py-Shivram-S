
from time import sleep
import sys

def isInRange(low,up,quantity):
  if quantity <= up and quantity >= low:
    return True
  return False

def vitals_ok(temperature, pulseRate, spo2):
  if (isInRange(95,102,temperature)) and (isInRange(60,100,pulseRate))  and (isInRange(90,1000,spo2)):
    print('Vitals critical!')
    return False
  return True
