import pymysql
import json

class DBTable():
    def __init__(self, Name, colName, colType, priKey, DB=None, autoPriKey=False, foreignKey=None, SQLFile=None, executeSQL=True):
        super(DBTable, self).__init__()
        self.Name = Name
        self.colName = colName
        self.colType = colType #dictionary
        self.priKey = priKey
        self.autoPriKey = autoPriKey
        self.foreignKey = foreignKey
        self.DB = DB
        self.SQLFile = SQLFile
        self.executeSQL = executeSQL
        if DB is not None:
            self.create()

    def create(self):
        autoSql = 'auto_increment ' if self.autoPriKey else ''
        sql = 'create table if not exists ' + self.Name + '('
        for Name in self.colName:
            if Name is self.priKey:
                sql += Name + ' ' + self.colType[Name] + ' not null ' + autoSql + 'primary key' + ','
            else:
                sql += Name + ' ' + self.colType[Name] + ','
        foreignSql = ''
        if self.foreignKey is not None:
            FaName = list(self.foreignKey.keys())[0]
            foreignSql = ',' + FaName + self.foreignKey[FaName] + ' int not null, foreign key fk_' + FaName + '(' + FaName + self.foreignKey[FaName] + ') references ' + FaName + '(' + self.foreignKey[FaName] + ')'#') ON UPDATE CASCADE ON DELETE RESTRICT'
        sql = sql[:-1]
        sql += foreignSql + ')engine=InnoDB default charset=utf8;'
        if self.SQLFile is not None:
            self.SQLFile.write(sql + '\n')
        self.DB.execute(sql)

    def data2str(self, data, div):
        ret = ''
        for item in data.keys():
            ret += item + '='
            if type(data[item]) is str:
                ret += '\'' + data[item].replace('\'', '\\\'') + '\'' + div
            else:
                ret += str(data[item]) + div
        return ret[:-len(div)]

    def insert(self, data):
        sql = 'insert into ' + self.Name + '(%s) values(%s)'
        cols = ', '.join('`{}`'.format(k) for k in data.keys())
        val_cols = ', '.join('%({})s'.format(k) for k in data.keys())
        res_sql = sql % (cols, val_cols)
        self.DB.execute(res_sql, data=data)

    def delete(self, data=None, cond=''):
        ret = self.select(cond=cond, data=data)
        if data is not None:
            cond = self.data2str(data, ' and ')
        if cond != '':
            sql = 'delete from ' + self.Name + ' where ' + cond + ';'
        else:
            sql = 'delete from ' + self.Name + ';'
        self.DB.execute(sql)
        return ret

    def update(self, data, condData):
        fieldAndValues = self.data2str(data, ',')
        condStr = self.data2str(condData, ' and ')
        sql = 'update ' + self.Name + ' set ' + fieldAndValues + ' where ' + condStr + ';'
        self.DB.execute(sql)
    
    def sel2json(self, datas):
        ret = []
        if datas is None or len(datas) == 0:
            return None
        for data in datas:
            json = {}
            for idx in range(len(data)):
                json[self.colName[idx]] = data[idx]
            ret.append(json)
        return ret

    def select(self, cond=None, data=None):
        if cond is None and data is None:
            sql = 'select * from ' + self.Name + ';'
        elif data is None:
            sql = 'select * from ' + self.Name + ' where ' + cond + ';'
        else:
            sql = 'select * from ' + self.Name + ' where ' + self.data2str(data, ' and ') + ';'
        return self.sel2json(self.DB.execute(sql, True))
    
    def deleteTable(self):
        sql = 'drop table ' + self.Name + ';'
        self.DB.execute(sql)

class MovieDB():
    def __init__(self, Host='localhost', User='root', Password='123456', Database='movieDB', Port=3306, Debug=False, executeSQL=True):
        super(MovieDB, self).__init__()
        self.executeSQL = executeSQL
        if executeSQL:
            self.connect(Host, User, Password, Database, Port)
        self.DEBUG = Debug
        if Debug:
            self.sqlLog = open('./sqlCommandTrace.log', 'w')
        self.tables = {}
    
    def execute(self, sql, requestRet=False, data=None):
        if not self.executeSQL:
            return
        if self.DEBUG:
            self.sqlLog.write(sql + '\n')
        if data is not None:
            self.cursor.execute(sql, data)
            self.commit()
            return
        self.cursor.execute(sql)
        if requestRet:
            ret = self.cursor.fetchall()
            return ret
    
    def commit(self):
        try:
            self.db.commit()
        except:
            self.db.rollback()

    def tableCreate(self, tableName, colType, priKey, autoPriKey=False, foreignKey=None, SQLFile=None, executeSQL=True):
        self.tables[tableName] = DBTable(tableName, list(colType.keys()), colType, priKey, self, autoPriKey, foreignKey, SQLFile=SQLFile, executeSQL=executeSQL)

    def delete(self):
        tableFa = None
        for table in self.tables.keys():
            if tableFa is None:
                tableFa = table
                continue
            self.tables[table].deleteTable()
        self.tables[tableFa].deleteTable()

    def connect(self, Host, User, Password, Database, Port):
        self.db = pymysql.connect(host=Host, user=User, password=Password, database=Database, port=Port)
        self.cursor = self.db.cursor()
    
    def close(self):
        self.db.close()
        if self.DEBUG:
            self.sqlLog.close()