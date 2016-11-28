Flask Example - MediaCloud Client App
=====================================

Small example Flask applicaton for the MAS.500 course (the beginner homework).
- Forked Rahul's MediaCloud Flask example: https://github.com/rahulbot/MediaCloud-Flask-Example
- Added inputs for picking a start and end date to search within 
  - The default start date is 09/01/2015, the default end date is 04/01/2016
- Changed the example to use the sentenceCount API method with "split" set to true, so it returns counts by week
- Used Highcharts.js to render the weekly results as a line chart


Installation
------------

- Make sure you have Python 2.7 (and the pip package manager).
- I also have Python 3.5 version in the other folder titled "Python35"
  - This homework was originally written in Python 3.5 environment. I changed several syntaxes to adjust it to Python 2.7. Please pardon me if there are still some syntaxes that I failed to fix.

You also need to install some requirements:

```
pip install -r requirements.pip
```

Copy `settings.config.template` to `settings.config` and edit it.

Use
---

Run this command and then visit `localhost:5000` with a web browser

```
python mcserver.py
```

You will be able to monitor progress in the `logs/mcserver.log` log file.

Deploying
---------

First, prep your Ubuntu machine:
```
sudo aptitude install python
sudo aptitude install libapache2-mod-wsgi
sudo pip install -r requirements
```

And make the `logs` folder writable by your web-user (ie. `www-data`).

Now follow the instructions for Configuring Apache:
  http://flask.pocoo.org/docs/deploying/mod_wsgi/

