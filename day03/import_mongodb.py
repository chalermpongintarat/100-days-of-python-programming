import json
import os
import csv
import time
import traceback
import subprocess

from pymongo import MongoClient, collation

def connect_mongodb():
    client = MongoClient(
        "127.0.0.1:27017",
        username="admin",
        password="",
        authSource="admin",
        authMechanism="SCRAM-SHA-256"
    )
    return client

client = connect_mongodb()

file_exception = open("exception.txt", "a")

path = "/sample/"
dir_list = os.listdir(path)
for x in dir_list:
    try:
        if '.' not in x:
            path_sample = '/sample/' + x + '/'
            dir_list_sample = os.listdir(path_sample)

            for n, y in enumerate(dir_list_sample):
                try:
                    start_time = time.time()
                    mydb = client[x]
                    db_name = y
                    collJson = mydb[db_name]

                    list_of_collections = mydb.list_collection_names()
                    if db_name not in list_of_collections:
                        json_path = path + x
                        json_dir = os.listdir(json_path)
                        if y.endswith("json"):
                            print(y, '('+str(n+1)+'/'+str(len(dir_list_sample))+')', y)
                            sizefile = os.path.getsize(json_path+'/'+y)
                            if sizefile != 0:
                                with open(json_path+'/'+y) as f:
                                    file_data = json.load(f)
                                collJson.insert_many(file_data)

                except Exception as e:
                    strError = str(traceback.format_exc())
                    print(strError)
                    file_exception.write(x+' '+str(strError) + "\n")

    except Exception as e:
        strError = str(traceback.format_exc())
        print(strError)
        file_exception.write(x+' '+str(strError) + "\n")

file_exception.close()