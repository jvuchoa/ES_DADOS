class Palindromo:
    def __init__(self, text1, text2, text3):
        self.text1 = text1
        self.text2 = text2
        self.text3 = text3

    def testP(self, texto):
        texto = ''.join(e for e in texto if e.isalnum()).lower()
        return texto == texto[::-1]

    def finalizar(self):
        if self.testP(self.text1):
            print(f"'{self.text1}' é um palíndromo")
        else:
            print(f"'{self.text1}' não é um palíndromo")

        if self.testP(self.text2):
            print(f"'{self.text2}' é um palíndromo")
        else:
            print(f"'{self.text2}' não é um palíndromo")

        if self.testP(self.text3):
            print(f"'{self.text3}' é um palíndromo")
        else:
            print(f"'{self.text3}' não é um palíndromo")

# Exemplo de uso
texto1 = "Roma me tem amor "
texto2 = "João"
texto3 = "A mala nada na lama "

verificador = Palindromo(texto1, texto2, texto3)
verificador.finalizar()
