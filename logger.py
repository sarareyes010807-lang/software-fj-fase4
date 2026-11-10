# Guarda los eventos y errores en el archivo software_fj.log

import logging

# Configuracion del archivo de log (se borra y se crea en cada ejecucion)
logging.basicConfig(
    filename="software_fj.log",
    filemode="w",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    encoding="utf-8",
)

# Este objeto lo importan los demas archivos para escribir en el log
log = logging.getLogger("software_fj")
