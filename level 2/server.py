import socket
import google.generativeai as genai
import os
import json
import time
import threading

genai.configure(api_key="AIzaSyCaEnBYA49l5S-nhvuFabjS_9X_LrBps-U")
model = genai.GenerativeModel('gemini-1.5-flash')
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
hostname = socket.gethostname()
ip_address = socket.gethostbyname(hostname)
port = 12345
server_socket.bind((ip_address, port))
server_socket.listen(5)

print(f"Server listening on {ip_address}:{port}")

def handle_client(client_socket, client_address):
    print(f"Connection from {client_address}")
    data = []
    prompts = client_socket.recv(1024)
    prompts = prompts.decode()
    prompts = json.loads(prompts)
    print(f"Received prompts: {prompts}")

    for prompt in prompts[1]:
        time_sent = time.time()
        print('Sent Request')
        response = model.generate_content(prompt)
        print('Got Response')
        time_rec = time.time()

        response_text = response.text if hasattr(response, 'text') else str(response)
        data.append(
            {
                "Prompt": prompt,
                "Message": response_text,
                "TimeSent": time_sent,
                "TimeRecvd": time_rec,
                "Source": "Gemini",
                "ClientID": prompts[0]
            }
        )
    json_out = json.dumps(data)
    client_socket.send(json_out.encode())
    client_socket.close()

while True:
    client_socket, client_address = server_socket.accept()
    client_thread = threading.Thread(target=handle_client, args=(client_socket, client_address))
    client_thread.start()
