import json
import os
import argparse

global filename 
filename ="task_data.json"
parser = argparse.ArgumentParser(description='Task Tracker')
parser.add_argument('data', type=str,help='[action] [id or description] [sub-action]',nargs='*')
args = parser.parse_args()

def add(id,description,pev_data:dict):
    pev_data[id] = description
    return f"Task added successfully (ID: {id})"

def main(args,pev_data:dict):
    try:
        
        action = args.data[0].lower()

        if action == 'add':
            _id = int(max(pev_data.keys()))+1
            description = args.data[1]
            message = add(_id,description,pev_data)
        elif action in ['update','delete']:
            _id = args.data[1]
            description = args.data[2]
        
        elif action.startswith('mark'):
            _id = args.data[1]
            action ='mark'
            description = action[4:]
        
        elif action == 'list':
            description = args.data[1]
        writeData(pev_data,filename)
        print(message) 
    
    except IndexError:
        print("For help please use -h")
        return None
 

def writeData(entry,filename):
    try:
        with open(filename, 'w') as file:
            json.dump(entry,fp=file)
        return True
    except Exception as e:
        print(e)
        return False

def readData(filename):
    task_data=dict()
    try:
        with open(filename, 'r') as file:
            task_data=json.load(fp=file)
        return task_data
    except Exception as e:
        print(e)
        return task_data



pev_data = readData(filename)
user_input = main(args,pev_data)
