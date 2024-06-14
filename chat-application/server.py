import socket
import threading

HOST = ''
PORT = 7744

# Dictionary to store connected clients
clients = {}

# Function to handle connected clients
def handle_client(client_socket, client_addr, name):
    try:
        while True:
            # Receive message from clients
            data = client_socket.recv(1024).decode()
            if not data:
                break

            # If client wants to exit from the chat
            if data.lower() in ["quit", "exit"]:
                broadcast(f"{name} has left the chat room.", client_socket)
                break

            # Broadcast message to all clients except the sender
            message = f"{name}: {data}"
            broadcast(message, client_socket)
    except Exception as e:
        print(f"Error handling client {client_addr}: {e}")
    finally:
        # Remove client from the dictionary and close the socket
        if name in clients:
            del clients[name]
            client_socket.close()
            broadcast(f"{name} has disconnected.", client_socket)

# Function to broadcast message to all clients except the sender
def broadcast(message, sender_socket=None):
    for name, client_socket in clients.items():
        if client_socket != sender_socket:
            try:
                client_socket.send(message.encode())
            except Exception as e:
                print(f"Error broadcasting the message to {name}: {e}")

# Main function to start the server
def main():
    # Create socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Bind socket
    server_socket.bind((HOST, PORT))

    # Listening for incoming connections
    server_socket.listen()
    print("Server listening for connections...")

    try:
        while True:
            # Accept incoming connection
            client_socket, client_addr = server_socket.accept()
            print(f"Connection from {client_addr}")

            # Receive client name and ensure it's unique
            while True:
                name = client_socket.recv(1024).decode()
                if name in clients:
                    client_socket.send("Name already taken. Try another name.".encode())
                else:
                    break

            # Add client to the dictionary
            clients[name] = client_socket

            # Start a new thread to handle the client
            client_thread = threading.Thread(target=handle_client, args=(client_socket, client_addr, name))
            client_thread.start()
            broadcast(f"{name} has joined the chat room.", client_socket)
    except KeyboardInterrupt:
        print("Server shutting down...")
    finally:
        server_socket.close()
        for client_socket in clients.values():
            client_socket.close()

if __name__ == "__main__":
    main()
