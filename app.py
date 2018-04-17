from config import database
from views import telegram
import logging

# add_user(123456)
# add_feed('htttp://google.com.br')
# add_userfeed(1, 1)

# check_feed('http://www.marduktv.com.br/feed/')

# 'http://www.marduktv.com.br/feed/'

# addfeed('789465', 'http://uol.com.br')
# addfeed('789465', 'http://google.com.br')
# addfeed('789465', 'http://queroworkar.com.br')
# addfeed('12465', 'http://queroworkar.com.br')

# add_link('http://queroworkar.com.br?id=123123', 'http://queroworkar.com.br')

if __name__ == '__main__':
    # logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    database.sync_db()
    telegram.initialize("")