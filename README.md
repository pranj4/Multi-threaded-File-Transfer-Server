Client-Server File Transfer Protocol
This project implements a basic client-server file transfer protocol using Python. The server allows multiple clients to connect and perform various file operations such as uploading, downloading, listing, and deleting files. The client interacts with the server using predefined commands.

Features
Multi-threaded Server: Handles multiple client connections simultaneously.
File Operations: Supports file upload, download, listing, and deletion.
Command-based Interaction: Clients communicate with the server using specific commands.

Usage
Server
Start the server:
python server.py

Client
Run the client:

python client.py


Use the following commands:

HELP: List all available commands.
LIST: List all files on the server.
UPLOAD <path>: Upload a file to the server.
DELETE <filename>: Delete a file from the server.
LOGOUT: Disconnect from the server.
