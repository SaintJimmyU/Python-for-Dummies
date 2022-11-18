from mimetypes import init


class ErrorDefinidoxMi(Exception):
    def __init__(self, valor):
        print("Fue el error por ", valor)

try:
    raise ErrorDefinidoxMi(4)
except ErrorDefinidoxMi:
    print("Error escrito")