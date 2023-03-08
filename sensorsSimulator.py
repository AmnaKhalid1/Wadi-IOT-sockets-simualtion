# -*- coding: utf-8 -*-
"""
Wadi Water Sensors Simulator
"""

from socket import *
from random import randint
from threading import Thread
import time

'''
sensor senses values of wadi and send it to server
prameters/  name(string) name of wadi
            region(string) the region where wadi is
            ip(string) ip number of the sensor
            port(int) port number
'''
class sensor:
    def __init__(self, name, region, ip, port):
        self.name = name
        self.region = region
        self.ip = ip
        self.port = port
        self.temp = 'None'
        self.speed = 0
        self.level = 0
        self.exist = 0
    
    # sense values of the wadi    
    def sense(self):
        self.exist = randint(0, 1)
        if self.exist == 1:
            self.temp = randint(5, 25)
            self.speed = randint(100, 120)
            self.level = randint(1, 6)
    
    # send values to server
    def send(self):
        serverName = 'localhost'
        serverPort = 65000

        #creat client socket
        clientSocket = socket(AF_INET, SOCK_STREAM)

        clientSocket.bind((self.ip, self.port))
        
        #connect to the server
        clientSocket.connect((serverName,serverPort))

        data = self.name + ',' + self.region + ',' + str(self.temp) + ',' + str(self.speed) + ',' + str(self.level) + ',' +str(self.exist)

        # send values to server
        clientSocket.send(data.encode())

        clientSocket.close()
        
        return
    
    # enter to priority queue according to existence of flow
    def queue(self, array):
        array.append(self)
        array.sort(reverse = True)
    
    # necessary functions to make object combarable
    def __lt__(self, obj):
        return ((self.exist) < (obj.exist))
  
    def __gt__(self, obj):
        return ((self.exist) > (obj.exist))
  
    def __le__(self, obj):
        return ((self.exist) <= (obj.exist))
  
    def __ge__(self, obj):
        return ((self.exist) >= (obj.exist))
  
    def __eq__(self, obj):
        return (self.exist == obj.exist)
    
    
def main():
    
    # list of used port numbers
    ports_used = [65000]
    
    # generate new port number in each call to avoid the only usage of ports error
    def getPort():
        port = randint(0, 65535)
        done = False
        while  not done :
            port = randint(0, 65535)
            if  port%2 == 0 and port  not in ports_used:
                done = True
                
        ports_used.append(port)
        return port
    
    # pririty queue of sensors
    priorityQueue = []
    
    # create list of sensors
    sensors = [sensor('Wadi Bani Khalid','Ash-Sharqiyyah','127.0.0.1', getPort ()),
               sensor('Wadi Shab','Ash-Sharqiyyah','127.0.0.2', getPort ()),
               sensor('Wadi Al-Abyad','Al-Batinah','127.0.0.3', getPort ()),
               sensor('Wadi Al-Hawqin','Al-Batinah','127.0.0.4', getPort ()),
               sensor('Wadi Dayqah','Musqat','127.0.0.5', getPort ()),
               sensor('Wadi Fida','Ad-Dhahirah','127.0.0.6', getPort ()),
               sensor('Wadi Al-Arabiyin','Musqat','127.0.0.7', getPort ()),
               sensor('Wadi Dam','Ad-Dhahirah','127.0.0.8', getPort ()) ,
               sensor('Wadi Tiwi','Ash-Sharqiyyah','127.0.0.9', getPort ()),
               sensor('Wadi Al-Ta’iyin','Ash-Sharqiyyah','127.0.0.10', getPort ())]
    
    # let sensors sense then enter to priority queue
    for s in sensors:
        s.sense()
        s.queue(priorityQueue)
    
    # send data sensed by sensors to server according to priority queue
    while priorityQueue:
        s = priorityQueue.pop(0)
        s.send() 

main()