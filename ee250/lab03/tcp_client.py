"""
Server receiver buffer is char[256]
If correct, the server will send a message back to you saying "I got your message"
Write your socket client code here in python
Establish a socket connection -> send a short message -> get a message back -> ternimate
use python "input->" function, enter a line of a few letters, such as "abcd"
"""
# Aaron Sesay
"https://github.com/usc-ee250-spring2021/lab02-footballman7.git"
import socket
import sys
HOST = '52.137.113.211'
PORT = 8080
#My azureuser is sesay
def main():
    
    # TODO: Create a socket and connect it to the server at the designated IP and port
    
    # TODO: Get user input and send it to the server using your TCP socket
    
    # TODO: Receive a response from the server and close the TCP connection


	
		with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
			s.connect((HOST, PORT))
			user = input("Give an input: ")
			s.sendall(user.encode())
			data = s.recv(1024)

		print('Received',repr(data))

if __name__ == '__main__':
    main()
