import socket

from simplenet.connection import Connection
from simplenet.__init__ import DEFAULT_SERVER_PORT, logger

class Client:
    """Simple client object that can be used to send/receive messages to/from a server.

    Keyword arguments:
    name -- String used to identify a given client instance (default "client")
    """

    def __init__(self, name: str = "client") -> None:
        self.name = name
        logger.info(f"New client '{self.name}' created")


    def connect(self, url: str = "", port: int = DEFAULT_SERVER_PORT) -> bool:
        """Create socket tied to client instance, attempt connection to other host. 
        Returns bool indicating outcome of connection attempt.

        Keyword arguments:
        url -- String used to identify host to connect TO (default "" for 'localhost')
        port -- Int used to identify port of selected host (default __init.py module's DEFAULT_SERVER_PORT)
        """

        ## initialize socket with address family/socket kind
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 

        try:
            sock.connect( (url, port) )
        except:
            logger.error(f"{self.name}: Connection refused, closing")
            sock.close()
            return False
        else:
            self.connection = Connection(sock, sock.getpeername()[0])
            logger.info(f"{self.name}: Connected to host: {self.connection.peername} on port: {port}")
            return True
            

    def send(self, data) -> (int | None):
        """Send data using client instance's defined connection.
        Return either an int indicating the length of message sent as confirmation,
        or None.
         
        Keyword arguments:
        data -- any object wished to be sent using a connection (required)
        """

        try:
            lensent = self.connection.send_data(data)
        except:
            logger.error(f"{self.name}: No existing connection for this client on send(). Run [client].connect")
        else:
            return lensent
        

    def recieve(self) -> (str | None):
        """Recieve data using client instance's defined connection.
        Return either a string containing the fetched data, or None.
        """

        try:
            message = self.connection.recieve_data()
        except:
            logger.error(f"{self.name}: No existing connection for this client on recieve(). Run [client].connect")
        else:
            logger.info(f"{self.name}: recieved: {message} from server: {self.connection.peername}")
            return message


    def close(self) -> None:
        """Close and delete client instance's defined connection."""

        try:
            sock = self.connection.socket
        except:
            logger.error(f"{self.name}:No existing connection for this client on close(). Run [client].connect")
        else:
            try:
                sock.shutdown(socket.SHUT_WR)
            except: 
                logger.error(f"{self.name}: Endpoint unreachable on close(), still closing socket.")
            finally:
                ## release resources associated with sockets
                sock.close()
                del self.connection
