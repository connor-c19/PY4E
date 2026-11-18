__all__ = ["client", "connection", "server"]

import logging
## Set default logger used by client/server
logger = logging.getLogger(__name__)
logging.basicConfig(filename='myapp.log', level=logging.INFO, filemode='w')



## Determines the default port used by server instances
DEFAULT_SERVER_PORT = 5000

## Determines max queue size used by server
DEFAULT_SERVER_QUEUE = 5

## Determines tick rate (in seconds) used by server
DEFAULT_SERVER_TR = .5

