class Aluno:
    def __init__(self, nome, nota1, nota2, nota3, nota4):
        self.nome=nome
        self.nota1 = nota1
        self.nota2 = nota2
        self.nota3 = nota3
        self.nota4 = nota4
        self.recuperacao = None
        self.media = self.calcular_media()

    def calcular_media(self):
        return (self.nota1 + self.nota2 + self.nota3 + self.nota4) / 4
    
    def precisa_recuperacao(self):
        return self.media < 6.0
    
    def aplicar_recuperacao(self, nota_recuperacao):
        self.recuperacao = nota_recuperacao
        self.media = (self.media + self.recuperacao) / 2

    def exibir_dados(self):
        print(f"Nome: {self.nome}")
        print(f"Notas: {self.nota1}, {self.nota2}, {self.nota3}, {self.nota4}")
        print(f"Média: {self.media:.2f}")
        if self.recuperacao is not None:
            print(f"Nota de recuperação: {self.recuperacao}")
        print("Situação:", "Recuperação" if self.precisa_recuperacao() else "Aprovado")