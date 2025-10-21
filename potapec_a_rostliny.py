#code by René Čakan

import tkinter
import random

##### Deklarace tříd

class Potapec:
    """
    Třída reprezentující potapěče jako herní objekt.
    Uchovává pozici, animační snímky a stav animace.
    """
    def __init__(self, x, y, obrazky):
        """
        Args:
            x, y: Počáteční pozice potapěče
            obrazky: Seznam PhotoImage objektů pro animaci
        """
        self.x = x
        self.y = y
        self.obrazky = obrazky  # Seznam snímků animace
        self.aktualni_snimek = 0  # Index aktuálního snímku
        self.id_canvas = None  # ID objektu na canvasu
    
    def get_obrazek(self):
        """
        Vrátí aktuální snímek animace.
        """
        return self.obrazky[self.aktualni_snimek]
    
    def dalsi_snimek(self):
        """
        Přepne na další snímek animace (cyklicky).
        """
        self.aktualni_snimek = (self.aktualni_snimek + 1) % len(self.obrazky)
    
    def pohyb(self, dx, dy, max_x, max_y):
        """
        Posune potapěče o zadaný vektor s kontrolou hranic.
        
        Args:
            dx, dy: Změna v x a y souřadnici
            max_x, max_y: Maximální rozměry herní plochy
        """
        self.x = max(30, min(max_x - 30, self.x + dx))
        self.y = max(30, min(max_y - 30, self.y + dy))
    
    def vzdalenost_od(self, x, y):
        """
        Vypočítá euklidovskou vzdálenost od bodu [x, y].
        (Pozn.: Tato metoda se už nepoužívá pro kolize, zachována pro kompatibilitu)
        
        Returns:
            Vzdálenost jako float
        """
        # !!! doplnit - použij Pythagorovu větu a pro odmocninu **0.5
        return 0
    
    def kolize_s(self, jiny_objekt, canvas):
        """
        AABB (Axis-Aligned Bounding Box) kolize pomocí canvas.bbox() - přesnější než kruhová kolize.
        Využívá skutečné bounding boxy vykreslených objektů na canvasu.
        
        Args:
            jiny_objekt: Instance objektu s atributem id_canvas (např. Rostlina)
            canvas: Reference na Canvas objekt
       ------------------------------------------------------------------------- 
        Případ 1: A je nalevo od B       Případ 2: A je napravo od B
            ┌──┐                              ┌──┐
            │A │     ┌──┐                     │B │  ┌──┐
            └──┘     │B │                     └──┘  │A │
                     └──┘                           └──┘
            x2 < ox1                          x1 > ox2

        Případ 3: A je nad B                Případ 4: A je pod B
            ┌──┐                              ┌──┐
            │A │                              │B │
            └──┘                              └──┘
            ┌──┐                              ┌──┐
            │B │                              │A │
            └──┘                              └──┘
            y2 < oy1                          y1 > oy2
        Tedy obdélníky se NEPŘEKRÝVAJÍ, pokud platí alespoň jedna z těchto podmínek:
        x2 < ox1  (A je vlevo od B) NEBO x1 > ox2 (A je vpravo od B) NEBO
        y2 < oy1  (A je nad B)     NEBO y1 > oy2 (A je pod B)
        Tedy negace této podmínky znamená, že se obdélníky překrývají.
        ---------------------------------------------------------------
        Returns:
            True pokud se bounding boxy objektů překrývají, jinak False
        """
        # Získáme bounding boxy z canvasu
        # bbox vrací tuple (x1, y1, x2, y2) kde:
        # - x1, y1 = levý horní roh
        # - x2, y2 = pravý dolní roh
        bbox1 = canvas.bbox(self.id_canvas)
        bbox2 = canvas.bbox(jiny_objekt.id_canvas)
        
        # Ošetření: pokud objekt není na canvasu, bbox vrací None
        if bbox1 is None or bbox2 is None:
            return False
        
        x1, y1, x2, y2 = bbox1
        ox1, oy1, ox2, oy2 = bbox2
        
        # AABB test: objekty se NEPŘEKRÝVAJÍ, pokud:
        # - pravý okraj A je vlevo od levého okraje B (x2 < ox1), NEBO
        # - levý okraj A je vpravo od pravého okraje B (x1 > ox2), NEBO
        # - dolní okraj A je nad horním okrajem B (y2 < oy1), NEBO
        # - horní okraj A je pod dolním okrajem B (y1 > oy2)
        # Negace této podmínky = objekty SE překrývají
        # !!!! DOPLNIT !!!! - vrátit True pokud se překrývají, jinak False
        return False


class Rostlina:
    """
    Třída pro rostlinu jako sbíratelný objekt.
    Každá rostlina má svou pozici a obrázek.
    """
    def __init__(self, x, y, obrazek):
        self.x = x
        self.y = y
        self.obrazek = obrazek
        self.id_canvas = None  # ID objektu na canvasu
        self.sebrana = False   # Příznak, zda už byla sebrána

class App(tkinter.Tk):
    def __init__(self, titulek, sirka, vyska):
        """
        Konstruktor hlavní aplikace - herního okna.
        """
        super().__init__()
        self.title(titulek)
        
        # Rozměry okna a pozice potapěče
        self.sirka, self.vyska = sirka, vyska
        
        # Skóre hráče
        self.score = 0
        
        # Příznak, zda animace běží
        self.animace_bezi = False
        
        # === GUI PRVKY ===
        
        # Frame (rám) pro ovládací prvky - umístíme dole
        self.panel = tkinter.Frame(self, bg="lightblue", height=50)
        self.panel.pack(side="top", fill="x")
        
        # Button pro start/stop animace
        # "▶ Start" / "⏸ Stop" 
        self.btn_anim = tkinter.Button(self.panel,text="▶ Start", command=self.toggle_animace, width=12)
        self.btn_anim.pack(side="left")
        
        # Label pro zobrazení skóre
        self.lbl_score = tkinter.Label(self.panel, text=f"Skore: {self.score}", bg="lightblue")
        self.lbl_score.pack(side="left", padx=100)
        
        # Label pro nápovědu
        
        # Canvas (plátno) pro kreslení hry
        self.canvas = tkinter.Canvas(
            self,
            width=sirka,
            height=vyska,
            background="lightcyan"
        )
        self.canvas.pack()
        
        # === NAČTENÍ SPRITE OBRÁZKŮ ===
        
        # Načtení sprite sheetu potapěče
        self.sprite = tkinter.PhotoImage(file="diversprite.png")
        
        # Seznam pro jednotlivé snímky animace potapěče
        obrazky_potapec = []
        for k in range(2):  # 2 řádky
            for j in range(4):  # 4 sloupce
                obr = self.get_obr_potapec(j, k)
                obrazky_potapec.append(obr)
        
        # Načtení obrázku rostliny (zmenšený na 40x60)
        self.obr_rostlina_orig = tkinter.PhotoImage(file="rasa.png")
        self.obr_rostlina = self.zmensit_obrazek(
            self.obr_rostlina_orig,
            40, 60
        )
        
        # === HERNÍ OBJEKTY ===
        
        # Vytvoření instance potapěče
        self.potapec = Potapec(sirka // 2, vyska // 2, obrazky_potapec)
        
        # Seznam rostlin ke sběru
        self.rostliny = []
        self.vytvor_rostliny(7)  # Vytvoříme 5 rostlin na náhodných pozicích
        
        # === NAVÁZÁNÍ UDÁLOSTÍ ===
        
        self.canvas.bind("<Button-1>", self.klik)  # Levé tlačítko myši
        self.canvas.bind("<Key>", self.klavesa)    # Stisk klávesy
        
        self.canvas.focus_set()  # Canvas dostane focus pro zachytávání kláves
        
        # Zobrazení potapěče na začátku
        self.zobraz_potapece()
        self.zobraz_rostliny()
    
    def get_obr_potapec(self, sloupec, radek):
        """
        Vyřízne jeden snímek ze sprite sheetu potapěče.
        
        Args:
            sloupec: Index sloupce (0-3)
            radek: Index řádku (0-1)
        
        Returns:
            PhotoImage s jedním snímkem animace
        """
        W, H = self.sprite.width(), self.sprite.height()
        sirka = W // 4  # Šířka jednoho snímku
        vyska = H // 2  # Výška jednoho snímku
        
        # Vytvoříme nový prázdný obrázek
        img = tkinter.PhotoImage(width=sirka, height=vyska)
        
        # Kopírujeme pixely z sprite sheetu
        for x in range(sirka):
            x1 = (sloupec * sirka) + x
            for y in range(vyska):
                y1 = (radek * vyska) + y
                r, g, b = self.sprite.get(x1, y1)
                
                # Bílá barva je průhledná (nekreslíme ji)
                if (r, g, b) != (255, 255, 255):
                    barva = f"#{r:02x}{g:02x}{b:02x}"
                    img.put(barva, (x, y))
        
        return img
    
    def zmensit_obrazek(self, original, nova_sirka, nova_vyska):
        """
        Zmenší obrázek na zadané rozměry (jednoduchý nearest-neighbor).
        
        Args:
            original: Původní PhotoImage
            nova_sirka: Cílová šířka
            nova_vyska: Cílová výška
        
        Returns:
            Zmenšený PhotoImage
        """
        puvodni_w, puvodni_h = original.width(), original.height()
        
        # Vytvoříme nový obrázek s novými rozměry
        novy = tkinter.PhotoImage(width=nova_sirka, height=nova_vyska)
        
        # Poměry zmenšení
        ratio_x = puvodni_w / nova_sirka
        ratio_y = puvodni_h / nova_vyska
        
        # Projdeme každý pixel nového obrázku
        for y in range(nova_vyska):
            for x in range(nova_sirka):
                # Zjistíme odpovídající pozici ve starém obrázku
                stary_x = int(x * ratio_x)
                stary_y = int(y * ratio_y)
                
                # Zkopírujeme barvu
                r, g, b = original.get(stary_x, stary_y)
                barva = f"#{r:02x}{g:02x}{b:02x}"
                novy.put(barva, (x, y))
        
        return novy
    
    def vytvor_rostliny(self, pocet):
        """
        Vytvoří zadaný počet rostlin na náhodných pozicích.
        
        Args:
            pocet: Kolik rostlin vytvořit
        """
        self.rostliny = []
        for _ in range(pocet):
            # Náhodná pozice s okrajem 50px od kraje
            x = random.randint(50, self.sirka - 50)
            y = random.randint(50, self.vyska - 50)
            rostlina = Rostlina(x, y, self.obr_rostlina)
            self.rostliny.append(rostlina)
    
    def zobraz_rostliny(self):
        """
        Vykreslí všechny rostliny na canvas.
        """
        for rostlina in self.rostliny:
            if not rostlina.sebrana:
                # Vytvoříme obrázek na canvasu a uložíme jeho ID
                rostlina.id_canvas = self.canvas.create_image(
                    rostlina.x,
                    rostlina.y,
                    anchor='center',
                    image=rostlina.obrazek,
                    tag="rostlina"
                )
    
    def zobraz_potapece(self):
        """
        Vykreslí potapěče na canvas na aktuální pozici.
        """
        # Smažeme starý obrázek potapěče
        self.canvas.delete("potapec")
        
        # Vytvoříme nový obrázek z aktuálního snímku potapěče
        self.potapec.id_canvas = self.canvas.create_image(
            self.potapec.x,
            self.potapec.y,
            anchor='center',
            image=self.potapec.get_obrazek(),
            tag="potapec"
        )
    
    def klik(self, event):
        """
        Obsluha kliknutí myší - přesune potapěče y souřadnici místa kliknutí.
        """
        self.potapec.y = event.y
        self.kontrola_kolize()
        self.zobraz_potapece()
    
    def pohyb_potapec(self, dx, dy):
        """
        Posune potapěče o zadaný vektor.
        
        Args:
            dx: Změna v x-ové souřadnici
            dy: Změna v y-ové souřadnici
        """
        # Delegujeme pohyb na objekt Potapec
        self.potapec.pohyb(dx, dy, self.sirka, self.vyska)
        
        self.kontrola_kolize()
        self.zobraz_potapece()
    
    def kontrola_kolize(self):
        """
        Zkontroluje, zda potapěč nesebral nějakou rostlinu.
        NOVĚ: Používá canvas.bbox() pro přesnou AABB kolizi.
        """
        for rostlina in self.rostliny:
            if not rostlina.sebrana:
                # ZMĚNA: Místo vzdalenost_od() používáme kolize_s()
                # která využívá canvas.bbox() pro přesnou detekci překryvu
                if self.potapec.kolize_s(rostlina, self.canvas):
                    rostlina.sebrana = True
                    self.canvas.delete(rostlina.id_canvas)
                    self.score += 1
                    self.aktualizuj_score()
                    
                    # Pokud byly sebrány všechny rostliny, vytvoř nové
                    if all(r.sebrana for r in self.rostliny):
                        self.vytvor_rostliny(7)
                        self.zobraz_rostliny()
    
    def aktualizuj_score(self):
        """
        Aktualizuje zobrazení skóre na labelu.
        """
        self.lbl_score.config(text=f"🌿 Skóre: {self.score}")
    
    def toggle_animace(self):
        """
        Zapne/vypne automatickou animaci potapěče.
        """
        self.animace_bezi = not self.animace_bezi
        
        if self.animace_bezi:
            self.btn_anim.config(text="⏸ Stop")
            self.animacni_smycka()
        else:
            self.btn_anim.config(text="▶ Start")
    
    def animacni_smycka(self):
        """
        Hlavní smyčka animace - mění snímky potapěče a pohybuje jím.
        """
        if not self.animace_bezi:
            return  # Ukončíme smyčku, pokud animace byla zastavena
        
        # Změna snímku animace (delegujeme na objekt Potapec)
        self.potapec.dalsi_snimek()
        
        # Automatický pohyb doprava (s přetočením přes okraj)
        self.potapec.x = (self.potapec.x + 5) % self.sirka
        
        # Kontrola kolizí a překreslení
        self.kontrola_kolize()
        self.zobraz_potapece()
        
        # Naplánujeme další snímek animace za 100ms
        self.after(100, self.animacni_smycka)
    
    def klavesa(self, event):
        """
        Obsluha stisku klávesy.
        """
        if event.keysym.lower() == "q":
            self.destroy()
            exit(0)
    
    def run(self):
        """
        Spuštění hlavní smyčky aplikace.
        """
        self.mainloop()

##### HLAVNÍ PROGRAM
if __name__ == "__main__":
    # Vytvoření a spuštění aplikace
    app = App("My window", 800, 600)
    app.run()

# EOF
