## 高级数据库demo backend

### 数据库初始化：mysql

- database：advanced_database_course
- username：demo
- password：demo

- sql文件：resource/static下面
    - databaseCreate.sql创建表
    
    - 使用sql文件初始化数据库
    
      - 各种数据表的Sql文件
        - 链接: https://pan.baidu.com/s/16-sii5pdHckfaOcDrTNs0A 
        - 提取码: 88wv
        
      - 数据库的sql文件
        - 链接: https://pan.baidu.com/s/1QFLq9UKjKmnkABf52AQv_g 
        - 提取码: b54n
        
    - 利用neo4j中生成parse_files和relations文件夹中的文件进行数据库初始化
        - parse_files中csv文件对应数据库中各个实体
        - relations中csv文件对应数据库中关系表，导入时，不使用relations的csv中的relation字段，仅使用相关的实体id。
        - 导入方式：使用intellij提供数据库导入csv能力，使用时注意字段对应是否一致
