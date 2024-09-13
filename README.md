
# Task Tracker cli 
Build a CLI app to track your tasks and manage your to-do list.



# Usage/Examples

### Adding a new task

```shell
python main.py add "Buy groceries"
# Output: Task added successfully (ID: 1)
```
### Updating and deleting tasks
```
python main.py update 1 "Buy groceries and cook dinner"
python main.py delete 1
```

### Marking a task as in progress or done
```
python main.py mark-in-progress 1
python main.py mark-done 1
```
### Listing all tasks
```
python main.py list
```
### Listing tasks by status
```
python main.py list done
python main.py list todo
python main.py list in-progress
```


## Tech Stack

**Language:** python3



## Acknowledgements

 - [from roadmap-task tacker](https://roadmap.sh/projects/task-tracker)


