import pygame
def Updatecell(pos,board):
    if(board[pos[0]][pos[1]][1]<2):return (0,pos[0],pos[1])
    if(board[pos[0]][pos[1]][1]>3):return (0,pos[0],pos[1])
    if(board[pos[0]][pos[1]][1]==2):return (board[pos[0]][pos[1]][0],pos[0],pos[1])
    return (1,pos[0],pos[1])
def Updateboard(change,board):
    nchange=set([])
    drawlist=[]
    updatedcells=[]
    for pos in change: updatedcells.append(Updatecell(pos,board))
    for pos in updatedcells:
        if(pos[0]!=board[pos[1]][pos[2]][0]):
            drawlist.append(pos)
            num=2*pos[0]-1
            board[pos[1]][pos[2]][0]=pos[0]
            for i in range(pos[1]-1,pos[1]+2):
                for j in range(pos[2]-1,pos[2]+2):
                    if not(i<0 or j<0 or i>(len(board)-1) or j>(len(board[0])-1)):
                        nchange.add((i,j))     
                        if(i!=pos[1] or j!=pos[2]): board[i][j][1]+=num
    return nchange,drawlist        
def Add(pos,num,board,change):
    board[pos[0]][pos[1]][0]=num
    change.add((pos[0],pos[1]))
    for i in range(pos[0]-1,pos[0]+2):
        for j in range(pos[1]-1,pos[1]+2):
            if not(i<0 or j<0 or i>(len(board)-1) or j>(len(board[0])-1) or(i==pos[0] and j==pos[1])):
                change.add((i,j))
                board[i][j][1]+=2*num-1
height=50
width=50
board=[[[0,0] for i in range(width)] for i in range(height)]
change=set()
pygame.init()
screen = pygame.display.set_mode((width*20,height*20))
pygame.display.set_caption('Game of Life')
for i in range(height):
    for j in range(width):
        if board[i][j][0]:rect_color=(0,0,0)
        else: rect_color=(255,255,255)
        if board[i][j][1]==2 :per_color=(0,0,255)
        elif board[i][j][1]==3:per_color=(0,255,0)
        elif board[i][j][1]>3:per_color=(255,0,0)
        else:per_color=(150,150,150)
        pygame.draw.rect(screen, rect_color, pygame.Rect(j*20,i*20,20,20))
        pygame.draw.rect(screen, per_color, pygame.Rect(j*20,i*20,20,20),2)
pygame.display.update()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                change,drawlist=Updateboard(change,board)
                for pos in drawlist:
                    if pos[0]:rect_color=(0,0,0)
                    else:rect_color=(255,255,255)
                    pygame.draw.rect(screen, rect_color, pygame.Rect(pos[2] * 20, pos[1] * 20, 20, 20))
                    for i in range(pos[1]-1,pos[1]+2):
                        for j in range(pos[2]-1,pos[2]+2):
                            if(i<0 or j<0 or i>=height or j>=width):continue
                            if board[i][j][1]==2 :per_color=(0,0,255)
                            elif board[i][j][1]==3:per_color=(0,255,0)
                            elif board[i][j][1]>3:per_color=(255,0,0)
                            else:per_color=(150,150,150)
                            pygame.draw.rect(screen, per_color, pygame.Rect(j * 20, i * 20, 20, 20),2)
                pygame.display.update()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            x=x//20
            y=y//20
            num=1-board[y][x][0]
            Add((y,x),num,board,change)
            if num:rect_color=(0,0,0)
            else:rect_color=(255,255,255)      
            pygame.draw.rect(screen, rect_color, pygame.Rect(x * 20, y * 20, 20, 20))
            for i in range(y-1,y+2):
                for j in range(x-1,x+2):
                    if(i<0 or j<0 or i>=height or j>=width):continue
                    if board[i][j][1]==2 :per_color=(0,0,255)
                    elif board[i][j][1]==3:per_color=(0,255,0)
                    elif board[i][j][1]>3:per_color=(255,0,0)
                    else:per_color=(150,150,150)
                    pygame.draw.rect(screen, per_color, pygame.Rect(j * 20, i * 20, 20, 20),2)
                pygame.display.update()
pygame.quit()