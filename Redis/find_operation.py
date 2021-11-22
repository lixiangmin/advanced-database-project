# -*- coding: utf-8 -*-
import csv
import redis
import timeit
from tqdm import tqdm
import json
import demjson

'''
测试一些场景下的读取效率
'''


# 计时函数
def clock(func):
    def clocked(*args, **kwargs):
        t0 = timeit.default_timer()
        result = func(*args, **kwargs)
        elapsed = float(timeit.default_timer() - t0)
        name = func.__name__
        arg_str = ', '.join(repr(arg) for arg in args)
        print('[%0.8fs] %s(%s) -> %r' % (elapsed, name, arg_str, result))
        return result

    return clocked


@clock
def csv2redis_movies_metadata(csv_path):
    r = redis.StrictRedis(host='127.0.0.1', port='6379')
    csv_file = csv.DictReader(open(csv_path, 'r', encoding='utf-8', ))
    pipe = r.pipeline(transaction=False)
    for row in tqdm(csv_file):
        id = row['id']
        for key, value in row.items():
            pipe.hset(str(id), str(key), str(value))


@clock
def update():
    r = redis.StrictRedis(host='127.0.0.1', port='6379')
    id_list = r.zrangebyscore("user_id", 0, 23000)
    for id in id_list:
        ratings = r.hkeys(id + '_ratings')
        for rating in ratings:
            r.hset(id + '_ratings', rating, 5.0)
    return


@clock
def delete():
    r = redis.StrictRedis(host='127.0.0.1', port='6379')
    id_list = r.zrangebyscore("user_id", 0, 23000)
    for id in id_list:
        ratings = r.delete(id + '_ratings')
    return


@clock
def get_genre(id):
    r = redis.StrictRedis(host='127.0.0.1', port='6379')
    id_list = r.lrange(id + '_love_genre', 0, -1)
    return r.hmget('genre_info', id_list)


@clock
def get_all_crew():
    r = redis.StrictRedis(host='127.0.0.1', port='6379')
    id_list = r.hkeys('myhash')  # 得到电影Id
    id_list_temp = [id + '_crew' for id in id_list]
    print(r.sunion(id_list_temp))


if __name__ == '__main__':
    get_many()
