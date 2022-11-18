import logging

# Personalizamos un Logger
# logger = logging.getLogger("Logger_Jimmy")
# print(logger)

# Llamamos al Logger del Modulo o paquete en el que estamos trabajando
logger = logging.getLogger(__name__)
print(logger)