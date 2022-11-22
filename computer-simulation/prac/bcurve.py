import pygame

pygame.init()
win = pygame.display.set_mode((700,700))
pygame.display.set_caption('B Curve')

font = pygame.font.SysFont('ubuntu', 32)

pt0 = font.render('P0', True, (255,255,255))
pt1 = font.render('P1', True, (255,255,255))
pt2 = font.render('P2', True, (255,255,255))
pt3 = font.render('P3', True, (255,255,255))

rect0 = pt0.get_rect()
rect1 = pt1.get_rect()
rect2 = pt2.get_rect()
rect3 = pt3.get_rect()

run = True
t = 0

p0 = (100.0, 500.0)
p1 = (200.0, 100.0)
p2 = (600.0, 80.0)
p3 = (650.0, 410.0)

while run:
    win.fill((0,0,0))
    pygame.time.delay(100)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    while t < 1:
        t += .004

        bz0 = (pow(1-t, 3) * p0[0], pow(1-t, 3) * p0[1])
        bz1 = (pow(1-t, 2) * 3 * t * p1[0], pow(1-t,2) * 3 * t * p1[1])
        bz2 = ((1-t) * 3 * t * t * p2[0], (1-t) * 3 * t * t * p2[1])
        bz3 = (pow(t, 3) * p3[0], pow(t, 3) * p3[1])

        p = (bz0[0]+bz1[0]+bz2[0]+bz3[0],bz0[1]+bz1[1]+bz2[1]+bz3[1])
        x, y = int(p[0]), int(p[1])

        rect0.center = p0
        rect1.center = p1
        rect2.center = p2
        rect3.center = p3

        win.blit(pt0, rect0)
        win.blit(pt1, rect1)
        win.blit(pt2, rect2)
        win.blit(pt3, rect3)

        pygame.draw.line(win, (255,255,255), p0, p1, 1)
        pygame.draw.line(win, (255,255,255), p2, p3, 1)
        pygame.draw.circle(win, (255,255,255), (x, y), 1)

        pygame.display.update()

pygame.quit()
