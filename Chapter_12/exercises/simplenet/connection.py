from socket import socket
import json

class Connection:
    """Connection objects are used by client/servers to logically organize information about a connection.

    Keyword arguments:
    socket -- the socket object used BY the instantiating client/server. (required)
    peername -- the hostname of the client/server the socket is connected TO (default None)
    """

    def __init__(self, socket: socket, peername: str = None):
        self.socket = socket
        self.peername = peername


    def recieve_data(self) -> (str | None):
        """Recieve data from a connection.
        Return either a string containing the fetched data, or None."""

        sock = self.socket

        ## loop through recieve cycles until data is fully recieved
        message = ""
        while True:
            ### recieve batch of bytes
            try:
                datachunk, _ = sock.recvfrom(4098)
            except:
                raise Exception(f"Error, most likley:\nConnection with: {self.peername} lost")
            else:
                datadecoded = datachunk.decode()
                message += datadecoded

                if len(datachunk) < 4098:
                    break

        message = message.strip()
        ## report on result
        if message:
            return message

                
    def send_data(self, data) -> (int | None):
        """Send data using a connection.
        Return either an int indicating the length of message sent as confirmation,
        or None.
         
        Keyword arguments:
        data -- any object wished to be sent using a connection (required)
        """

        sock = self.socket
        
        ## encode data into UTF-8
        datastring = json.dumps(data)
        databytes = (datastring+"\n").encode()

        ## loop through send cycles until data is fully sent
        lendatabytes = len(databytes)
        lensentdatatotal = 0
        try:
            while lensentdatatotal < lendatabytes:
                ### send rest of 'databytes' based on how much has already been sent
                lensentdata = sock.send(databytes[lensentdatatotal:])
                lensentdatatotal += lensentdata
        except:
            raise Exception(f"Error, most likley:\nConnection with: {self.peername} lost")
        else:
            ## report on result
            if lendatabytes:
                return lendatabytes