import csv
import pandas as pd


def parse_data(data_filename, data_type, data_index, data_id="id", neglect=None):
    if neglect is None:
        neglect = [19730, 29503, 35587]
    with open("data/" + data_filename + ".csv", "r", encoding='UTF-8') as data_file:
        reader = csv.reader(data_file)
        next(reader)
        file = open("parse_files/" + data_type + ".csv", "w")
        writer = csv.writer(file)
        header = ""
        ids = []
        for i, read_data in enumerate(reader):
            if len(read_data) <= data_index:
                continue
            datas = eval(read_data[data_index])
            if not isinstance(datas, list) or i in neglect:
                print(i, read_data)
                continue
            for data in datas:
                if header == "":
                    header = data.keys()
                    writer.writerow(header)
                if not ids.__contains__(data.get(data_id)):
                    writer.writerow(data.values())
                    ids.append(data.get(data_id))
                else:
                    print("repeated_data:")
                    print(data.values())
        print("-----------------------      end " + data_type + " parsing      -------------------------------")


def parse_meta_data():
    neglect = [19730, 29503, 35587]
    with open("data/movies_metadata.csv", "r", encoding='UTF-8') as data_file:
        reader = csv.reader(data_file)
        file = open("parse_files/movies_metadata.csv", "w")
        writer = csv.writer(file)
        header = next(reader)
        writer.writerow(header)
        idList = []
        dataList = []
        for i, data in enumerate(reader):
            if i in neglect:
                continue
            if data[5] in idList:
                idx = idList.index(data[5])
                data = dataList[idx]
            idList.append(data[5])
            dataList.append(data)
            writer.writerow(data)
        print("-----------------------      end movies_meta_data parsing      -------------------------------")


def parse_necessary_data():
    parse_data("movies_metadata", "genres", 3)
    parse_data("movies_metadata", "production_companies", 12)
    parse_data("movies_metadata", "production_countries", 13, "iso_3166_1")
    parse_data("movies_metadata", "spoken_languages", 17, "iso_639_1")
    parse_data("credits", "crews", 1)
    parse_data("credits", "casts", 0)
    parse_data("keywords", "keywords", 1)
    parse_meta_data()


def generate_relations_by_movies_metadata(relation_name, data_type, data_index, data_id, relation, neglect=None):
    if neglect is None:
        neglect = [19730, 29503, 35587]
    file = open("relations/" + relation_name + ".csv", "w")
    writer = csv.writer(file)
    writer.writerow(["movieId", data_type + "Id", "relation"])
    with open("data/movies_metadata.csv", "r", encoding='UTF-8') as movies_metadata_file:
        reader = csv.reader(movies_metadata_file)
        next(reader)
        for i, movie_metadata in enumerate(reader):
            if len(movie_metadata) != 24 or i in neglect:
                continue
            movie_id = movie_metadata[5]
            if len(movie_metadata[data_index]) != 0:
                items = eval(movie_metadata[data_index])
                for item in items:
                    row = [movie_id, item.get(data_id), relation]
                    writer.writerow(row)
    print("-----------------------      finish " + relation_name + " generating      -------------------------------")


def generate_relations_by_movies_and_extra(relation_name, extra_file_path, extra_data_type, extra_data_index,
                                           extra_data_id,
                                           extra_data_movie_id_index, relation):
    file = open("relations/" + relation_name + ".csv", "w")
    writer = csv.writer(file)
    writer.writerow(["movieId", extra_data_type + "Id", "relation"])
    extra_file = open(extra_file_path, "r")
    extra_file_reader = csv.reader(extra_file)
    next(extra_file_reader)
    dict = {}
    for extra_data in extra_file_reader:
        dict[extra_data[extra_data_movie_id_index]] = eval(extra_data[extra_data_index])
    with open("data/movies_metadata.csv", "r", encoding='UTF-8') as movies_metadata_file:
        reader = csv.reader(movies_metadata_file)
        next(reader)
        for movie_metadata in reader:
            if len(movie_metadata) != 24:
                continue
            movie_id = movie_metadata[5]
            extra_data = dict.get(movie_id)
            if extra_data:
                for data in extra_data:
                    row = [movie_id, data.get(extra_data_id), relation]
                    writer.writerow(row)


def generate_relations():
    generate_relations_by_movies_metadata("genres_relation", "genre", 3, "id", "belong_to")
    generate_relations_by_movies_metadata("spoken_languages_relation", "language", 17, "iso_639_1", "speak")
    generate_relations_by_movies_metadata("production_countries_relation", "country", 13, "iso_3166_1", "product")
    generate_relations_by_movies_metadata("production_companies_relation", "company", 12, "id", "product")
    generate_relations_by_movies_and_extra("keywords_relation", "data/keywords.csv", "keyword", 1, "id", 0, "describe")
    generate_relations_by_movies_and_extra("crews_relation", "data/credits.csv", "crew", 1, "id", 2, "work_in")
    generate_relations_by_movies_and_extra("casts_relation", "data/credits.csv", "cast", 0, "id", 2, "act")


def row_count(filename):
    with open(filename) as in_file:
        return sum(1 for _ in in_file)


def merge(a_file, b_file, int_idx, efficient=False):
    big_file = open("data/" + a_file + ".csv", "r", encoding='UTF-8')
    big_file_reader = csv.reader(big_file)
    merged_file = open("parse_files/" + a_file + "_merged.csv", "w", encoding='UTF-8')
    merged_file_writer = csv.writer(merged_file)
    header = next(big_file_reader)
    merged_file_writer.writerow(header)
    big_file_data = []
    for row in big_file_reader:
        for idx in int_idx:
            if row[idx] != '':
                row[idx] = int(row[idx])
        big_file_data.append(row)
    with open("data/" + b_file + ".csv", "r", encoding='UTF-8') as small_file:
        small_file_reader = csv.reader(small_file)
        next(small_file_reader)
        row_num = row_count("data/" + b_file + ".csv")
        if efficient is False:
            for small_file_data in small_file_reader:
                for idx in int_idx:
                    if small_file_data[idx] != '':
                        small_file_data[idx] = int(small_file_data[idx])
                if small_file_data not in big_file_data:
                    big_file_data.append(small_file_data)
            big_file_data.sort()
            merged_file_writer.writerows(big_file_data)
        else:
            is_small_end = False
            row = next(small_file_reader)
            for idx in int_idx:
                if row[idx] != '':
                    row[idx] = int(row[idx])
            i = 0
            while i < len(big_file_data):
                d = big_file_data[i]
                if is_small_end:
                    merged_file_writer.writerow(d)
                    i += 1
                else:
                    if d[0] < row[0] or (d[0] == row[0] and d[1] < row[1]):
                        merged_file_writer.writerow(d)
                        i += 1
                        continue
                    elif d[0] > row[0] or (d[0] == row[0] and d[1] > row[1]):
                        merged_file_writer.writerow(row)
                        i -= 1
                    # 处理同一个人对同一部电影的多次评价，取最新的评价
                    else:
                        if int(d[3]) > int(row[3]):
                            merged_file_writer.writerow(d)
                        else:
                            merged_file_writer.writerow(row)
                    i += 1
                    # 处理small文件里最后一个没有写入的问题
                    if small_file_reader.line_num == row_num:
                        is_small_end = True
                        continue
                    row = next(small_file_reader)
                    for idx in int_idx:
                        if row[idx] != '':
                            row[idx] = int(row[idx])
    print("-----------------------      finish " + a_file + " generating      -------------------------------")


def merge_files():
    merge("links", "links_small", [0, 1, 2])
    merge("ratings", "ratings_small", [0, 1], efficient=True)


def check_num(a_file, b_file):
    print("big_file_data_num: " + str(row_count("data/" + b_file + ".csv")))
    print("small_file_data_num: " + str(row_count("data/" + a_file + ".csv")))
    print("merged_data_num: " + str(row_count("parse_files/" + a_file + "_merged.csv")))


print("-----------------------      start data parsing      -------------------------------")

# parse_necessary_data()

print("-----------------------  start relations generating  -------------------------------")
# generate_relations()

print("-----------------------  merge two files  -----------------------------")
merge_files()

# check_num("links", "links_small")
# check_num("ratings", "ratings_small")

