__author__ = 'jakesawyer'

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import edmunds_selenium_driver as driver
import csv
import xml.etree.cElementTree as ET

drv = driver.DRIVER
meta_titles = {"Discussion_Title", "Started_By", "Tags"}
post_titles = {"Author", "Date", "Post"}

def get_meta_discussion_title():
  print("Getting discussion title")
  return drv.find_element_by_xpath("//div[@class='PageTitle']/h1")

def get_meta_author():
  print("Getting Author")
  return drv.find_element_by_xpath("//span[@class='Author']/a[@class='Username']")

def get_meta_tags():
  print ("Getting tags")
  return drv.find_elements_by_xpath("//div[@class='InlineTags Meta']/ul/li/a")

def get_post_authors():
  print ("Getting post authors")
  return drv.find_elements_by_xpath("//a[@class='Username']")

def get_post_dates():
  print ("Getting post dates")
  return drv.find_elements_by_xpath("//span[@class='MItem DateCreated']/a/time")

def get_post_body():
  print ("Getting post body")
  return drv.find_elements_by_xpath("//div[@class='Item-Body']/div[@class='Message']")

def make_export_list(discussion_title):
  #meta_title = get_meta_discussion_title()
  meta_author = get_meta_author()
  meta_tags = get_meta_tags()
  post_authors = get_post_authors()
  post_dates = get_post_dates()
  post_body = get_post_body()
  export_list = []
  meta_list = []
  post_list = []
  tags_list = []
  print("Post Title: " + discussion_title + "\nAuthor: " + meta_author.text)
  meta_list.append([discussion_title, meta_author.text])
  for i in range(len(meta_tags)):
    print("\nTags:", meta_tags[i].text)
    tags_list.append([meta_tags[i].text])
  #print("author: " + str(len(post_authors)), "\ndate: " + str(len(post_dates)), "\nPost: " + str(len(post_body)))
  for j in range(len(post_authors)):
    print("\nAuthor:", post_authors[j].text, "\nDate:", post_dates[j].get_attribute("title"), "\nPost Body:", post_body[j].text)
    post_list.append([post_authors[j].text, post_dates[j].get_attribute("title"), post_body[j].text])
    print("")
  go_to_later_pages(discussion_title)
  export_list.append([meta_list, tags_list, post_list])
  create_xml_file(discussion_title, export_list)

def go_to_later_pages(make=""):
  try:
    while drv.find_element_by_xpath("//div[@id='PagerAfter']/a[@ref = 'next']").is_displayed():
      print("'Next' button displayed")
      elem = drv.find_element_by_xpath("//div[@id='PagerAfter']/a[@ref = 'next']")
      elem.click()
      make_export_list(make+"2")
      #csv_appender(ex_list, "%s.csv" % (make))
      page_num = page_num + 1
  except:
    print("End of new pages")

def create_xml_file(name, results):
  thread = ET.Element("thread")

  meta = ET.SubElement(thread, "meta")
  title = ET.SubElement(meta, "title")
  title.text = "%s" % str(results[0][0][0][0])
  author = ET.SubElement(meta, "author")
  author.text = "%s" % str(results[0][0][0][1])

  tags = ET.SubElement(thread, "tags")
  for i in results[0][1]:
    ET.SubElement(tags, "tag",{'text':str(i[0])})

  posts = ET.SubElement(thread, "posts")
  for i in results[0][2]:
    ET.SubElement(posts, "post_author", {'author':i[0], 'date':i[1], 'body':i[2]})

  tree = ET.ElementTree(thread)
  tree.write("data/%s.xml" % name)


#get datetime along with <time> title