import tkinter
import sys

class App(tkinter.Tk):
    def __init__(self, imgfile, tile_size=20):
        super().__init__()
        self.title("Pixelated Image")
        self.tile_size = tile_size
        self.obrazek = tkinter.PhotoImage(file=imgfile)
        self.obr_orig = self.obrazek.copy()
        self.sirka, self.vyska = self.obrazek.width(), self.obrazek.height()
        print(f"Načtený obrázek {imgfile} má rozměry {self.sirka}x{self.vyska}px")

        self.canvas = tkinter.Canvas(self, width=self.sirka, height=self.vyska)
        self.canvas.pack()
        self.canvas.create_image(0, 0, anchor='nw', image=self.obrazek)

        # provést rozkostičkování
        self.pixelate()
        self.mainloop()

    def pixelate(self):
        ts = self.tile_size
        for y in range(0, self.vyska, ts):
            for x in range(0, self.sirka, ts):
                r_sum = g_sum = b_sum = count = 0
                # spočítat průměr barvy v čtverečku
                for by in range(ts):
                    for bx in range(ts):
                        if x+bx < self.sirka and y+by < self.vyska:
                            r,g,b = self.obr_orig.get(x+bx, y+by)
                            r_sum += r
                            g_sum += g
                            b_sum += b
                            count += 1
                r_avg = r_sum // count
                g_avg = g_sum // count
                b_avg = b_sum // count
                color = f'#{r_avg:02x}{g_avg:02x}{b_avg:02x}'
                # vyplnit čtvereček průměrnou barvou
                for by in range(ts):
                    for bx in range(ts):
                        if x+bx < self.sirka and y+by < self.vyska:
                            self.obrazek.put(color, (x+bx, y+by))
        print("Obrázek byl rozkostičkován.")

# --- HLAVNÍ PROGRAM ---
if __name__ == "__main__":
    imagefile = "onepiece.png"
    app = App(imagefile, tile_size=20)
