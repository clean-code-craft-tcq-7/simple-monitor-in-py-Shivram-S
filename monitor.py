
from time import sleep
import sys

def isNotInRange(low,up,quantity):
  if quantity > up or quantity < low:
    return True
  return False

def vitals_ok(temperature, pulseRate, spo2):
  if isNotInRange(95,102,temperature) or isNotInRange(60,100,pulseRate)  or isNotInRange(90,1000,spo2):
    print('Vitals critical!')
    return False
  return True
