class Persona():
    def __init__(self) -> None:
        pass

    def brincar(self):
        print("brincar")

    @classmethod
    def correr(cls):
        print("correr")

    @staticmethod
    def nadar():
        print("nadar")

jimmy = Persona()
jimmy.nadar()