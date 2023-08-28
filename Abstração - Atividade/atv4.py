class Retangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcular_area(self):
        return self.base * self.altura

retangulo = Retangulo(5, 4)

area = retangulo.calcular_area()
print(f"A área do retângulo é: {area} unidades quadradas")
