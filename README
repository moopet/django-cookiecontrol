Django-cookiecontrol
====================

A Django pluggable to provide CookieControl support

Cookie Control is a mechanism for obtaining a user's explicit consent for the use of cookies on their computer.

It was created by [Civic UK](http://civicuk.com/ "Civic UK") because recent legislation requires websites to obtain explicit consent before leaving behind or reading files (mostly cookies) on user's computers.

To find out more about Cookie Control please visit [Civic's Cookie Control home page](http://civicuk.com/cookie-law/index "Civic's Cookie Control home page").

The functions you're most likely to want to call are

    CookieControl.cookieLawApplies()
    CookieControl.consented()

This app doesn't currently allow you to use the CookieControl callbacks directly,
since that would end up tangling up too much JavaScript, but you can wrap things
with those methods instead.


Installation
------------

    Go to http://civicuk.com/cookie-law/cookie_configuration_v5 to customise and download the latest version of Cookie Control.
    Put the javascript file in /cookiecontrol/static/cookiecontrol/js/cookieControl.js
    It's not included with this distribution due to having a conflicting license, and you probably want the latest version anyway, right?

Usage
-----

    {% load cookiecontrol %}
    {% cookiecontrol %}


Required Settings
-----------------

COOKIECONTROL_PRIVACY_URL - URL for your site's privacy policy
COOKIECONTROL_COUNTRIES - a country like 'United Kingdom' or a list of
countries (see official documentation)

Optional Settings
-----------------

COOKIECONTROL_SHAPE - 'triangle' or 'diamond' (defaults to triangle)
COOKIECONTROL_POSITION - 'left' or 'right' (defaults to left)
COOKIECONTROL_HIDE - boolean (defaults to False)
COOKIECONTROL_HIDE_AFTER- time until widget disappears (seconds, defaults to 30)
COOKIECONTROL_START_OPEN - boolean (defaults to False)

If COOKIECONTROL_HIDE is set to True, then the widget will not appear anymore after the
user has consented.
