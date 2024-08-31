import google.generativeai as genai
import time
import os
import json

genai.configure(api_key="AIzaSyCaEnBYA49l5S-nhvuFabjS_9X_LrBps-U")

model = genai.GenerativeModel('gemini-1.5-flash')

data = []
with open('input.txt', 'r') as file:
    for line in file:
        temp = {
            "Prompt": line.strip(),
            "Message": '',
            "TimeSent": time.time(),
            "TimeRecvd": 0,
            "Source": 'Gemini'
        }
        print('Sent Req')
        response = model.generate_content(line.strip())
        print('Got Res')


        temp['TimeRecvd'] = time.time()
        temp['Message'] = response.text
        data.append(temp)

with open('output.json', 'w') as file:
    json.dump(data, file, indent=4)

print("JSON data has been written to output.json")


# print(response.text)