import pandas as pd
import requests
import os
import pickle
import time

URL = 'http://127.0.0.1:54878/'

def File_Reader(file_R, num):
    Reader = pd.read_csv(file_R, sep=';', encoding='iso-8859-1')
    data_R = Reader.iloc[0:num, :]
    Pack_Data = pickle.dumps(data_R)
    return Pack_Data


Num = int(input('Enter the quantity of the tweets:'))
print('Enter the path of the file:')
File_Path = input()

Data_Ready_For_Sending = File_Reader(File_Path, Num)
Size_data = os.path.getsize(File_Path)
if int(Size_data) == 0 and int(Size_data) < 0:
    print("error")
else:
    print("Verification completed")

Command = input('Enter the command:')
if Command != 'STAT' and Command != 'ENTI':
    print('Your Command is not in the list of Command,Please enter it again')
    Command = input('enter again:')

rst = requests.request("POST", URL + Command, data=Data_Ready_For_Sending)

time.sleep(2)
Get_Data = pickle.loads(rst.content)
print("please enter the path of the file for saving Getting data")
File_Getting_Path = input()
Get_Data.to_csv(File_Getting_Path, sep=';', encoding='iso-8859-1')
