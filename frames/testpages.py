import tkinter as tk
import time

class TestPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg=controller.bg_color)
        self.controller = controller
        self.bild_index=0
        # Timer starten
        self.start_time = 0
        filepath = "images/"+controller.randBilder[self.bild_index]
        self.img = tk.PhotoImage(file=filepath)
        label_links = tk.Label(self, text="Veganes Produkt",font=controller.title_font, fg=controller.fg_color, bg=controller.bg_color)
        label_rechts = tk.Label(self, text="Tierisches Produkt",font=controller.title_font, fg=controller.fg_color, bg=controller.bg_color)
        self.picture = tk.Label(self, image=self.img, fg=controller.fg_color, bg=controller.bg_color)
        label_links.grid(row=0,column=0, padx=(350,0), pady=100, sticky=tk.W)
        self.picture.grid(row=1,column=1, padx=(0,50))
        label_rechts.grid(row=0,column=3, padx=(0,350), pady=100, sticky=tk.E)
        # Rotes Kreuz hinzufügen
        self.error_img = tk.PhotoImage(file="images/error.png")
        self.label_error = tk.Label(self,image=self.error_img,fg=controller.fg_color, bg=controller.bg_color)
        self.label_error.grid(row=2,column=1)
        self.label_error.grid_forget()
        self.grid_columnconfigure(0,weight=1)
        self.grid_columnconfigure(1,weight=1)
        controller.bind("<KeyPress-e>", self.press_key)
        controller.bind("<KeyPress-i>", self.press_key)
    def enable_keys(self):
        self.controller.bind("<KeyPress-e>", self.press_key)
        self.controller.bind("<KeyPress-i>", self.press_key)
        return "break"
    def press_key(self, event):
        if(self.bild_index+1==20):    # Wenn alle 20 Bilder angezeigt wurden => Zwischenmeldung
            self.controller.unbind("<KeyPress-e>")
            self.controller.unbind("<KeyPress-i>")
            self.controller.show_frame("TestZwischenInfo")
        else:
            # Überprüfen ob Eingabe richtig war, je nach gedrückter Taste
            bild = self.controller.randBilder[self.bild_index][0]
            if((bild=='v' and event.char=='e') or (bild=='t' and event.char=='i')):
                self.label_error.grid_forget()
                # Wenn ja Timer stoppen, speichern, neustarten und nächstes Bild anzeigen
                end_time = time.time()
                reaktionszeit = round(end_time - self.start_time, 4)
                print(reaktionszeit)
                self.start_time = time.time()
                self.bild_index+=1 # => Fehler beheben
                filepath = "images/"+self.controller.randBilder[self.bild_index]
                self.img = tk.PhotoImage(file=filepath)
                self.picture.configure(image=self.img)
                self.picture.image = self.img
            else:
                # Wenn Nein X anzeigen
                self.label_error.grid(row=2,column=1)
            
            # Verzögerung für gedrückte Tasten
            self.controller.unbind("<KeyPress-e>")
            self.controller.unbind("<KeyPress-i>")
            self.controller.after(300,self.enable_keys)
            