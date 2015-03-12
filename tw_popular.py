from random import shuffle
def is_ascii(s):
    return all(ord(c) < 128 for c in s)

def popular(word):
    from twython import Twython
    APP_KEY = 'fLmKqsDDHkmnKOv3F1HwdJC8q'
    APP_SECRET = '9SEzEWzgXYgLKFxTXg4qdeHEHKfcCYBQMNAB044yD2pMvG0tsR'
    
    t = Twython(APP_KEY, APP_SECRET)
    i=0
    tw_accs=['nytimes','huffingtonpost','ABCNewsLive','guardian']
    shuffle(tw_accs)
    while i<len(tw_accs):   
        search = t.get_user_timeline(screen_name=tw_accs[i], count=55)
        for w in search:
            if word in w['text'].lower() and is_ascii(w['text']):
                return w['text']
        i+=1
    return "Nothing found..."

    
        
        
        