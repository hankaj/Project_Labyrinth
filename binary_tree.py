import pygame
import random
import time

def pawel_tree(size):
    grid = []
    choice = ('N','W')
    white =(255, 255, 255)
    black =(0, 0, 0)

    in_pixels = 10
    dlay = int(1000/(size**2))

    bordur = size*2 + 1
    last = size*2 -2
    dis = size*2*in_pixels+in_pixels
    screen = pygame.display.set_mode(size=(dis, dis))
    pygame.display.set_caption("Project Labyrinth") 
    
    
    # Creating a modified grid below
    for i in range(1, size*2):
        grid.append([])
    
    for x in range(1, size*2):
        for y in range(1, size*2):
            if x % 2 == 1:
                if y % 2 == 1:
                    grid[x-1].append(1)
                elif y % 2 == 0:
                    grid[x-1].append(0)
            elif x % 2 == 0:
                grid[x-1].append(0)
    
    # Path carving
    def Connect(a, b):
        where = choice[random.randint(0, 1)]
        if a == 0 and b == 0:
            grid[0][b + 1] = 1
            grid[a + 1][0] = 1
    
        elif a == 0 and b != last:
            grid[0][b+1]=1

        elif b == 0 and a != last:
            grid[a+1][0]=1

        else:
            if where == 'N':
                grid[a-1][b]=1
            else:
                grid[a][b-1]=1
    
    
    def Draw(a,b):
        if grid[a][b] == 1:
            pygame.draw.rect(screen,white,[a*in_pixels,b*in_pixels,in_pixels,in_pixels])
        elif grid[a][b]==0:
            pygame.draw.rect(screen,black,[a*in_pixels,b*in_pixels,in_pixels,in_pixels])
    

    for i in range(0,last+1,2):
        for j in range(0,last+1,2):
            Connect(i,j)
    
    # adding a border
    grid.insert(0,[])
    grid.append([])
    for i in range(0,bordur):
        grid[0].append(0)
        grid[bordur-1].append(0)
    
    for i in range(1,bordur-1):
        grid[i].insert(0,0)
        grid[i].append(0)
    
    finish = False
    while not finish:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finish = True
        for i in range(bordur):
            for j in range(bordur):
                Draw(j,i)
        pygame.display.update()
   
    pygame.quit()
    
    
