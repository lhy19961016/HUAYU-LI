import pandas as pd
import numpy as np
import urllib.request
import os
import pickle

URL = 'http://localhost:9527/'


def File_Reader(file_R, num):
    Reader = pd.read_csv(file_R, sep=';', encoding='iso-8859-1')
    data_R = Reader.iloc[0:num, :]
    Reader_Arr = np.array(data_R)
    Reader_List = Reader_Arr.tolist()
    Pack_Data = pickle.dumps(Reader_List)
    return Pack_Data


def http_post(url, file_pickle):
    headers = {'User-Agent': 'User-Agent:Mozilla/5.0'}
    req = urllib.request.Request(url, data=file_pickle, headers=headers)
    response = urllib.request.urlopen(req)
    return response.read()


Num = int(input('Enter the quantity of the tweets:'))
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
# --------------------Check file's existence----------------
Size_data = os.path.getsize(File_Path)
if int(Size_data) == 0 and int(Size_data) < 0:
    print("error")
else:
    print("Verification completed")
# -----------Check file's size----------------
Command = input('Enter the command:')
if Command != 'STAT' and Command != 'ENTI':
    while 1:
        print('Your Command is not in the list of Command,Please enter it again')
        Command = input('enter again:')
        try:
            if Command == 'STAT' and 'ENTI':
                break
        except:
            pass
# --------------Check Command--------
File_Ready_For_Sending = File_Reader(File_Path, Num)
Resp_Data = http_post(URL, File_Ready_For_Sending)
print(Resp_Data)
