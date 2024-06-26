import tkinter as tk
import time

class TestPage(tk.Frame):
    def __init__(self, parent, controller, typ):
        tk.Frame.__init__(self, parent)
        self.configure(bg=controller.bg_color)
        self.controller = controller
        self.test_index=0
        self.typ = typ
        # Timer starten
        self.start_time = 0
        filepath = "images/"+controller.randBilder[self.test_index]
        self.img = tk.PhotoImage(file=filepath)
        # Text je nach Test wählen
        text_links,text_rechts = None, None
        if(typ=="bilder"):
            text_links = "Veganes Produkt"
            text_rechts = "Tierisches Produkt"
            self.picture = tk.Label(self, image=self.img, fg=controller.fg_color, bg=controller.bg_color)
            self.picture.grid(row=1,column=1, padx=(0,50))
        elif(typ=="adjektive"):
            text_links = "Gutes Adjektiv"
            text_rechts = "Schlechtes Adjektiv"
            # Erstes Adjektiv bestimmen
            if(controller.randAdjektive[self.test_index][0]==0):
                text_adjektiv = controller.gute_Adjektive[controller.randAdjektive[self.test_index][1]]
            else:
                text_adjektiv = controller.schlechte_Adjektive[controller.randAdjektive[self.test_index][1]]
            self.text = tk.Label(self,text=text_adjektiv,font=controller.title_font, fg=controller.fg_color, bg=controller.bg_color)
            self.text.grid(row=1,column=1, padx=(0,50))
        else:
            if(typ=="ba1"):
                text_links = "Gutes Adjektiv\noder\nTierisches Produkt"
                text_rechts = "Schlechtes Adjektiv\noder\nVeganes Produkt"
                self.array = controller.randAB1
                # Erstes Adjektiv bestimmen
                if(self.array[self.test_index][0]==0):
                    text_adjektiv = controller.gute_Adjektive[self.array[self.test_index][1]]
                else:
                    text_adjektiv = controller.schlechte_Adjektive[self.array[self.test_index][1]]
            elif(typ=="ba2"):
                text_links = "Gutes Adjektiv\noder\nVeganes Produkt"
                text_rechts = "Schlechtes Adjektiv\noder\nTierisches Produkt"
                self.array = controller.randAB2
                # Erstes Adjektiv bestimmen
                if(self.array[self.test_index][0]==0):
                    text_adjektiv = controller.gute_Adjektive[self.array[self.test_index][1]]
                else:
                    text_adjektiv = controller.schlechte_Adjektive[self.array[self.test_index][1]]
            self.textOderBild = tk.Label(self,text=text_adjektiv,font=controller.title_font, fg=controller.fg_color, bg=controller.bg_color)
            self.textOderBild.grid(row=1,column=1, padx=(0,50))
        label_links = tk.Label(self, text=text_links,font=controller.title_bold_font, fg=controller.fg_color, bg=controller.bg_color)
        label_rechts = tk.Label(self, text=text_rechts,font=controller.title_bold_font, fg=controller.fg_color, bg=controller.bg_color)
        label_links.grid(row=0,column=0, padx=(350,0), pady=100, sticky=tk.W)
        label_rechts.grid(row=0,column=3, padx=(0,350), pady=100, sticky=tk.E)
        # Rotes Kreuz hinzufügen
        self.error_img = tk.PhotoImage(file="images/error.png")
        self.label_error = tk.Label(self,image=self.error_img,fg=controller.fg_color, bg=controller.bg_color)
        self.label_error.grid(row=2,column=1)
        self.label_error.grid_forget()
        self.grid_columnconfigure(0,weight=1)
        self.grid_columnconfigure(1,weight=1)
    def enable_keys(self):
        self.controller.bind("<KeyPress-e>", self.press_key)
        self.controller.bind("<KeyPress-i>", self.press_key)
        return "break"
    def press_key(self, event):
        # Überprüfen ob Eingabe richtig war, je nach gedrückter Taste
        if(self.typ=="bilder"):
            bild = self.controller.randBilder[self.test_index][0]
            if((bild=='v' and event.char=='e') or (bild=='t' and event.char=='i')):
                if(self.test_index+1==20):    # Wenn alle 20 Bilder angezeigt wurden => Zwischenmeldung
                    self.controller.unbind("<KeyPress-e>")
                    self.controller.unbind("<KeyPress-i>")
                    self.controller.show_frame("TestZwischenInfo0")
                else:
                    self.label_error.grid_forget()
                    self.test_index+=1
                    filepath = "images/"+self.controller.randBilder[self.test_index]
                    self.img = tk.PhotoImage(file=filepath)
                    self.picture.configure(image=self.img)
                    self.picture.image = self.img
            else:
                # Wenn Nein X anzeigen
                self.label_error.grid(row=2,column=1)
        elif(self.typ=="adjektive"):
            # Überprüfen ob Adjektiv richtig zugeordnet wurde (links gute rechts schlechte Adjektive)
            array_indikator = self.controller.randAdjektive[self.test_index][0]
            if((array_indikator==0 and event.char=='e') or (array_indikator==1 and event.char=='i')):
                if(self.test_index+1==20):    # Wenn alle 20 Bilder angezeigt wurden => Zwischenmeldung
                    self.controller.unbind("<KeyPress-e>")
                    self.controller.unbind("<KeyPress-i>")
                    self.controller.show_frame("TestZwischenInfo1")
                else:
                    self.label_error.grid_forget()
                    self.test_index+=1
                    # Adjektiv bestimmen
                    if(self.controller.randAdjektive[self.test_index][0]==0):
                        text_adjektiv = self.controller.gute_Adjektive[self.controller.randAdjektive[self.test_index][1]]
                    else:
                        text_adjektiv = self.controller.schlechte_Adjektive[self.controller.randAdjektive[self.test_index][1]]
                    self.text["text"] = text_adjektiv
            else:
                # Wenn Nein X anzeigen
                self.label_error.grid(row=2,column=1)
        else:
            # Überprüfen ob gerade ein Wort oder ein Bild angezeigt wurde
            if(type(self.array[self.test_index]) is str): # -> Bild
                anfangsbuchtstabe = self.array[self.test_index][0]
                if(self.typ=="ba1"):
                    if((anfangsbuchtstabe=='t' and event.char=='e') or (anfangsbuchtstabe=='v' and event.char=='i')):
                        if(self.test_index+1==20):    # Wenn alle 20 Bilder angezeigt wurden => Zwischenmeldung
                            self.controller.unbind("<KeyPress-e>")
                            self.controller.unbind("<KeyPress-i>")
                            self.controller.show_frame("TestZwischenInfo2")
                        else:
                            self.label_error.grid_forget()
                            # Wenn ja Timer stoppen, speichern und neustarten
                            end_time = time.time()
                            reaktionszeit = round(end_time - self.start_time, 4)
                            # In die CSV Datei schreiben
                            self.controller.datei.write("BA1;"+str(reaktionszeit)+"\n")
                            self.start_time = time.time()
                            self.test_index+=1
                            # Nächstes Adjektiv anzeigen
                            if(self.array[self.test_index][0]==0):
                                text_adjektiv = self.controller.gute_Adjektive[self.array[self.test_index][1]]
                            else:
                                text_adjektiv = self.controller.schlechte_Adjektive[self.array[self.test_index][1]]
                            self.textOderBild["text"] = text_adjektiv
                            self.img = ""
                            self.textOderBild.configure(image=self.img)
                            self.textOderBild.image = self.img
                    else:
                        # Wenn Nein X anzeigen
                        self.label_error.grid(row=2,column=1)
                else:
                    if((anfangsbuchtstabe=='v' and event.char=='e') or (anfangsbuchtstabe=='t' and event.char=='i')):
                        if(self.test_index+1==20):    # Wenn alle 20 Bilder angezeigt wurden => Zwischenmeldung
                            self.controller.unbind("<KeyPress-e>")
                            self.controller.unbind("<KeyPress-i>")
                            self.controller.show_frame("EndPage")
                        else:
                            self.label_error.grid_forget()
                            # Wenn ja Timer stoppen, speichern und neustarten
                            end_time = time.time()
                            reaktionszeit = round(end_time - self.start_time, 4)
                            self.controller.datei.write("BA2;"+str(reaktionszeit)+"\n")
                            self.start_time = time.time()
                            self.test_index+=1
                            # Nächstes Adjektiv anzeigen
                            if(self.array[self.test_index][0]==0):
                                text_adjektiv = self.controller.gute_Adjektive[self.array[self.test_index][1]]
                            else:
                                text_adjektiv = self.controller.schlechte_Adjektive[self.array[self.test_index][1]]
                            self.textOderBild["text"] = text_adjektiv
                            self.img = ""
                            self.textOderBild.configure(image=self.img)
                            self.textOderBild.image = self.img
                    else:
                        # Wenn Nein X anzeigen
                        self.label_error.grid(row=2,column=1)
            else: # -> Wort
                # Überprüfen ob Adjektiv richtig zugeordnet wurde (links gute rechts schlechte Adjektive)
                array_indikator = self.array[self.test_index][0]
                if((array_indikator==0 and event.char=='e') or (array_indikator==1 and event.char=='i')):
                    if(self.test_index+1==20):    # Wenn alle 20 Bilder angezeigt wurden => Zwischenmeldung
                        self.controller.unbind("<KeyPress-e>")
                        self.controller.unbind("<KeyPress-i>")
                        self.controller.show_frame("EndPage")
                    else:
                        self.label_error.grid_forget()
                        # Wenn ja Timer stoppen, speichern und neustarten
                        end_time = time.time()
                        reaktionszeit = round(end_time - self.start_time, 4)
                        if(self.typ=="ba1"):
                            self.controller.datei.write("BA1;"+str(reaktionszeit)+"\n")
                        else:
                            self.controller.datei.write("BA2;"+str(reaktionszeit)+"\n")
                        self.start_time = time.time()
                        self.test_index+=1
                        # Nächstes Bild anzeigen
                        filepath = "images/"+self.array[self.test_index]
                        self.img = tk.PhotoImage(file=filepath)
                        self.textOderBild.configure(image=self.img)
                        self.textOderBild.image = self.img
                else:
                    # Wenn Nein X anzeigen
                    self.label_error.grid(row=2,column=1)

        # Verzögerung für gedrückte Tasten
        self.controller.unbind("<KeyPress-e>")
        self.controller.unbind("<KeyPress-i>")
        self.controller.after(300,self.enable_keys)
            