import csv

from py2neo import *


def generate_node_and_relations(graph, movie_node, data, node_label, relation, node_id="id", is_right_node=True):
    for item in data:
        node_id_value = item.get(node_id)
        node = Node(node_label)
        node.update(item)
        graph.merge(node, node_label, node_id)
        if is_right_node:
            r = Relationship(node, relation, movie_node, id=str(movie_node["id"]) + node_label + str(node_id_value))
        else:
            r = Relationship(movie_node, relation, node, id=str(movie_node["id"]) + node_label + str(node_id_value))
        graph.merge(r, relation, "id")


if __name__ == '__main__':

    url = "http://localhost:7474/"
    graph = Graph(url, auth=("neo4j", "1234567890"), name="movies")

    node_matcher = NodeMatcher(graph)
    relationship_matcher = RelationshipMatcher(graph)
    movies_metadata_file = open("data/movies_metadata.csv", "r")
    movies_metadata_reader = csv.reader(movies_metadata_file)
    next(movies_metadata_reader)

    keywords_file = open("data/keywords.csv", "r")
    keywords_reader = csv.reader(keywords_file)
    next(keywords_reader)
    keywords_dict = {}
    for keyword in keywords_reader:
        keywords_dict[keyword[0]] = eval(keyword[1])

    credits_file = open("data/credits.csv", "r")
    credits_reader = csv.reader(credits_file)
    next(credits_reader)
    credits_dict = {}
    for credit in credits_reader:
        credits_dict[credit[2]] = [eval(credit[0]), eval(credit[1])]

    for movies_metadata in movies_metadata_reader:
        if len(movies_metadata) != 24:
            continue
        movie_id = movies_metadata[5]
        movie_exist = False
        movie_node = node_matcher.match("Movie").where(id=movie_id).first()
        if movie_node is None:
            movie_node = Node("Movie", adult=movies_metadata[0], budget=movies_metadata[2], homepage=movies_metadata[4],
                              id=movies_metadata[5], imdb_id=movies_metadata[6], original_language=movies_metadata[7],
                              original_title=movies_metadata[8], overview=movies_metadata[9],
                              popularity=movies_metadata[10],
                              poster_path=movies_metadata[11], release_date=movies_metadata[14],
                              revenue=movies_metadata[15],
                              runtime=movies_metadata[16], status=movies_metadata[18], tagline=movies_metadata[19],
                              title=movies_metadata[20], video=movies_metadata[21], vote_average=movies_metadata[22],
                              vote_count=movies_metadata[23])

        genres = eval(movies_metadata[3])
        generate_node_and_relations(graph, movie_node, genres, "Genre", "BELONG_TO", "id", False)

        production_companies = eval(movies_metadata[12])
        generate_node_and_relations(graph, movie_node, production_companies, "Company", "PRODUCT")

        production_countries = eval(movies_metadata[13])
        generate_node_and_relations(graph, movie_node, production_countries, "Country", "PRODUCT", "iso_3166_1")

        spoken_languages = eval(movies_metadata[17])
        generate_node_and_relations(graph, movie_node, spoken_languages, "Language", "SPEAK", "iso_639_1", False)

        keywords = keywords_dict.get(movie_id)
        if keywords:
            generate_node_and_relations(graph, movie_node, keywords, "Keyword", "DESCRIBE")

        credits = credits_dict.get(movie_id)
        casts = credits[0]
        crews = credits[1]
        if casts:
            generate_node_and_relations(graph, movie_node, casts, "Cast", "ACT")
        if crews:
            generate_node_and_relations(graph, movie_node, crews, "Crew", "WORK_IN")
