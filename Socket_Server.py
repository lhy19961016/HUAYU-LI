import socket
import pandas as pd
from collections import Counter
import time
from pycorenlp import StanfordCoreNLP
import pickle


# --------------------------Find the 10 popular words in the data-------------
def Top_Words_Stat(data):
    content_tweets = data.iloc[0:-1, 6]
    dic = {}
    for i in content_tweets:
        wordlist = i.replace(",", "").replace("\r\n", " ").replace("\n", " ").split(" ")
        for ele in wordlist:
            if ele not in dic.keys() and ele not in ['', '-'] and '?' not in ele:
                dic[ele] = 1
            elif ele not in ["", "-"] and '?' not in ele:
                dic[ele] += 1
    Sort_Words = Counter(dic)
    Sort_Words = Sort_Words.most_common(10)
    tmp = {"The most Popular words in the tweets": Sort_Words}
    df_tmp = pd.DataFrame(tmp, columns=["The most Popular words in the tweets"])
    return df_tmp


# --------------------------Find the 10 popular tweets with his authors and the number of the retweets in the data-------------
def Top_Tweets_Stat(data):
    tmp = {"Tweet content": [], "User Name": [], "RTs": []}
    data = data.sort_values(by='RTs', ascending=False)
    data = data.reset_index(drop=True)
    for i in range(10):
        tmp["Tweet content"].append(data['Tweet content'].iloc[i])
        tmp["User Name"].append(data['User Name'].iloc[i])
        tmp["RTs"].append(data['RTs'].iloc[i])

    Df_tmp = pd.DataFrame(data=tmp, columns=tmp.keys())
    return Df_tmp


# --------------------------Find the info is the country in tweets and retweets in the data-------------
def Countries_Tweets_Stat(data):
    tmp = {"Latitude": [], "Longitude": []}
    data_LA = data.iloc[0:-1, 9]
    data_LO = data.iloc[0:-1, 10]
    for i in range(len(data)):
        tmp["Latitude"].append(data['Latitude'].iloc[i])
        tmp["Longitude"].append(data['Longitude'].iloc[i])
    Df_tmp = pd.DataFrame(data=tmp, columns=tmp.keys())
    return Df_tmp


# --------------------------Find the 10 popular authors in the data-------------
def Top_Author_Stat(data):
    tmp = {"Popular Author": [], "Followers": []}
    data = data.sort_values(by='Followers', ascending=False)
    data = data.reset_index(drop=True)
    for i in range(10):
        tmp["Popular Author"].append(data['Nickname'].iloc[i])
        tmp["Followers"].append(data['Followers'].iloc[i])

    Df_tmp = pd.DataFrame(data=tmp, columns=tmp.keys())
    return Df_tmp


def Command_STAT(data):
    Top_Words = Top_Words_Stat(data)
    Top_tweets = Top_Tweets_Stat(data)
    Top_Author = Top_Author_Stat(data)
    Info_Countries = Countries_Tweets_Stat(data)
    # ------------------Merge the all data after processing-------------------
    Res_data = pd.concat([Top_Words, Top_tweets, Top_Author, Info_Countries], axis=1)
    Res = Res_data.to_csv(r"G:/FileInTheDataBase.csv", encoding="iso-8859-1")
    return Res


def Command_ENTI(data, NLP):  # nlp = StanfordCoreNLP('http://localhost:9000')
    data_df = data.iloc[0:-1, 6]
    res = []
    with open('G:/TEST.txt', 'w', encoding='utf-8') as ff:
        data_df.to_string(ff)
    flag = 0
    with open('G:/TEST.txt', 'r', encoding='utf-8') as ff:
        for ele in ff:
            annotated = NLP.annotate(ele, properties={
                'annotators': 'dcoref',
                'outputFormat': 'json',
            })
            res.append(annotated)
        ff.close()
        res.reverse()
        return res


if __name__ == '__main__':
    sk = socket.socket()
    ip_port = ("0.0.0.0", 8008)
    sk.bind(ip_port)
    sk.listen()
    print('Connection established!')

    conn, addr = sk.accept()
    print("connect client:", addr)
    with conn:
        while True:
            Msg_Data = conn.recv(4096)  # ->1
            if not Msg_Data:
                conn.sendall("Error:Invalid Info".encode('utf-8'))
                break
            conn.send("Get the size and command".encode('utf-8'))  # <-2
            Size_Data = Msg_Data[4:-1]
            Size_Data = int(Size_Data)
            print(type(Size_Data))
            Request_Name = Msg_Data[0:3]
            Count_Rest_data = 0
            Data_Concat = []
            # ------------------Because the size of file >>>>>>>>4096 byte,we need get it by step-----
            while Count_Rest_data < Size_Data:
                Data_Get = conn.recv(4096)  # ->3
                Data_Concat.append(Data_Get)
                Count_Rest_data += len(Data_Get)

            Data_Get_Pickle = pickle.loads(b"".join(Data_Concat))

            if Request_Name == b"STAT":
                Pack = Command_STAT(Data_Get_Pickle)
                Pack_Size = int(len(Pack))
                conn.send(Pack_Size.encode('utf-8'))  # <-4
                time.sleep(2)
                conn.send(pickle.dumps(Pack))  # <-5
            if Request_Name == b"ENTI":
                nlp = StanfordCoreNLP('http://localhost:9000/', 9000)
                Pack = Command_ENTI(Data_Get_Pickle, nlp)
                Pack_Size = int(len(Pack))
                conn.send(Pack_Size.encode('utf-8'))
                time.sleep(2)
                conn.send(pickle.dumps(Pack))
    conn.close()
