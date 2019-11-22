# coding:utf-8

import socket
import pandas as pd


data = pd.read_csv('G:/dataSet.csv', sep=';', encoding='iso-8859-1')  # Open the csv file
client = socket.socket()
client.connect(('localhost', 8887))
request = input('Enter request:')

while True:
    client.send(request.encode('utf-8'))
    client.recv(1024)
    client.send(data.encode('utf-8'))
    request_res_size = client.recv(1024)
    print('Size of data:', request_res_size)
    client.send('Ready for receiving '.encode('utf-8'))
    received_size = 0
    received_data = b''
    while received_size < int(request_res_size.decode()):
        if request == 'STAT':
            received_data.to_csv(r'G:\Stat_data.csv', encoding='iso-8859-1')
            data = client.recv(1024)
            received_size += len(data)
            received_data += data
        elif request == 'ENTI':
            received_data.to_csv(r'G:\Enti_data.csv', encoding='iso-8859-1')
            data = client.recv(1024)
            received_size += len(data)
            received_data += data
    else:
        print('transmission has done!')

client.close()
