import logging

""" loggin en realidad tiene su origen en la libreria de Java Log4j el cual tiene como funcion 
    registrar mendiante mensajes transacciones en tiempo de ejecucion.

    basicConfig Permite establecer su comportamiento mediante los siguientes parametros:
    level = Indica el Nivel de Prioridad de mensajes (el minimo es "debug" y el maximo "Critical")
    filename = Indicamos un archivo donde se almacenar la informacion de los mensajes registrados
    filemode = Al indicar el estado "w" indicamos que se va a sobreescribir la informacion del archivo,
                Si no indicamos este parametro, el archivo acumulara la informacion en cada ejecucion. """

logging.basicConfig(level=logging.DEBUG,filename="Ejemplo_Logs.log",filemode="w") 

logging.debug("Log de Debugging")
logging.info("Log Informativo")
logging.warning("Log de Advertencia")
logging.error("Log de Error")
logging.critical("Log de Error Critico")