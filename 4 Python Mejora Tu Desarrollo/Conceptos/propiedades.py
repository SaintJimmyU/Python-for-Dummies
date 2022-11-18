class Circulo():

    def __init__(self,radio):
        self.radio=radio

    @property #Con esta directiva @ declaramos una Propiedad.
    def area(self):
        return 3.1416*(self.radio**2)
        
c=Circulo(10)
print(c.area)