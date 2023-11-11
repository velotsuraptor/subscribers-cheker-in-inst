import importlib
from data import *
import history_of_subscribers
import records

# in the next line paste everything you copied from the page with subscribers
subscribers = '''      '''
subs = define_subscriber(subscribers.split('\n'))

append_data_to_file(subs)
rewrite_records()
# Remove the quotes (''')  after the next line only when you have 2 records (or more) of your subscribers, otherwise
# code won't run! (PS you will also have to remove quotes in the last way, cuz there's no long comments in Python).
# So far all you have to do is to pass your copied data and to help the code with the language. Don't try to change
# anything except the places I've mentioned in comments!
'''
saved_subscribers = eval(records.all_saved[-2])
print(saved_subscribers.difference(subs))
print('How much people unsubscribed (or changed their names lol): ' + str(len(saved_subscribers.difference(subs))))
'''
