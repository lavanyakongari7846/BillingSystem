import pymongo
from pymongo import MongoClient
from random import randint
import copy
#Step 1: Connect to MongoDB - Note: Change connection string as needed
client = MongoClient(port=27017)#("mongodb://127.0.0.1:27017/?compressors=disabled&gssapiServiceName=mongodb")#(port=27017)
db = None
tb_name = None
id_1 = 0

#Step 2: Create sample data

def check_db_exist(db_name):
    global db
    ret=-1
    lst_dbs = client.list_database_names()
    for db_in in lst_dbs:
        print(db_in)
    if db_name in lst_dbs:
        ret = 1

    return ret

def create_db_in_mongo(db_name):
    global db
    if check_db_exist(db_name):
        print("Database {0} already Exist".format(db_name))
        db=client[db_name]
    else:
        db = client[db_name]
        print("Database {0} created".format(db_name))

def check_tb_exist(tb_nm):
    global db
    ret=-1
    lst_tbs = db.list_collection_names()
    if tb_nm in lst_tbs:
        ret = 1
    return ret

def create_table_in_mongo(tb_nm):
    global db, tb_name
    if check_tb_exist(tb_nm):
        print("Table {0} already Exist".format(tb_nm))
        tb_name = db['Bills']
        print(tb_name)
    else:
        tb_name = db[tb_nm]
        print("Table {0} created".format(tb_nm))

def get_std_json(s_name,s_clg,s_class,s_per):
    global id_1
    #for x in range(1, 10):
    id_1 = id_1 + 1
    std_json_table = {
        'iD' : id_1,
        's_name' : s_name,
        's_clg' : s_clg,
        's_class' : s_class,
        's_per' : s_per
    }
    
    return std_json_table

def writ_rcd_many_to_mongo(table):
    
    global db, tb_name, id_1
    lst=[]
    id_1 = id_1 + 1
    print(id_1)
    #table['iD'] = id_1
    #print(table)
    lst.append(table)
    #print(lst)
    result=db.tb_name.insert_many(table)
    #print('Created {0} {1}'.format(table,result.inserted_id))

def writ_rcd_to_mongo(table):
    
    global db, tb_name, id_1
    id_1 = id_1 + 1
    table['iD'] = id_1
    temp = {}
    temp = copy.deepcopy(table)
    print("temp",temp)
    table.clear()
    result=db.tb_name.insert_one(temp)
    temp.clear()
    print('Created {0} {1}'.format(table,result.inserted_id))      

def read_rcd_to_mongo():
    global db, tb_name
    d={}
    ret = -1
    i=0
    print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
    try :
        records = db.tb_name.find()
        print("records",records)
        if records:
            for x in records:
                print(x)
                d[i]=x
                i=i+1
            ret = d
        else:
            print("No records")
        return ret
    except:
        print("NO TABLE")
        return ret
        
def read_one_rcd_mongo(rec_id):
    global db, tb_name
    d={}
    ret = -1
    i=0
    try:
        cursor = db.tb_name.find({"iD":rec_id})
        
        for recc in cursor:
            return recc
        '''
        if cursor:
            for document in cursor:
                print(document)
                d[i]=document
                i=i+1
            return d
        else:
            print("No Records")
        '''
        
    except:
        print("no table")
        return d
    
    
def delete_db_in_mongo():

    global db, tb_name
    
    ret=-1
    if db:
        print(db.tb_name.drop())
        ret=1
        db = ""
        tb_name = ""
    return ret

def del_tb_rec(rec_id):
    
    global db,tb_name 
    Filter = {'iD': rec_id}
    print(Filter)
    result = db.tb_name.delete_one(Filter)
    print("Record {0} Deleted".format(result))
    #print("API call recieved:", result.acknowledged)
    #print("Documents deleted:", result.deleted_count)

def upd_tb_rec(rec_id, rec):
    global db,tb_name

    myquery = { 'iD' : rec_id }
    newvalues = { "$set": rec }

    u=db.tb_name.update_many(myquery,newvalues)
    print("Record {0} updated".format(u))
    print("API call recieved:", u.acknowledged)
    #print("Documents deleted:", u.updated_count)


