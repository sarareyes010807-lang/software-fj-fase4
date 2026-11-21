import logging
import os
from datetime import datetime

def get_timestamp_actual():
    """Devuelve fecha y hora actual."""
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def get_nombre_archivo_log():
    """Devuelve el nombre del archivo de log."""
    return "sistema_fj.log"

def crear_log(mensaje, nivel="info"):
    """Crea un registro en el log."""
    logger = logging.getLogger("sistema_fj")
    if nivel == "info":
        logger.info(mensaje)
    elif nivel == "error":
        logger.error(mensaje)
    elif nivel == "warning":
        logger.warning(mensaje)
    else:
        logger.debug(mensaje)

def configurar_logger(nombre="sistema_fj", archivo="sistema_fj.log", nivel=logging.INFO):
    """Configura el logger del sistema."""
    logger = logging.getLogger(nombre)
    logger.setLevel(nivel)

    if getattr(logger, "_fj_handler_agregado", False):
        return logger

    formato = logging.Formatter("| %(asctime)s | %(levelname)s | %(funcName)s | %(message)s")
    handler = logging.FileHandler(archivo, encoding="utf-8")
    handler.setFormatter(formato)
    logger.addHandler(handler)
    logger._fj_handler_agregado = True
    return logger

