class Aluno:
    def __init__(self, nome, nota1, nota2):
        self.nome = nome
        self.nota1 = nota1
        self.nota2 = nota2

    def calcular_media(self):
        return (self.nota1 + self.nota2) / 2

aluno = Aluno("Julia", 8.5, 9.0)

media = aluno.calcular_media()
print(f"A média do aluno {aluno.nome} é: {media}")
