import http.client
conn = http.client.HTTPConnection("openapi.gg.go.kr")
conn.request("GET", "/Publtolt?KEY=9bee44ffc03b4586a53534934f51af1c&pIndex=1&pSize=50&SIGUN_CD=41310") #서버에 GET 요청 
req = conn.getresponse() #openAPI 서버에서 보내온 요청을 받아옴
print(req.status,req.reason)

#import http.client
#import xml.dom.minidom
#s=http.client.HTTPConnection("openapi.gg.go.kr")
#s.request("GET","/Publtolt?KEY=9bee44ffc03b4586a53534934f51af1c&Type=xml&pIndex=1")
#req=s.getresponse()
#data=req.read()
#dom=xml.dom.minidom.parseString(data)
#print(req.getheaders())
#print(dom.toxml())
