def GetPendingTasks():
    pending_file = open("PendingTasks.txt","r")
    pending_tasks = pending_file.readlines()
    return pending_tasks

def GetFinishedTasks():
    finished_file = open("PendingTasks.txt","r")
    finished_tasks = finished_file.readlines()
    return finished_tasks

def DisplayTasks(tasks):
    print("-"*75)
    count = 1
    for task in tasks:
        print(str(count) + ". "+  task)
        count += 1
    print("-"*75)