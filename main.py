import pygame


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
                    pygame.draw.rect(surface, (0, 255, 255), (lX, lY, dist, dist), 1)
                else:
                    pygame.draw.rect(surface, (180, 110, 255),(lX, lY, dist, dist))
                pygame.display.update()
                return
            lX = lX + dist
        lX = 0
        lY = lY + dist
        


def makeMaze(surface, s, w):
    
    dist = s//w;
    
    lX = 0
    lY = 0
    
    for p in range(w):
        for q in range(w):
            pygame.draw.rect(surface, (0, 255, 255),(lX, lY, dist, dist), 1)
            lX = lX + dist
        lX = 0
        lY = lY + dist
        
    pygame.display.update()

def main():

    pygame.init()
    screen_size = 1000
    screen_width = 50
    run = True
    
    win = pygame.display.set_mode((screen_size, screen_size))
    pygame.display.set_caption("Breadth First Path Finding Algorithm")
    clock = pygame.time.Clock()
    win.fill((0,0,0))
    makeMaze(win, screen_size, screen_width)

    while run:
        clock.tick(10)
        pygame.time.delay(10)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()        
            makeObstacle(win, screen_size, screen_width, pos)
            
        
    
    


main()
