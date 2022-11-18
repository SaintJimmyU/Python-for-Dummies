import logging
from stat import filemode

""" Un log handler permite controlar los logger y personalizarlos. 
    Cuando se utiliza handler ya no es necesario utilizar logging.basicConfig """

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

""" Aqui lo configuramos el Controlador para salida por consola"""
handler_consola = logging.StreamHandler()
formato_logs = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
handler_consola.setFormatter(formato_logs)
logger.addHandler(handler_consola)

""" Aqui lo configuramos el Controlador para salida por archivo, el cual lo crea """
handler_archivo = logging.FileHandler("archivo.log",mode="w") # Aqui añadi el modo para sobre escritura
handler_archivo.setLevel(logging.ERROR)
handler_archivo.setFormatter(formato_logs)
logger.addHandler(handler_archivo)

logger.info("Mensaje de Registro Informativo")

logger.error("Log de Error") # Añadi un mensaje para el "archivo.log"
