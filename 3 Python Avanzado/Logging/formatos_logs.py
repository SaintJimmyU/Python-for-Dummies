from distutils.log import debug
import logging

""" Tenemos argumentos para utilizar en basiConfig para indicar un Formato "format" de mensaje. 
    %(asctime) --> indica la hora del log
    %(levelname) --> indica el Nivel
    %(message) --> indica el mensaje definido
    s --> indica que es un String 
    
    Tambien podemos agregar un formato de Fecha o tiempo -->  datefmt="%H:%M:%S"
    """

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s",
    datefmt="%H:%M:%S"
)

""" Podemos Establecer un Valor a una variable e incluirla en un mensaje"""
nombre = "Jimmy"
logging.error(f"{nombre} provoco el error")


""" Aqui provocaremos un error para hacer pruebas de mensajes """
try:
    division = 1/0
except:
    logging.error("division por cero")
    logging.exception("Mensaje de Error por Division por cero: ")


logging.warning("Log de Advertencia")
logging.error("Log de Error")
logging.critical("Log de Error Critico")