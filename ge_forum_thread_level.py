__author__ = 'jakesawyer'


from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import edmunds_selenium_driver as driver
import csv

drv = driver.DRIVER
titles = {"Discussion_Title", "Started_By", "Started_On", "Replies", "Views"}

def get_discussion_titles():
  """
  Gets all the discussion titles on the current page
  :return: A list of selenium elements for each of the discussion topics
  """
  print("Getting discussion titles")
  return (drv.find_elements_by_xpath("//tbody/tr/td[@class='DiscussionName']/div[@class='Wrap']/a"))

def print_discussion_titles():
  """
  Prints all the discussion titles on the current page
  :return:
  """
  elem = get_discussion_titles()
  for i in range(len(elem)):
    print(elem[i].text)

def get_started_by():
  """
  Gets all of the started by usernames on the current page
  :return: A list of selenium elements for each of the started by usernames
  """
  print("Getting the started by username")
  return (drv.find_elements_by_xpath("//tbody/tr/td[@class='BlockColumn BlockColumn-User FirstUser']/div[@class='Block Wrap']/a[@class='UserLink BlockTitle']"))

def print_started_by():
  """
  Prints all of the started by usernames on the current page
  :return:
  """
  elem = get_started_by()
  for i in range(len(elem)):
    print(elem[i].text)

def get_started_on():
  """
  Gets a list of selenium elements with the started on dates for the current page
  :return:
  """
  print("Getting printed on date")
  return (drv.find_elements_by_xpath("//tbody/tr/td[@class='BlockColumn BlockColumn-User FirstUser']/div[@class='Block Wrap']/div[@class='Meta']/a/time"))

def print_started_on():
  elem = get_started_on()
  for i in range(len(elem)):
    print(elem[i].get_attribute("title"))

def get_num_replies():
  """
  Gets a list of selenium elements with the number of replies to each post
  :return:
  """
  print("Geting number of replies")
  return (drv.find_elements_by_xpath("//tbody/tr/td[@class='BigCount CountComments']/div[@class='Wrap']/span"))

def print_num_replies():
  elem = get_num_replies()
  for i in range(len(elem)):
    print(elem[i].text)

def get_num_views():
  """
  Gets a list of selenium elements for the number of views for each post
  :return:
  """
  print("Getting number of views")
  return (drv.find_elements_by_xpath("//tbody/tr/td[@class='BigCount CountViews']/div[@class='Wrap']/span"))

def print_num_views():
  elem = get_num_views()
  for i in range(len(elem)):
    print(elem[i].text)

def make_export_list(p = False):
  """
  Returns a list of lists containing the Discussion title, started by username, started on date, number of replies, and number of views
  :param p: Default = False; If true it will print the returned list to the console
  :return: A list of lists
  """
  print("Creating export list")
  dt = get_discussion_titles()
  sb = get_started_by()
  so = get_started_on()
  nr = get_num_replies()
  nv = get_num_views()
  export_list = []
  for i in range(len(dt)):
    export_list.append([dt[i].text, sb[i].text, so[i].get_attribute("title"), nr[i].text, nv[i].text])
  if p == True:
    for i in range(len(export_list)):
      print(export_list[i])
  return(export_list)

def go_to_later_pages(make):
  page_num = 2
  try:
    while drv.find_element_by_class_name("p-%s" % page_num).is_displayed():
      elem = drv.find_element_by_class_name("p-%s" % page_num)
      elem.click()
      ex_list = make_export_list(True)
      csv_appender(ex_list, "%s.csv" % (make))
      page_num = page_num + 1
  except:
    print("End of new pages")



def csv_writer(data, path):
  print("Writing csv")
  titles = []
  titles.append(["Discussion_Title", "Started_By", "Started_On", "Replies", "Views"])
  with open(path, "w") as csv_file:
    writer = csv.writer(csv_file, delimiter=",")
    for title in titles:
      writer.writerow(title)
    for line in data:
      writer.writerow(line)

def csv_appender(data, path):
  print("Appending csv")
  titles = []
  titles.append(["Discussion_Title", "Started_By", "Started_On", "Replies", "Views"])
  with open(path, "a") as csv_file:
    writer = csv.writer(csv_file, delimiter=",")
    for title in titles:
      writer.writerow(title)
    for line in data:
      writer.writerow(line)