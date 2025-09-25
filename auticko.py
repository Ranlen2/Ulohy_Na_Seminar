#code by Rene Cakan
import tkinter

class Platno(tkinter.Canvas):
    def vytvor_auticko(self, x, y, barva="red", tag="auticko"):
        self.delete(tag)
        self.create_rectangle(x-30, y-15, x+30, y+10, fill=barva, outline="black", tags=tag)
        self.create_polygon(x-20, y-15, x+20, y-15, x+15, y-25, x-15, y-25, fill=barva, outline="black", tags=tag)
        self.create_polygon(x-13, y-25, x+12, y-25, x+10, y-18, x-11, y-18, fill="#87CEEB", outline="black", tags=tag)
        self.create_oval(x+25, y-10, x+28, y-7, fill="yellow", outline="black", tags=tag)
        self.create_oval(x-28, y-10, x-25, y-7, fill="yellow", outline="black", tags=tag)
        self.create_oval(x-20, y+5, x-10, y+15, fill="black", tags=tag)
        self.create_oval(x+10, y+5, x+20, y+15, fill="black", tags=tag)
        return tag

class App(tkinter.Tk):
    DELAY = 50
    SPEED = 5

    def __init__(self, titulek, sirka, vyska, pozice):
        super().__init__()
        self.title(titulek)
        self.geometry(f"{sirka}x{vyska}+{pozice[0]}+{pozice[1]}")
        self.canvas = Platno(self, width=sirka, height=vyska, background="#87CEEB")
        self.canvas.pack()
        self.canvas.create_rectangle(0, vyska-80, sirka, vyska-40, fill="#555555", outline="#555555")
        self.x = sirka // 2
        self.y = vyska - 60
        self.barva = "red"
        self.rychlost = 0
        self.prujezdy = 0
        self.canvas.vytvor_auticko(self.x, self.y, self.barva)
        self.counter_text = self.canvas.create_text(100, 30, text=f"Průjezdy: {self.prujezdy}", font=("Arial", 16), fill="black")
        self.bind("<Left>", self.jed_rika)
        self.bind("<Right>", self.jed_rika)
        self.bind("<space>", self.stop_auto)
        self.bind("<r>", self.zmena_barvu)
        self.bind("<g>", self.zmena_barvu)
        self.bind("<b>", self.zmena_barvu)
        self.canvas.focus_set()
        self.running = True
        self.after(self.DELAY, self.tik)

    def jed_rika(self, udalost):
        if udalost.keysym == "Left":
            self.rychlost = -self.SPEED
        elif udalost.keysym == "Right":
            self.rychlost = self.SPEED

    def stop_auto(self, udalost):
        self.rychlost = 0

    def zmena_barvu(self, udalost):
        if udalost.keysym.lower() == "r":
            self.barva = "red"
        elif udalost.keysym.lower() == "g":
            self.barva = "green"
        elif udalost.keysym.lower() == "b":
            self.barva = "blue"
        self.canvas.vytvor_auticko(self.x, self.y, self.barva)

    def tik(self):
        if self.running:
            self.x += self.rychlost
            if self.x > self.canvas.winfo_width():
                self.x = 0
                self.prujezdy += 1
                self.canvas.itemconfig(self.counter_text, text=f"Průjezdy: {self.prujezdy}")
            elif self.x < 0:
                self.x = self.canvas.winfo_width()
                self.prujezdy += 1
                self.canvas.itemconfig(self.counter_text, text=f"Průjezdy: {self.prujezdy}")
            self.canvas.vytvor_auticko(self.x, self.y, self.barva)
        self.after(self.DELAY, self.tik)

    def run(self):
        self.mainloop()

if __name__ == "__main__":
    app = App("My window", 600, 400, (50, 50))
    app.run()
