import asyncio
import ormClass, sqlPublic
from models import User, Blog, Comment
import logging

'''
testScript of ormClass,sqlPubic,models
'''

loop = asyncio.get_event_loop()

@asyncio.coroutine
def test():
    yield from sqlPublic.create_pool(user='root', password='123456', db='awesome', loop=loop)
    u = User(name='Test', email='test@example.com', passwd='12345678', image='about:blank')
    queryList = yield from User.findAll()
    logging.info('findAll() test ok!!')
    logging.info('findAll() count:')
    logging.info(str(len(queryList)))

    for userInfo in queryList:
        yield from userInfo.remove()

    yield from u.save()
    logging.info('save() test ok!!')


#for x in test():
#    pass
loop.run_until_complete(test())
loop.run_forever()