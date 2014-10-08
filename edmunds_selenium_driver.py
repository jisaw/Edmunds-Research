__author__ = 'jakesawyer'

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import random
import time

DRIVER = webdriver.Firefox()
ACTIONS = ActionChains(DRIVER)

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
  if r<16 and r>9:
    time.sleep(random.randint(0,30))
    return True
  else:
    return False
