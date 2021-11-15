# MongoDB

In this part, we offer all the files required to load data into the remote MongoDB.



## File structure

- config.ini: store the remote URL of the MongoDB, containing the host version and the docker version
- data_preprocess.py: merge the two CSV files containing the data of the same table, i.e., links.csv & ratings.csv
- data_load.py: read the preprocessed data saved in CSV files and write it into the remote MongoDB (URL stored in the file config.ini)



## How to use

### Step 1: Data Preprocess

Copy the original data directory ( have to be named /data/ ) into the current directory and run the following command in the shell:

```shell
mkdir parse_files
python3 data_preprocess.py
```

The process result would be saved in the files in the created directory parse_files, named links_merged.csv and rating_merged.csv.



### Step 2: Data Load

First, make sure the remote MongoDB is ready and save the URL of MongoDB in the file config.ini. Run the following command then in the shell to write the data saved in the directory data into MongoDB:

```shell
python3 data_load.py
```



