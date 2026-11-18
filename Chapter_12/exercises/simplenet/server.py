import socket
import threading

from time import sleep

from simplenet.connection import Connection
from simplenet.__init__ import DEFAULT_SERVER_PORT, DEFAULT_SERVER_QUEUE, DEFAULT_SERVER_TR, logger

class Server:
    """Simple server object that can be used to send/recieve messages 
    to/from multiple clients simultaneously

    Keyword arguments:
    name -- String used to identify a given client instance (default "client")
    """

    def __init__(self, name: str = "server") -> None:
        self.name = name
        logger.info(f"New server '{self.name}' created")


    def _handle_client_thread(self, curr: Connection) -> None:
        """Handle client interaction via dedicated thread

        Keyword arguments:
        curr -- Connection object created to track information 
            of client-server connection
        """
        address = curr.peername

        while True:
            #### grab data
            try:
                message = curr.recieve_data()
            except:
                logger.error(f"{self.name}: Lost connection with address: {address}")
                break
            else:
                if message in ["", None]:
                    break
                else:
                    #### send ack message
                    logger.info(f"{self.name}: Recieved: {message} from address: {address}")
                    curr.send_data(f"Ack - recieved {message}")


    def _core(self) -> None:
        """Define core routine for server, called by exposed 'run()' function."""

        sock = self.binding.socket
        client_threads: list[threading.Thread] = []

        ### listen on port
        sock.listen(DEFAULT_SERVER_QUEUE)
        sock.setblocking(False)

        ## while true, send data, recieve data
        while True:
    
            ### accept next in queue
            try: newsock, address = sock.accept()
            except: logger.debug(f"{self.name}: No new connections")
            else:
                address = address if address else 'Unavailable'
                logger.info(f"{self.name}: Accepted new connection from address: {address}")

                ### create new connection object
                curr = Connection(newsock, address)
                
                ### send welcome message
                curr.send_data(f"Connected to server: {self.name}: - welcome!")

                ### allocate thread to client connection
                ct = threading.Thread(
                target=self._handle_client_thread,
                args=(),
                kwargs={"curr":curr}
                )

                ct.start()
                client_threads.append(ct)
                logger.info(f"Clients connected = {len(client_threads)}")

            finally:
                ### clean up dead connection threads
                copy = client_threads.copy()
                for ct in client_threads:
                    if not ct.is_alive(): copy.remove(ct)

                client_threads = copy
                logger.debug(f"Clients left = {len(client_threads)}")


                sleep(DEFAULT_SERVER_TR)


    def run(self, url: str = "", port: int = DEFAULT_SERVER_PORT) -> (None | bool):
        """Bind socket tied to client instance, then run _core(). 
        Returns either none (blocks) indicating server is running, 
        or bool value 'False' indicating outcome of connection attempt.

        Keyword arguments:
        url -- String used to identify host to bind to (default "" for 'localhost')
        port -- Int used to identify port of selected host (default __init.py module's DEFAULT_SERVER_PORT)
        """

        ## initialize socket with address family/socket kind
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        try:
            sock.bind((url, port))
        except:
            logger.info(f"{self.name}: Binding refused, closing")
            sock.close()
            return False
        else:
            self.binding = Connection(sock, None)
            logger.info(f"{self.name}: Bound to host: {url} on port: {port}")

            self._core() ## FIXME: Open thread for core functionality


    def stop(self) -> None:
        """Close and delete server instance's defined binding."""
        
        try:
            sock = self.binding.socket
        except:
            logger.error(f"{self.name}: No existing connection on stop(). Run [server].run")
        else:
            try:
                sock.shutdown(socket.SHUT_WR)
            except: 
                logger.warning(f"{self.name}: Endpoint unreachable on stop(), still closing socket.")
            finally:
                ## release resources associated with sockets
                sock.close()
                del self.binding

    


