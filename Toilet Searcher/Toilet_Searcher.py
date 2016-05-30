#from xml.etree.ElementTree import parse

##tree = parse("Toilet.xml")
##note = tree.getroot()
##print(note.get("date"))
##print(note.get("foo", "default"))
##print(note.keys())
##print(note.items())

#import urllib.request
#import xml.etree.ElementTree as etree

#def main():

#    ##서울공공데이터사용
#    key = 'yourKey'
#    url = "http://openAPI.seoul.go.kr:8088/%s/xml/SJWPerform/1/5" % key

#    data = urllib.request.urlopen(url).read()

#    filename = "Toilet.xml"
#    f = open(filename, "wb") #다른 사람들의 예제처럼 "w"만 해서 했더니 에러가 발생
#    f.write(data)
#    f.close()

#    #파싱하기
#    tree = etree.parse(filename)
#    root = tree.getroot()

#    for a in root.findall('row'):
#        print(a.findtext('DATA_STD_DE'))
#        print(a.findtext('SIGUN_NM'))
#        print(a.findtext('PUBLFACLT_DIV_NM'))
#        print(a.findtext('PBCTLT_PLC_NM'))
#        print(a.findtext('LOCPLC_ROADNM_ADDR'))
#        print('----------------------')

#if __name__ == "__main__":
#    main()



##--------------------------------위는 구현된 부분

# -*- coding: utf-8 -*-

import urllib.request,urllib.parse 
from urllib.request import urlopen
import http.client
from urllib.parse import urlencode
from urllib.parse import quote_plus
from xml.etree import ElementTree
class DaumOpenAPI:
    #url�Է½� �� ���ĵ� 
    server = 'api.suwon.go.kr'
    regKey = 'q6mrRozl07bNXTjHeLqmLSvN4U%2FK7qvApXtiNo23QVTjFNjjIy2X8CE1YDV0snaOMTYKqjWQjdj1mi79PQLAKQ%3D%3D'
    query = '스타벅스'                          #질의검색
    location = '37.340226,126.733629'               #위도경도
    radius= '20000'                         #반경 0~20000
    count = '15'                          #페이지에 보여질 갯수1~15
    page = '1'                            #페이지번호1~3
    sort = '2'                            #0:정확도, 1:거리, 2:인기
    format = "xml"                        #xml
    andSign = '&'
    conn = None
    queryParams =None
    baseUrl = 'http://api.suwon.go.kr/openapi-data/service/Toilet/getToilet?pageNo=1&numOfRows=10&ServiceKey='
    xmlData = None


    #def __init__(self):
        #print('init')
    def myURIBuilder(self):
         self.queryParams = ('?' + urlencode({ quote_plus('query') : self.query,
                               quote_plus('location') : self.location,
                               quote_plus('radius') : self.radius,
                               quote_plus('count') : self.count,
                               quote_plus('sort') : self.sort,
                               quote_plus('page') : self.page, 
                               quote_plus('apikey'):self.regKey
                                }))
    #검색할 장소 xml형식으로 불러오기    

    def getData(self): 
        conn = http.client.HTTPConnection(self.server)
        print('connection complate')

        conn.request('GET',self.baseUrl+ self.queryParams )
        print(self.baseUrl+ self.queryParams)
        print('request complate\n')

        req = conn.getresponse()
        self.xmlData = req.read()
        print(req.status,req.reason)

        print(self.xmlData.decode('utf8'))

    def updateQueryParam(self,key):

        self.query = key
        self.myURIBuilder()

    def printInfo(self,rss):
        for element in rss.findall("item"):
           print('-------------------------------------------------------------------------------')

           print('장소명:'+element.findtext('title'))

           print('카테고리:'+element.findtext('category'))

           print('전화번호:'+element.findtext('phone'))

           print('구주소:'+element.findtext('address'))

           print('도로명주소:'+element.findtext('newAddress'))

           print('거리:'+element.findtext('distance')+'미터')

           print('방향:'+element.findtext('direction'))
           print('-------------------------------------------------------------------------------')
    def extractTitleData(self):
       rss = (ElementTree.parse(urlopen(self.baseUrl + self.queryParams))).getroot()
       
       self.printInfo(rss)
    def getdataFromQuery(self,key):
        self.updateQueryParam(key)
        rss = (ElementTree.parse(urlopen(self.baseUrl + self.queryParams))).getroot()
        #print(self.baseUrl + self.queryParams)
        return rss
    def getUrl(self,key):
        self.updateQueryParam(key)
        return self.baseUrl + self.queryParams
if (__name__ == '__main__') :
    a = DaumOpenAPI()
        #print(type(a.count))
    a.printInfo(a.getdataFromQuery('산기대'))
        #a.getData()
