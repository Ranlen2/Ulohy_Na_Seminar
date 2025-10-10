# code by Rene Cakan

import tkinter
import random
import sys

class App(tkinter.Tk):
    def __init__(self, imgfile, block_size=5, circle_radius=15):
        super().__init__()
        self.title("Impresionistický obrázek – kolečka podle bloků")
        self.block_size = block_size
        self.circle_radius = circle_radius
        self.obrazek = tkinter.PhotoImage(file=imgfile)
        self.obr_orig = self.obrazek.copy()
        self.sirka, self.vyska = self.obrazek.width(), self.obrazek.height()
        print(f"Načtený obrázek {imgfile} má rozměry {self.sirka}x{self.vyska}px")

        # vytvoření plátna
        self.canvas = tkinter.Canvas(self, width=self.sirka, height=self.vyska, bg="white")
        self.canvas.pack()

        # seznam teček (x, y, barva)
        self.body = self.vyber_pixely()
        random.shuffle(self.body)

        # vykreslení koleček
        self.vykresli_kolecka()

        self.mainloop()

    def vyber_pixely(self):
        """
        Rozdělí obrázek na bloky block_size x block_size,
        v každém vybere náhodný pixel a uloží jeho pozici + barvu.
        """
        body = []
        bs = self.block_size
        for by in range(0, self.vyska, bs):
            for bx in range(0, self.sirka, bs):
                # náhodná pozice v rámci bloku
                rx = bx + random.randint(0, bs - 1)
                ry = by + random.randint(0, bs - 1)
                if rx < self.sirka and ry < self.vyska:
                    r, g, b = self.obr_orig.get(rx, ry)
                    barva = f'#{r:02x}{g:02x}{b:02x}'
                    body.append((rx, ry, barva))
        print(f"Vygenerováno {len(body)} koleček.")
        return body

    def vykresli_kolecka(self):
        """
        Vykreslí kolečka s poloměrem circle_radius v náhodném pořadí.
        """
        r = self.circle_radius
        for (x, y, barva) in self.body:
            self.canvas.create_oval(
                x - r, y - r,
                x + r, y + r,
                fill=barva, outline=barva
            )
        print("Hotovo – impresionistický obraz dokončen.")

if __name__ == "__main__":
    imagefile = "onepiece.png"
    app = App(imagefile, block_size=5, circle_radius=15)
