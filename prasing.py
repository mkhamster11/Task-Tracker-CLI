import argparse
_description ="""
# Adding a new task
task-cli add "Buy groceries"
# Output: Task added successfully (ID: 1)

# Updating and deleting tasks
task-cli update 1 "Buy groceries and cook dinner"
task-cli delete 1

# Marking a task as in progress or done
task-cli mark-in-progress 1
task-cli mark-done 1

# Listing all tasks
task-cli list

# Listing tasks by status
task-cli list done
task-cli list todo
task-cli list in-progress"""




def clean_args(args):
    try:
        action = args.data[0].lower()
        id =None
        if action == 'add':
            description = args.data[1]
        
        elif action in ['update','delete']:
            id = args.data[1]
            description = args.data[2]
        
        elif action.startswith('mark'):
            id = args.data[1]
            action ='mark'
            description = action[4:]
        
        elif action == 'list':
            description = args.data[1]
        
        return id,action,description
    except IndexError:
        print("For help please use -h")
        
# print(id,description,"---",action)
data=clean_args(args)
print(data)