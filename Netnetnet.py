class Server:
    ip_pull = 2
    ip_router = 0
    router = ''

    def __init__(self):
        self.ip = Server.ip_pull
        self.buffer = []
        router_ip = 1
        Server.ip_pull += 1

    def send_data(self, data):
        print('123')
        if self in Server.router.lst:
            print('321')
            print(Server.router.buffer)
            Server.router.buffer.append(data)
            print(Server.router.buffer)


    def get_data(self):
        self.buffer_dub = self.buffer
        self.buffer = []
        return self.buffer_dub

    def get_ip(self):
        return self.ip
class Router:

    def __init__(self):
        self.lst = []
        self.buffer = []
        Server.router = self

    def link(self, server):
        self.lst.append(server)

    def unlink(self, server):
        self.lst.remove(server)

    def send_data(self):
        print(self.buffer)
        self.buffer = []

class Data:

    def __init__(self, data, ip):
        self.data = ''
        self.ip = 0

b = Server()
c = Router()
c.link(b)
data = Data("Hi", 0)
b.send_data(data)