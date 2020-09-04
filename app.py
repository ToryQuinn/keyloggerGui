import keyboard
from tkinter import *
import argparse



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
       

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run a Keylogger Gui For S n' Gs, press shift+ctrl+x to quit")
    parser.add_argument('-f',
                        '--font',
                        type=str,
                        default="Helvetica",
                        help="The font name, e.g. Helvetica")
    parser.add_argument('-s',
                        '--size',
                        type=int,
                        default=99,
                        help="The size of the font in pixels")
    parser.add_argument('-w',
                        '--weight',
                        type=str,
                        choices=["bold", "boldface", "normal"],
                        default="normal",
                        help="Font weight: bold, boldface, normal")
    parser.add_argument('-t',
                        '--text-color',
                        type=str,
                        default="#ff00ff",
                        help="Text Color as text, e.g. red, black, purple, color codes also work")
    parser.add_argument('-b',
                        '--background-color',
                        type=str,
                        default="#6600CC",
                        help="Color of the Background in text")
    args = parser.parse_args()
    k = Keylogger(args.font,
                  args.size,
                  args.weight,
                  args.text_color,
                  args.background_color
    )
    k.run()
    

        

    
        
