class Uno:
    def hazlo(self):
        print("hazlo de Uno")

    def haz_algo(self):#virtual
        self.hazlo()

class Dos(Uno):
    def hazlo(self):
        print("hazlo de Dos")

uno = Uno()
dos = Dos()

uno.haz_algo()
dos.haz_algo()

#? Nota: la situación en la cual la subclase puede modificar el comportamiento 
# de su superclase (como en el ejemplo) se llama polimorfismo. La palabra proviene 
# del griego (polys: "muchos, mucho" y morphe, "forma, forma"), lo que significa que 
# una misma clase puede tomar varias formas dependiendo de las redefiniciones realizadas 
# por cualquiera de sus subclases.

# El método, redefinido en cualquiera de las superclases, que cambia el comportamiento 
# de la superclase, se llama virtual.

