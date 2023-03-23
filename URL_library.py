# This is a simplified version of the code written in 'basic_web_browser.py'
# 4 lines instead of 11

import urllib.request, urllib.parse, urllib.error

fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
for line in fhand:
    print(line.decode().strip())