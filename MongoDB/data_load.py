import pymongo
import csv
import pandas as pd
import configparser
import json


def _process(str):
    list = str.split('"')
    if len(list) != 1:
        for i in range(len(list)):
            if i % 2 == 0:
                continue
            temp1 = list[i]
            temp2 = list[i]

            temp2=temp2.replace("'", '’')
            str=str.replace(temp1, temp2)
    return str


config = configparser.ConfigParser()
config.read('config.ini')
ip = config.get('server', 'ip_addr')
remote_url = config.get('server', 'remote_url')
db_name = 'full_movie_lens'

if __name__ == '__main__':

    myclient = pymongo.MongoClient(remote_url)
    mydb = myclient[db_name]
    mycol = mydb['credit']

    bid_info = csv.DictReader(
        open('./data/credits.csv', 'r', encoding='utf-8-sig'))
    dict_data = {}
    i=0
    for lines in bid_info:
        if bid_info.line_num == 1:
            continue
        else:
            lines['id'] = int(lines['id'])
            
            lines['cast'] = lines['cast'].replace("None", 'null')
            temp = lines['cast'].replace("'", '"')
            try:
                json.loads(temp)
            except json.decoder.JSONDecodeError:            
                str = _process(lines['cast'])
                lines['cast'] = str.replace("'", '"')
                json.loads(lines['cast'])
            else:
                lines['cast'] = temp


            lines['crew'] = lines['crew'].replace("None", 'null')
            temp = lines['crew'].replace("'", '"')
            try:
                json.loads(temp)
            except json.decoder.JSONDecodeError:            
                str = _process(lines['crew'])
                lines['crew'] = str.replace("'", '"')
                json.loads(lines['crew'])
            else:
                lines['crew'] = temp

            dict_data['crew']=json.loads( lines['crew'])
            dict_data['cast']=json.loads( lines['cast'])
            dict_data['_id']=lines['id']
     
            x = mycol.insert_one(dict_data)
            i=i+1
            print(f"{i} Done.")
