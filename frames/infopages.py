import tkinter as tk

class InfoPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg=controller.bg_color)
        self.controller = controller
        explain_title = tk.Label(self,text="Vorabinformationen",font=controller.title_bold_font, fg=controller.fg_color, bg=controller.bg_color)
        explain_title.pack(padx=40,pady=(60,40),anchor="w")
        explain_text = tk.Label(self,justify=tk.LEFT,text="Um das Ergebnis nicht zu beeinflussen,\nminimieren Sie bitte Ablenkungen in Ihrer Umgebung und beenden Sie alle anderen Programme.\n\nWenn Sie Schwierigkeiten haben, die Aufgabe zu erkennen,\nstellen Sie bitte den Helligkeitsregler Ihres Monitors auf  \"Maximum\"!\n\nWenn Sie dieses Fenster schließen, beendet sich der Test automatisch (nicht empfohlen).",font=controller.title_font, fg=controller.fg_color, bg=controller.bg_color)
        explain_text.pack(padx=40,pady=(0,40),anchor="w")
        continue_button = tk.Button(self, text="Verstanden und Fortfahren",font=controller.normal_font, command=lambda: controller.show_frame("TestInfoPage"))
        continue_button.pack(padx=40,pady=20,anchor="w")
        continue_button.config(height=1, width=30)

class TestInfoPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg=controller.bg_color)
        self.controller = controller
        explain_title = tk.Label(self,justify=tk.LEFT, text="Ablauf des IAT-Test",font=controller.title_bold_font, fg=controller.fg_color, bg=controller.bg_color)
        explain_title.pack(padx=40,pady=(60,40), anchor="w")
        explain_text = tk.Label(self,justify=tk.LEFT, text="In dieser Studie werden Sie einen impliziten Assoziationstest (IAT) absolvieren,\nin dem Sie aufgefordert werden, Bilder und Wörter so schnell wie möglich in Gruppen zu sortieren.\nZusätzlich zum IAT gibt es einige Fragen zu Ihrer Person.\n\nDieser Test sollte etwa 10 Minuten dauern.",font=controller.title_font, fg=controller.fg_color, bg=controller.bg_color)
        explain_text.pack(padx=40,pady=(0,40), anchor="w")
        continue_button = tk.Button(self, text="Verstanden und Fortfahren",font=controller.normal_font, command=lambda: controller.show_frame("BZInfoPageA"))
        continue_button.pack(padx=40, pady=20, anchor="w")
        continue_button.config(height=1, width=30)

class BZInfoPageA(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg=controller.bg_color)
        self.controller = controller
        explain_title = tk.Label(self,justify=tk.LEFT,text="Ablauf des IAT-Test",font=controller.title_bold_font, fg=controller.fg_color, bg=controller.bg_color)
        explain_title.pack(padx=40,pady=(60,40),anchor="w")
        explain_point1 = tk.Label(self,justify=tk.LEFT,text="In der nächsten Aufgabe wird Ihnen eine Anzahl von Wörtern oder Bildern (\"Items\")gezeigt,\ndie Sie in Gruppen zuordnen sollen.\n\nEs ist wichtig, dass Sie dies so schnell und fehlerfrei wie möglich tun.\n\nWenn Sie zu langsam vorgehen, oder zu viele Fehler machen,\nwird ihr Ergebnis nicht feststellbar sein.\n\nDieser Teil der Studie wird ungefähr 5 Minuten dauern.\n\nEs folgt nun die Auflistung der Kategorien und der einzelnen Items,\ndie zu den jeweiligen Kategorien gehören.",font=controller.title_font, fg=controller.fg_color, bg=controller.bg_color)
        explain_point1.pack(padx=40,pady=(0,40),anchor="w")
        continue_button = tk.Button(self, text="Verstanden und Fortfahren",font=controller.normal_font, command=lambda: controller.show_frame("BZInfoPageB"))
        continue_button.pack(padx=40, pady=20, anchor="w")
        continue_button.config(height=1, width=30)

class BZInfoPageB(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg=controller.bg_color)
        self.controller = controller
        frame = tk.Frame(self,bg=controller.bg_color)
        frame.pack(anchor="w")
        explain_title = tk.Label(frame,anchor="w",text="Ablauf des IAT-Test",font=controller.title_bold_font, fg=controller.fg_color, bg=controller.bg_color)
        explain_title.grid(row=0,column=0,padx=40,pady=(60,5))
        tabellenkopf1 = tk.Label(frame,anchor="w",text="Kategorien",font=controller.normal_font,fg=controller.fg_color, bg="#dfcaa0")
        tabellenkopf1.grid(row=1,column=0,padx=(40,2),pady=(40,2),sticky=tk.W+tk.E)
        tabellenkopf2 = tk.Label(frame,anchor="w",text="Items",font=controller.normal_font,fg=controller.fg_color, bg="#dfcaa0")
        tabellenkopf2.grid(row=1,column=1,padx=2,pady=(40,2),sticky=tk.W+tk.E)
        tabellenspalte10 = tk.Label(frame,anchor="w",text="Gut",font=controller.normal_font,fg=controller.fg_color, bg="#f5f5dc")
        tabellenspalte10.grid(row=2,column=0,padx=(40,2),pady=2,sticky=tk.W+tk.E)
        tabellenspalte20 = tk.Label(frame,anchor="w",text="Schlecht",font=controller.normal_font,fg=controller.fg_color, bg="#f5f5dc")
        tabellenspalte20.grid(row=3,column=0,padx=(40,2),pady=2,sticky=tk.W+tk.E)
        # gute Adjektive in einer Liste anzeigen
        gA = ""
        bA = ""
        for i in range(len(controller.gute_Adjektive)):
            if(i!=len(controller.gute_Adjektive) and i>0): 
                gA += ", "
                bA += ", "
            gA += controller.gute_Adjektive[i]
            bA += controller.schlechte_Adjektive[i]
        tabellenspalte11 = tk.Label(frame,anchor="w",text=gA,font=controller.normal_font,fg=controller.fg_color, bg="#f5f5dc")
        tabellenspalte11.grid(row=2,column=1,padx=2,pady=2,sticky=tk.W+tk.E)
        tabellenspalte21 = tk.Label(frame,anchor="w",text=bA,font=controller.normal_font,fg=controller.fg_color, bg="#f5f5dc")
        tabellenspalte21.grid(row=3,column=1,padx=2,pady=2,sticky=tk.W+tk.E)
        # Kategorien tierische und Vegane Produkte
        tabellenspalte30 = tk.Label(frame,anchor="w",text="Tierische Produkte",font=controller.normal_font,fg=controller.fg_color, bg="#f5f5dc")
        tabellenspalte30.grid(row=4,column=0,padx=(40,2),pady=2,sticky=tk.W+tk.E)
        tabellenspalte31 = tk.Label(frame,anchor="w",text="Bilder von tierischen Produkten",font=controller.normal_font,fg=controller.fg_color, bg="#f5f5dc")
        tabellenspalte31.grid(row=4,column=1,padx=2,pady=2,sticky=tk.W+tk.E)
        tabellenspalte40 = tk.Label(frame,anchor="w",text="Vegane Produkte",font=controller.normal_font,fg=controller.fg_color, bg="#f5f5dc")
        tabellenspalte40.grid(row=5,column=0,padx=(40,2),pady=2,sticky=tk.W+tk.E)
        tabellenspalte41 = tk.Label(frame,anchor="w",text="Bilder von veganen Produkten",font=controller.normal_font,fg=controller.fg_color, bg="#f5f5dc")
        tabellenspalte41.grid(row=5,column=1,padx=2,pady=2,sticky=tk.W+tk.E)
        # Denken sie daran
        text_titel = tk.Label(self,text="Denken Sie daran",font=controller.normal_bold_font,fg=controller.fg_color, bg=controller.bg_color)
        text_titel.pack(pady=(30,10),padx=40,anchor="w")
        text = tk.Label(self,justify=tk.LEFT,text=">      Legen Sie Ihre Zeigefinger auf die Tasten \"e\" und \"i\", um schnell reagieren zu können.\n>      Zwei Hinweisfelder oben werden Ihnen zeigen, welche Wörter oder Bilder zu welcher Taste gehören.\n>      Jedes Wort oder Bild hat eine korrekte Zuordnung. Meist sind diese sehr leicht.\n>      Der Test wird kein Ergebnis rückmelden, wenn Sie zu langsam sind - bemühen Sie sich bitte, so schnell wie möglich zu reagieren.\n>      Rechnen Sie damit, dass Sie ein paar Fehler machen werden, weil Sie zu schnell reagieren. Das ist kein Problem.\n>      Um ein genaues Ergebnis zu erhalten, meiden Sie Ablenkungen und bleiben Sie konzentriert.",font=controller.normal_font,fg=controller.fg_color, bg=controller.bg_color)
        text.pack(padx=40,anchor="w")
        controller.testIndex=0
        continue_button = tk.Button(self, text="Verstanden und Test beginnen",font=controller.normal_font, command=lambda: controller.show_frame("TestPage"))
        continue_button.pack(padx=40, pady=40, anchor="w")
        continue_button.config(height=1, width=30)

class TestZwischenInfo(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg=controller.bg_color)
        self.controller = controller
        titel = tk.Label(self,text="Testteil 1 abgeschlossen")
        titel.pack()
