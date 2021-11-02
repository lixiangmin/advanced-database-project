import csv


def parse_data(data_filename, data_type, data_index, data_id="id"):
    with open("data/" + data_filename + ".csv", "r", encoding='UTF-8') as data_file:
        reader = csv.reader(data_file)
        next(reader)
        file = open("parse_files/" + data_type + ".csv", "w")
        writer = csv.writer(file)
        header = ""
        ids = []
        for read_data in reader:
            if len(read_data) <= data_index:
                continue
            datas = eval(read_data[data_index])
            if not isinstance(datas,list):
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


def parse_necessary_data():
    parse_data("movies_metadata", "genres", 3)
    parse_data("movies_metadata", "production_companies", 12)
    parse_data("movies_metadata", "production_countries", 13,"iso_3166_1")
    parse_data("movies_metadata", "spoken_languages", 17, "iso_639_1")
    parse_data("credits", "crews", 1)
    parse_data("credits", "casts", 0)
    parse_data("keywords", "keywords", 1)


def generate_relations_by_movies_metadata(relation_name, data_type, data_index, data_id, relation):
    file = open("relations/" + relation_name + ".csv", "w")
    writer = csv.writer(file)
    writer.writerow(["movieId", data_type + "Id", "relation"])
    with open("data/movies_metadata.csv", "r", encoding='UTF-8') as movies_metadata_file:
        reader = csv.reader(movies_metadata_file)
        next(reader)
        for movie_metadata in reader:
            if len(movie_metadata) != 24:
                continue
            movie_id = movie_metadata[5]
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
    generate_relations_by_movies_metadata("production_countries_relation", "country", 12, "iso_3166_1", "product")
    generate_relations_by_movies_metadata("production_companies_relation", "company", 13, "id", "product")
    generate_relations_by_movies_and_extra("keywords_relation", "data/keywords.csv", "keyword", 1, "id", 0, "describe")
    generate_relations_by_movies_and_extra("crews_relation", "data/credits.csv", "crew", 1, "id", 2, "work_in")
    generate_relations_by_movies_and_extra("casts_relation", "data/credits.csv", "cast", 0, "id", 2, "act")


print("-----------------------      start data parsing      -------------------------------")

parse_necessary_data()

print("-----------------------  start relations generating  -------------------------------")
generate_relations()
