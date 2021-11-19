## Tutorial

* Step 1.

  * 将原始`csv`文件保存在`../data/`路径下

* Step 2.

  * `python dataProcess.py`

    * 运行约`12min`，将生成如下文件：

      ```
      create&insert.sql
      processedData
      |   credits_new.csv
      |   credits_newcast.csv
      |   credits_newcrew.csv
      |   keywords.csv
      |   keywordskeywords.csv
      |   movies_metadata.csv
      |   ...
      ```

      `sql`文件包含建表并插入所有`csv`的操作

      以`credits`为例，对于原`credits.csv`先把字段`order`，`character`修改为`_order`、`_character`保存为`../data/credits_new.csv`文件

      - 将该文件中的`json`字段删除得到`./processedData/credits_new.csv`文件

      - 将该文件中的`cast json list`字段建表，增加主键`autoId`，外键`credits_newid`，得到`credits_newcast.csv`
      - `credits_newcrew.csv`同理

* Step 3.

  * `dataProcess.py`中的`Data, DataJson`变量保存了一个表所有数据
    * `Data[i][key]`表示主表第`i`行`key`字段的`value`
      * 如`Data[0]['id']`
    * `DataJson[Child][i][key]`表示子表`Child`第`i`行`key`字段的`value`
      * 如`DataJson['cast'][0]['cast_id']`

