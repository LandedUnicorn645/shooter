import pygame, socket, pickle

class Server:
    '''a simple server class that '''
    def __init__(self):
        self.sock = socket(AF_INET, SOCK_STREAM)
        self.win = #window
        self.screenwidth = 1000
        self.screenheight = 1000
        self.clients = []

    def getClients(self):
        server_addr = (ip, port)
        self.sock.bind(server_addr)
        self.socket.listen(2)
        while len(self.clients) < 2:
            client, client_Addr = socke.accpet()
            self.clients.append((client,client_addr))
            #start a thread that listens for info from client

    def recievingData(self, client, addr):
        while True:
            recievedata = client.recv(pickle.loads(4096))
            if recievedata:
                if recievedata[0] == "move":
                    self.checkMove(client, recievedata)
                elif recievedata[0] == "shoot":
                    self.shoot(client, recievedata)

    def checkMove(self, client, data):
        size = 40
        if data[1] == "x":
            x = self.clients[client].x
            if x >= 5 and x + size <= self.settings.screenwidth:
                #update x value and move it
        elif data[1] == "y":
            y = self.clients[client].y
            if y > 5 and y + size <= self.settings.screenheight:
                #update y value and draw it

    
