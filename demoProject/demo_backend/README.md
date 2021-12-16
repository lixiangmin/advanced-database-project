## 高级数据库demo backend

### 数据库：mysql

- database：advanced_database_course
- username：demo
- password：demo

- sql文件：resource/static下面
    - databaseCreate.sql创建表
    - 使用sql文件初始化数据库
      - 链接: https://pan.baidu.com/s/16-sii5pdHckfaOcDrTNs0A 
      - 提取码: 88wv
    - 利用neo4j中生成parse_files和relations文件夹中的文件进行数据库初始化
        - parse_files中csv文件对应数据库中各个实体
        - relations中csv文件对应数据库中关系表，导入时，不使用relations的csv中的relation字段，仅使用相关的实体id。
        - 导入方式：使用intellij提供数据库导入csv能力，使用时注意字段对应是否一致

### todo
-  利用python爬虫爬取相关数据
    -  poster的url
    -  电影链接

### finished
-  电影推荐接口
    - params： movie id
    - api: movie/recommend/{id}
    - response: 推荐id对应电影的数据

- 电影分页接口
    - params： offset(page)和count(size)
    - api: movie/list/{page}/{size}
    - response: 根据偏移(页码)和需要的数目(页大小)获取对应电影的数据

