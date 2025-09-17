#code by Rene Cakan

import tkinter

class App(tkinter.Tk):
    def __init__(self, titulek, sirka, vyska):
        super().__init__()
        self.title(titulek)
        self.canvas = tkinter.Canvas(self, width=sirka, height=vyska, background="#000000")
        self.canvas.pack()
        self.canvas.focus_set()

        self._clicked = False
        self._coordinates = [0, 0]

        self.canvas.bind("<Button-1>", self.MousePress)
        self.canvas.bind("<KeyPress>", self.ButtonPress)

    def DrawFlag(self):
        self.canvas.delete("vlajka")
        self.canvas.create_rectangle(self._coordinates[0]-150, self._coordinates[1]-100,
        self._coordinates[0]+150, self._coordinates[1],fill="#FFFFFF", outline="", tags="vlajka")

        self.canvas.create_rectangle(self._coordinates[0]-150, self._coordinates[1],
        self._coordinates[0]+150, self._coordinates[1]+100,fill="#D7141A",outline="", tags="vlajka")

        self.canvas.create_polygon([self._coordinates[0]-150, self._coordinates[1]-100,
        self._coordinates[0], self._coordinates[1], self._coordinates[0]-150,
        self._coordinates[1]+100], fill="#11457E", outline="", tags="vlajka")

    def Run(self):
        self.mainloop()

    def MousePress(self, event):
        if not self._clicked:
            self._coordinates = [event.x, event.y]
            self._clicked = True
            self.DrawFlag()

    def ButtonPress(self, event):
        if event.keysym == "Up":
            self._coordinates[1] -= 10
        if event.keysym == "Down":
            self._coordinates[1] += 10
        if event.keysym == "Left":
            self._coordinates[0] -= 10
        if event.keysym == "Right":
            self._coordinates[0] += 10
        self.DrawFlag()

if __name__ == "__main__":
    app = App("My window", 800, 600)
    app.Run()
