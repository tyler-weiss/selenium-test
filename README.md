# README #


# Description #
Jumping into Selenium

### How do I get set up? ###
Well this runs on python so, let's first make sure you have a python package manager (pip)

'sudo easy_install pip'  or if you have HomeBrew 'brew install python'

![install pip](https://i.stack.imgur.com/TaAFP.gif)

Sweet! Now you have pip installed.

I usually do a virtualenv with projects (option)
http://virtualenvwrapper.readthedocs.io/en/latest/install.html#basic-installation
```
pip install virtualenvwrapper
```
look through this http://virtualenvwrapper.readthedocs.io/en/latest/install.html#basic-installation
```
mkvirtualenv VMforTestingSelenium
workon VMforTestingSelenium
```
now run
```
pip install -r requirements.txt
```
You now have everything that was listed in the requirements.txt file. (which in this case is only python's selenium package and dependencies)

Okay let's make sure we have a driver that selenium can use
https://sites.google.com/a/chromium.org/chromedriver/downloads
https://chromedriver.storage.googleapis.com/2.30/chromedriver_mac64.zip


Okay let's test this puppy!

```
python python_org_search_chrome.py
```
