def get_reddit(sub_reddit):
    import praw
    
    common = open("words.txt").read().split("\n")
    word_dict = {}
    
    
    r = praw.Reddit(user_agent='Mozilla/5.0')
    subreddit = r.get_subreddit(sub_reddit)
    
    word_list = []
    
    for submission in subreddit.get_hot(limit=100):
        try:
            word_list += ((submission.title).lower()).split()
        except:
            pass
    for w in word_list:
        if w not in common and w.isalnum():
            if w in word_dict:
                word_dict[w]+=1
            else:
                word_dict[w]=1
    
    top_words = sorted(word_dict.items(),key=lambda(k,v):(v,k),reverse=True)[:100]
    
    for words in top_words:
        yield words