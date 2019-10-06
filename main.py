import pygame
import queue
from tkinter import *
from tkinter import messagebox


def makeObstacle(surface, s, w, pos):

    dist = s//w

    lX = 0
    lY = 0

    for p in range(w):
        for q in range(w):
            area = pygame.Rect(lX, lY, dist, dist)
            if area.collidepoint(pos):
                # print(pos)
                if surface.get_at(pos)[0:3] == (180, 110, 255):
                    pygame.draw.rect(surface, (0, 0, 0), (lX, lY, dist, dist))
                    pygame.draw.rect(surface, (0, 255, 255),
                                     (lX, lY, dist, dist), 1)
                else:
                    pygame.draw.rect(surface, (180, 110, 255),
                                     (lX, lY, dist, dist))
                pygame.display.update()
                return
            lX = lX + dist
        lX = 0
        lY = lY + dist


def makeMaze(surface, s, w):

    dist = s//w

    lX = 0
    lY = 0

    for p in range(w):
        for q in range(w):
            pygame.draw.rect(surface, (0, 255, 255), (lX, lY, dist, dist), 1)
            lX = lX + dist
        lX = 0
        lY = lY + dist

    pygame.display.update()


def Breadth_First_Algorithm(surface, s, w):

    dist = s//w

    start = (0, 0)
    finish = (s - dist, s - dist)

    pygame.draw.rect(surface, (0, 0, 255), (start, (dist, dist)))
    pygame.draw.rect(surface, (0, 255, 0), (finish, (dist, dist)))

    pygame.display.update()

    count = 0

    X = start[0] + (dist//w)
    Y = start[1] + (dist//w)

    path = queue.Queue()
    add = ""
    path.put(add)

    while True:

        add = path.get()

        X = X + (add.count('R') - add.count('L')) * dist
        Y = Y + (add.count('D') - add.count('U')) * dist
        try:
            if add[-1] != 'L' and X < (s - dist):
                if surface.get_at((X + dist, Y))[0:3] != (180, 110, 255):
                    path.put(add + 'R')
                    if surface.get_at((X + dist, Y))[0:3] != (0, 255, 0):
                        res = add + 'R'
                        print("Found: ", res)
                        break
        except:
            pass            
        
        try:
            if add[-1] != 'R' and X > dist:
                if surface.get_at((X - dist, Y))[0:3] != (180, 110, 255):
                    path.put(add + 'L')
                    if surface.get_at((X - dist, Y))[0:3] != (0, 255, 0):
                        res = add + 'L'
                        print("Found: ", res)
                        break
                    
        except:
            pass
        try:
            if add[-1] != 'D' and Y > dist:
                if surface.get_at((X, Y - dist))[0:3] != (180, 110, 255):
                    path.put(add + 'U')
                    if surface.get_at((X, Y - dist))[0:3] != (0, 255, 0):
                        res = add + 'U'
                        print("Found: ", res)
                        break
        except:
            pass
        try:
            if add[-1] != 'U' and Y < (s - dist):
                if surface.get_at((X, Y + dist))[0:3] != (180, 110, 255):
                    path.put(add + 'D')
                    if surface.get_at((X, Y + dist))[0:3] != (0, 255, 0):
                        res = add + 'D'
                        print("Found: ", res)
                        break
        except:
            pass
        count += 1

        if count >= (w*w) or path.empty() == True:
            print("Maze not Found")
            messagebox.showinfo("Path not found!")
            return

    X = start[0] + (dist//w)
    Y = start[1] + (dist//w)

    pygame.draw.rect(surface, (0, 255, 0), ((X, Y), (dist, dist)))

    for r in res:
        if r == 'L':
            X = X - dist
        if r == 'R':
            X = X + dist
        if r == 'U':
            Y = Y - dist
        if r == 'D':
            Y = Y + dist

        pygame.draw.rect(surface, (0, 255, 0), ((X, Y), (dist, dist)))
    
    pygame.display.update()


def main():

    pygame.init()
    screen_size = 500
    screen_width = 10
    run = True
    lock = 0

    win = pygame.display.set_mode((screen_size, screen_size))
    pygame.display.set_caption("Breadth First Path Finding Algorithm")
    clock = pygame.time.Clock()
    win.fill((0, 0, 0))
    makeMaze(win, screen_size, screen_width)

    while run:
        clock.tick(10)
        pygame.time.delay(10)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        if event.type == pygame.MOUSEBUTTONDOWN and lock == 0:
            pos = pygame.mouse.get_pos()
            makeObstacle(win, screen_size, screen_width, pos)
        keys = pygame.key.get_pressed()
        for key in keys:
            if keys[pygame.K_SPACE]:
                lock = 1
        if lock == 1:
            Breadth_First_Algorithm(win, screen_size, screen_width)
            lock = 2


main()
