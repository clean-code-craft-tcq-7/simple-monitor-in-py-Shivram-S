
from time import sleep
import sys

def isNotInRange(low,up,quantity):
  if quantity > up or quantity < low:
    return True
  return False

def vitals_ok(temperature, pulseRate, spo2):
  if isNotInRange(95,102,temperature):
    print('Temperature critical!')
    return False
  if isNotInRange(60,100,pulseRate):
    print('Pulse critical!')
    return False
  if spo2<90:
    print('SPO2 critical!')
    return False
  return True
