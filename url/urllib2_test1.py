import urllib

response = urllib.urlopen("http://www.baidu.com/")

html = response.read()
html = html.decode("utf-8")

print html
