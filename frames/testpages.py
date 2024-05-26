import tkinter as tk

class TestPage(tk.Frame):
    def __init__(self, parent, controller, path, index):
        tk.Frame.__init__(self, parent)
        self.configure(bg=controller.bg_color)
        self.controller = controller
        filepath = "images/"+path
        self.img = tk.PhotoImage(file=filepath)
        self.label_links = tk.Label(self, text="Veganes Produkt",font=controller.title_font, fg=controller.fg_color, bg=controller.bg_color)
        label_rechts = tk.Label(self, text="Tierisches Produkt",font=controller.title_font, fg=controller.fg_color, bg=controller.bg_color)
        self.picture = tk.Label(self, image=self.img, fg=controller.fg_color, bg=controller.bg_color)
        self.label_links.grid(row=0,column=0, padx=(350,0), pady=100, sticky=tk.W)
        self.picture.grid(row=1,column=1, padx=(0,50))
        label_rechts.grid(row=0,column=3, padx=(0,350), pady=100, sticky=tk.E)
        self.grid_columnconfigure(0,weight=1)
        self.grid_columnconfigure(1,weight=1)
        controller.bind("e", self.press_e)
    def press_e(self, event):
        self.img = tk.PhotoImage(file="images/vegan01.png")
        self.picture.configure(image=self.img)
        self.picture['image'] = self.img
        print("Grr")
        self.label_links.configure(text="Grr")
        #controller.show_frame("TestPage"+str(index))