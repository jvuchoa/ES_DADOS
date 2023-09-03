class D_Livro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor
    def detalhes(self):
        return f"Título: {self.titulo}, Autor: {self.autor}"
livro1 = D_Livro("O Ceifador", "Neal Shusterman")
print(livro1.detalhes()) 
