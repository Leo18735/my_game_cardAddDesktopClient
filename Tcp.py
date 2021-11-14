import socket


class Tcp:
    def __init__(self, ip, port):
        self._ip: str = ip
        self._port: int = port

    def send(self, data: str) -> None:
        try:
            print(self._ip)
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.connect((self._ip, self._port))
            sock.sendall(data.encode(encoding="utf-8"))
            sock.close()
        except (socket.gaierror, TimeoutError):
            raise Exception("Wrong ip")
        except ConnectionRefusedError:
            raise Exception("Wrong ip or port")
        except Exception as e:
            raise Exception("New exception: " + str(e) + str(type(e)))
        return

    def receive(self):
        raise NotImplementedError()

    def send_receive(self):
        raise NotImplementedError()

    def receive_send(self):
        raise NotImplementedError()
