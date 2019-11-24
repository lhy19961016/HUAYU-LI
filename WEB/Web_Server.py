from http.server import HTTPServer, BaseHTTPRequestHandler
import pandas as pd
from collections import Counter
import pickle
import sqlite3

from pycorenlp import StanfordCoreNLP


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


# --------------------------Find the 10 popular tweets with his authors and the number of the retweets in the
# data-------------
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
    Res_data = pickle.dumps(Res_data)
    Res = Res_data.to_csv(r"G:/FileInTheDataBase.csv", encoding="iso-8859-1")
    return Res


def Command_ENTI(data, NLP):
    nlp = StanfordCoreNLP('http://localhost:9000')
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
        res = pickle.dumps(res)
        return res


class RequestHeandler(BaseHTTPRequestHandler):
    def _set_headers(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()

    def _html(self,message):
        """This just generates an HTML document that includes `message`
        in the body. Override, or re-write this do do more interesting stuff.
        """
        content = f"<html><body><h1>{message}</h1></body></html>"
        return content.encode("utf8")  # NOTE: must return a bytes object!

    def do_GET(self):
        self._set_headers()
        self.wfile.write(_html("hi!"))

    def do_HEAD(self):
        self._set_headers()

    def do_POST(self):
        data_length = int(self.headers['Content-Length'])
        data = self.rfile.read(data_length)
        data_Get = pickle.loads(data)
        path = str(self.path)
        if path == '/STAT':
            df = Command_STAT(data_Get)
            self.send_response(200)
            self._set_headers()
            self.wfile.write(pickle.dumps(df))
        elif path == '/ENTI':
            df = Command_ENTI(data_Get)
            self.send_response(200)
            self._set_headers()
            self.wfile.write(pickle.dumps(df))
        #else:
            #self.send_error(404, "Not Found")


def run(server_class=HTTPServer, handler_class=RequestHeandler, addr="localhost", port=9527):
    server_address = (addr, port)
    httpd = server_class(server_address, handler_class)
    print(f"Starting httpd server on {addr}:{port}")
    httpd.serve_forever()


if __name__ == '__main__':
    run()
