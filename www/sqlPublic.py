import aiomysql, logging, asyncio

'''
mysql 操作的公共用接口
'''

def log(sql, args=()):
    logging.info('SQL: %s' %sql)

@asyncio.coroutine
def create_pool(loop, **kw):
    '''
    创建mysql连接池
    '''
    logging.info('create database connection pool....')
    global __pool
    __pool = yield from aiomysql.create_pool(
        host = kw.get('host', 'localhost'),
        port = kw.get('port', 3306),
        user = kw['user'],
        password = kw['password'],
        db = kw['db'],
        charset = kw.get('charset', 'utf8'),
        autocommit = kw.get('autocommit', True),
        maxsize = kw.get('maxsize', 10),
        minsize = kw.get('minsize', 1),
        loop = loop
    )

#@asyncio.coroutine
async def select(sql, args, size=None):
    '''
    select执行
    '''
    log(sql, args)
    global __pool
    async with __pool.get() as conn:
        async with conn.cursor(aiomysql.DictCursor) as cur:
            await cur.execute(sql.replace('?', '%s'), args or ())
            if size:
                rs = await cur.fetchmany(size)
            else:
                rs = await cur.fetchall()
        logging.info('rows returned :%s' %len(rs))
        return rs

#@asyncio.coroutine
async def execute(sql, args, autocommit=True):
    '''
    insert,update,delete语句
    '''
    log(sql)
    global __pool
    async with __pool.get() as conn:
        if not autocommit:
            await conn.begin()
        try:
            async with conn.cursor(aiomysql.DictCursor) as cur:
                await cur.execute(sql.replace('?', '%s'), args)
                affected = cur.rowcount
            if not autocommit:
                await conn.commit()
        except BaseException as e:
            if not autocommit:
                await conn.rollback()
            raise
        return affected