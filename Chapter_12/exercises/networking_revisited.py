from simplenet import client, server
from time import sleep
import threading

def client_thread_routine(client: client.Client):
    name = client.name
    if client.connect():
        client.send(f"Hi from {name}")

        while True:
            if (message := input(f"Enter next message from {name} (q to exit)\n>>>")) !="q":
                client.send(message)
            else:
                client.close()
                break


if __name__ == "__main__":
    #Spawn a server bound to SERVER_PORT
    myserver = server.Server("My Server")

    ## run server
    ## allocate it's own thread
    serverthread = threading.Thread(
        target=myserver.run,
        args=(),
        kwargs={}
    )

    serverthread.start()

    sleep(.5)

    #Spawn clients from list [NAMES]
    names = ["client1", "client2", "client3"]

    clientthreads: list[threading.Thread] = []

    ## each gets its own thread
    for name in names:
        myclient = client.Client(name)

        clientthread = threading.Thread(
            target=client_thread_routine,
            args=([myclient]),
            kwargs={}
        )

        clientthreads.append(clientthread)

    ## each thread runs a send/receive cycle, then terminates client on input (y/n)
    for t in clientthreads:
        t.start()

    # Wait for all clientthreads to finish
    for t in clientthreads:
        t.join()

    # Shutdown server
    if input():
        serverthread.join()