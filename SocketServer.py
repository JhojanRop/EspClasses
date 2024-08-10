import socket


class SocketServer:
    def __init__(self, ipv4, port, timeout=None):
        self.ipv4 = ipv4
        self.port = port
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        if timeout:
            self.server.settimeout(timeout)


    def start(self):
        try:
            self.server.bind((self.ipv4, self.port))
            self.server.listen(5)
            print(f"Server is listening at port {self.ipv4}:{self.port}...")
            return True
        except Exception as e:
            print(f"Error starting server: {e}. Exiting...")
            self.server.close()
            return False


    def accept(self):
        conn, addr = self.server.accept()
        print(f"Request recive from {addr[0]}:{addr[1]}")
        return conn, addr
    

    def send(self, conn, data):
        try:
            conn.send(data)
            return True
        except Exception as e:
            print(f"Error sending data: {e}")
            return False


    def receive(self, conn, size):
        try:
            data = conn.recv(size)
            return data
        except Exception as e:
            print(f"Error receiving data: {e}")
            return None


    def close(self, conn):
        try:
            conn.close()
            return True
        except Exception as e:
            print(f"Error closing connection: {e}")
            return False