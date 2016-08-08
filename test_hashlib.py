import hashlib
from datetime import datetime

db={}
m=hashlib.sha1()

def register(user,password):
    salt = user+'12'
    m.update((password+salt).encode('utf-8'))
    db[user]=m.hexdigest()
    print('%s is in\npassword in db: %s'%(user,m.hexdigest()))

def login(user,password):
    m=hashlib.sha1()
    salt=user+'12'
    m.update((password + salt).encode('utf-8'))
    if user in db:
        if db[user] == m.hexdigest():
            print('longin successful!')
        else:print('password is wrong!')
    else:print('user is not exist.')


register('jmy','sunwen88')
login('jmy','fuqihua')
login('jmy','sunwen88')
login('ipromiseu','sunwen88')