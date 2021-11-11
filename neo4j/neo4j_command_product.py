import csv


def get_relation_command(fromNode, fromNodeProperty, fromProperty, toNode, toNodeProperty, toProperty,
                         relation, filename):
    print(
        ':auto using periodic commit 100000 load csv with headers from "file:/' + filename + '" as line match (from:' + fromNode + ' {' + fromNodeProperty + ': line.' + fromProperty + '}),(to:' + toNode + ' {' + toNodeProperty + ':line.' + toProperty + '}) merge (from)-[r:' + relation + '{relation:line.relation}]-(to);')


def get_add_command(node_name, prefix, filename, excluded_property=[]):
    with open(prefix + filename, "r", encoding='UTF-8') as file:
        reader = csv.reader(file)
        header = next(reader)
        command_part = ""
        count = len(excluded_property) + 1
        for property in header:
            if not excluded_property.__contains__(property):
                command_part += property + ":line." + property
                if count < len(header):
                    count = count + 1
                    command_part += ","
        print(
            ':auto using periodic commit 100000 load csv with headers from "file:/' + filename + '" as line with line create (:' + node_name + ' {' + command_part + '});')


get_add_command("movie", 'parse_files/', 'movies_metadata.csv',
                ["genres", "production_companies", "production_countries", "spoken_languages", "belongs_to_collection"])

get_add_command("cast", 'parse_files/', "casts.csv")
get_add_command("crew", 'parse_files/', "crews.csv")
get_add_command("genre", 'parse_files/', "genres.csv")
get_add_command("keyword", 'parse_files/', "keywords.csv")
get_add_command("company", 'parse_files/', "production_companies.csv")
get_add_command("country", 'parse_files/', "production_countries.csv")
get_add_command("language", 'parse_files/', "spoken_languages.csv")

get_relation_command("movie", "id", "movieId", "genre", "id", "genreId", "BELONG_TO", 'genres_relation.csv')
get_relation_command("movie", "id", "movieId", "language", "iso_639_1", "languageId", "BELONG_TO",
                     "spoken_languages_relation.csv")
get_relation_command("cast", "id", "castId", "movie", "id", "movieId", "ACT", "casts_relation.csv")
get_relation_command("crew", "id", "crewId", "movie", "id", "movieId", "WORK_IN", "crews_relation.csv")
get_relation_command("keyword", "id", "keywordId", "movie", "id", "movieId", "DESCRIBE", "keywords_relation.csv")
get_relation_command("company", "id", "companyId", "movie", "id", "movieId", "PRODUCT",
                     "production_companies_relation.csv")
get_relation_command("country", "iso_3166_1", "countryId", "movie", "id", "movieId", "PRODUCT",
                     "production_countries_relation.csv")
