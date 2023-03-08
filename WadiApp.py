import tkinter as tk
from tkinter import ttk
from tkinter import * 
from tkinter.ttk import *
from PIL import Image, ImageTk
from random import randint

from socket import *


ports_used = [65000]

def getPort ():
    port = randint(0, 65535)
    done = False
    while  not done :
        port = randint(0, 65535)
        if  port%3 == 0 and port  not in ports_used:
            done = True
            
    ports_used.append(port)
    return port

def GetWadiInfo ():
    serverName = 'localhost'
    serverPort = 65000

    #creat client socket
    clientSocket = socket(AF_INET, SOCK_STREAM)

    clientSocket.bind(('127.0.0.11',getPort ()))
    
    #connect to the server
    clientSocket.connect((serverName,serverPort))

    All_wadis = clientSocket.recv(1024).decode().split(",")
    
    
    All_wadis_lists = []#nested list
    #split the wadis each wadi a list
    for i in range (0,len(All_wadis)-1,6):
        
        All_wadis_lists.append(All_wadis[i: i+6])
        
    
    clientSocket.close()
    return All_wadis_lists
        

class FirstPage(tk.Tk):
    def refresh (self):
        #get from the server the data 
        self.wadis = GetWadiInfo ()
        
    def wadi_1 (self,titles, info,clicked):
        titles.config(foreground ="#012030" )
        info.config(foreground ="#012030" )
      
       
        
        
        text = clicked.get()
        for wadi in self.wadis:
            if wadi[0].strip() == text.strip():
                
                flow = 'Yes'
                if wadi[5] == '0':
                    flow = 'No'
                    wadi_info = "\n"+wadi[0]+"\n"+wadi[1]+"\n"+wadi[2]+"\n"+wadi[3]+" Km/hr"+"\n"
                    wadi_info += wadi[4]+" m"+"\n"+flow+"\n"
                else:
                    wadi_info = "\n"+wadi[0]+"\n"+wadi[1]+"\n"+wadi[2]+" C"+"\n"+wadi[3]+" Km/hr"+"\n"
                    wadi_info += wadi[4]+" m"+"\n"+flow+"\n"
                
                info.config(foreground ="#012030" ,text=wadi_info)
         
      
        
    def popupmsg():
        popup = tk.Tk()
        popup.wm_title("Hello")
        popup.configure(bg="white")
        #open logo image and assign it to a button
        image = Image.open('logo.png')
        python_image = image.resize((200,200), Image.ANTIALIAS)
        python_image = ImageTk.PhotoImage(python_image )
        font =('times', 50, 'bold')
        logo = tk.Button(popup,image = python_image ,borderwidth=0,bg="white")
        logo.grid(row = 0, column = 1,padx = 30, pady = 10)
        
        #set the labels of the first page
        msg ="WadiApp is \n a water monitoring system"
        label = tk.Label(popup, text=msg, font=('times', 50, 'bold'), justify="center",bg="white", fg="#012030")
        label.grid(row = 1, column = 1 ,padx = 15, pady =5)
        button2 =tk.Button(popup, text ="Let's get started",bg="#13678A",fg="#9AEBA3"
                ,height = 1 , width = 13,font= ("Times", 30, "bold"), command = popup.destroy)
	
		# putting the button in its place by
		# using grid
        button2.grid(row = 2, column = 1 ,padx = 15, pady =25)
        
        popup.mainloop()
        
    def __init__(self):
        #initialize the wadi data 
        self.wadis = GetWadiInfo ()
        #call first page 
        FirstPage.popupmsg()
        super().__init__()
        #configure the window settings
        self.title("Wadi App")
        self.geometry("1300x1000")
        self.resizable(0,0)
        self.configure(bg="white")
        
        #the logo image opended 
        self.image = Image.open('logo.png')
        self.python_image = self.image.resize((200,200), Image.ANTIALIAS)
        self.python_image = ImageTk.PhotoImage(self.python_image )
        font =('times', 40, 'bold')
        #asign the logo image to a button
        logo = tk.Button(self,image = self.python_image ,borderwidth=0,bg="white",
                       command = lambda : self.tkraise())
        logo.grid(row = 0, column = 0,padx = 30, pady = 0,sticky ="W")
        
     
		# label of frame Layout 2
		
        label = ttk.Label(self,background="white" ,justify = "left",text ="Choose a wadi \n to check :"
                         
                          , font = ("times",20,"bold") ,foreground ="#012030")
        
		# putting the grid in its place by using grid
        label.grid( row = 1, column = 0,padx = 1, pady =1)
        
        
        info = ttk.Label(self,background="white" ,justify = "center",text =""
                         
                          , font = font ,foreground ="#012030")
        
		# putting the grid in its place by using grid
        info.grid( row = 2, column = 4,padx = 10, pady =10)
        
         
        
        titles = ttk.Label(self,background="white" ,justify = "center",
                      text ="Name :\nRegion:\nTemperature:\nSpeed: \nLevel:\nFlow :"
                         
                          , font = ('times', 20, 'bold') ,foreground ="white")
        
		# putting the grid in its place by using grid
        titles.grid( row = 1, column = 3,columnspan =3,padx = 300, pady =10,sticky="W")
        
        r_ = ttk.Label(self,background="white" ,justify = "center",text =""
                         
                          , font = ('times', 20) ,foreground ="white")
        
		# putting the grid in its place by using grid
        r_.grid( row = 1, column = 3,padx = 1, pady =1,sticky="E")
        
        

  
        # Dropdown menu options
        options = [
            'Wadi Bani Khalid',
            'Wadi Shab',
            'Wadi Al-Abyad',
            'Wadi Al-Hawqin',
            'Wadi Dayqah',
            'Wadi Fida', 
            'Wadi Al-Arabiyin',
            'Wadi Dam',
            'Wadi Tiwi',
            'Wadi Al-Ta’iyin'
        ]
          
        # datatype of menu text
        clicked = StringVar()
          
        # initial menu text
        clicked.set( "'Wadi Bani Khalid'" )
          
        # Create Dropdown menu
        drop = OptionMenu( self , clicked , *options)
        drop.grid( row = 2, column = 0,padx = 100, pady =10, sticky="W")
                
        

		# putting the grid in its place by using grid
        button2 = tk.Button(self, text ="Check",bg="#13678A",fg="white"
                ,height = 1 , width = 5,font= ("Times", 20),
		command = lambda :self.wadi_1(titles,r_,clicked) )
	
		# putting the button in its place by using grid
        button2.grid(row = 3, column = 0 ,padx = 5, pady =5)
        
        
        # putting the grid in its place by using grid
        button3 = tk.Button(self, text ="Refresh",bg="#13678A",fg="white"
                ,height = 1 , width = 5,font= ("Times", 20),
		command = lambda :self.refresh() )
	
		# putting the button in its place by using grid
        button3.grid(row = 4, column = 0 ,padx = 5, pady =5)
        
        
        Wadi_info = ttk.Label(self,background="white" ,justify = "left",text ="Wadi information:"
                         
                          , font = ("times", 35) ,foreground ="#012030")
        
		# putting the grid in its place by using grid
        Wadi_info.grid( row = 0, column = 3,padx = 200, pady =10, sticky="E")
        #vertical line
        ttk.Separator(self, orient=VERTICAL).grid(column=2, row=0, rowspan=7, sticky='ns')
       
  
if __name__ == '__main__':   

    # Driver Code
    app = FirstPage()
    app.mainloop()	
    