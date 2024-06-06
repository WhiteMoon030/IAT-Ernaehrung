import tkinter as tk
import time
from tkinter import font as tkfont
from frames.startpage import StartPage
from frames.infopages import InfoPage, TestInfoPage, BZInfoPageA, BZInfoPageB, TestZwischenInfo
from frames.testpages import TestPage

# Klasse welche die gesamte App steuert
class App(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        # Informationen zum Test
        self.gute_Adjektive = ["Angenehm","Ansprechend","Glücklich","Nett","Hervorragend","Fröhlich","Sympathisch","Attraktiv","Frieden","Liebevoll"]
        self.schlechte_Adjektive = ["Widerlich","Unangenehm","Distanziert","Qual","Schrecklich","Scheußlich","Böse","Minderwertig","Übel","Ignorant"]
        # Bilder Reihenfolge
        self.randBilder = ['vegan07.png', 'tierisch01.png', 'vegan02.png', 'vegan06.png', 'vegan08.png', 'vegan05.png', 'tierisch06.png', 'vegan01.png', 'tierisch08.png', 'tierisch05.png', 'tierisch10.png', 'vegan04.png', 'tierisch04.png', 'vegan09.png', 'vegan10.png', 'tierisch02.png', 'vegan03.png', 'tierisch07.png', 'tierisch03.png', 'tierisch09.png']
        self.testIndex = -1
        # Zufällige Reihenfolge der guten & schlechten Adjektive
        # Eine 0 im ersten Wert des Tupels steht für den Array mit guten_Adjektiven
        # Eine 1 im ersten Wert des Tupels steht für den Array mit schlechten_Adjektiven
        # Der zweite Wert im Tupel repräsentiert den Index des Adjektives im jeweiligen Array
        self.randAdjektive = [(0, 4), (0, 5), (1, 5), (0, 1), (0, 0), (1, 7), (0, 6), (1, 2), (1, 3), (0, 7), (0, 3), (1, 6), (1, 0), (0, 9), (0, 8), (1, 1), (1, 9), (1, 8), (0, 2), (1, 4)]
        # Fenster auf Vollbild setzen
        self.attributes("-fullscreen",True)
        # Schriftarten für alle Ansichten definieren
        self.title_font = tkfont.Font(family="Cambria", size=30)
        self.title_bold_font = tkfont.Font(family="Cambria", size=30, weight=tkfont.BOLD)
        self.normal_font = tkfont.Font(family="Cambria", size=20)
        self.normal_bold_font = tkfont.Font(family="Cambria", size=20, weight=tkfont.BOLD)
        self.fg_color = "black"
        self.bg_color = "white"
        # Container für alle Ansichten des Programmes
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        self.frames = {}
        index = 0
        for F in (StartPage, InfoPage, TestInfoPage, BZInfoPageA, BZInfoPageB, TestPage, TestZwischenInfo, TestPage):
            page_name = F.__name__
            if F == TestPage:
                if index==0:
                    frame = F(parent=container, controller=self, typ="bilder")
                if index==1:
                    frame = F(parent=container, controller=self, typ="adjektive")
            else:
                frame = F(parent=container, controller=self)
            if F==TestPage:
                self.frames[page_name+str(index)] = frame
                index += 1
            else:
                self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")
        self.show_frame("StartPage")

    def show_frame(self, page_name):
        '''Zeige ein Fenster anhand seines Namens an'''
        frame = self.frames[page_name]
        # Timer auf 0 setzten
        if(page_name=="TestPage0" or page_name=="TestPage1"):
            frame.enable_keys()
            #frame.start_time = time.time()
        frame.tkraise()

if __name__ == "__main__":
    app = App()
    app.mainloop()