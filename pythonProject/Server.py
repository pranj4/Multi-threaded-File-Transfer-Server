import os
import threading
import socket

IP = socket.gethostbyname(socket.gethostname())
PORT = 4466
ADDR = (IP, PORT)
SIZE = 1024
FORMAT = 'UTF-8'
SERVER_DATA_PATH = "Server_data"

if not os.path.exists(SERVER_DATA_PATH):
    os.makedirs(SERVER_DATA_PATH)

def handle_client(conn, addr):
    print(f"New Connection {addr} is connected")
    conn.send("OK@welcome to the file server".encode(FORMAT))

    while True:
        data = conn.recv(SIZE).decode(FORMAT)
        data = data.split("@")
        cmd = data[0]
        print(cmd)

        if cmd.lower() == "help":
            send_data = "OK@"
            send_data += "LIST: list all the files on the server. \n"
            send_data += "UPLOAD <path>: Upload a file to the server. \n"
            send_data += "DELETE <filename>: Delete a file from the server. \n"
            send_data += "LOGOUT: Disconnect from the server. \n"
            send_data += "HELP: List all the commands"
            conn.send(send_data.encode(FORMAT))

        elif cmd.lower() == "logout":
            break

        elif cmd.lower() == "list":
            files = os.listdir(SERVER_DATA_PATH)
            send_data = "OK@"

            if len(files) == 0:
                send_data += "The server directory is empty."
            else:
                send_data += "\n".join(f for f in files)
            conn.send(send_data.encode(FORMAT))

        elif cmd.lower() == "upload":
            name, text = data[1], data[2]
            filepath = os.path.join(SERVER_DATA_PATH, name)
            with open(filepath, "w") as f:
                f.write(text)

            send_data = "OK@File uploaded successfully."
            conn.send(send_data.encode(FORMAT))

        elif cmd.lower() == "delete":
            name = data[1]
            filepath = os.path.join(SERVER_DATA_PATH, name)
            if os.path.exists(filepath):
                os.remove(filepath)
                send_data = "OK@File deleted successfully."
            else:
                send_data = "ERROR@File not found."
            conn.send(send_data.encode(FORMAT))

    conn.close()
    print(f"[DISCONNECTED] {addr} disconnected")

def main():
    print("Server is starting")
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(ADDR)
    print("Server is now listening")
    server.listen()

    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()

if __name__ == "__main__":
    main()
