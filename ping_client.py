# -*- coding: utf-8 -*-
"""ping_client.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1xZZQRBlHNSEupVKRdI-vd8X21D9e8mcv
"""

import socket

# Function to send ping request
def sendPing():
  s=socket.socket()

  # Server port
  port = 7000

  #connect to server on a local machine
  s.connect(('127.0.0.1',port))
  print("Client successfully connected to server: " +" \n")
  
  #send ping message
  message =input("Enter your message")
  s.send(message.encode())

  # Receive response from server
  message=s.recv(1024).decode()
  print(message)
  s.close()

# Driver function
if __name__ == '__main__':

  #Trigger Ping client
  sendPing()
