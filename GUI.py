from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from urllib.request import urlopen
from main import get_pic, bingo, get_wiki_url
import webbrowser


seed = input('Input seed: ')

window = Tk()

window.title('DARK SOULS bingo')
window.configure(width=500, height=500, bg='lightgray')
bingolist = bingo(seed)
counter = 0
buttonlist = []
imagelist = []
def onClick(itm):
    print(buttonlist[bingolist.index(itm)])
    webbrowser.open(get_wiki_url(itm))

for x in range(5):
    for y in range(5):
        item = bingolist[counter]
        image_url = get_pic(item)
        u = urlopen(image_url)
        data = u.read()
        u.close()
        img = ImageTk.PhotoImage(data=data)
        btn = ttk.Button(text=item, command=lambda itm = item: onClick(itm))
        buttonlist.append(btn)
        imagelist.append(img)
        buttonlist[counter].config(image=imagelist[counter])
        buttonlist[counter].grid(row=x, column=y, ipadx=30, ipady=30)
        counter = counter+1

window.mainloop()