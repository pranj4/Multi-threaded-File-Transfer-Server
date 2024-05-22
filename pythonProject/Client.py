import socket

IP = socket.gethostbyname(socket.gethostname())
PORT = 4466
ADDR = (IP, PORT)
SIZE = 1024
FORMAT = 'UTF-8'

def main():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(ADDR)

    while True:
        data = client.recv(SIZE).decode(FORMAT)
        cmd, msg = data.split("@")

        if cmd == "OK":
            print(f"{msg}")
        elif cmd == "DISCONNECTED":
            print(f"{msg}")
            break

        data = input(">")
        data = data.split(" ", 1)
        cmd = data[0]

        if cmd.lower() == "help":
            client.send(cmd.encode(FORMAT))
        elif cmd.lower() == "logout":
            client.send(cmd.encode(FORMAT))
            break
        elif cmd.lower() == "list":
            client.send(cmd.encode(FORMAT))
        elif cmd.lower() == "upload":
            path = data[1]
            with open(f"{path}", "r") as f:
                text = f.read()
            filename = path.split("/")[-1]
            send_data = f"{cmd}@{filename}@{text}"
            client.send(send_data.encode(FORMAT))
        elif cmd.lower() == "delete":
            filename = data[1]
            send_data = f"{cmd}@{filename}"
            client.send(send_data.encode(FORMAT))

    print("Disconnected from the server.")
    client.close()

if __name__ == "__main__":
    main()
