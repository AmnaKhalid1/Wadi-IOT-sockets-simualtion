# -*- coding: utf-8 -*-
"""
Server

purpose\    - recieve information of wadies from sensors
            - send wadies information to user interface
"""

from socket import *

# asign wadi information to their sensor ip
wadi = {'127.0.0.1':['Wadi Bani Khalid'], 
       '127.0.0.2':['Wadi Shab'],
       '127.0.0.3':['Wadi Al-Abyad'], 
       '127.0.0.4':['Wadi Al-Hawqin'], 
       '127.0.0.5':['Wadi Dayqah'], 
       '127.0.0.6':['Wadi Fida'], 
       '127.0.0.7':['Wadi Al-Arabiyin'], 
       '127.0.0.8':['Wadi Dam'], 
       '127.0.0.9':['Wadi Tiwi'], 
       '127.0.0.10':['Wadi Al-Ta’iyin']}

# sensor ip numbers
ips = [ip for ip in wadi.keys()]

# user interface ip number
UI_IP = '127.0.0.11'

# server port and name
serverPort = 65000
serverName = 'localhost'

# creat server socket
serverSocket = socket(AF_INET, SOCK_STREAM) 

# bind server socket
serverSocket.bind((serverName,serverPort))

# listen to incoming TCP requests
serverSocket.listen(1) 

while True:
    
     # creat connection socket after request coming 
     connectionSocket, addr = serverSocket.accept() 
     
     # if socket ip is sensor socket
     if addr[0]  in ips:    
         
         #recieve data from the sensor
         data = connectionSocket.recv(1024).decode()
         
         # put wadi's data in a list
         values = data.split(',')
         
         # update wadi information
         wadi[addr[0]] = values

     # if ip socket is the UI ip
     elif addr[0] == UI_IP :
         
         # put wadies information in a nested list
         nested_list = list(wadi.values())
         
         # save data as string
         data = ""
         for w in nested_list :
             one = ""
             for info in w :
                 one += info+","
            
             data+= one 
         
            # send data to UI
         connectionSocket.send(data.encode())
     
     # close connection socket 
     connectionSocket.close()
     
         