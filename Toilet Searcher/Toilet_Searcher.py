#-*- encoding: utf-8 -*-

from urllib.parse import urlparse
import http.client

url="http://openapi.gg.go.kr/Publtolt?KEY=9bee44ffc03b4586a53534934f51af1c&Type=xml&pIndex=1&pSize=50"
parts = urlparse(url)
parts.path

conn = http.client.HTTPConnection("openapi.gg.go.kr")
conn.request("GET", "/Publtolt?KEY=9bee44ffc03b4586a53534934f51af1c&Type=xml&pIndex=1&pSize=50")
req = conn.getresponse()
print(req.status, req.reason)
cLen = req.getheader("Content-Length")
req.read(cLen) 