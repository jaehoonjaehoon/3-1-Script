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

# -*- coding: cp949 -*-

#from urllib.request
#from urllib import urlencode, quote_plus

#url = 'http://api.suwon.go.kr/openapi-data/service/Toilet/getToilet'
#queryParams = '?' + urlencode({ quote_plus('ServiceKey') : '서비스키', quote_plus('numOfRows') : '999', quote_plus('pageNo') : '1' })

#request = Request(url + queryParams)
#request.get_method = lambda: 'GET'
#response_body = urlopen(request).read()
#print(response_body)