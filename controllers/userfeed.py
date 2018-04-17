import feedparser
from models import feed as model_feed
from models import userfeed as model_userfeed
from models import link as model_link

def send_for_users(guid, feed_id):
    users = model_userfeed.get_users_by_feed(feed_id)
    for user in users:
        print(user, guid)
        model_link.add(guid, feed_id)

def extract_feeds(url, feed_id):
    parse = feedparser.parse(url)
    for entrie in parse['entries']:
        guid = entrie.guid
        link = model_link.get(guid, feed_id)
        if(not link):
            send_for_users(guid, feed_id)

def update():
    feeds = model_feed.get_all()
    for feed in feeds:
        feed_id = feed[0]
        url = feed[1]
        extract_feeds(url, feed_id)