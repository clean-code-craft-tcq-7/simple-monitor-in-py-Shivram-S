
from time import sleep
import sys

def isInRange(low,up,quantity):
  if quantity <= up and quantity >= low:
    return True
  return False

def vitals_ok(temperature, pulseRate, spo2):
  if (not isInRange(95,102,temperature)) or (not isInRange(60,100,pulseRate))  or  spo2 < 90:
    print('Vitals critical!')
    for i in range(6):
      print('\r* ', end='')
      sys.stdout.flush()
      sleep(1)
      print('\r *', end='')
      sys.stdout.flush()
      sleep(1)
    return False
  return True
