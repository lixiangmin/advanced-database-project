# **Neo4j database**

## 数据库容器启动命令

- 4核cpu
- 8g内存

```
docker run -d --name neo4j-4cpu-8gmem -p 7474:7474 -p 7687:7687 -v /home/neo4j/data:/data -v /home/neo4j/logs:/logs -v /home/neo4j/conf:/var/lib/neo4j/conf -v /home/neo4j/import:/var/lib/neo4j/import --env NEO4J_AUTH=neo4j/123456 --env NEO4J_dbms_directories_import=import --cpus 4 --memory 8g  neo4j
```

## 插入结点（100000 load csv）

### 采用create语句（不加主键）

#### Genres 

- 412 ms

#### movies_metadata 

- 3847 ms


## 创建主键约束

```
create constraint on (m:movie) assert m.id is unique;

create constraint on (g:genre) assert g.id is unique;

create constraint on (c:cast) assert c.id is unique;

create constraint on (c:crew) assert c.id is unique;

create constraint on (k:keyword) assert k.id is unique;

create constraint on (c:company) assert c.id is unique;

create constraint on (c:country) assert c.iso_3166_1 is unique;

create constraint on (l:language) assert l.iso_639_1 is unique;

create constraint on (u:user) assert u.userId is unique;
```


### 采用merge语句（加主键）

 #### movies_metadata 

```
using periodic commit 100000 load csv with headers from "file:///movies_metadata.csv" as line with line merge (:movie {adult:COALESCE(line.adult, "none"),budget:COALESCE(line.budget, "none"),homepage:COALESCE(line.homepage, "none"),id:COALESCE(line.id, "none"),imdb_id:COALESCE(line.imdb_id, "none"),original_language:COALESCE(line.original_language, "none"),original_title:COALESCE(line.original_title, "none"),overview:COALESCE(line.overview, "none"),popularity:COALESCE(line.popularity, "none"),poster_path:COALESCE(line.poster_path, "none"),release_date:COALESCE(line.release_date, "none"),revenue:COALESCE(line.revenue, "none"),runtime:COALESCE(line.runtime, "none"),status:COALESCE(line.status, "none"),tagline:COALESCE(line.tagline, "none"),title:COALESCE(line.title, "none"),video:COALESCE(line.video, "none"),vote_average:COALESCE(line.vote_average, "none"),vote_count:COALESCE(line.vote_count, "none")});
```

- 6991 ms

- Added 45433 nodes, Set 863227 properties, Added 45433 labels

#### Genres 

```
using periodic commit 100000 load csv with headers from "file:///genres.csv" as line with line merge (:genre {id:COALESCE(line.id, "none"),name:COALESCE(line.name, "none")});
```

- 69 ms

- Added 20 nodes, Set 40 properties, Added 20 labels

#### Casts

```
using periodic commit 100000 load csv with headers from "file:///casts.csv" as line with line merge (:cast {cast_id:COALESCE(line.cast_id, "none"),character:COALESCE(line.character, "none"),credit_id:COALESCE(line.credit_id, "none"),gender:COALESCE(line.gender, "none"),id:COALESCE(line.id, "none"),name:COALESCE(line.name, "none"),order:COALESCE(line.order, "none"),profile_path:COALESCE(line.profile_path, "none")});
```

- 16027 ms
- Added 206136 nodes, Set 1649088 properties, Added 206136 labels

#### Crews

```
using periodic commit 100000 load csv with headers from "file:///crews.csv" as line with line merge (:crew {credit_id:COALESCE(line.credit_id, "none"),department:COALESCE(line.department, "none"),gender:COALESCE(line.gender, "none"),id:COALESCE(line.id, "none"),job:COALESCE(line.job, "none"),name:COALESCE(line.name, "none"),profile_path:COALESCE(line.profile_path, "none")});
```

- 10099 ms
- Added 161571 nodes, Set 1130997 properties, Added 161571 labels

#### Keywords

```
using periodic commit 100000 load csv with headers from "file:///keywords.csv" as line with line merge (:keyword {id:COALESCE(line.id, "none"),name:COALESCE(line.name, "none")});
```

- 705 ms
- Added 19954 nodes, Set 39908 properties, Added 19954 labels

#### production_companies

```
using periodic commit 100000 load csv with headers from "file:///production_companies.csv" as line with line merge (:company {name:COALESCE(line.name, "none"),id:COALESCE(line.id, "none")});
```

- 786 ms
- Added 23692 nodes, Set 47384 properties, Added 23692 labels

#### production_countries

```
using periodic commit 100000 load csv with headers from "file:///production_countries.csv" as line with line merge (:country {iso_3166_1:COALESCE(line.iso_3166_1, "none"),name:COALESCE(line.name, "none")});
```

-  153 ms
- Added 161 nodes, Set 322 properties, Added 161 labels

#### spoken_language

```
using periodic commit 100000 load csv with headers from "file:///spoken_languages.csv" as line with line merge (:language {iso_639_1:COALESCE(line.iso_639_1, "none"),name:COALESCE(line.name, "none")});
```

- 73 ms
- Added 133 nodes, Set 266 properties, Added 133 labels

#### user

```
using periodic commit 100000 load csv with headers from "file:///ratings_merged.csv" as line with line merge (:user {userId:COALESCE(line.userId, "none")});
```

-  294165 ms
- Created 270554 nodes, Set 270554 properties, Added 270554 labels

## 插入联系（100000 load csv)

### 不加主键，建联系非常慢（genres与movies需要花30分钟）

### 加主键后

#### Genres && movies

```
using periodic commit 100000 load csv with headers from "file:///genres_relation.csv" as line match (from:movie {id: line.movieId}),(to:genre {id:line.genreId}) merge (from)-[r:BELONG_TO{relation:line.relation}]-(to);
```

- 6000 ms
- Created 91006 relationships, Set 91006 properties

#### Casts && movies

```
using periodic commit 100000 load csv with headers from "file:///casts_relation.csv" as line match (from:cast {id: line.castId}),(to:movie {id:line.movieId}) merge (from)-[r:ACT{relation:line.relation}]-(to);
```

- 35276 ms
- Created 560779 relationships, Set 560779 properties

#### Crews && movies

```
using periodic commit 100000 load csv with headers from "file:///crews_relation.csv" as line match (from:crew {id: line.crewId}),(to:movie {id:line.movieId}) merge (from)-[r:WORK_IN{relation:line.relation}]-(to);
```

- 28244 ms
- Created 422768 relationships, Set 422768 properties

#### Keywords && movies

```
using periodic commit 100000 load csv with headers from "file:///keywords_relation.csv" as line match (from:keyword {id: line.keywordId}),(to:movie {id:line.movieId}) merge (from)-[r:DESCRIBE{relation:line.relation}]-(to);
```

- 9683 ms
- Created 156584 relationships, Set 156584 properties

#### Production_companies && movies

```
using periodic commit 100000 load csv with headers from "file:///production_companies_relation.csv" as line match (from:company {id: line.companyId}),(to:movie {id:line.movieId}) merge (from)-[r:PRODUCT{relation:line.relation}]-(to);
```

- 6716 ms
- Created 70464 relationships, Set 70464 properties

#### Production_countries && movies

```
using periodic commit 100000 load csv with headers from "file:///production_countries_relation.csv" as line match (from:country {iso_3166_1: line.countryId}),(to:movie {id:line.movieId}) merge (from)-[r:PRODUCT{relation:line.relation}]-(to);
```

- 29343 ms
- Created 49368 relationships, Set 49368 properties

#### Spoken_language && movies

```
using periodic commit 100000 load csv with headers from "file:///spoken_languages_relation.csv" as line match (from:movie {id: line.movieId}),(to:language {iso_639_1:line.languageId}) merge (from)-[r:SPEAK{relation:line.relation}]-(to);
```

- 3576 ms
- Created 53266 relationships, Set 53266 properties

#### User && movies

```
using periodic commit 100000 load csv with headers from "file:///ratings_merged.csv" as line match (from:user {userId: line.userId}),(to:movie {id:line.movieId}) merge (from)-[r:RANK{rating:line.rating,timestamp:line.timestamp}]-(to);
```

- 1212196 ms
- Created 11437747 relationships, Set 22875494 properties


##查询节点

###User

```
Match(u:user) Return u;
```

- 26ms
- 270554 records

###Movie

```
Match(m:movie) Return m;
```

- 25 ms
- 45433 records

###Language

```
Match(l:language) Return l;
```

- 24 ms
- 133 records

###Cast

```
Match(c:cast) Return c;
```

- 24 ms
- 206136 records

###Crew

```
Match(c:crew) Return c;
```

- 22 ms
- 161571 records

###Company

```
Match(c:company) Return c;
```

- 23 ms
- 23692 records

###Country

```
Match(c:country) Return c;
```

- 22 ms
- 161 records

###Genre

```
Match(g:genre) Return g;
```

- 21 ms
- 20 records

###Keyword

```
Match(k:keyword) Return k;
```

- 20 ms
- 19954 records

##查询关系

###User && Movie

```
MATCH (:user)-[r]->(:movie) RETURN r;
```

- 48 ms
- 11437747 records

###Crew && Movie

```
MATCH (:crew)-[r]->(:movie) RETURN r;
```

- 31 ms
- 422798 records

###Cast && Movie

```
MATCH (:cast)-[r]->(:movie) RETURN r;
```

- 30 ms
- 560815 records

###Keyword && Movie

```
MATCH (:keyword)-[r]->(:movie) RETURN r;
```

- 30 ms
- 156600 records

###Genre && Movie

```
MATCH (:movie)-[r]->(:genre) RETURN r;
```

- 28 ms
- 91015 records

###Language && Movie

```
MATCH (:movie)-[r]->(:language) RETURN r;
```

- 27 ms
- 53266 records

###Company && Movie

```
MATCH (:company)-[r]->(:movie) RETURN r;
```

- 30 ms
- 70464 records

###Country && Movie

```
MATCH (:country)-[r]->(:movie) RETURN r;
```

- 31 ms
- 49368 records

##查询案例

###查找2000年之后上映的全部电影(单类节点的查询)

```

```

###查找所有的喜剧片（利用关系和节点的查询）

```

```

###查找平均评分4.0以上的电影（利用关系和节点并运算的查询）

```

```

##更新节点

### User

```
Match(u:user) SET u +={testProperty:"测试"} Return u;
```

- 21 ms
- Set 270554 properties

```
Match(u:user) REMOVE u.testProperty Return u;
```

- 21 ms
- Set 270554 properties

### Movie

```
Match(m:movie) SET m +={testProperty:"测试"} Return m;
```

- 18 ms
- Set 45433 properties

```
Match(m:movie) REMOVE m.testProperty Return m;
```

- 19 ms
- Set 270554 properties

### Crew

```
Match(c:crew) SET c +={testProperty:"测试"} Return c;
```

- 17 ms
- Set 161571 properties

```
Match(c:crew) REMOVE c.testProperty Return c;
```

- 17 ms
- Set 161571 properties

### Cast

```
Match(c:cast) SET c +={testProperty:"测试"} Return c;
```

- 17 ms
- Set 206136 properties

```
Match(c:cast) REMOVE c.testProperty Return c;
```

- 16 ms
- Set 206136 properties

### Country

```
Match(c:country) SET c +={testProperty:"测试"} Return c;
```

- 16 ms
- Set 161 properties

```
Match(c:country) REMOVE c.testProperty Return c;
```

- 17 ms
- Set 161 properties

### Company

```
Match(c:company) SET c +={testProperty:"测试"} Return c;
```

- 18 ms
- Set 23692 properties

```
Match(c:company) REMOVE c.testProperty Return c;
```

- 21 ms
- Set 23692 properties

### Language

```
Match(l:language) SET l +={testProperty:"测试"} Return l;
```

- 17 ms
- Set 133 properties

```
Match(l:language) REMOVE l.testProperty Return l;
```

- 16 ms
- Set 133 properties

### Genre

```
Match(g:genre) SET g +={testProperty:"测试"} Return g;
```

- 16 ms
- Set 20 properties

```
Match(g:genre) REMOVE g.testProperty Return g;
```

- 16 ms
- Set 20 properties

### Keyword

```
Match(k:keyword) SET k +={testProperty:"测试"} Return k;
```

- 17 ms
- Set 19954 properties

```
Match(k:keyword) REMOVE k.testProperty Return k;
```

- 19 ms
- Set 19954 properties

