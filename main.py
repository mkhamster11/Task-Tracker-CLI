import json
import os
import argparse
from datetime import datetime
from messages import *
global base_dict,status_list ,filename,time_format

filename ="task_data.json"
base_dict = {"description":"","status":"todo","createdAt":"","updatedAt":""}
time_format = "%Y-%m-%dT%H:%M:%S"
status_list = [
    "done",
    "todo",
    "in-progress"
    ]

###################### parsering ###################################
parser = argparse.ArgumentParser(description='Task Tracker')
parser.add_argument('data', type=str,help='[action] [id or description] [sub-action]',nargs='*')
args = parser.parse_args()

def add(id,description,pev_data:dict):
    time_now = datetime.now()
    base_dict["description"]= description
    base_dict['createdAt'] = time_now.strftime(time_format)
    base_dict['updatedAt'] = time_now.strftime(time_format)
    pev_data[id] = base_dict
    return f"Task added successfully (ID: {id})"


def searchList(args,pev_data:dict):
    try:
        condition=args.data[1]
        if condition in status_list:
            print("| ID |  STATUS   |    CREATEDAT    |    UPDATEDAT    |    DESCRIPTION    |")                
            for key,entry in pev_data.items():
                if entry['status'] == condition:
                    print(f"|{key}|{entry['status']}|{entry['createdAt']}|{entry['updatedAt']}|{entry['description']}|")
        else:
            return f"please select only in this status: \n{status_list}"
    except IndexError:
        print("| ID |  STATUS   |    CREATEDAT    |    UPDATEDAT    |    DESCRIPTION    |")                
        for key,entry in pev_data.items():
            print(f"|{key}|{entry['status']}|{entry['createdAt']}|{entry['updatedAt']}|{entry['description']}|")
    except Exception as e:
        return e
def delete(id,pev_data):
    del pev_data[id]
    return f"Task successfully deleted (ID: {id})"

def update(id,description,pev_data:dict):
    time_now = datetime.now()
    temp_dict = pev_data.get(id)
    if not temp_dict:
        return vaild_id(id)
    
    temp_dict["description"]= description
    temp_dict['updatedAt'] = time_now.strftime(time_format)
    pev_data[id] = temp_dict
    return f"Task updated successfully (ID: {id})"

def status_update(id,status,pev_data:dict):
    time_now = datetime.now()
    temp_dict = pev_data.get(id)
    if not temp_dict:
        return vaild_id(id)
    temp_dict["status"]= status
    temp_dict['updatedAt'] = time_now.strftime(time_format)
    pev_data[id] = temp_dict
    return f"Task status successfully (ID: {id})"

def main(args,pev_data:dict):
    try:
        
        action = args.data[0].lower()

        if action == 'add':
            indexs = pev_data.keys()
            if indexs:
                _id = int(max(indexs))+1
            else: 
                _id = 1

            description = args.data[1]
            message=add(_id,description,pev_data)

        elif action in 'delete':
            _id = args.data[1]

            message=delete(_id,pev_data)

        elif action in 'update':
            _id = args.data[1]
            description = args.data[2]
            message=update(_id,description,pev_data)

        elif action.startswith('mark'):
            _id = args.data[1]
            status_type = action[5:].lower()
            if status_type in status_list:
                message=status_update(_id,status_type,pev_data)
            else:
                message = f"please select only in this status: \n{status_list}"
        
        elif action == 'list':
            message = searchList(args,pev_data)
        
        else:
            message="For help please use -h"
        writeData(pev_data)
        print(message)

    except Exception as e:
        print(e)
        return None
 

def writeData(entry):
    try:
        with open(filename, 'w') as file:
            json.dump(entry,fp=file)
        return True
    except Exception as e:
        print(e)
        return False

def readData():
    task_data=dict()
    try:
        with open(filename, 'r') as file:
            task_data=json.load(fp=file)
        return task_data
    except Exception as e:
        print("No data")
        return task_data



pev_data = readData()
output = main(args,pev_data)



