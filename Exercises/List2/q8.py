class Aluno:
    def __init__(self,nome, nota1, nota2, nota3):
        self.nome = nome
        self.nota1 = nota1
        self.nota2 = nota2
        self.nota3 = nota3
        
   
    def c_media(self):
        media = (self.nota1+self.nota2+self.nota3)/3
        return media
m1 = Aluno("João",8.6,6.4,7)
media = m1.calcular_media()
print("Média do aluno:", round(media, 1)) #FORMA PARA ARREDONDAR O RESULTADO
