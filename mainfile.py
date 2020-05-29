import tweepy
import datetime
import sys
import json
import tmysql
import ttweets
import schedule
import time

#Twitter APIを使用するためのConsumerキー、アクセストークン設定
Consumer_key = ''
Consumer_secret = ''
Access_token = ''
Access_secret = ''


def authtwitter():
    #認証
    auth = tweepy.OAuthHandler(Consumer_key, Consumer_secret)
    auth.set_access_token(Access_token, Access_secret)

    api = tweepy.API(auth, wait_on_rate_limit = True, retry_count = 10, retry_delay = 10, retry_errors = set([130,401, 404, 500, 503]))
    return(api)


def gettwitterdata():
    api = authtwitter()

  //twitter idを指定
    results = api.user_timeline(screen_name="", count=2)

    for result in results:
        print(result.id)
        #print(result.created_at)
        #print(result.text)

def printTweetBySearch(s):
    api = authtwitter() # 認証

    tweets = tweepy.Cursor(api.search, q = s, include_entities = True, tweet_mode = 'extended', result_type='recent', lang = 'ja', count=100).items()       # 日本のツイートのみ取得

    for tweet in tweets:
        if tweet.favorite_count + tweet.retweet_count >= 5:
            #print('＝＝＝＝＝＝＝＝＝＝')
            #print('twid : ',tweet.id)               # tweetのIDを出力。ユニークなもの
            #print('user : ',tweet.user.screen_name) # ユーザー名
            #print('date : ', tweet.created_at)      # 呟いた日時
            #print(tweet.full_text)                  # ツイート内容
            #print('favo : ', tweet.favorite_count)  # ツイートのいいね数
            #print('retw : ', tweet.retweet_count)   # ツイートのリツイート数
            tmegumimysql.inputtweetinfo(tweet.id,tweet.created_at,tweet.full_text,tweet.favorite_count,tweet.retweet_count)

            retweeters = api.retweets(tweet.id)

            for i in range(len(retweeters)):
                tl_json = retweeters[i]._json
                wtf = tl_json['user']

                tmegumitweets.inputtweetinfo(tweet.id,wtf['screen_name'])



def job():#twitter idを指定
    printTweetBySearch('from:@ exclude:retweets filter:images')

def main():
    #gettwitterdata()
    schedule.every(1).minutes.do(job)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()
