#code by Rene Cakan

import tkinter

class App(tkinter.Tk):
    def __init__(self, titulek, sirka, vyska):
        super().__init__()
        self.title(titulek)
        self.canvas = tkinter.Canvas(self, width=sirka, height=vyska, background="#000000")
        self.canvas.pack()
        self.cas = 0
        self.running = False
        self.state = 0
        self.bind("<space>", self.toggle)

    def tik(self):
        if self.running:
            self.cas += 1
            m, s = divmod(self.cas, 60)
            self.canvas.itemconfig("hodiny", text=f"{m:02}:{s:02}")
            self.after(1000, self.tik)

    def toggle(self, event):
        if self.state == 0:
            self.running = True
            self.state = 1
            self.tik()
        elif self.state == 1:
            self.running = False
            self.state = 2
        elif self.state == 2:
            self.cas = 0
            self.canvas.itemconfig("hodiny", text="00:00")
            self.state = 0

    def run(self):
        self.canvas.create_text(200,100,text="00:00",anchor=tkinter.CENTER, fill="red",font="Times 80 bold",tags="hodiny")
        self.mainloop()

if __name__ == "__main__":
    app = App("My window", 400, 200)
    app.run()
