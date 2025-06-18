from tkinter import *
from tkinter import ttk





class Super():
    def __init__(self):
        self.mode = "dark"
        self.light_mode()

        self.root = Tk()
        self.root.title("Superhero Name Generator")
        #self.root.resizable(0,0)
        self.root.grid()
        self.root.configure(bg = self.bg_colour)

        self.root.rowconfigure(list(range(12)), weight = 1)
        self.root.columnconfigure(0, weight = 1)

        self.title_label = Label(self.root, font = "Verdana 20 bold", text = "Hero name generator", fg = self.t_colour, bg = "purple")
        self.title_label.grid(sticky = NSEW)

        self.adjectives = ["Happy", "Awesome", "Outgoing", "Funky"]
        self.radio_var = IntVar()
        self.radio_var.set(99)

        self.adjective_label = Label(self.root, font = "Verdana 16", text = "Choose an adjectives", fg = self.t_colour, bg = self.bg_colour)
        self.adjective_label.grid(sticky = NSEW)

        for i in range(4):
            Radiobutton(self.root, font = "Verdana 11",text=self.adjectives[i], variable=self.radio_var, value = i, fg = self.t_colour, bg = self.bg_colour).grid(row = (i+2), column = 0, sticky="nsew", columnspan=1, padx=60)

        self.colour_label = Label(self.root, font = "Verdana 16", text = "Choose a colour", fg = self.t_colour, bg = self.bg_colour)
        self.colour_label.grid(sticky = NSEW)

        self.choose = Entry(self.root, justify = CENTER)
        self.choose.grid()

        self.animal_label = Label(self.root, font = "Verdana 16", text = "Choose an animal", fg = self.t_colour, bg = self.bg_colour)
        self.animal_label.grid(sticky = NSEW)

        self.select_animal = ttk.Combobox(self.root,font = "Verdana 16", state = "readonly", values = ["Cockatiel", "Anteater", "Tasmanian devil"])
        self.select_animal.grid(padx=10,pady=10)

        self.name_button = Button(self.root, text="GO!",fg = self.t_colour, bg = self.bg_colour, font="Verdana 16",command=self.name)
        self.name_button.grid(padx=10,pady=10)

    def light_mode(self):
        if self.mode == "light":
            self.t_colour = "black"
            self.bg_colour = "white"
        else:
            self.t_colour = "white"
            self.bg_colour="black"

    def name(self):
        self.name = str(self.adjectives[self.radio_var.get()]) + " " + str(self.choose.get()) + " " + self.select_animal.get()
        self.name_label = Label(self.root, font = "Verdana 16", text = self.name, fg = self.t_colour, bg = self.bg_colour)
        self.name_label.grid(sticky = NSEW,row=12)

    def run(self):
        self.root.mainloop()
app = Super()
app.run()

