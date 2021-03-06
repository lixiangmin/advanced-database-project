import os
import math
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
    print(fileName + '.csv preparation finished.')

def exportCSV(Data, colType, fileName):
    colList = list(colType.keys())
    dataList = []
    for item in Data:
        dataList.append([])
        for colName in colList:
            dataList[-1].append(item[colName])
    test = pd.DataFrame(columns=colList, data=dataList)
    '''
    # debug code
    if fileName == 'movies_metadataspoken_languages':
        print(list(test.values)[506])
        print(list(test.values)[507])
        print(list(test.values)[508])
    '''
    if not os.path.exists('./processedData'):
        os.makedirs('./processedData')
    test.to_csv('./processedData/' + fileName + '.csv', index=None, encoding='utf-8')
    print(fileName + '.csv export finished.')

def GenSQL(fileName, SQLFile):
    output = [
        '',
        'select \'insert ' + fileName + ' : \';',
        'load data infile \'/home/lc/Task/Course/DBcourse/src/processedData/' + fileName + '.csv\'',
        'into table ' + fileName,
        'fields terminated by \',\' optionally enclosed by \'\"\'',
        'lines terminated by \'\\n\'',
        'IGNORE 1 LINES;'
    ]
    for item in output:
        SQLFile.write(item + '\n')

def importCSV(DB, fileName, colType, priKey, addPriKey=False, mergeFile=None, Export2CSV=True, Insert2DB=False, SQLFile=None):
    colTypeFa = {}
    colTypeCh = {}
    for key in colType.keys():
        if type(colType[key]) is str: # not json
            colTypeFa[key] = colType[key]
        else: # json/json list
            colTypeCh[key] = colType[key]

    autoIdDict = {}
    DB.tableCreate(fileName, colTypeFa, priKey, SQLFile=SQLFile, executeSQL=Insert2DB)
    for key in colTypeCh.keys():
        if 'autoId' in colTypeCh[key]['colType']:
            autoIdDict[key] = 0
        DB.tableCreate(
            tableName=fileName + colTypeCh[key]['name'],
            colType=colTypeCh[key]['colType'],
            priKey=colTypeCh[key]['priKey'],
            autoPriKey=colTypeCh[key]['autoPriKey'],
            foreignKey={fileName : colTypeCh[key]['foreignKey']},
            SQLFile=SQLFile,
            executeSQL=Insert2DB)

    if SQLFile is not None:
        GenSQL(fileName, SQLFile)
        for key in colTypeCh.keys():
            GenSQL(fileName + colTypeCh[key]['name'], SQLFile)

    if not Export2CSV and not Insert2DB:
        return

    dataset = pd.read_csv('../data/' + fileName + '.csv', header=0, encoding='utf-8', dtype=str)
    cols = dataset.columns
    dataList = list(dataset.values)
    if mergeFile is not None:
        for file2merge in mergeFile:
            dataList += list(pd.read_csv('../data/' + file2merge + '.csv', header=0, encoding='utf-8', dtype=str).values)

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
                        data[key] = math.nan
                else:
                    data[key] = str(item[key])
            except:
                data[key] = None
                continue
        if addPriKey:
            priId += 1
            data[priKey] = priId
            Data.append(data)
            continue
        if priKey not in data.keys() or data[priKey] in idSet or data[priKey] is None or data[priKey] == math.nan:
            continue
        for key in colTypeCh.keys():
            if type(item[key]) is not str: #None
                continue
            if colTypeCh[key]['type'] == 'json':
                item[key] = '[' + item[key] + ']'
            item[key] = eval(item[key])
            if type(item[key]) is list:
                for dataItem in item[key]:
                    if type(dataItem) is dict:
                        dataItem[fileName + colTypeCh[key]['foreignKey']] = data[colTypeCh[key]['foreignKey']]
                        '''
                        # debug code
                        if data[colTypeCh[key]['foreignKey']] == 0 or data[colTypeCh[key]['foreignKey']] is None or data[colTypeCh[key]['foreignKey']] is math.nan:
                            print(data[colTypeCh[key]['foreignKey']])
                        '''
                        if 'autoId' in colTypeCh[key]['colType']:
                            dataItem['autoId'] = autoIdDict[key]
                            autoIdDict[key] += 1
                        dataJson[key].append(dataItem)

        idSet.add(data[priKey])
        Data.append(data)
        for key in colTypeCh.keys():
            for item in dataJson[key]:
                DataJson[key].append(item)

    '''
    # debug code
    # print(DataJson['spoken_languages'][507])
    # print(Data[126])
    for idx in range(1000):
        if Data[19000 + idx]['imdb_id'] == 'tt0113002':
            print(Data[19000 + idx])
            print(Data[19001 + idx])
    '''
    
    if Export2CSV:
        exportCSV(Data, colTypeFa, fileName)
        for key in colTypeCh.keys():
            colTypeCh[key]['colType'][fileName + colTypeCh[key]['foreignKey']] = colTypeFa[colTypeCh[key]['foreignKey']]
            exportCSV(DataJson[key], colTypeCh[key]['colType'], fileName + colTypeCh[key]['name'])

    if Insert2DB:
        print(fileName + '.csv data insert begin...')
        for idx, item in enumerate(Data):
            if idx % 1000 == 0:
                print(idx)
            DB.tables[fileName].insert(item)
        for key in colTypeCh.keys():
            for idx, item in enumerate(DataJson[key]):
                if idx % 1000 == 0:
                    print(idx)
                DB.tables[fileName + colTypeCh[key]['name']].insert(item)
        print(fileName + '.csv data insert finished.')

if __name__ == '__main__':

    movieDB = MovieDB()
    SQLFile = open('./create&insert.sql', 'w')
    SQLFile.write('set @@sql_mode=ANSI;\n\n')
    SQLFile.write('create database movieDB character set utf8;\n')
    SQLFile.write('use movieDB;\n\n')

    Export2CSV = True
    Insert2DB = False
    
    proMovies_metadata = True
    proLinks = True
    proRatings = True
    proCredits = True
    proKeywords = True

    # movies_metadata
    if proMovies_metadata:
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
                    'autoPriKey' : False,
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
                    'autoPriKey' : False,
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
                        'name' : 'varchar(150)',
                        'autoId' : 'int'
                    },
                    'autoPriKey' : False,
                    'priKey' : 'autoId',
                    'foreignKey' : 'id'
                },
                'production_countries' : {
                    'type' : 'list',
                    'name' : 'production_countries',
                    'colType' : {
                        'iso_3166_1' : 'varchar(10)',
                        'name' : 'varchar(100)',
                        'autoId' : 'int'
                    },
                    'autoPriKey' : False,
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
                    'autoPriKey' : False,
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
            priKey='id',
            Export2CSV=Export2CSV,
            Insert2DB=Insert2DB,
            SQLFile=SQLFile
        )

    # links
    if proLinks:
        importCSV(
            DB=movieDB,
            fileName='links',
            colType={
                'movieId' : 'int',
                'imdbId' : 'int',
                'tmdbId' : 'int'
            },
            priKey='movieId',
            mergeFile=['links_small'],
            Export2CSV=Export2CSV,
            Insert2DB=Insert2DB,
            SQLFile=SQLFile
        )

    # ratings
    if proRatings:
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
            mergeFile=['ratings_small'],
            Export2CSV=Export2CSV,
            Insert2DB=Insert2DB,
            SQLFile=SQLFile,
            addPriKey=True
        )

    # credits
    if proCredits:
        preCSV('credits')
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
                    'autoPriKey' : False,
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
                    'autoPriKey' : False,
                    'priKey' : 'autoId',
                    'foreignKey' : 'id'
                },
                'id' : 'int'
            },
            priKey='id',
            Export2CSV=Export2CSV,
            Insert2DB=Insert2DB,
            SQLFile=SQLFile
        )

    # keywords
    if proKeywords:
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
                    'autoPriKey' : False,
                    'priKey' : 'autoId',
                    'foreignKey' : 'id'
                }
            },
            priKey='id',
            Export2CSV=Export2CSV,
            Insert2DB=Insert2DB,
            SQLFile=SQLFile
        )

    if SQLFile is not None:
        SQLFile.close()