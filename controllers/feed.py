import feedparser
from models import feed
from models import user
from models import userfeed

def check_feed(url):
    parse = feedparser.parse(url)
    return parse.version

def get_msg(text):
    space = text.find(' ')
    if(not space > 0):
        return False
    return text[space + 1:]

def save_feed(userid, url):
    user_id = user.add(userid)
    feed_id = feed.add(url)
    result = userfeed.add(user_id, feed_id)
    if(result):
        return True
    return False