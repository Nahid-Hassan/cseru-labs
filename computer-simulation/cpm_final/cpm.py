class Activity:
    def __init__(self, idx, activity, duration) -> None:
        self.idx = idx
        self.activity = activity
        self.duration = duration
                                                                # activity object
        self.predecessor = []
        self.successor = []
        self.es = 0   # early start
        self.ef = 0   # early finished
        self.ls = 0   # late start
        self.lf = 0   # late finished

activities = {}       # contain all the activities as dictionary
index = []            # contain task/activity id

for task in open('./in_cpm.txt'):     # task contain -> id, activity, duration, ...
    task = task.strip().split(',')
    idx = int(task[0])                
    predecessor = task[3].split(';')  

    index.append(idx) 
    activities[idx] = Activity(idx, task[1], int(task[2]))

    if len(predecessor) > 0 and predecessor[0] != '':           # read activity    
        for pre in predecessor:
            activities[idx].predecessor.append(int(pre))
            activities[int(pre)].successor.append(idx)

maxEF = 0
for idx in index:
    if len(activities[idx].predecessor) == 0:
        activities[idx].ef = activities[idx].duration 
    else:
        mx_time = 0
        for pre in activities[idx].predecessor:
            if mx_time < activities[pre].ef:                    # forward pass
                mx_time = activities[pre].ef
        
        activities[idx].es = mx_time
        activities[idx].ef = activities[idx].duration + mx_time
    maxEF = max(maxEF, activities[idx].ef) 

for i in range(len(index)):
    idx = index[len(index) - 1 - i]
    
    if len(activities[idx].successor) == 0:
        activities[idx].lf = maxEF
        activities[idx].ls = maxEF - activities[idx].duration
    else:                                                       # backward pass
        min_time = 999
        for s in activities[idx].successor:
            if min_time > activities[s].ls:
                min_time = activities[s].ls
        
        activities[idx].lf = min_time
        activities[idx].ls = min_time - activities[idx].duration

result = []
for idx in index:
    if activities[idx].ef == activities[idx].lf:
        result.append(activities[idx].activity)

print('Critical Path:', result, '\nMinimum finishing time:', maxEF)