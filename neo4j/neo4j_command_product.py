import csv


def get_relation_command(from_node, from_node_property, from_property, to_node, to_node_property, to_property,
                         relation, filename, relation_property='relation:line.relation'):
    print(
        'using periodic commit 100000 load csv with headers from "file:///' + filename + '" as line match (from:' + from_node + ' {' + from_node_property + ': line.' + from_property + '}),(to:' + to_node + ' {' + to_node_property + ':line.' + to_property + '}) merge (from)-[r:' + relation + '{' + relation_property + '}]-(to);')


def get_add_command(node_name, prefix, filename, excluded_property=[]):
    with open(prefix + filename, "r", encoding='UTF-8') as file:
        reader = csv.reader(file)
        header = next(reader)
        command_part = ""
        count = len(excluded_property) + 1
        for property in header:
            if not excluded_property.__contains__(property):
                command_part += property + ":COALESCE(line." + property + ", \"none\")"
                if count < len(header):
                    count = count + 1
                    command_part += ","
        print(
            'using periodic commit 100000 load csv with headers from "file:///' + filename +
            '" as line with line merge (:' + node_name + ' {' + command_part + '});')


get_add_command("movie", 'parse_files/', 'movies_metadata.csv',
                ["genres", "production_companies", "production_countries", "spoken_languages", "belongs_to_collection"])

get_add_command("cast", 'parse_files/', "casts.csv")
get_add_command("crew", 'parse_files/', "crews.csv")
get_add_command("genre", 'parse_files/', "genres.csv")
get_add_command("keyword", 'parse_files/', "keywords.csv")
get_add_command("company", 'parse_files/', "production_companies.csv")
get_add_command("country", 'parse_files/', "production_countries.csv")
get_add_command("language", 'parse_files/', "spoken_languages.csv")
get_add_command("user", 'parse_files/', "ratings_merged.csv", ["movieId", "rating", "timestamp"])

get_relation_command("movie", "id", "movieId", "genre", "id", "genreId", "BELONG_TO", 'genres_relation.csv')
get_relation_command("movie", "id", "movieId", "language", "iso_639_1", "languageId", "SPEAK",
                     "spoken_languages_relation.csv")
get_relation_command("cast", "id", "castId", "movie", "id", "movieId", "ACT", "casts_relation.csv")
get_relation_command("crew", "id", "crewId", "movie", "id", "movieId", "WORK_IN", "crews_relation.csv")
get_relation_command("keyword", "id", "keywordId", "movie", "id", "movieId", "DESCRIBE", "keywords_relation.csv")
get_relation_command("company", "id", "companyId", "movie", "id", "movieId", "PRODUCT",
                     "production_companies_relation.csv")
get_relation_command("country", "iso_3166_1", "countryId", "movie", "id", "movieId", "PRODUCT",
                     "production_countries_relation.csv")
get_relation_command("user", "userId", "userId", "movie", "id", "movieId", "RANK", 'ratings_merged.csv',
                     'rating:line.rating,timestamp:line.timestamp')
