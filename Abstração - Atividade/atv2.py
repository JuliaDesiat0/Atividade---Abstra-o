class Cachorro:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def latir(self):
        print("Woof!")

cachorro = Cachorro("Snoop", 3)

cachorro.latir()
