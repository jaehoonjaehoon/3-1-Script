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
