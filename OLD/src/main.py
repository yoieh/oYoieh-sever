import pygame
import sys
import os
import socket
import time
import threading
import random
import socket
from pygame.locals import *
from UserSQL import *


class startServer():
    def downloadSQL(self):
        self.SQLUserDatabase = SQLUserDatabase()
        self.selectUsers = self.SQLUserDatabase.selectUsers()

        self.selectUsers
        self.userDB = self.SQLUserDatabase.userDB

        #(16 * 50) * (16 * 25)

    def createLists(self):
        pass


class main():

    startServer = startServer()
    startServer.downloadSQL()

    running = True
    while running:
        pass


if __name__ == "__main__":
    main()
    # cProfile.run("main()")
    sys.exit()
