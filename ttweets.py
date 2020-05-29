import tweepy
from datetime import datetime
import time
import sys
import json
from oauth2client.service_account import ServiceAccountCredentials
from httplib2 import Http
import mysql.connector


def inputtweetinfo(twid,rtuser):
    # ホスト名等入力
    conn = mysql.connector.connect(host='', 
                                  port=, 
                                  db='', 
                                  user='', 
                                  passwd='', 
                                  charset="utf8")
 
    cur = conn.cursor(buffered=True)
    
    #print(rtuser) ugoku
    #SQL
    sql1 = "SELECT * FROM tweetbunseki WHERE tweetid in ('" + str(twid) + "');" 
    cur.execute(sql1)
    rows = cur.fetchall()




    check = False

    if not rows:
        check = True
    

    for row in rows:
        #print(row)
        if(str(twid)==str(row[1]) and rtuser==row[2]):
            #すでにツイートが存在するので、ツイートIDとユーザー名が同じか確認しにいく
            check = False
            break
        else:
            check =True
            #sql = "INSERT INTO tweetbunseki (tweetid,rtuser) VALUES ('" + str(twid) + "','" + str(rtuser) + "');"
            #cur.execute(sql)

    if(check):
        sql = "INSERT INTO tweetbunseki (tweetid,rtuser) VALUES ('" + str(twid) + "','" + str(rtuser) + "');"
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
