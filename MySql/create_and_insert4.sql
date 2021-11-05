CREATE TABLE IF NOT EXISTS `LINKS`(
   Id INT,
   Imdbid INT,
   Tmdbid INT,
   PRIMARY KEY ( Id )
);
CREATE TABLE IF NOT EXISTS `LINKS_SMALL`(
   Id INT,
   Imdbid INT,
   Tmdbid INT,
   PRIMARY KEY ( Id )
);
CREATE TABLE IF NOT EXISTS `RATINGS_SMALL`(
   userId INT,
   movieId INT,
   rating FLOAT,
   timestamp INT
);
CREATE TABLE IF NOT EXISTS `RATINGS`(
   userId INT,
   movieId INT,
   rating FLOAT,
   timestamp INT
);
load data infile 'E:/mysql/links.csv'
into table links
fields terminated by ',' optionally enclosed by '"' escaped by '"'
lines terminated by '\r\n';
load data infile 'E:/mysql/links_small.csv'
into table links_small
fields terminated by ',' optionally enclosed by '"' escaped by '"'
lines terminated by '\r\n';
load data infile 'E:/mysql/ratings_small.csv'
into table ratings_small
fields terminated by ',' optionally enclosed by '"' escaped by '"'
lines terminated by '\r\n';
load data infile 'E:/mysql/ratings.csv'
into table ratings
fields terminated by ',' optionally enclosed by '"' escaped by '"'
lines terminated by '\r\n';