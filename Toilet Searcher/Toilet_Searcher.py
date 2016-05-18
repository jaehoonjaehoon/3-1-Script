#from tkinter import *

#app = Tk()
#app.title("your")
#app.geometry('800x600')

#b1 = Button(app, text = "click me!", width = 10)
#b1.pack()

#app.mainloop()

from urllib.parse import urlparse
url="http://openapi.gg.go.kr/Publtolt?KEY=9bee44ffc03b4586a53534934f51af1c&Type=xml&pIndex=1"
parts = urlparse(url)
print(parts)

import xml.parsers.expat
def start_element(name, attrs):
    print('Start element:', name, attrs) 

def char_data(data):
    print('Character data:', repr(data))

pa = xml.parsers.expat.ParserCreate() 	#xmlparser 객체 생성
pa.StartElementHandler = start_element 	#이벤트 핸들러 연결
pa.CharacterDataHandler = char_data 	#이벤트 핸들러 연결
pa.Parse("""<?xml version="1.0"?><book ISBN="1111">
<title>Loving Python</title></book>""")
