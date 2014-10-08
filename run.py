import ge_forum_mainpage as SelD
import ge_forum_thread_level as SelM
import ge_forum_post_level as SelP
import edmunds_selenium_driver as driver
import time
import traceback
import os.path

def main():
  driver.screen_start()
  print("Starting process, current local time ->",time.localtime())
  SelD.open_site()
  for make in driver.MAKES:
    SelD.select_make(make)
    SelD.click_cars_go()
    dtitles = SelM.get_discussion_titles()
    titles = []
    for title in dtitles:
      titles.append(title.text)
    for i in range(len(dtitles)):
      driver.random_timeout()
      try:
        dtitles = SelM.get_discussion_titles()
        print ("\n\n",i,"\n\n")
        dtitles[i].click()
        SelP.make_export_list(titles[i])
        SelD.drv.back()
      except:
        if os.path.isfile("log.txt"):
          f = open("log.txt", "a")
          e = "\nERROR AT %s\nERROR: %s" % (titles[i], traceback.print_exc())
          print(e)
          f.write(e)
          f.close()
        else:
          f = open("log.txt", "w")
          e = "\nERROR AT %s\nERROR: %s" % (titles[i], traceback.print_exc())
          print(e)
          f.write(e)
          f.close()
    #SelM.csv_writer(ex_list, "data/%s.csv" % (make))
    #SelM.go_to_later_pages(make)
    #SelD.drv.get("http://forums.edmunds.com")
  print("\n\nFinished TOPICS\n\n")
  SelD.close()
  driver.screen_stop()
  print("Process finished, current local time ->", time.localtime())

if __name__ == "__main__":
  main()