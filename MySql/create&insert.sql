set @@sql_mode=ANSI;

create database movieDB;
use movieDB;

select 'create tables';
create table if not exists movies_metadata(adult varchar(10),budget double,homepage varchar(1000),id int not null primary key,imdb_id varchar(10),original_language varchar(5),original_title varchar(200),overview varchar(2000),popularity double,poster_path varchar(100),release_date varchar(15),revenue double,runtime double,status varchar(200),tagline varchar(1000),title varchar(200),video varchar(10),vote_average double,vote_count int)engine=InnoDB default charset=utf8;
create table if not exists movies_metadatabelongs_to_collection(id int,name varchar(100),poster_path varchar(200),backdrop_path varchar(200),autoId int not null primary key,movies_metadataid int not null, foreign key fk_movies_metadata(movies_metadataid) references movies_metadata(id))engine=InnoDB default charset=utf8;
create table if not exists movies_metadatagenres(id int,name varchar(100),autoId int not null primary key,movies_metadataid int not null, foreign key fk_movies_metadata(movies_metadataid) references movies_metadata(id))engine=InnoDB default charset=utf8;
create table if not exists movies_metadataproduction_companies(id int,name varchar(100),autoId int not null primary key,movies_metadataid int not null, foreign key fk_movies_metadata(movies_metadataid) references movies_metadata(id))engine=InnoDB default charset=utf8;
create table if not exists movies_metadataproduction_countries(iso_3166_1 int,name varchar(100),autoId int not null primary key,movies_metadataid int not null, foreign key fk_movies_metadata(movies_metadataid) references movies_metadata(id))engine=InnoDB default charset=utf8;
create table if not exists movies_metadataspoken_languages(iso_639_1 varchar(10),name varchar(100),autoId int not null primary key,movies_metadataid int not null, foreign key fk_movies_metadata(movies_metadataid) references movies_metadata(id))engine=InnoDB default charset=utf8;
create table if not exists links(movieId int not null primary key,imdbId int,tmdbId int)engine=InnoDB default charset=utf8;
create table if not exists ratings(userId int,movieId int,rating double,timestamp bigint,rId int not null primary key)engine=InnoDB default charset=utf8;
create table if not exists credits_new(id int not null primary key)engine=InnoDB default charset=utf8;
create table if not exists credits_newcast(cast_id int,_character varchar(1000),credit_id varchar(100),gender int,id int,name varchar(100),_order int,profile_path varchar(100),autoId int not null primary key,credits_newid int not null, foreign key fk_credits_new(credits_newid) references credits_new(id))engine=InnoDB default charset=utf8;
create table if not exists credits_newcrew(credit_id varchar(1000),department varchar(100),gender int,id int,job varchar(100),name varchar(100),profile_path varchar(100),autoId int not null primary key,credits_newid int not null, foreign key fk_credits_new(credits_newid) references credits_new(id))engine=InnoDB default charset=utf8;
create table if not exists keywords(id int not null primary key)engine=InnoDB default charset=utf8;
create table if not exists keywordskeywords(id int,name varchar(100),autoId int not null primary key,keywordsid int not null, foreign key fk_keywords(keywordsid) references keywords(id))engine=InnoDB default charset=utf8;

select 'insert movies_metadata : ';
load data infile '/home/processedData/movies_metadata.csv'
into table movies_metadata
fields terminated by ',' optionally enclosed by '"'
lines terminated by '\n'
IGNORE 1 LINES;

select 'insert movies_metadatabelongs_to_collection : ';
load data infile '/home/processedData/movies_metadatabelongs_to_collection.csv'
into table movies_metadatabelongs_to_collection
fields terminated by ',' optionally enclosed by '"'
lines terminated by '\n'
IGNORE 1 LINES;

select 'insert movies_metadatagenres : ';
load data infile '/home/processedData/movies_metadatagenres.csv'
into table movies_metadatagenres
fields terminated by ',' optionally enclosed by '"'
lines terminated by '\n'
IGNORE 1 LINES;

select 'insert movies_metadataproduction_companies : ';
load data infile '/home/processedData/movies_metadataproduction_companies.csv'
into table movies_metadataproduction_companies
fields terminated by ',' optionally enclosed by '"'
lines terminated by '\n'
IGNORE 1 LINES;

select 'insert movies_metadataproduction_countries : ';
load data infile '/home/processedData/movies_metadataproduction_countries.csv'
into table movies_metadataproduction_countries
fields terminated by ',' optionally enclosed by '"'
lines terminated by '\n'
IGNORE 1 LINES;

select 'insert movies_metadataspoken_languages : ';
load data infile '/home/processedData/movies_metadataspoken_languages.csv'
into table movies_metadataspoken_languages
fields terminated by ',' optionally enclosed by '"'
lines terminated by '\n'
IGNORE 1 LINES;

select 'insert links : ';
load data infile '/home/processedData/links.csv'
into table links
fields terminated by ',' optionally enclosed by '"'
lines terminated by '\n'
IGNORE 1 LINES;

select 'insert ratings : ';
load data infile '/home/processedData/ratings.csv'
into table ratings
fields terminated by ',' optionally enclosed by '"'
lines terminated by '\n'
IGNORE 1 LINES;

select 'insert credits_new : ';
load data infile '/home/processedData/credits_new.csv'
into table credits_new
fields terminated by ',' optionally enclosed by '"'
lines terminated by '\n'
IGNORE 1 LINES;

select 'insert credits_newcast : ';
load data infile '/home/processedData/credits_newcast.csv'
into table credits_newcast
fields terminated by ',' optionally enclosed by '"'
lines terminated by '\n'
IGNORE 1 LINES;

select 'insert credits_newcrew : ';
load data infile '/home/processedData/credits_newcrew.csv'
into table credits_newcrew
fields terminated by ',' optionally enclosed by '"'
lines terminated by '\n'
IGNORE 1 LINES;

select 'insert keywords : ';
load data infile '/home/processedData/keywords.csv'
into table keywords
fields terminated by ',' optionally enclosed by '"'
lines terminated by '\n'
IGNORE 1 LINES;

select 'insert keywordskeywords : ';
load data infile '/home/processedData/keywordskeywords.csv'
into table keywordskeywords
fields terminated by ',' optionally enclosed by '"'
lines terminated by '\n'
IGNORE 1 LINES;
