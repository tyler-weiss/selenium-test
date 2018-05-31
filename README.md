
# Description #
Jumping into Selenium

### How do I get set up? ###
Well this runs on python so, let's first make sure you have a **python package manager (pip)**

'sudo easy_install pip'  or if you have HomeBrew 'brew install python'

![install pip](https://i.stack.imgur.com/TaAFP.gif)

Sweet! Now you have pip installed.

(**begin optional virtual machine stuff**)

Usually you would want to run with virtualenv for projects. It creates a shim for packages and executables so that version don't interfere with other projects.  
http://virtualenvwrapper.readthedocs.io/en/latest/install.html#basic-installation
```
pip install virtualenvwrapper
```
look through this http://virtualenvwrapper.readthedocs.io/en/latest/install.html#basic-installation
```
mkvirtualenv VMforTestingSelenium
workon VMforTestingSelenium
```

(**end optional virtual machine stuff**)

now run
```
pip install -r requirements.txt
```
You now have everything that was listed in the requirements.txt file. (which in this case is only python's selenium package and dependencies)

Okay let's make sure we have a **driver that selenium can use to control a browser**
https://sites.google.com/a/chromium.org/chromedriver/downloads  <-- look here
https://chromedriver.storage.googleapis.com/2.30/chromedriver_mac64.zip (latest I grabbed and is included in this directory, if you need to grab another make sure it is moved in this directory and called correctly (path) in the python file you run.

Okay let's test this puppy!

```
python python_org_search_chrome.py
```
It did a thing!

 - "Great! Look at the file you just ran and now you can start writing a test script."

It didn't do the thing!

 - " ¯\\_(ツ)_/¯, message me and I'll see if I can help."
