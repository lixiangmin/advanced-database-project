import pymongo
import csv
import configparser
import logging

# config log format
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s')

# read and load configuration of remote DB
config = configparser.ConfigParser()
config.read('config.ini')
ip = config.get('server', 'ip_addr')
remote_url = config.get('server', 'remote_url')

# basic DB information definition
db_name = 'full_movie_lens'

def _load_credit(mydb):
    logging.info("Start loading credits...")
    col = mydb['credit']

    # open CSV file restoring the proprocessed data
    bid_info = csv.DictReader(
        open('./data/credits.csv', 'r', encoding='utf-8-sig'))
    
    # FIXME: the row index control in this function has some bugs, causing printing logs with wrong row data
    total = 45404
    i = 2

    # write data to DB row by row
    for lines in bid_info:
        if bid_info.line_num == 1:
            continue
        else:
            temp_row_data = {}

            # for row in which data is with wrong format that cannot be parsed,
            # e.g., with id that is not an int value, skip the row
            try:
                temp_row_data['crew'] = eval(lines['crew'])
                temp_row_data['cast'] = eval(lines['cast'])
                temp_row_data['_id'] = int(lines['id'])
            except SyntaxError:
                logging.error(f"Wrong format data: row {i}")
                i = i+1
                continue

            # for row in which data has a duplicate key with data written before,
            # skip the row
            try:
                col.insert_one(temp_row_data)
            except pymongo.errors.DuplicateKeyError:
                logging.warning(f"Duplicate key: {temp_row_data['_id']} in row {i}")
                i = i+1                
                continue

            i = i+1
            rate = i*100 / total
            if rate % 5 == 0:
                logging.info(f"{rate}% finished.")
            
    logging.info("Credits loading finish...")



if __name__ == '__main__':
    # DB connection
    myclient = pymongo.MongoClient(remote_url)
    mydb = myclient[db_name]

    # data loading
    _load_credit(mydb=mydb)
    