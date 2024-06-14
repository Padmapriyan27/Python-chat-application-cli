# Python Chat Application (CLI)

This is a simple command-line chat application for linux implemented in Python using sockets and threading. The application consists of a server and multiple clients that can connect to the server to send and receive messages in real-time.

## Features

- Multiple clients can connect to the server simultaneously.
- Messages sent by any client are broadcasted to all other connected clients.
- Clients can gracefully exit the chat by sending "quit" or "exit".
- Server handles each client connection in a separate thread for concurrent communication.

## Prerequisites

- Python 3.x installed on your system.

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/Padmapriyan27/Python-chat-application-cli.git
    cd Python-chat-application-cli
    ls
    cd chat-application
    ls
    ```

2. Ensure you have Python 3 installed. You can check your Python version with:
    ```bash
    python --version
    ```

## Usage

### Starting the Server

1. Open a terminal and navigate to the repository directory.
2. Start the server:
    ```bash
    python server.py
    ```
3. The server will start listening for incoming connections on the specified port.

### Starting a Client

1. Open a new terminal window.
2. Navigate to the repository directory.
3. Start a client:
    ```bash
    python client.py
    ```
4. Enter your name when prompted. Ensure each client uses a unique name.
5. Start sending messages. All messages will be broadcasted to other connected clients.
6. Type "quit" or "exit" to leave the chat.

### Example

1. Start the server:
    ```bash
    python server.py
    ```
    Output:
    ```
    Server listening for connections...
    ```

2. Start a client in a new terminal:
    ```bash
    python client.py
    ```
    Output:
    ```
    Enter your name: Alice
    ```

3. Start another client in a new terminal:
    ```bash
    python client.py
    ```
    Output:
    ```
    Enter your name: Bob
    ```

4. Now, Alice and Bob can chat with each other. If Alice sends a message:
    ```
    Alice: Hello, Bob!
    ```

   Bob will see:
    ```
    Alice: Hello, Bob!
    ```

5. If Bob wants to exit, he can type "exit" or "quit":
    ```
    Bob: exit
    ```

   Alice will see:
    ```
    Bob has left the chat room.
    ```

## Files

- `chat-application`: The folder.
- `server.py`: The server-side script.
- `client.py`: The client-side script.
- `README.md`: This readme file.


