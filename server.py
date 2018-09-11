import pygame, socket, pickle

class Server:
    '''Server class that connects multiple clients and checks and verifies
        actions done by the users

        Atrributes :
            sock - the sock that connects to all the clients and listens for data
            screenwidth - the width of the window that the game is on
            screenheight - the height of the window that the game is on
            clients - a list of client objects that are connected

        Methods :
            getClients - accepts the clients and creates a thread to listen for incoming data
            recieveDate - for each client, listens for incoming data and verifies the data
            checkMove - verifies the data sent if the client moves

            '''
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
            client, client_addr = socke.accpet()
            client = Client(client, client_addr)
            self.clients.append(client)
            #start a thread that listens for info from client

    def recievingData(self, client):
        while True:
            recievedata = client.recv(pickle.loads(4096))
            if recievedata:
                if recievedata[0] == "move":
                    self.checkMove(client, recievedata)
                elif recievedata[0] == "shoot":
                    self.shoot(client, recievedata)
                self.sendData(recievedata)

    def checkMove(self, client, data):
        size = client.size
        if data[1] == "x":
            x = data[2]
            if x >= 5 and x + size <= self.settings.screenwidth - 5:
                client.x = x
        elif data[1] == "y":
            y = data[2]
            if y > 5 and y + size <= self.settings.screenheight - 5:
                client.y = y
