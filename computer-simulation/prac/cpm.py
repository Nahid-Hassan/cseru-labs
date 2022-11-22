class Activities:
    def __init__(self, idx, activities, duration) -> None:
        self.idx = idx
        self.activities = activities
        self.duration = duration
        self.predecessor = []
        self.successor = []
        self.es, self.ef, self.ls, self.lf = 0, 0, 0, 0

activities = {}
index = []

for task in open('./in.txt'):
    task = task.strip().split(',')
    idx = int(task[0])
    predecessor = task[3].split(';')

    index.append(idx)
    activities[idx] = Activities(idx, task[1], int(task[2]))

    if predecessor[0] != '':
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
            if mx_time < activities[pre].ef:
                mx_time = activities[pre].ef
            
        activities[idx].es = mx_time
        activities[idx].ef = mx_time + activities[idx].duration
    maxEF = max(maxEF, activities[idx].ef)

print(maxEF)

for i in range(len(index)):
    idx = index[len(index) - 1 - i]

    if len(activities[idx].successor) == 0:
        activities[idx].lf = maxEF
        activities[idx].ls = maxEF - activities[idx].duration
    else:
        mn_time = 324324
        for s in activities[idx].successor:
            if activities[s].ls < mn_time:
                mn_time = activities[s].ls
        
        activities[idx].lf = mn_time
        activities[idx].ls = mn_time - activities[idx].duration

result = [activities[idx].activities for idx in index if activities[idx].ef == activities[idx].lf]
print(result)