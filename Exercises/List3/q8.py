class temp:
    def __init__(self, fahrenheit, celcius):
        self.fahrenheit = fahrenheit
        self.celcius = celcius

    def calcular_CforF(self):
        tempC = (self.fahrenheit - 32) * 5/9
        return tempC

    def calcular_FforC(self):
        tempF = (self.celcius * 9/5) + 32
        return tempF


t1 = temp(68.0, 20.0)


tempCelsius = t1.calcular_CforF()
print(f"{t1.fahrenheit} graus Fahrenheit equivalem a {tempCelsius:.2f} graus Celsius")


tempFahrenheit = t1.calcular_FforC()
print(f"{t1.celcius} graus Celsius equivalem a {tempFahrenheit:.2f} graus Fahrenheit")
