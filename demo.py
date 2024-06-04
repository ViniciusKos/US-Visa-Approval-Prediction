from us_visa.logger import logging
from us_visa.exception import USvisaException
import sys


try:
    a = 1 / "10"
    logging.info("deu bom")
except Exception as e:
    logging.info("deu ruim")
    raise USvisaException(e, sys) from e