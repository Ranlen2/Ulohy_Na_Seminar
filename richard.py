#code by Rene Cakan

import tkinter

class App(tkinter.Tk):
    DELAY = 200

    def __init__(self, titulek, sirka, vyska):
        super().__init__()
        self.x, self.y = sirka//2, vyska//2
        self.i = 13
        self.smer = "right"
        self.title(titulek)
        self.canvas = tkinter.Canvas(self, width=sirka, height=vyska, background="white")
        self.canvas.pack()
        self.canvas.focus_set()
        self.canvas.bind("q", self.ukonci)
        self.canvas.bind("<Button-1>", self.klik)
        self.canvas.bind("<Up>", self.lizani)
        self.canvas.bind("<Left>", self.kouknuti_doleva)
        self.canvas.bind("<Right>", self.kouknuti_doprava)

        self.obrazky = [tkinter.PhotoImage(file=f"kocka/richard-{n}.png") for n in range(26)]
        self.zobraz_kocku()

    def zobraz_kocku(self):
        self.canvas.delete("kocka")
        self.kocka = self.canvas.create_image(self.x, self.y, anchor='center', image=self.obrazky[self.i], tag="kocka")

    def anim(self, frames, konecny_obrazek):
        def krok(idx=0):
            if idx < len(frames):
                self.i = frames[idx]
                self.zobraz_kocku()
                self.after(self.DELAY, krok, idx+1)
            else:
                self.i = konecny_obrazek
                self.zobraz_kocku()
        krok()

    def lizani(self, event=None):
        start_smer = self.smer
        if start_smer == "right":
            self.anim(list(range(8,14)), 22)
        else:
            self.anim(list(range(8,14)), 13)

    def kouknuti_doleva(self, event=None):
        self.smer = "left"
        self.anim(list(range(23,26)), 13)

    def kouknuti_doprava(self, event=None):
        self.smer = "right"
        self.anim(list(range(18,21)), 22)

    def klik(self, event):
        self.x, self.y = event.x, event.y
        self.zobraz_kocku()

    def ukonci(self, event):
        self.destroy()
        exit(0)

    def run(self):
        self.zobraz_kocku()
        self.mainloop()


if __name__ == "__main__":
    app = App("My window", 800, 600)
    app.run()
