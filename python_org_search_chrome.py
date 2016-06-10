import time
from selenium import webdriver, common
OKGREEN = '\033[92m'
FAIL = '\033[91m'
ENDC = '\033[0m'



print "Grabbing the Chrome webdriver"
driver = webdriver.Chrome('./chromedriver')  # Optional argument, if not specified will search path.
driver.set_window_size(920,1020)
time.sleep(3)
print OKGREEN, "driver.get('http://www.google.com/xhtml')"
driver.get('http://www.google.com/xhtml')
time.sleep(1) # Let the user actually see something!
print "search_box = driver.find_element_by_name('q')"
search_box = driver.find_element_by_name('q')
print "search_box.send_keys('ChromeDriver')"
search_box.send_keys('do a barrel roll')
time.sleep(2)
print "search_box.submit()"
search_box.submit()
time.sleep(5) # Let the user actually see something!

driver.get('http://www.google.com/xhtml')
search_box = driver.find_element_by_name('q')
search_box.send_keys('zerg rush')
search_box.submit()
time.sleep(150)

print "driver.quit()", ENDC
driver.quit()
