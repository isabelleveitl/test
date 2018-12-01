class Model:
    def calc_fahrenheit(self, celsius):
        return (celsius - 32) / 1.8

    def calc_celsius(self,fahrenheit):
        return 32 + (1.8 * fahrenheit)

