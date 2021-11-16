# redis数据库性能测试
## 简介
csv_to_redis.py实现了将所选电影数据库导入redis数据库并计时的操作

redis_base_test.py 实现了对redis五种数据类型基本操作的计时测试
# Quick start
运行
```
python csv_to_redis.py
python redis_base_test.py
```
运行时目录
```
.
├── movie #电影数据集
│   ├── credits.csv
│   ├── keywords.csv
│   ├── links.csv
│   ├── links_small.csv
│   ├── movies_metadata.csv
│   ├── ratings.csv
│   └── ratings_small.csv
├── readme.md
├── csv_to_redis.py
└── redis_base_test.py
```
## 优势使用场景
## 性能测试
增删改查测试：
除了`redis_base_test.py`测试以外，还使用使用阿里云提供的`memtier-benchmark`，redis自带的`redis-benchmark`两个基准测试辅助是redis数据库性能。