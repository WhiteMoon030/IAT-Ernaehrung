import tkinter as tk
from tkinter import font as tkfont
from frames.startpage import StartPage
from frames.infopages import InfoPage, TestInfoPage, BZInfoPageA, BZInfoPageB

# Klasse welche die gesamte App steuert
class App(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        # Informationen zum Test
        self.gute_Adjektive = ["Angenehm","Ansprechend","Glücklich","Nett","Hervorragend","Fröhlich","Sympathisch","Attraktiv","Frieden","Liebevoll"]
        self.schlechte_Adjektive = ["Widerlich","Unangenehm","Distanziert","Qual","Schrecklich","Scheußlich","Böse","Minderwertig","Übel","Ignorant"]
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
        for F in (StartPage, InfoPage, TestInfoPage, BZInfoPageA, BZInfoPageB):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")
        self.show_frame("StartPage")

    def show_frame(self, page_name):
        '''Zeige ein Fenster anhand seines Namens an'''
        frame = self.frames[page_name]
        frame.tkraise()

if __name__ == "__main__":
    app = App()
    app.mainloop()