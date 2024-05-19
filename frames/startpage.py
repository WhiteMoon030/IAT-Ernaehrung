import tkinter as tk

# Startseite zur Eingabe des Pseudonyms
class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg=controller.bg_color)
        self.controller = controller
        # Beschreibung zum Eingabefeld
        label = tk.Label(self, text="Bitte wählen Sie Ihre zugewiesene Nummer aus!", font=controller.title_font, fg=controller.fg_color, bg=controller.bg_color)
        label.pack(padx=20,pady=(200,20))
        # Auswahlfeld zur Auswahl der personalisierten Nummer
        items = []
        for i in range(1,21):
            items.append(str(i))
        variable = tk.StringVar(self)
        variable.set("1")
        op = tk.OptionMenu(self,variable,*items)
        op.pack(pady=20)
        op.config(font=controller.normal_font)
        menu_item = self.nametowidget(op.menuname)
        menu_item.config(font=controller.normal_font)
        # Weiter Button
        continue_button = tk.Button(self, text="Weiter",font=controller.normal_font, command=lambda: controller.show_frame("InfoPage"))
        continue_button.pack(pady=20)
        continue_button.config(height=1, width=15)