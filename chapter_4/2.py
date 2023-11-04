# 2
from http import client
# 3.1
c = client.HTTPConnection('www.google.com')
# 3.2
res = c.request('GET', '/')
# 3.3
res = c.getresponse().read()