def nytimes():
    import urllib
    from bs4 import BeautifulSoup
    
    url = "http://rss.nytimes.com/services/xml/rss/nyt/InternationalHome.xml"
    
    common = open("words.txt").read().split("\n")
    
    htmltext = urllib.urlopen(url).read()
    soup = BeautifulSoup(htmltext)
    
    word_dict = {}
    word_list = []
    
    i = 0
    
    for link in soup.findAll('title'):
        if i > 1:
            try:
                word_list+=((link.text).lower()).split()
            except:
                pass
        i += 1
    
    for w in word_list:
        if w not in common and w.isalnum():
            if w in word_dict:
                word_dict[w]+=1
            else:
                word_dict[w]=1
    
    top_words = sorted(word_dict.items(),key=lambda(k,v):(v,k),reverse=True)[:100]
    
    for words in top_words:
        yield words

if __name__ == '__main__':           
    nytimes()