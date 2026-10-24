import socket
from time import sleep

def create_socket(url: str, port: int) -> tuple[socket.socket, str]:
    ## initialize socket with address family/socket kind
    mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    ## connect socket with url:port
    try:
        mysock.connect( (url, port) )
    except:
        print("Connection refused, closing")
        close_socket(mysock)
        quit()

    peername = mysock.getpeername()

    print(f"Connected to peer: {peername}")

    return (mysock, peername)


def close_socket(mysock: socket.socket):
    try:
        mysock.shutdown(socket.SHUT_WR)

    except: 
        print("Endpoint unreachable, still closing socket.")

    ## release resources associated with sockets
    mysock.close()


def send_data(mysock: socket.socket, data: str) -> int:
    ## encode data into UTF-8
    databytes = (data+"\n").encode()

    ## loop through send cycles until data is fully sent
    lendatabytes = len(databytes)
    lensentdatatotal = 0
    while lensentdatatotal < lendatabytes:
        ### send rest of 'databytes' based on how much has already been sent
        lensentdata = mysock.send(databytes[lensentdatatotal:])
        lensentdatatotal += lensentdata

    return lensentdatatotal


def recieve_data(mysock: socket.socket) -> tuple[str, str]:
    ## loop through recieve cycles until data is fully recieved
    message = ""
    address = "none"
    while True:
        ### recieve batch of bytes
        datachunk, address = mysock.recvfrom(4098)

        datadecoded = datachunk.decode()
        message += datadecoded

        if len(datachunk) < 4098:
            break

    return (message.strip(), address)


if __name__ == '__main__':
    ## create client socket and connect to server
    #url = input("What url would you like to connect to? (leave blank for internal):\n")
    #if url == '':
    url = "localhost"

    port = int(input("What port would you like to connect to?:\n"))

    mysock, peername = create_socket(url, port)

    ## while true, send data, recieve data
    while True:
        ### grab input
        data = input("Please insert a message.\n Type 'close' to terminate connection:\n")

        ### screen for termination
        if data != "close":
            #### send data
            lensentdata = send_data(mysock, data)
            print(f"Sent: {data}\n of length: {lensentdata}\n to host: {peername}\n")            

            #### wait for data to hit server
            sleep(1)

            #### recieve data
            message, address = recieve_data(mysock)
            print(f"Recieved: {message} from address: {address if address else 'Unavailable'}\n")

        ### terminate condition
        else:
            break

    ## terminate connection between sockets
    close_socket(mysock)
