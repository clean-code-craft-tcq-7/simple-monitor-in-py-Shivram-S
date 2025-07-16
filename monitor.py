
from time import sleep
import sys

def isNotInRange(low,up,quantity):
  if quantity > up or quantity < low:
    return True
  return False

def vitals_ok(temperature, pulseRate, spo2):
    flag = True
    if isNotInRange(95,102,temperature) or isNotInRange(60,100,pulseRate) or spo2<90:
        print('Temperature critical!')
        flag = False
    return flag
