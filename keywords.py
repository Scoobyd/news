def app():
    import reddit
    import twitter
    import nytimes

    
    dict_all = {}
    i=0
    reddit_accs=['news','worldnews','technology']
    while i<len(reddit_accs):   
        for r in reddit.get_reddit(reddit_accs[i]):
            if r[0] in dict_all:
                dict_all[r[0]]+=r[1]
            else:
                dict_all[r[0]]=r[1]
        i+=1
     
    #Twitter feeds
    j=0
    tweet_accs=['washingtonpost','huffingtonpost','huffingtonpost','BBCBreaking','cnnbrk','WSJbreakingnews','CBSTopNews','SkyNewsBreak','ABCNewsLive','guardian']
    while j<len(tweet_accs):
        for t in twitter.tweets(tweet_accs[j]):
            if t[0] in dict_all:
                dict_all[t[0]]+=t[1]
            else:
                dict_all[t[0]]=t[1]
        j+=1
    
    #News sites
    '''
    for i in nytimes.nytimes():
        if i[0] in dict_all:
            dict_all[i[0]]+=i[1]
        else:
            dict_all[i[0]]=i[1]
       '''     
    return sorted(dict_all.items(),key=lambda(k,v):(v,k),reverse=True)[:10]
