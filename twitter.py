def tweets(user):
	from twython import Twython
	
	common = open("words.txt").read().split("\n")
	
	APP_KEY = 'fLmKqsDDHkmnKOv3F1HwdJC8q'
	APP_SECRET = '9SEzEWzgXYgLKFxTXg4qdeHEHKfcCYBQMNAB044yD2pMvG0tsR'
	
	t = Twython(APP_KEY, APP_SECRET)
	
	search = t.get_user_timeline(screen_name=user, count=35)
	word_list = []
	word_dict = {}
	
	for tweet in search:
		try:
			tweet['text'] = (tweet['text'].lower()).replace('islamic state', 'isis')
			tweet['text'] = (tweet['text'].lower()).replace('united kingdom', 'britain')
			tweet['text'] = (tweet['text'].lower()).replace('ukrainian', 'ukraine')
			tweet['text'] = (tweet['text'].lower()).replace('president obama', 'obama')
			tweet['text'] = (tweet['text'].lower()).replace('united states', 'usa')
			tweet['text'] = (tweet['text'].lower()).replace('russian', 'russia')
			word_list += tweet['text'].split()
		except:
			pass


	for w in word_list:
		if w not in common and w.isalnum():
			if w in word_dict:
				word_dict[w] += 1
			else:
				word_dict[w] = 1
	
	top_words = sorted(word_dict.items(), key=lambda(k, v):(v, k), reverse=True)[:100]
	
	for words in top_words:
		yield words
		
		
