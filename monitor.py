
from time import sleep
import sys


def vitals_ok(temperature, pulseRate, spo2):
  if temperature > 102 or temperature < 95 or pulseRate < 60 or pulseRate > 100 or spo2 < 90:
    print('Vitals critical!')
    return False
  return True
