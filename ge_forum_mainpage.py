__author__ = 'jakesawyer'

from selenium.webdriver.common.action_chains import ActionChains
import edmunds_selenium_driver as driver

drv = driver.DRIVER
act = driver.ACTIONS

def open_site():
  """
  Opens http://forums.edmunds.com/
  :return: None
  """
  drv.get("http://forums.edmunds.com/")
  print("Web page opened")

def select_make(str_make):
  """
  Takes in a string parameter, the name of the make fo the car and selects that from the Make menu on the web page
  :param str_make: The make of the car

  OPTIONS:

  acura
  alfa-romeo
  am-general
  aston-martin
  audi
  bentley
  bmw
  bugatti
  buick
  cadillac
  chevrolet
  chrysler
  daewoo
  dodge
  eagle
  ferrari
  fiat
  fisker
  ford
  geo
  gmc
  honda
  hummer
  hyundai
  infiniti
  isuzu
  jaguar
  jeep
  kia
  lamborghini
  land-rover
  lexus
  lincoln
  lotus
  maserati
  maybach
  mazda
  mclaren
  mercedes-benz
  mercury
  mini
  mitsubishi
  nissan
  oldsmobile
  panoz
  plymouth
  pontiac
  porsche
  ram
  rolls-royce
  saab
  saturn
  scion
  smart
  spyker
  subaru
  suzuki
  tesla
  toyota
  volkswagen
  volvo

  :return:
  """
  drv.find_element_by_xpath("//select[@id='Form_make']/option[@value='%s']" % str_make).click()
  print("Make selected")

def select_model(str_model):
  """
  TODO: Make models selectable based on the Make
  :param str_model:
  :return:
  """

def select_topic(str_topic):
  """
  Takes in a string parameter, the name of the topic
  :param str_topic: name of the topic

  OPTIONS:

  buying-selling
  classic-cars
  features-accessories
  fuel-types
  hybrids-evs
  insurance
  news-events
  repairs-maintenance
  safety
  tuning-modification
  using-forums
  warranty
  general
  """
  drv.find_element_by_xpath("//select[@id='TopicSearch']/option[@value='%s']" % (str_topic)).click()
  print("Topic selected")

def select_subtopic(str_subtopic):
  """
  TODO: Make subtopic selectable based on topic
  :param str_subtopic:
  :return:
  """

def click_cars_go():
  """
  Clicks on the GO button to continue to the selected forums based on make and model
  :return:
  """
  drv.find_element_by_xpath("//input[@id='Form_Go_Cars']").click()
  print("Cars go clicked")


def click_topics_go():
  """
  Clicks on the GO button to continue to the selected forums based on topic and subtopic
  :return:
  """
  drv.find_element_by_xpath("//input[@id='Form_Go_Topics']").click()
  print("Topics go clicked")

def close():
  drv.close()
  print("Driver closed")

def back():
  drv.back()
  print("Went back a page")