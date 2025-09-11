#code by Rene Cakan

import tkinter

class App(tkinter.Tk):
    def __init__(self, titulek, sirka, vyska):
        super().__init__()
        self.title(titulek)
        self.canvas = tkinter.Canvas(self, width=sirka, height=vyska, background="#000000")
        self.canvas.pack()
    def run(self):	
        self.canvas.create_rectangle(250, 200, 550, 300,fill="#FFFFFF", outline="")
        self.canvas.create_rectangle(250, 300, 550, 400,fill="#D7141A", outline="")
        self.canvas.create_polygon([250, 200, 400, 300, 250,400],fill="#11457E", outline="")

        self.mainloop()
if __name__ == "__main__":
    app = App("My window", 800, 600)
    app.run()
