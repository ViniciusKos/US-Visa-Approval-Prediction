from us_visa.logger import logging
from from_root import from_root
logging.debug("hallo2")

import os
os.makedirs(os.path.join(from_root(),"notebooks"), exist_ok=True)
