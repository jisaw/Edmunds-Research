__author__ = 'jakesawyer'

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import random
import time
from pyvirtualdisplay import Display

DRIVER = webdriver.Firefox()
ACTIONS = ActionChains(DRIVER)
DISPLAY = Display(visible=0, size=(800, 600))


MAKES = ['acura',
  'alfa-romeo',
  'am-general',
  'aston-martin',
  'audi',
  'bentley',
  'bmw',
  'bugatti',
  'buick',
  'cadillac',
  'chevrolet',
  'chrysler',
  'daewoo',
  'dodge',
  'eagle',
  'ferrari',
  'fiat',
  'fisker',
  'ford',
  'geo',
  'gmc',
  'honda',
  'hummer',
  'hyundai',
  'infiniti',
  'isuzu',
  'jaguar',
  'jeep',
  'kia',
  'lamborghini',
  'land-rover',
  'lexus',
  'lincoln',
  'lotus',
  'maserati',
  'maybach',
  'mazda',
  'mclaren',
  'mercedes-benz',
  'mercury',
  'mini',
  'mitsubishi',
  'nissan',
  'oldsmobile',
  'panoz',
  'plymouth',
  'pontiac',
  'porsche',
  'ram',
  'rolls-royce',
  'saab',
  'saturn',
  'scion',
  'smart',
  'spyker',
  'subaru',
  'suzuki',
  'tesla',
  'toyota',
  'volkswagen',
  'volvo']

TOPICS = ['buying-selling',
  'classic-cars',
  'features-accessories',
  'fuel-types',
  'hybrids-evs',
  'insurance',
  'news-events',
  'repairs-maintenance',
  'safety',
  'tuning-modification',
  'using-forums',
  'warranty',
  'general']

class Edmunds_selenium_driver():


  def __init__(self):
    self.d = DRIVER
    self.a = ACTIONS

def random_timeout():
  r = random.randint(0,20)
  if r<20 and r>10:
    print("Sleeping")
    time.sleep(random.randint(0,30))
    return True
  else:
    print("Not Sleeping")
    return False

def screen_start():
  DISPLAY.start()

def screen_stop():
  DISPLAY.stop()