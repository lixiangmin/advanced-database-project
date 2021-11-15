import math

import json
import pandas as pd

from MovieDB import *

def preCSV(fileName):
    dataset = pd.read_csv('../data/' + fileName + '.csv', header=0, encoding='utf-8', dtype=str)
    dataList = dataset.values
    for i in range(len(dataList)):
        for j in range(len(dataList[i])):
            dataList[i][j] = dataList[i][j].replace('\'order\'', '\'_order\'')
            dataList[i][j] = dataList[i][j].replace('\'character\'', '\'_character\'')
    dataset.to_csv('../data/' + fileName + '_new.csv', index=False, sep=',')

def importCSV(DB, fileName, colType, priKey, addPriKey=False):
    dataset = pd.read_csv('../data/' + fileName + '.csv', header=0, encoding='utf-8', dtype=str)
    cols = dataset.columns
    dataList = dataset.values
    colTypeFa = {}
    colTypeCh = {}
    for key in colType.keys():
        if type(colType[key]) is str: # not json
            colTypeFa[key] = colType[key]
        else: # json/json list
            colTypeCh[key] = colType[key]
    
    DB.tableCreate(fileName, colTypeFa, priKey)
    for key in colTypeCh.keys():
        DB.tableCreate(
            tableName=fileName + colTypeCh[key]['name'],
            colType=colTypeCh[key]['colType'],
            priKey=colTypeCh[key]['priKey'],
            autoPriKey=colTypeCh[key]['autoPriKey'],
            foreignKey={fileName : colTypeCh[key]['foreignKey']})

    Data = []
    DataJson = {}
    for key in colTypeCh.keys():
        DataJson[key] = []
    idSet = set()
    priId = 0
    for iteM in dataList:
        item = {}
        for idx in range(len(cols)):
            item[cols[idx]] = iteM[idx]
        data = {}
        dataJson = {}
        for key in colTypeCh.keys():
            dataJson[key] = []
        for key in colTypeFa.keys():
            try:
                if colTypeFa[key] == 'int' or colTypeFa[key] == 'double':
                    if not math.isnan(float(item[key])):
                        data[key] = int(item[key]) if colTypeFa[key] == 'int' else float(item[key])
                else:
                    data[key] = str(item[key])
            except:
                continue
        if addPriKey:
            priId += 1
            data[priKey] = priId
            Data.append(data)
            continue
        if priKey not in data.keys() or data[priKey] in idSet:
            continue
        for key in colTypeCh.keys():
            if colTypeCh[key]['type'] == 'json':
                item[key] = '[' + item[key] + ']'
            item[key] = eval(item[key])
            for dataItem in item[key]:
                dataItem[fileName + colTypeCh[key]['foreignKey']] = data[colTypeCh[key]['foreignKey']]
                dataJson[key].append(dataItem)

        idSet.add(data[priKey])
        Data.append(data)
        for key in colTypeCh.keys():
            for item in dataJson[key]:
                DataJson[key].append(item)
    
    for idx, item in enumerate(Data):
        if idx % 1000 == 0:
            print(idx)
        DB.tables[fileName].insert(item)
    for key in colTypeCh.keys():
        for idx, item in enumerate(DataJson[key]):
            if idx % 1000 == 0:
                print(idx)
            DB.tables[fileName + colTypeCh[key]['name']].insert(item)

if __name__ == '__main__':

    movieDB = MovieDB()

    # movies_metadata
    importCSV(
        DB=movieDB,
        fileName='movies_metadata',
        colType={
            'adult' : 'varchar(10)',
            'belongs_to_collection' : {
                'type' : 'json',
                'name' : 'belongs_to_collection',
                'colType' : {
                    'id' : 'int',
                    'name' : 'varchar(100)',
                    'poster_path' : 'varchar(200)',
                    'backdrop_path' : 'varchar(200)',
                    'autoId' : 'int'
                },
                'autoPriKey' : True,
                'priKey' : 'autoId',
                'foreignKey' : 'id'
            },
            'budget' :  'double',
            'genres' : {
                'type' : 'list',
                'name' : 'genres',
                'colType' : {
                    'id' : 'int',
                    'name' : 'varchar(100)',
                    'autoId' : 'int'
                },
                'autoPriKey' : True,
                'priKey' : 'autoId',
                'foreignKey' : 'id'
            },
            'homepage' : 'varchar(1000)',
            'id' : 'int',
            'imdb_id' : 'varchar(10)',
            'original_language' : 'varchar(5)',
            'original_title' : 'varchar(200)',
            'overview' : 'varchar(2000)',
            'popularity' : 'double',
            'poster_path' : 'varchar(100)',
            'production_companies' : {
                'type' : 'list',
                'name' : 'production_companies',
                'colType' : {
                    'id' : 'int',
                    'name' : 'varchar(100)',
                    'autoId' : 'int'
                },
                'autoPriKey' : True,
                'priKey' : 'autoId',
                'foreignKey' : 'id'
            },
            'production_countries' : {
                'type' : 'list',
                'name' : 'production_countries',
                'colType' : {
                    'iso_3166_1' : 'int',
                    'name' : 'varchar(100)',
                    'autoId' : 'int'
                },
                'autoPriKey' : True,
                'priKey' : 'autoId',
                'foreignKey' : 'id'
            },
            'release_date' : 'varchar(15)',
            'revenue' : 'double',
            'runtime' : 'double',
            'spoken_languages' : {
                'type' : 'list',
                'name' : 'spoken_languages',
                'colType' : {
                    'iso_639_1' : 'varchar(10)',
                    'name' : 'varchar(100)',
                    'autoId' : 'int'
                },
                'autoPriKey' : True,
                'priKey' : 'autoId',
                'foreignKey' : 'id'
            },
            'status' : 'varchar(200)',
            'tagline' : 'varchar(1000)',
            'title' : 'varchar(200)',
            'video' : 'varchar(10)',
            'vote_average' : 'double',
            'vote_count' : 'int'
        },
        priKey='id'
    )

    # links
    importCSV(
        DB=movieDB,
        fileName='links',
        colType={
            'movieId' : 'int',
            'imdbId' : 'int',
            'tmdbId' : 'int'
        },
        priKey='movieId'
    )

    # ratings
    importCSV(
        DB=movieDB,
        fileName='ratings',
        colType={
            'userId' : 'int',
            'movieId' : 'int',
            'rating' : 'double',
            'timestamp' : 'bigint',
            'rId' : 'int'
        },
        priKey='rId',
    )

    # credits
    importCSV(
        DB=movieDB,
        fileName='credits_new',
        colType={
            'cast' : {
                'type' : 'list',
                'name' : 'cast',
                'colType' : {
                    'cast_id' : 'int',
                    '_character' : 'varchar(1000)',
                    'credit_id' : 'varchar(100)',
                    'gender' : 'int',
                    'id' : 'int',
                    'name' : 'varchar(100)',
                    '_order' : 'int',
                    'profile_path' : 'varchar(100)',
                    'autoId' : 'int'
                },
                'autoPriKey' : True,
                'priKey' : 'autoId',
                'foreignKey' : 'id'
            },
            'crew' : {
                'type' : 'list',
                'name' : 'crew',
                'colType' : {
                    'credit_id' : 'varchar(1000)',
                    'department' : 'varchar(100)',
                    'gender' : 'int',
                    'id' : 'int',
                    'job' : 'varchar(100)',
                    'name' : 'varchar(100)',
                    'profile_path' : 'varchar(100)',
                    'autoId' : 'int'
                },
                'autoPriKey' : True,
                'priKey' : 'autoId',
                'foreignKey' : 'id'
            },
            'id' : 'int'
        },
        priKey='id'
    )

    # keywords
    importCSV(
        DB=movieDB,
        fileName='keywords',
        colType={
            'id' : 'int',
            'keywords' : {
                'type' : 'list',
                'name' : 'keywords',
                'colType' : {
                    'id' : 'int',
                    'name' : 'varchar(100)',
                    'autoId' : 'int'
                },
                'autoPriKey' : True,
                'priKey' : 'autoId',
                'foreignKey' : 'id'
            }
        },
        priKey='id'
    )