import logging

def obtener_auditor():
    logging.basicConfig(
        filename='vitalis_audit.log',
        level=logging.INFO,
        format='%(asctime)s | %(levelname)s | ORIGEN: %(module)s | %(message)s'
    )
    return logging.getLogger("VitalisAuditor")