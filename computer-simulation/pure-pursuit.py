import math 

vf = 20      # fighter velocity
fp = (0, 0)  # fighter position

# collect bomber position from file
bomber_coordinates = []
for line in open('./bomber_coordinates.txt'):
    x, y = line.strip().split(',')
    x, y = int(x), int(y)

    bomber_coordinates.append([x, y])

# print(bomber_coordinates)
T = len(bomber_coordinates)

fighter_coordinates = [fp]
for t in range(T):
    if t > 10:
        print("Bomber Escaped!!")
        break

    dist = math.dist(bomber_coordinates[t], fighter_coordinates[t])
    if dist <= 10:
        print("Yes, at time {} and at position {}".format(t, fighter_coordinates[t]))
        break
    else:
        fx = fighter_coordinates[t][0] + vf * ((bomber_coordinates[t][0] - fighter_coordinates[t][0]) / dist)
        fy = fighter_coordinates[t][1] + vf * ((bomber_coordinates[t][1] - fighter_coordinates[t][1]) / dist)

        fighter_coordinates.append([fx, fy])
    