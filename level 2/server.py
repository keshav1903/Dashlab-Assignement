# Server.py

import socket
import google.generativeai as genai
import os
import json
import time

genai.configure(api_key="AIzaSyCaEnBYA49l5S-nhvuFabjS_9X_LrBps-U")

model = genai.GenerativeModel('gemini-1.5-flash')


server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


hostname = socket.gethostname()
ip_address = socket.gethostbyname(hostname)


port = 12345


server_socket.bind((ip_address, port))


server_socket.listen(5)

print(f"Server listening on {ip_address}:{port}")

while True:
  
    client_socket, client_address = server_socket.accept()
    print(f"Connection from {client_address}")
    genai.configure(api_key="AIzaSyCaEnBYA49l5S-nhvuFabjS_9X_LrBps-U")

    model = genai.GenerativeModel('gemini-1.5-flash')


    data = []
    promts = client_socket.recv(1024)
    promts = promts.decode()
    promts = json.loads(promts)
    print(f"Received prompts: {promts}")

    for prompt in promts[1]:
        time_sent = time.time()
        print('Sent Req')
        response = model.generate_content(prompt)
        print('Got Res')
        time_rec = time.time()

        response_text = response.text if hasattr(response, 'text') else str(response)

        data.append(
            {
                "Prompt" : prompt,
                "Message": response_text,
                "TimeSent": time_sent,
                "TimeRecvd" : time_rec,
                "Source" : "Gemini",
                "CientID": promts[0]
            }
        )



    json_out = json.dumps(data)
    client_socket.send(json_out.encode())

    client_socket.close()