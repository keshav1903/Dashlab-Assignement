import socket
import time
import json

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

hostname = socket.gethostname()
ip_address = socket.gethostbyname(hostname)

port = 12345

client_socket.connect((ip_address, port))

prompts =['Client1', [
    'What is an operating system?',
    'What is the OSI model?',
    'Who was Alan Turing?',
    'How do computer networks work?'
]]

json_message = json.dumps(prompts)
client_socket.send(json_message.encode())

 
response_data = b''
while True:
    part = client_socket.recv(4096)  
    response_data += part
    if len(part) < 4096:  
        break

response = response_data.decode()
response = json.loads(response)

with open('output1.json', 'w') as file:
    json.dump(response, file, indent=4)

print("Client 1 done")

client_socket.close()
