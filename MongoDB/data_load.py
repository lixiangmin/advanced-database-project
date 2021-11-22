import pymongo
import csv
import configparser
import logging
from datetime import datetime
import traceback

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

    result=[]
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
                temp_row_data['id'] = int(lines['id'])
            except SyntaxError:
                logging.error(f"Wrong format data: row {i}")
                i = i+1
                continue

            # for row in which data has a duplicate key with data written before,
            # skip the row
            try:
                col.insert_one(temp_row_data)
            except pymongo.errors.DuplicateKeyError:
                logging.warning(
                    f"Duplicate key: {temp_row_data['_id']} in row {i}")
                i = i+1
                continue

            i = i+1
            rate = i*100 / total
            if rate % 5 == 0:
                logging.info(f"{rate}% finished.")

    logging.info("Credits loading finish...")


def _load_movie(mydb):
    logging.info("Start loading movie metadata...")
    col = mydb['movies_metadata']

    # open CSV file restoring the proprocessed data
    bid_info = csv.DictReader(
        open('./data/movies_metadata.csv', 'r', encoding='utf-8-sig'))

    total = 45467
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
                temp_row_data['adult'] = lines['adult'] == 'TRUE'

                if lines['belongs_to_collection'] != '' and lines['belongs_to_collection'] != None:
                    temp_row_data['belongs_to_collection'] = eval(
                        lines['belongs_to_collection'])

                if lines['budget'] != '' and lines['budget'] != None:
                    temp_row_data['budget'] = int(lines['budget'])

                if lines['genres'] != '' and lines['genres'] != None:
                    temp_row_data['genres'] = eval(lines['genres'])

                if lines['homepage'] != '' and lines['homepage'] != None:
                    temp_row_data['homepage'] = lines['homepage']

                if lines['id'] != '' and lines['id'] != None:
                    temp_row_data['_id'] = int(lines['id'])

                if lines['imdb_id'] != '' and lines['imdb_id'] != None:
                    temp_row_data['imdb_id'] = lines['imdb_id']

                if lines['original_language'] != '' and lines['original_language'] != None:
                    temp_row_data['original_language'] = lines['original_language']

                if lines['original_title'] != '' and lines['original_title'] != None:
                    temp_row_data['original_title'] = lines['original_title']

                if lines['overview'] != '' and lines['overview'] != None:
                    temp_row_data['overview'] = lines['overview']

                if lines['popularity'] != '' and lines['popularity'] != None:
                    temp_row_data['popularity'] = float(lines['popularity'])

                if lines['poster_path'] != '' and lines['poster_path'] != None:
                    temp_row_data['poster_path'] = lines['poster_path']

                if lines['production_companies'] != '' and lines['production_companies'] != None:
                    temp_row_data['production_companies'] = eval(
                        lines['production_companies'])

                if lines['production_countries'] != '' and lines['production_countries'] != None:
                    temp_row_data['production_countries'] = eval(
                        lines['production_countries'])

                if lines['release_date'] != '' and lines['release_date'] != None:
                    temp_row_data['release_date'] = datetime.strptime(
                        lines['release_date'], '%Y-%m-%d')

                if lines['revenue'] != '' and lines['revenue'] != None:
                    temp_row_data['revenue'] = int(lines['revenue'])

                if lines['runtime'] != '' and lines['runtime'] != None:
                    temp_row_data['runtime'] = float(lines['runtime'])

                if lines['spoken_languages'] != '' and lines['spoken_languages'] != None:
                    temp_row_data['spoken_languages'] = eval(
                        lines['spoken_languages'])

                if lines['status'] != '' and lines['status'] != None:
                    temp_row_data['status'] = lines['status']

                if lines['tagline'] != '' and lines['tagline'] != None:
                    temp_row_data['tagline'] = lines['tagline']

                if lines['title'] != '' and lines['title'] != None:
                    temp_row_data['title'] = lines['title']

                if lines['video'] != '' and lines['video'] != None:
                    temp_row_data['video'] = lines['video'] == 'TRUE'

                if lines['vote_average'] != '' and lines['vote_average'] != None:
                    temp_row_data['vote_average'] = float(
                        lines['vote_average'])

                if lines['vote_count'] != '' and lines['vote_count'] != None:
                    temp_row_data['vote_count'] = int(lines['vote_count'])

            except ValueError:
                logging.error(f"Wrong format data: row {i}")
                traceback.print_exc()
                i = i+1
                continue
            except SyntaxError:
                logging.error(f"Wrong format data: row {i}")
                traceback.print_exc()
                i = i+1
                continue

            # for row in which data has a duplicate key with data written before,
            # skip the row
            try:
                col.insert_one(temp_row_data)
            except pymongo.errors.DuplicateKeyError:
                logging.warning(
                    f"Duplicate key: {temp_row_data['_id']} in row {i}")
                i = i+1
                continue

            i = i+1
            rate = i*100 / total
            if rate % 2 == 0:
                logging.info(f"{rate}% finished.")

    logging.info("Movie metadata loading finish...")


def _load_keyword(mydb):
    logging.info("Start loading keywords...")
    col = mydb['keywords']

    # open CSV file restoring the proprocessed data
    bid_info = csv.DictReader(
        open('./data/keywords.csv', 'r', encoding='utf-8-sig'))
    # bid_info = csv.DictReader(
    #     open('./data/demo.csv', 'r', encoding='utf-8-sig'))
    total = 46420
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
                if lines['id'] != '' and lines['id'] != None:
                    temp_row_data['id'] = int(lines['id'])

                if lines['keywords'] != '' and lines['keywords'] != None:
                    temp_row_data['keywords'] = eval(
                        lines['keywords'])

            except ValueError:
                logging.error(f"Wrong format data: row {i}")
                traceback.print_exc()
                i = i+1
                continue
            except SyntaxError:
                logging.error(f"Wrong format data: row {i}")
                traceback.print_exc()
                i = i+1
                continue

            # for row in which data has a duplicate key with data written before,
            # skip the row
            try:
                col.insert_one(temp_row_data)
            except pymongo.errors.DuplicateKeyError:
                logging.warning(
                    f"Duplicate key: {temp_row_data['_id']} in row {i}")
                i = i+1
                continue

            i = i+1
            rate = i*100 / total
            if rate % 2 == 0:
                logging.info(f"{rate}% finished.")

    logging.info("keywords loading finish...")


def _load_link(mydb):
    logging.info("Start loading links...")
    col = mydb['links']

    # open CSV file restoring the proprocessed data
    bid_info = csv.DictReader(
        open('./parse_files/links_merged.csv', 'r', encoding='utf-8-sig'))
    # bid_info = csv.DictReader(
    #     open('./data/demo.csv', 'r', encoding='utf-8-sig'))
    total = 45853
    i = 1

    # write data to DB row by row
    for lines in bid_info:
        if bid_info.line_num == 1:
            continue
        else:
            temp_row_data = {}

            # for row in which data is with wrong format that cannot be parsed,
            # e.g., with id that is not an int value, skip the row
            try:
                if lines['movieId'] != '' and lines['movieId'] != None:
                    temp_row_data['movieId'] = int(lines['movieId'])
                if lines['imdbId'] != '' and lines['imdbId'] != None:
                    temp_row_data['imdbId'] = int(lines['imdbId'])
                if lines['tmdbId'] != '' and lines['tmdbId'] != None:
                    temp_row_data['tmdbId'] = int(lines['tmdbId'])                    
            except ValueError:
                logging.error(f"Wrong format data: row {i}")
                traceback.print_exc()
                i = i+1
                continue
            except SyntaxError:
                logging.error(f"Wrong format data: row {i}")
                traceback.print_exc()
                i = i+1
                continue

            # for row in which data has a duplicate key with data written before,
            # skip the row
            col.insert_one(temp_row_data)

            i = i+1
            rate = i*100 / total
            if rate % 2 == 0:
                logging.info(f"{rate}% finished.")

    logging.info("links loading finish...")

def _load_rating(mydb):
    logging.info("Start loading ratings...")
    col = mydb['ratings']

    # open CSV file restoring the proprocessed data
    bid_info = csv.DictReader(
        open('./parse_files/ratings_merged.csv', 'r', encoding='utf-8-sig'))
    # bid_info = csv.DictReader(
    #     open('./data/demo.csv', 'r', encoding='utf-8-sig'))
    total = 45853
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
                if lines['userId'] != '' and lines['userId'] != None:
                    temp_row_data['userId'] = int(lines['userId'])
                if lines['movieId'] != '' and lines['movieId'] != None:
                    temp_row_data['movieId'] = int(lines['movieId'])
                if lines['rating'] != '' and lines['rating'] != None:
                    temp_row_data['rating'] = float(lines['rating'])  
                if lines['timestamp'] != '' and lines['timestamp'] != None:
                    temp_row_data['timestamp'] = int(lines['timestamp'])                                        
            except ValueError:
                logging.error(f"Wrong format data: row {i}")
                traceback.print_exc()
                i = i+1
                continue
            except SyntaxError:
                logging.error(f"Wrong format data: row {i}")
                traceback.print_exc()
                i = i+1
                continue

            try:
                col.insert_one(temp_row_data)
            except pymongo.errors.DuplicateKeyError:
                logging.warning(
                    f"Duplicate key: {temp_row_data['_id']} in row {i}")
                i = i+1
                continue


            i = i+1
            rate = i*100 / total
            if rate % 2 == 0:
                logging.info(f"{rate}% finished.")

    logging.info("links loading finish...")


if __name__ == '__main__':
    # DB connection
    myclient = pymongo.MongoClient(remote_url)
    mydb = myclient[db_name]

    # data loading
    _load_credit(mydb=mydb)
    # _load_movie(mydb=mydb)
    # _load_keyword(mydb=mydb)
    # _load_link(mydb=mydb)
    # _load_rating(mydb=mydb)
