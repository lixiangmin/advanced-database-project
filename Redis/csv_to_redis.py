# -*- coding: utf-8 -*- 
import csv
import redis
import timeit
from tqdm import tqdm
import json
import demjson

'''
把本课程选定的数据库各个表导入到redis中
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



class RedisTT(object):
    def __init__(self):
        self.host = 'localhost'
        self.port = '6379'
        self.r = redis.StrictRedis(host=self.host, port=self.port)

    def insertRedis(self, name, key, value):  # 把每个tuple看做一个对象，插入到redis之中，keys选择键
        self.r.hset(name, key, value)


'''
大概的思路是使用hash结构，把每个tuple看做一个对象，hash表的key是表中的主键，然后每个column Type为key
目前这种做法还是依赖于先对csv文件分析并人为选择hash表的id
可以实现根据ID快速查询每个电影的详细信息
表名：movies_metadata
'''


@clock
def csv2redis_movies_metadata(csv_path):
    r = redis.StrictRedis(host='127.0.0.1', port='6379')
    csv_file = csv.DictReader(open(csv_path, 'r', encoding='utf-8', ))
    pipe = r.pipeline(transaction=False)
    for row in tqdm(csv_file):
        id = row['id']
        for key, value in row.items():
            pipe.hset(str(id), str(key), str(value))


# 表名：ratings
@clock
def csv2redis_rating(csv_path):
    r = redis.StrictRedis(host='127.0.0.1', port='6379')
    csv_file = csv.DictReader(open(csv_path, 'r', encoding='utf-8', ))
    pipe = r.pipeline(transaction=False)
    for row in tqdm(csv_file):
        use_id = row['userId']
        movieId = row['movieId']
        rating = row['rating']
        timestamp = row['userId']
        json_data = [{'rating': rating, 'userId': timestamp}]
        pipe.hset(use_id + '_ratings', movieId, json.dumps(json_data))


# 表名：links
@clock
def csv2redis_links(csv_path):
    r = redis.StrictRedis(host='127.0.0.1', port='6379')
    csv_file = csv.DictReader(open(csv_path, 'r', encoding='utf-8', ))
    pipe = r.pipeline(transaction=False)
    for row in tqdm(csv_file):
        movieId = row['movieId']
        imdbId = row['imdbId']
        tmdbId = row['tmdbId']
        json_data = [{'imdbId': imdbId, 'tmdbId': tmdbId}]
        pipe.set(movieId + '_links', json.dumps(json_data))


# 表名：keywords
'''
存两张表，一张是id与keyword的对应，一张是movieid与keywordid对应
500it/s,使用处理过的可以更快
'''

# 解析的版本，效率低
@clock
def csv2redis_keywords(csv_path):
    r = redis.StrictRedis(host='127.0.0.1', port='6379')
    csv_file = csv.DictReader(open(csv_path, 'r', encoding='utf-8', ))
    pipe = r.pipeline(transaction=False)
    for row in tqdm(csv_file):
        movieId = row['id']
        for item in demjson.decode(row['keywords']):
            pipe.set(str(item['id']) + '_kw', item['name'])
            pipe.lpush(str(movieId) + 'keywords', item['id'])

# 只聚焦于存储，csv2redis_keywords实现合理的数据结构，但时间较长
@clock
def csv2redis_keywords_raw(csv_path):
    r = redis.StrictRedis(host='127.0.0.1', port='6379')
    csv_file = csv.DictReader(open(csv_path, 'r', encoding='utf-8', ))
    pipe = r.pipeline(transaction=False)
    for row in tqdm(csv_file):
        pipe.set(row['id'] + '_kw', row['keywords'])


# 表名：credits
'''
30it/s，主要是json数据给的不好，包含了数据清理的过程
'''


@clock
def csv2redis_credits(csv_path):
    r = redis.StrictRedis(host='127.0.0.1', port='6379')
    csv_file = csv.DictReader(open(csv_path, 'r', encoding='utf-8', ))
    pipe = r.pipeline(transaction=False)
    for row in tqdm(csv_file):
        movieId = row['id']
        # 给的JSON数据不符合要求，None不加引号
        row['cast'] = row['cast'].replace('None', "'None'")
        row['crew'] = row['crew'].replace('None', "'None'")
        for item in demjson.decode(row['cast']):
            for key, value in item.items():
                pipe.hset(movieId + '_cast', key, value)
        for item in demjson.decode(row['crew']):
            for key, value in item.items():
                pipe.hset(movieId + '_crew', key, value)

# 只聚焦于如何存，csv2redis_credits实现合理的数据结构，但时间较长
@clock
def csv2redis_credits_raw(csv_path):
    r = redis.StrictRedis(host='127.0.0.1', port='6379')
    csv_file = csv.DictReader(open(csv_path, 'r', encoding='utf-8', ))
    pipe = r.pipeline(transaction=False)
    for row in tqdm(csv_file):
        pipe.set(row['id'] + '_cast', row['cast'])
        pipe.set(row['id'] + '_crew', row['crew'])



if __name__ == '__main__':
    print("------------------------开始读入movies_metadata.csv------------------------")
    csvPath = './movie/movies_metadata.csv'
    #csv2redis_movies_metadata(csvPath)

    print("------------------------开始读入ratings.csv------------------------")
    csvPath = './movie/ratings.csv'
    #csv2redis_rating(csvPath)

    print("------------------------开始读入credits.csv------------------------")
    csvPath = './movie/credits.csv'
    csv2redis_credits_raw(csvPath)

    print("------------------------开始读入keywords.csv------------------------")
    csvPath = './movie/keywords.csv'
    csv2redis_keywords_raw(csvPath)

    print("------------------------开始读入links.csv------------------------")
    csvPath = './movie/links.csv'
    csv2redis_links(csvPath)
