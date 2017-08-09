import cookielib
import urllib2

url = 'http://www.baidu.com'

print "First method"
response1 = urllib2.urlopen(url)
print response1.getcode()
print len(response1.read())

print "Secondary method"
req = urllib2.Request(url)
req.add_header('user-agent', 'Mozilla/5.0')
response2 = urllib2.urlopen(req)
print response2.getcode()
print len(response2.read())

print "Third method"
cj = cookielib.CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
urllib2.install_opener(opener)
response3 = urllib2.urlopen(url)
print response3.getcode()
print cj
print response3.read()