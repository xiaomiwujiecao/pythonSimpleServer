import socket


def server():
    global port
    host = "localhost"
    comms_socket = socket.socket()
    comms_socket.bind((host, port))
    print("Waiting for a char at", host, "on port", port)
    comms_socket.listen(10)
    send_data = ""
    while True:
        connection, address = comms_socket.accept()

        print("open chat with", address)
        while send_data != "EXIT":
            print(connection.recv(4096).decode("UTF-8"))
            send_data = "Replay with:"
            connection.send(bytes(send_data, "UTF-8"))
        send_data = ""
        connection.close()


def client():
    global port
    host = input("enter the host you want to communicate" +
                 "with(leave blank for localhost)"
                 )
    if host == "":
        host = "localhost"
    comms_socket = socket.socket()

    print("Starting a chat with ", host, "on port", port)
    comms_socket.connect((host, port))
    while True:
        send_data = input("message:")
        comms_socket.send(bytes(send_data, "UTF-8"))
        print(comms_socket.recv(4096).decode("UTF-8"))


port = int(input("Enter the port you want to communicate on 0 for default"))

if port == 0:
    port = 50000
while True:
    print("your option are:")
    print("1- wait for chat ")
    print("2- initiate a chat")
    print("3- exit")
    option = int(input("option:"))
    if option == 1:
        server()
    elif option == 2:
        client()
    elif option == 3:
        break
    else:
        print("I don't recognize that option")
