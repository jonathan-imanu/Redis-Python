import socket
import threading


def main():
    # You can use print statements as follows for debugging, they'll be visible when running tests.
    print("Logs from your program will appear here!")

    # Uncomment this to pass the first stage
    #
    server_socket = socket.create_server(("localhost", 6379))
    connection, address = server_socket.accept()  # wait for client
    with connection:
        while True:
            req = connection.recv(1024)
            pong_resp = "+PONG\r\n"
            connection.send(pong_resp.encode())

if __name__ == "__main__":
    main()
