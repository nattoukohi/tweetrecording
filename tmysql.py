import tweepy
from datetime import datetime
import time
import sys
import json
from oauth2client.service_account import ServiceAccountCredentials
from httplib2 import Http
import mysql.connector


def inputtweetinfo(twid,twdate,txt,fav,rt):
    # ホスト名等入力
    conn = mysql.connector.connect(host='', 
                                  port=, 
                                  db='', 
                                  user='', 
                                  passwd='', 
                                  charset="utf8")
 
    cur = conn.cursor(buffered=True)
    
    print(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    #SQL
    sql1 = "SELECT * FROM tweetdatabase WHERE tweetid in ('" + str(twid) + "');" 
    cur.execute(sql1)
    rows = cur.fetchall()

    check = False

    if not rows:
        check = True

    for row in rows:
        #print(row)
        if(str(twid)==str(row[1])):
            #すでにツイートが存在するので、favとrtが同じか確認しにいく
            if(fav==row[5] and rt==row[6]):
                #このときは何もしない]
                #print("change to false")
                check = False
                break
            else:
                #print("change to true")
                check = True
        else:
            #print("change to true because the id does not match")
            check = True

    if(check):
        sql = "INSERT INTO tweetdatabase (tweetid,currenttime,tweetdate,text,fav,rt) VALUES ('" + str(twid) + "','" + datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "','" + str(twdate) + "','" + txt + "'," + str(fav) + "," + str(rt) + ");"
        
        # 実行
        cur.execute(sql)
        # データ取得
        #rows = cur.fetchall()
                    

    


    """result = []
    for row in rows:
        if(weponname in row[2])or(weponname in row[4]):
            result.append("**"+ row[0] + "**")
        else:
            result.append(row[0])
       
    return result"""

    conn.commit()
 
    # 接続を閉じる
    cur.close()
    conn.close()
