import pandas as pd
import numpy as np
import urllib.request
import os
import json

URL = 'http://127.0.0.1:8000/'


def File_Reader(file_R, num):
    Reader = pd.read_csv(file_R, sep=';', encoding='iso-8859-1')
    data_R = Reader.iloc[0:num, :]
    Reader_Arr = np.array(data_R)
    Reader_List = Reader_Arr.tolist()
    Pack_Data = json.dumps(Reader_List)
    return Pack_Data


def http_post(url, file_json):
    req = urllib.request.Request(url, file_json)
    response = urllib.request.urlopen(req)
    return response.read()


Num = int(input('Enter the quantity of the tweets:'))
print('Enter the path of the file:')
File_Path = input()
Size_data = os.path.getsize(File_Path)
if int(Size_data) == 0 and int(Size_data) < 0:
    print("error")
else:
    print("Verification completed")
# -----------Check files----------------
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
