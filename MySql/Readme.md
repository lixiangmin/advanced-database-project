## Mysql Document

* `mysql`服务（可在`MovieDB.py`的`class MovieDB`构造函数中修改配置）

  ```
  user: root
  password: 123456
  database: movieDB
  port: 3306
  ```

* 由于`credits.csv`文件中字段`order`，`character`在`mysql`中是关键字，调用`dataProcess.py`中的函数`preCSV('credits')`生成文件`credits_new.csv`，其中原关键字字段变为`_order`，`_character`

* 数据文件路径为`../data/*.csv`

* 运行`dataProcess.py`，会依次建表并将所有数据插入数据库。

