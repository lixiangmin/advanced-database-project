create table if not exists movie
(
    adult             varchar(10),
    budget            double,
    homepage          varchar(1000),
    id                int not null primary key,
    imdb_id           varchar(10),
    original_language varchar(5),
    original_title    varchar(200),
    overview          varchar(2000),
    popularity        double,
    poster_path       varchar(255),
    release_date      varchar(15),
    revenue           double,
    runtime           double,
    status            varchar(200),
    tagline           varchar(1000),
    title             varchar(200),
    video             varchar(10),
    score             double,
    vote_average      double,
    vote_count        int
) engine = InnoDB
  default charset = utf8
  AUTO_INCREMENT = 1;

create table if not exists genre
(
    id   int not null primary key,
    name varchar(100)
) engine = InnoDB
  default charset = utf8
  AUTO_INCREMENT = 1;

create table if not exists movie_genre
(
    genre_id    int not null,
    relation_id int not null primary key auto_increment,
    movie_id    int not null,
    foreign key fk_movie (movie_id) references movie (id),
    foreign key fk_genre (genre_id) references genre (id)
) engine = InnoDB
  default charset = utf8
  AUTO_INCREMENT = 1;

create table if not exists production_company
(
    id   int not null primary key,
    name varchar(150)
) engine = InnoDB
  default charset = utf8
  AUTO_INCREMENT = 1;

create table if not exists movie_production_company
(
    production_company_id int not null,
    relation_id           int not null unique auto_increment primary key,
    movie_id              int not null,
    foreign key fk_movie (movie_id) references movie (id),
    foreign key fk_production_company (production_company_id) references production_company (id)
) engine = InnoDB
  default charset = utf8
  AUTO_INCREMENT = 1;
create table if not exists production_country
(
    iso_3166_1 varchar(10) not null primary key,
    name       varchar(100)
) engine = InnoDB
  default charset = utf8
  AUTO_INCREMENT = 1;
create table if not exists movie_production_country
(
    iso_3166_1  varchar(10) not null,
    relation_id int         not null auto_increment primary key,
    movie_id    int         not null,
    foreign key fk_movie (movie_id) references movie (id),
    foreign key fk_production_country (iso_3166_1) references production_country (iso_3166_1)
) engine = InnoDB
  default charset = utf8
  AUTO_INCREMENT = 1;
create table if not exists spoken_language
(
    iso_639_1 varchar(10) not null primary key,
    name      varchar(100)
) engine = InnoDB
  default charset = utf8
  AUTO_INCREMENT = 1;
create table if not exists movie_spoken_language
(
    iso_639_1   varchar(10) not null,
    relation_id int         not null auto_increment primary key,
    movie_id    int         not null,
    foreign key fk_movie (movie_id) references movie (id),
    foreign key fk_spoken_language (iso_639_1) references spoken_language (iso_639_1)
) engine = InnoDB
  default charset = utf8
  AUTO_INCREMENT = 1;

create table if not exists link
(
    id       int not null auto_increment primary key,
    movie_id int not null,
    imdb_id  int,
    tmdb_id  int,
    foreign key fk_movie (movie_id) references movie (id)
) engine = InnoDB
  default charset = utf8
  AUTO_INCREMENT = 1;
create table if not exists user
(
    id   int not null primary key,
    name varchar(100)
) engine = InnoDB
  default charset = utf8
  AUTO_INCREMENT = 1;

create table if not exists rating
(
    user_id   int not null,
    movie_id  int not null,
    score    double,
    timestamp bigint,
    rating_id int not null auto_increment primary key,
    foreign key fk_movie (movie_id) references movie (id),
    foreign key fk_user (user_id) references user (id)
) engine = InnoDB
  default charset = utf8
  AUTO_INCREMENT = 1;

create table if not exists cast
(
    cast_id      int,
    _character   varchar(1000),
    credit_id    varchar(100),
    gender       int,
    id           int not null primary key,
    name         varchar(100),
    _order       int,
    profile_path varchar(100)
) engine = InnoDB
  default charset = utf8
  AUTO_INCREMENT = 1;
create table if not exists crew
(
    credit_id    varchar(1000),
    department   varchar(100),
    gender       int,
    id           int not null primary key,
    job          varchar(100),
    name         varchar(100),
    profile_path varchar(100)
) engine = InnoDB
  default charset = utf8
  AUTO_INCREMENT = 1;

create table if not exists movie_crew
(
    crew_id     int not null,
    relation_id int not null auto_increment primary key,
    movie_id    int not null,
    foreign key fk_movie (movie_id) references movie (id),
    foreign key fk_cast (crew_id) references crew (id)
) engine = InnoDB
  default charset = utf8
  AUTO_INCREMENT = 1;

create table if not exists movie_cast
(
    cast_id     int not null,
    relation_id int not null auto_increment primary key,
    movie_id    int not null
) engine = InnoDB
  default charset = utf8
  AUTO_INCREMENT = 1;
create table if not exists keyword
(
    id   int not null PRIMARY KEY,
    name varchar(100)
) engine = InnoDB
  default charset = utf8
  AUTO_INCREMENT = 1;

create table if not exists movie_keyword
(
    keyword_id  int not null,
    movie_id    int not null,
    relation_id int not null auto_increment primary key,
    foreign key fk_movie (movie_id) references movie (id),
    foreign key fk_keyword (keyword_id) references keyword (id)
) engine = InnoDB
  default charset = utf8
  AUTO_INCREMENT = 1;

create index movie_id_index
    on rating (movie_id);

create index user_id_index
    on rating (user_id);
