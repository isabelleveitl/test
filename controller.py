#nur der Controller kennt model & View > Model & View komplett unabhängig voneinander

class Controller:
    def __init__(self, model, view):

        self.model = model
        self.view = view
        self.view.set_listener(self.change)

    def change(self, value):
        fahrenheit = self.model.calc_fahrenheit(value)
        celsius = self.model.calc_celsius(value)
        self.view.set_values(fahrenheit, celsius)

    def start(self):
        self.change(0) ##wenn das Fenster geöffnet wird, dann ist die Scale am Anfang auf Null
        self.view.show()