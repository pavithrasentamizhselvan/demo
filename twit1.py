import tweepy
from textblob import TextBlob
auth=tweepy.OAuthHandler(con_key,con_sec_key)
auth.set_access_token(acc_token,acc_sec_token)
api=tweepy.API(auth)
q=input("Enter any word")
tweets=api.search(q)
pos=0
neu=0
neg=0
#print(tweets.length())
for tweet in tweets:
    print(TextBlob(tweet.text))
    an=TextBlob(tweet.text)
    #print(an.sentiment)
    if(an.sentiment.polarity>0):
        print("Positive")
        pos=pos+1
    elif(an.sentiment.polarity==0):
        print("Neutral")
        neu=neu+1
    else:
        print("Negatie")
        neg=neg+1

if(pos>neu & pos>neg):
    print("Best")
elif(neu>pos & neu>neg):
    print("Good")
else:
    print("Bad")

#get key and token from twitter developer account by creating app in that
    
    
    
    
    
