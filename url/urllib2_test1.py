import urllib2
response = urllib2.urlopen('http://www.ifeng.com/')
html = response.read()

print html
