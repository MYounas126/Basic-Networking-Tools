# In this script, we create a TCP server that listens on all interfaces on port 9998. 
# When a client connects, we accept the connection and create a new thread to handle the client. 
# The client handler thread reads in the data from the client, prints it out, and sends an ACK 
# message back to the client. This script is a simple example of a TCP server that can handle 
# multiple clients concurrently.
import socket
import threading

IP = "0.0.0.0"
PORT = 9998

# this is our client-handling thread
def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((IP, PORT))
    server.listen(5)
    print(f"[*] Listening on {IP}:{PORT}")

    while True:
        client, addr = server.accept()
        print(f"[*] Accepted connection from: {addr[0]}:{addr[1]}")
        client_handler = threading.Thread(target=handle_client, args=(client,))
        client_handler.start()

def handle_client(client_socket):
    with client_socket as sock:
        request = sock.recv(1024)
        print(f"[*] Received: {request.decode('utf-8')}")
        sock.send(b"ACK")

if __name__ == "__main__":
    main()
