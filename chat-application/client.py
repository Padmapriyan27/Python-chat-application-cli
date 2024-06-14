import socket
import threading

HOST = ''
PORT = 7744

# Function to receive messages from server
def receive_messages(client_socket, exit_flag):
    try:
        while not exit_flag.is_set():
            # Receive message from server
            message = client_socket.recv(1024).decode()
            if not message:
                break
            print(message)
    except Exception as e:
        if not exit_flag.is_set():  # Ignore errors if the exit flag is set
            print(f"Error receiving message: {e}")
    finally:
        # Close the client socket
        client_socket.close()

# Main function to start the client
def main():
    # Create socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        # Connect to server
        client_socket.connect((HOST, PORT))

        # Send client's name to server
        name = input("Enter your name: ")
        client_socket.send(name.encode())

        # Flag to indicate exit condition
        exit_flag = threading.Event()

        # Start a thread to receive messages from server
        receive_thread = threading.Thread(target=receive_messages, args=(client_socket, exit_flag))
        receive_thread.start()

        # Send messages to server
        while True:
            message = input()
            client_socket.send(message.encode())

            # If client wants to exit
            if message.lower() in ["quit", "exit"]:
                exit_flag.set()  # Set exit flag to stop receiving thread
                break

    except Exception as e:
        print(f"Error: {e}")

    finally:
        # Close socket and ensure receive thread is joined
        exit_flag.set()
        client_socket.close()
        receive_thread.join()

if __name__ == "__main__":
    main()
