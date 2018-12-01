#Gesamte Darstellung soll im Konstruktor implementiert sein
#Methode show oder start - mit Aufruf soll die view erzeug twerden

import tkinter as tk

class View:
    def __init__(self):
        self.listener = None

        self.window = tk.Tk() ##muss nicht window heißen > TK ist das Hauptfenster
        self.window.title("F/C Umrechnung")
        self.window.resizable(False, False) ##weder die Höhe noch die Breite sind veränderbar

        self.heading = tk.Label(self.window, text="Celsius in Fahrenheit Umrechnung", font="Helvetica 13 bold")
        self.heading.grid(row=0, column=0, columnspan=2, padx=20, pady=10) #2 Spalten 3 Zeilen gibt es gesamt > span = über beide

        self.entry = tk.Scale(self.window, command=self.trigger_event, from_=-200, to=200, orient=tk.HORIZONTAL)
        self.entry.grid(row=1, column=0,columnspan=2, sticky=tk.W + tk.E, padx=20)

        self.fahrenheit = tk.Label(self.window, font="Helvetica 9 bold")
        self.fahrenheit.grid(row=2, column=0 )

        self.celsius = tk.Label(self.window, font="Helvetica 9 bold")
        self.celsius.grid(row=2, column=1)

    def trigger_event(self, value):
        if self.listener:
            self.listener(int(value))

    ##Listener hinzufügen (Funktion wird ausgeführt wenn Event ausgeführt)
    def set_listener(self, listener):
        self.listener=listener


    @property ##damit Controller Zugriff darauf erhält
    def value(self):
        return self.entry.get() #der Wert der am Schieberegler steht


    def set_values(self, fahrenheit, celsius):
        self.fahrenheit['text'] = "{:.2f} ° Celsius ist \n{:.2f}°F".format(self.value, fahrenheit) #fahrenheit #1. Element links unten
        self.celsius['text'] = "{:.2f} °F ist \n{:.2f}°Celsius".format(self.value, celsius)

    def show(self):
        self.window.mainloop()
