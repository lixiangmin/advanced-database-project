# -*- coding: utf-8 -*-  
import timeit
import redis
import random

'''
这个文件主要测试redis五种数据类型的增删改查性能，使用的数据是随机生成的
'''


class RedisTT(object):
    def __init__(self):
        self.host = 'localhost'
        self.port = '6379'
        self.r = redis.StrictRedis(host=self.host, port=self.port)

    def insertRedis(self, name, keyName, jsonStr):  # ���뵽redis��
        self.r.hset(name, keyName, jsonStr)


# 计时函数
def clock(func):
    def clocked(*args, **kwargs):
        t0 = timeit.default_timer()
        result = func(*args, **kwargs)
        elapsed = timeit.default_timer() - t0
        name = func.__name__
        arg_str = ', '.join(repr(arg) for arg in args)
        print('[%0.8fs] %s(%s) -> %r | avg_latency_ms = %0.8fs | QPS = %0.8fs' % (elapsed, name, arg_str, result, elapsed/int(arg_str),int(arg_str)/elapsed))
        return result

    return clocked


# 测试string的插入性能
@clock
def add_to_redis_string(x):
    # conn = redis.ConnectionPool(host='127.0.0.1', port='6379')
    # db = redis.Redis(connection_pool=conn)
    db = redis.StrictRedis(host='127.0.0.1', port='6379')
    pipe = db.pipeline(transaction=False)
    for i in range(x):
        pipe.set(str(i) + '_string', str(i))
    return 'Finish'


@clock
def put_to_redis_string(x):
    # conn = redis.ConnectionPool(host='127.0.0.1', port='6379')
    # db = redis.Redis(connection_pool=conn)
    db = redis.StrictRedis(host='127.0.0.1', port='6379')
    pipe = db.pipeline(transaction=False)
    for i in range(x):
        pipe.set(str(i) + '_string', str(i + 1))
    return 'Finish'


@clock
def find_from_redis_string(x):
    # conn = redis.ConnectionPool(host='127.0.0.1', port='6379')
    # db = redis.Redis(connection_pool=conn)
    db = redis.StrictRedis(host='127.0.0.1', port='6379')
    pipe = db.pipeline(transaction=False)
    for i in range(x):
        pipe.get(str(i) + '_string')
    return 'Finish'


@clock
def delete_from_redis_string(x):
    # conn = redis.ConnectionPool(host='127.0.0.1', port='6379')
    # db = redis.Redis(connection_pool=conn)
    db = redis.StrictRedis(host='127.0.0.1', port='6379')
    pipe = db.pipeline(transaction=False)
    for i in range(x):
        pipe.delete(str(i) + '_string')
    return 'Finish'


# 测试hash的插入性能
@clock
def add_to_redis_hash(x):
    # conn = redis.ConnectionPool(host='127.0.0.1', port='6379')
    # db = redis.Redis(connection_pool=conn)
    db = redis.StrictRedis(host='127.0.0.1', port='6379')
    pipe = db.pipeline(transaction=False)
    for i in range(x):
        pipe.hset(str(i) + '_hash', str(i), str(i))
    return 'Finish'


# 测试单个hash value的插入性能
@clock
def add_to_redis_hash(x):
    # conn = redis.ConnectionPool(host='127.0.0.1', port='6379')
    # db = redis.Redis(connection_pool=conn)
    db = redis.StrictRedis(host='127.0.0.1', port='6379')
    pipe = db.pipeline(transaction=False)
    for i in range(x):
        pipe.hset('hash_insert_test', str(i), str(i))
    return 'Finish'


# 测试单个hash value的修改性能
@clock
def post_to_single_redis_hash(x):
    # conn = redis.ConnectionPool(host='127.0.0.1', port='6379')
    # db = redis.Redis(connection_pool=conn)
    db = redis.StrictRedis(host='127.0.0.1', port='6379')
    pipe = db.pipeline(transaction=False)
    for i in range(x):
        pipe.hset('hash_insert_test', str(i), str(i))
    return 'Finish'


# 测试单个hash value的查询性能
@clock
def find_from_single_redis_hash(x):
    # conn = redis.ConnectionPool(host='127.0.0.1', port='6379')
    # db = redis.Redis(connection_pool=conn)
    db = redis.StrictRedis(host='127.0.0.1', port='6379')
    pipe = db.pipeline(transaction=False)
    for i in range(x):
        pipe.hget('hash_insert_test', str(i))
    return 'Finish'


# 测试单个hash value的删除性能
@clock
def delete_from_single_redis_hash(x):
    # conn = redis.ConnectionPool(host='127.0.0.1', port='6379')
    # db = redis.Redis(connection_pool=conn)
    db = redis.StrictRedis(host='127.0.0.1', port='6379')
    pipe = db.pipeline(transaction=False)
    for i in range(x):
        pipe.hdel('hash_insert_test', str(i))
    return 'Finish'


# 测试有序set的插入性能
@clock
def add_to_redis_set(x):
    # conn = redis.ConnectionPool(host='127.0.0.1', port='6379')
    # db = redis.Redis(connection_pool=conn)
    db = redis.StrictRedis(host='127.0.0.1', port='6379')
    pipe = db.pipeline(transaction=False)
    for i in range(x):
        pipe.zadd(str(i) + '_set', {'bob': 100, 'mike': 99, 'lucy': 87})
    return 'Finish'


# 测试单个有序set的插入性能
@clock
def put_to_single_redis_set(x):
    # conn = redis.ConnectionPool(host='127.0.0.1', port='6379')
    # db = redis.Redis(connection_pool=conn)
    db = redis.StrictRedis(host='127.0.0.1', port='6379')
    pipe = db.pipeline(transaction=False)
    for i in range(x):
        pipe.zadd('single_ordered_set', {str(i): i})
    return 'Finish'


# 测试单个有序set的删除性能
@clock
def delete_from_single_redis_set(x):
    # conn = redis.ConnectionPool(host='127.0.0.1', port='6379')
    # db = redis.Redis(connection_pool=conn)
    db = redis.StrictRedis(host='127.0.0.1', port='6379')
    pipe = db.pipeline(transaction=False)
    for i in range(x):
        pipe.zrem(str(i) + '_set', str(i))
    return 'Finish'


# 测试无序set的插入性能
@clock
def add_to_redis_uset(x):
    # conn = redis.ConnectionPool(host='127.0.0.1', port='6379')
    # db = redis.Redis(connection_pool=conn)
    db = redis.StrictRedis(host='127.0.0.1', port='6379')
    pipe = db.pipeline(transaction=False)
    for i in range(x):
        pipe.sadd(str(i) + '_uset', 1, 2, 3, 4, 5, 6, 7, 8, 9)
    return 'Finish'


# 测试list的插入性能
@clock
def add_to_redis_list(x):
    # conn = redis.ConnectionPool(host='127.0.0.1', port='6379')
    # db = redis.Redis(connection_pool=conn)
    db = redis.StrictRedis(host='127.0.0.1', port='6379')
    pipe = db.pipeline(transaction=False)
    for i in range(x):
        pipe.lpush(str(i) + '_list', 1, 2, 3, 4, 5, 6, 7, 8, 9)
    return 'Finish'


# 测试list的插入性能
@clock
def put_to_redis_list(x):
    # conn = redis.ConnectionPool(host='127.0.0.1', port='6379')
    # db = redis.Redis(connection_pool=conn)
    db = redis.StrictRedis(host='127.0.0.1', port='6379')
    pipe = db.pipeline(transaction=False)
    for i in range(x):
        pipe.lpush(str(i) + '_list', 1, 2, 3, 4, 5, 6, 7, 8, 9)
    return 'Finish'


# 测试list的插入性能
@clock
def find_from_redis_list(x):
    # conn = redis.ConnectionPool(host='127.0.0.1', port='6379')
    # db = redis.Redis(connection_pool=conn)
    db = redis.StrictRedis(host='127.0.0.1', port='6379')
    pipe = db.pipeline(transaction=False)
    for i in range(x):
        pipe.lpush(str(i) + '_list', 1, 2, 3, 4, 5, 6, 7, 8, 9)
    return 'Finish'


# 测试list的插入性能
@clock
def delete_from_redis_list(x):
    # conn = redis.ConnectionPool(host='127.0.0.1', port='6379')
    # db = redis.Redis(connection_pool=conn)
    db = redis.StrictRedis(host='127.0.0.1', port='6379')
    pipe = db.pipeline(transaction=False)
    for i in range(x):
        pipe.lpush(str(i) + '_list', 1, 2, 3, 4, 5, 6, 7, 8, 9)
    return 'Finish'


if __name__ == '__main__':
    times = 1000000
    # 实际上数据类型不一致并不影响k-v这种模式的存储效率，所以除了完全测试String外，剩下的对value的增删改查进行测试
    print('每个操作执行' + str(times) + '次')
    print("-------------开始测试String数据类型的增删改查效率-------------")
    add_to_redis_string(times)
    put_to_redis_string(times)
    find_from_redis_string(times)
    delete_from_redis_string(times)

    print("-------------开始测试hash数据类型的增删改查效率-------------")
    add_to_redis_hash(times)
    post_to_single_redis_hash(times)
    find_from_single_redis_hash(times)
    delete_from_single_redis_hash(times)

    print("-------------开始测试ordered-set数据类型的增删改查效率-------------")
    add_to_redis_set(times)
    put_to_single_redis_set(times)
    delete_from_single_redis_set(times)

    print("-------------开始测试unordered-set数据类型的增删改查效率-------------")
    add_to_redis_uset(times)

    print("-------------开始测试list数据类型的增删改查效率-------------")
    add_to_redis_list(times)
