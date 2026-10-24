import socket

def create_socket(url: str, port: int) -> socket.socket:
    ## initialize socket with address family/socket kind
    mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    mysock.bind((url, port))

    return mysock


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
    ## create server socket
    port = int(input("What port would you like to bind to?\n"))

    mysock = create_socket('localhost', port)

    ## while true, send data, recieve data
    while True:
        ### listen on port
        mysock.listen(5)

        ### accept next in queue
        newsock, address = mysock.accept()
        print(f"### Accepted new connection from address: {address if address else 'Unavailable'}###\n")

        ### send welcome message
        send_data(newsock, "Connected to server - welcome!")

        ### recieve data until terminate
        while True:
            #### grab data
            message, _ = recieve_data(newsock)
            print(f"M - Recieved: {message} from address: {address if address else 'Unavailable'}\n")

            if message == "":
                print(f"### Lost connection with address: {address if address else 'Unavailable'}###\n")
                break

            else:
                #### send ack message
                send_data(newsock, f"Ack - recieved {message}\n")
                
            #except:
                #newsock.shutdown(socket.SHUT_RDWR)

        

    ## terminate connection between sockets
    close_socket(mysock)
