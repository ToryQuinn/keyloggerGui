import keyboard
from tkinter import *

class Keylogger:
    def __init__(self,
                 fontName="Helvetica",
                 fontSize=99,
                 fontWeight="normal",
                 textColor="#ff00ff",
                 backgroundColor="#6600CC"):
        self.tk = Tk()
        self.text_buffer = []
        self.label = Label(self.tk,
                           text="",
                           font=(fontName, fontSize, fontWeight),
                           fg=textColor,
                           bg=backgroundColor)
        self.tk.configure(bg=backgroundColor)

    def updateText(self):
        self.label["text"] = '+'.join(self.text_buffer)
        
    def addKey(self,key):
        self.text_buffer.append(key)
        self.updateText()

    def delKey(self, key):
        self.text_buffer.remove(key)
        self.updateText()

    def callback(self, event):
        key = event.name.lower()
        if keyboard.is_pressed(event.name):
            if not key in self.text_buffer:
                self.addKey(key)
        else:
            self.delKey(key)
        if (all(x in self.text_buffer for x in ["shift", "ctrl","x"])):
            self.tk.destroy()
        
    def run(self):
        self.label.pack()
        keyboard.hook(callback=self.callback)
        mainloop()
