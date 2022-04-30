import json
import csv

def get_json_values(file, key):

    with open(file, "r") as jsonfile:
        items = json.load(jsonfile)

        with open("{}_output.csv".format(key), "w", newline ='') as ids:
            writer = csv.writer(ids)

            def get_all(myjson,key):
                if type(myjson) == str:
                    myjson = json.loads(myjson)
                if type(myjson) is dict:
                    for jsonkey in myjson:
                        if type(myjson[jsonkey]) in (list,dict):
                            get_all(myjson[jsonkey], key)
                        elif jsonkey == key and myjson[jsonkey] != '':
                            writer.writerow([myjson[jsonkey]])
                elif type(myjson) is list:
                    for item in myjson:
                        if type(item) in (list,dict):
                            get_all(item,key)
            
            output =  get_all(items,key)