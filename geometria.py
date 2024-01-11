class Retangulo:
    def __init__(self, base, altura) -> None:
        self.base = base
        self.altura = altura
        

    def area(self):
        return(self.base * self.altura)
    
    def perimetro(self):
        perimetro = 2*self.base + 2*self.altura
        return perimetro


a = Retangulo(10, 10)

a.area
