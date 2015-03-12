import keywords
import time
import tw_popular
from textblob import TextBlob

from wordpress_xmlrpc import Client, WordPressPost
from wordpress_xmlrpc.methods.posts import GetPosts, NewPost
from wordpress_xmlrpc.methods.users import GetUserInfo
from string import capitalize

wp = Client('http://evsum.com/news/xmlrpc.php', 'Zenryo', 'ANFmEta6xLEACy')

post = WordPressPost()
post.title = 'Top words: '
post.content = 'List for ' + time.strftime("%m-%d-%H") + ': <br />'

post.terms_names = {'post_tag': ['List'], 'category': ['Uncategorised']}
sum = 0
i=1
# target = open('logs/summary_'+(time.strftime("%m-%d-%H"))+'.txt', 'w')

def is_ascii(s):
    return all(ord(c) < 128 for c in s)
    
for words in keywords.app():
    if is_ascii(words[0]):
        if i<5:
            if i==4:
                post.title+=str(words[0])
            else:
                post.title+=str(words[0])+', '
        i+=1
    text = str(tw_popular.popular(words[0]))
    blob = TextBlob(text).sentiment.polarity
    sum += blob
    post.content += "- " + capitalize(str(words[0])) + ": Number of mentions: " + str(words[1]) + " Reference: <span style='color:red'>" + text + "</span><br />"

print str(sum)
post.post_status = 'publish'
wp.call(NewPost(post))
        
        
print 'Done...'
