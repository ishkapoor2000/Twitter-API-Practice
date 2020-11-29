import tweepy
from collections import Counter

auth = tweepy.OAuthHandler('APIKEY' ,'APISECRETKEY')
auth.set_access_token('ACCESSTOKEN' ,'ACCESSSECRETTOKEN')
api = tweepy.API(auth, wait_on_rate_limit = True)

def Gather_Tweets():

	all = []
	friends = api.friends_ids()
	for friend in friends:
		new_tweets = api.user_timeline(api.get_user(friend).screen_name, count = 20, page = 5, tweet_mode = "extended")
		tweets = [tweet.full_text.upper() for tweet in new_tweets]
		all.append(tweets)

	return all

def Slipt_Tweets():

	all_tweets = Gather_Tweets()
	split = []
	for tweets in all_tweets:
		for tweet in tweets:
			split_tweets = tweet.splir(" ")
			split.append(split_tweets)

	return split

def Sort_Ticker():

	sort_list = Slipt_Tweets()
	tickers = []
	for sentence in sort_list:
		for word in sentence:
			if word.startswith("$") and word[1:len(word)].isalpha() and len(word) < 6:
				tickers.append(word)

def Organize_Trending():

	tickers = Sort_Ticker()
	data = Counter(tickers).most_common(25)

	return data

print(Organize_Trending())