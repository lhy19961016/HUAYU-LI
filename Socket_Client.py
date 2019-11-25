# coding:utf-8

import socket
import pandas as pd
import pickle
import os


def File_Reader(file_R):
    Reader = pd.read_csv(file_R, sep=';', encoding='iso-8859-1')
    Reader_1 = Reader.iloc[0:7, ]
    Pack_Data = pickle.dumps(Reader_1)
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
client = socket.socket()
client.connect(('127.0.0.1', 8008))
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
    File_Byte = File_Reader(File_Path)
    Size_File_Byte = os.stat(File_Path).st_size
    # ----------------Send the Command and Size_File-------e.g:"STAT9999999(999...is size of the file
    client.send((request + str(Size_File_Byte)).encode('utf-8'))  # 1->
    # ---------------------From server client get the"Get the size and command"-------------
    received_MSG_1 = client.recv(4096)  # 2<-
    print(received_MSG_1.decode())
    # ------------------------Client send the data to Server for processing-----
    client.send(File_Byte)  # 3->
    # ---------------------Get the Size of Returned file and the file after pickling-------------------
    Size_Returned_File = client.recv(4096)  # 4<-
    Count_Rest_Data = 0
    Data_Get = []
    # -------We have made sure about the files need to STAT or ENTI on server,so there is only one situation
    while Count_Rest_Data < int(Size_Returned_File.decode()):
        Data_Returned = client.recv(4096)  # 5<-
        Data_Get.append(Data_Returned)
        Data_Get += Data_Returned

    Data_Returned_Unpickle = pickle.loads(b"".join(Data_Get))
    Data_Returned_Unpickle.to_csv(r'./' + request + '_data.csv', encoding='iso-8859-1')

    client.close()
