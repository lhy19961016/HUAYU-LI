# coding:utf-8

import socket
import pandas as pd
import pickle
import os
import time


def File_Reader(file_R):
    Reader = pd.read_csv(file_R, sep=';', encoding='iso-8859-1')
    Pack_Data = pickle.dumps(Reader)
    return Pack_Data


print('Enter the path of the file:')
File_Path = input()
if not os.path.exists(File_Path):
    while 1:
        print('File do not exist,please enter again')
        File_Path = input('Enter again:')
        try:
            if os.path.exists(File_Path):
                break
        except:
            pass


Stream_Data = File_Reader(File_Path)
client = socket.socket()
client.connect(('127.0.0.1', 8898))
request = input('Enter request:')
while True:
    if request != 'STAT' and request != 'ENTI':
        while 1:
            print('Your Command is not in the list of Command,Please enter it again')
            request = input('enter again:')
            try:
                if request == 'STAT' and 'ENTI':
                    break
            except:
                pass
    client.send(request.encode('utf-8'))
    client.recv(1024)
    time.sleep(2)
    client.send(Stream_Data)
    request_res_size = client.recv(1024)
    print('Size of data:', request_res_size)
    client.send('Ready for receiving '.encode('utf-8'))
    received_size = 0
    received_data = b''
    while received_size < int(request_res_size.decode()):
        if request == 'STAT':
            received_data = pickle.loads(received_data)
            received_data.to_csv(r'G:\Stat_data.csv', encoding='iso-8859-1')
            data = client.recv(1024)
            received_size += len(data)
            received_data += data
        elif request == 'ENTI':
            received_data = pickle.loads(received_data)
            received_data.to_csv(r'G:\Enti_data.csv', encoding='iso-8859-1')
            data = client.recv(1024)
            received_size += len(data)
            received_data += data
    else:
        print('transmission has done!')

client.close()
