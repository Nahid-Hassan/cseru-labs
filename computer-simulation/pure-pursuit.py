import math 
import pygame

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

pygame.init()
win = pygame.display.set_mode((300,400))
pygame.display.set_caption('Bomber - Fighter')

run = True
while run:
    pygame.time.delay(100)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        for i in range(len(fighter_coordinates)):
            fp = fighter_coordinates[i]
            bp = bomber_coordinates[i]
            pygame.time.delay(100)
            fp = [abs(fp[0]), abs(fp[0])]
            bp = [abs(bp[0]), abs(bp[0])]

            print(fp, bp)

            pygame.draw.line(win, (255,0,0), fp, bp, 1)
            pygame.display.update()

pygame.quit()