import pygame, time, sys, secrets
from time import sleep
from pygame import *

width, height, r, g, b, side, stop = 360, 360, 255, 255, 255, 40, False
list, lock_list, x, y, start, dir, helpWin = [], [], 0, 0, False, 1, 0
extend, pos, index, exitMenu, exitHelp, case, nr = 0, 1, 1, False, False, 1, 3

pygame.init()
pygame.font.init()
myfont = pygame.font.SysFont('Comic Sans MS', side//2)
menuFont = pygame.font.SysFont('Comic Sans MS', height//(2*nr+2))
helpFont = pygame.font.SysFont('Comic Sans MS', height//(6*nr+6))
menuText = [["Play", "Mode", "Exit"],["Casual", "Auto solve", "Generator"]]
helpButton = pygame.image.load("./images/helpButton.jpg")
helpButton = pygame.transform.scale(helpButton, (80, 80))
clickSound = pygame.mixer.Sound("./sounds/click.mp3")
selectSound = pygame.mixer.Sound("./sounds/select.mp3")

helpText ="""Sudoku is a board game, where you have to
complete a 81x81 board with digits from 1 to 9.
The board is devided in 9 fields and each
contains 9 blocks where to fill with digits.
The rule is to complete the board without have
on same line, column or field two same digits.
Initially, on the board can exists digits that
can't be replaced or changed. You can play a
generated game, fill initial numbers and then
start the game or auto solve it. """

screen = pygame.display.set_mode([width,height])
border = pygame.image.load("./images/border.jpg")
border = pygame.transform.scale(border, (width, height))


def generate(limitNumbers):
    global stop, start
    for i in range(limitNumbers):
        while True:
            x, y = secrets.randbelow(9), secrets.randbelow(9)
            if not list[x][y].lock:
                list[x][y].number = chr(secrets.randbelow(9)+49)
                if test(x,y):
                    list[x][y].lock = True
                    break
    stop = True
    start = True

def prev(helpWin):
    global exitHelp, index, pos
    if helpWin == 0:
        exitHelp = True
        index = 0
        pos = 0
        menu()
    else:
        next(helpWin-1)
        
def next(helpWin):
    helpWin += 1
    while True:
        helpX = pygame.image.load("./images/help"+str(helpWin)+".jpg")
        helpX = pygame.transform.scale(helpX, (width, height))
        screen.blit(helpX,(0,0))
        sudoku = helpFont.render("Sudoku",False, (0,g,0))
        screen.blit(sudoku, (width//2-15, height-45))
        
        sudoku = helpFont.render("Next",False, (0,0,b))
        screen.blit(sudoku, (width//2+85, height-45))
        
        sudoku = helpFont.render("Prev",False, (0,0,b))
        screen.blit(sudoku, (width//2-85, height-45))
        
        for event in pygame.event.get():
            if event.type == QUIT:
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse = pygame.mouse.get_pos()
                if mouse[1] >= 305 and mouse[1] <= 345:
                    if mouse[0] >= 70 and mouse[0] <= 135:
                        if helpWin != 0:
                            helpWin -= 1
                        prev(helpWin)
                    elif mouse[0] >= 255 and mouse[0] <= 315:
                        if helpWin < 2:
                            next(helpWin)
        
        pygame.display.flip()

def menu():
    global index, pos, case, helpWin, exitMenu, exitHelp, extend
    while not exitMenu:
        for i in range(1,nr+1):
            mouse = pygame.mouse.get_pos()
            if mouse[0] >= width//2-width//4 and mouse[0] <= width-width//4 and mouse[1] >= i*height/(nr+1)-height//(2*nr+2) and mouse[1] <= i*height/(nr+1)-height//(2*nr+2) + height//(2*nr-1):
                pos = i
        ok = True
        for i in range(1,nr+1):
            mouse = pygame.mouse.get_pos()
            if mouse[0] >= width//2-width//4 and mouse[0] <= width-width//4 and mouse[1] >= i*height/(nr+1)-height//(2*nr+2) and mouse[1] <= i*height/(nr+1)-height//(2*nr+2) + height//(2*nr-1):
                ok = False
        if ok == True:
            pos = 0
        if mouse[0] >= 0 and mouse[0] <= 80 and mouse[1] >= 0 and mouse[1] <= 80:
            pos = -1
        for event in pygame.event.get():
            if event.type == QUIT:
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                pygame.mixer.Channel(0).play(clickSound)
                if not pos == -1:
                    if index == 1:
                        if not pos == 2:
                            exitMenu = True
                        else:
                            index = 2
                    else:
                        case = pos
                        index = 1
                else:
                    w, h, index, nl = 0, 0, 0, 0
                    temp = [""]
                    while not exitHelp:
                        mouse = pygame.mouse.get_pos()
                        help = pygame.image.load("./images/help0.jpg")
                        help = pygame.transform.scale(help, (w, h))
                        if w < 360:
                            w += 1.2
                            h += 1.2
                        for event in pygame.event.get():
                            if event.type == QUIT:
                                quit()
                            if event.type == pygame.MOUSEBUTTONDOWN:
                                if mouse[1] >= 305 and mouse[1] <= 345:
                                    if mouse[0] >= 70 and mouse[0] <= 135:
                                        prev(helpWin)
                                    elif mouse[0] >= 255 and mouse[0] <= 315:
                                        next(helpWin)
                        screen.blit(help, (0, 0))
                        if w > 360:
                            sudoku = helpFont.render("Sudoku",False, (0,g,0))
                            screen.blit(sudoku, (width//2-15, height-45))
                            
                            sudoku = helpFont.render("Next",False, (0,0,b))
                            screen.blit(sudoku, (width//2+85, height-45))
                            
                            sudoku = helpFont.render("Prev",False, (0,0,b))
                            screen.blit(sudoku, (width//2-85, height-45))
                            if index < len(helpText):
                                if helpText[index] != '\n':
                                    temp[nl] += helpText[index]
                                else:
                                    nl += 1
                                    temp.append("")
                            for i in range(nl+1):
                                text = helpFont.render(temp[i],False, (r,0,0))
                                screen.blit(text, (15,10+i*height//(4*nr+4)))
                            sleep(0)
                            index += 1
                        pygame.display.flip()
                    exitHelp = False
        screen.blit(border, (0, 0))
        screen.blit(helpButton,(0,0))
        for i in range(1,nr+1):
            extend = 0
            if not pos == -1:
                if i == pos:
                    extend = 12
            pygame.draw.rect(screen, (102,0,0), pygame.Rect(width//2-width//4-extend//2, i*height/(nr+1)-height//(2*nr+2)-extend//2,width//2+extend,height//(2*nr-1)+extend),0,0,20,20,20,20)
        
        for i in range(1,nr+1):
            extend = 0
            if not pos == -1:
                if i == pos:
                    extend = 6
            menuFont = pygame.font.SysFont('Comic Sans MS', 3*height//(8*nr+8)+extend)
            text = menuFont.render(menuText[index-1][i-1],False, (r,0,0))
            text_rect = text.get_rect(center = (width//2, i*height/(nr+1)-height//(8*nr+8)))
            screen.blit(text,text_rect)
        pygame.display.flip()

def backtraking(x, y):
    global dir
    speed = 0
    if x == 9:
        sleep(3)
        exit()
    while x != 9 or y != 8:
        for event in pygame.event.get():
            if event.type == QUIT:
                quit()
        screen.fill((0,0,0))
        grid()
        pygame.draw.line(screen, (0,g,0), (0, height), (width, height), 4) 
        pygame.draw.line(screen, (0,g,0), (width, 0), (width, height), 4)
        pygame.display.flip() 
        if x != 9: 
            if list[x][y].lock:
                if dir == 1:    
                    if y != 8:
                        y += 1
                    else:
                        y = 0
                        if x != 9:
                            x += 1
                else:    
                    if y != 0:
                        y -= 1
                    else:
                        y = 8
                        if x != 0:
                            x -= 1
            else:
                if list[x][y].number == "":
                    inf = 0
                else:
                    inf = ord(list[x][y].number)-48
                if inf == 9:
                    list[x][y].number == ""
                        
                    screen.fill((0,0,0))
                    grid()
                    pygame.draw.line(screen, (0,g,0), (0, height), (width, height), 4) 
                    pygame.draw.line(screen, (0,g,0), (width, 0), (width, height), 4)
                    
                    sleep(speed)
                    dir = -1
                else:
                    for value in range(inf+1, 10):
                        list[x][y].number = chr(value+48)
                        
                        screen.fill((0,0,0))
                        grid()
                        pygame.draw.line(screen, (0,g,0), (0, height), (width, height), 4) 
                        pygame.draw.line(screen, (0,g,0), (width, 0), (width, height), 4)
                        
                        pygame.display.flip()
                        sleep(speed)
                        
                        if test(x, y):
                            dir = 1
                            break
                            
                    if not test(x, y):
                       list[x][y].number = ""
                       
                       screen.fill((0,0,0))
                       grid()
                       pygame.draw.line(screen, (0,g,0), (0, height), (width, height), 4) 
                       pygame.draw.line(screen, (0,g,0), (width, 0), (width, height), 4)
                        
                       pygame.display.flip()
                       
                       dir = -1
                         
            if dir == 1:    
                if y != 8:
                    y += 1
                else:
                    y = 0
                    if x != 9:
                        x += 1
            else: 
                if list[x][y].number == "9":
                    list[x][y].number = ""
                    screen.fill((0,0,0))
                    grid()
                    pygame.draw.line(screen, (0,g,0), (0, height), (width, height), 4) 
                    pygame.draw.line(screen, (0,g,0), (width, 0), (width, height), 4)
                    
                    pygame.display.flip()
                if y != 0:
                    y -= 1
                else:
                    y = 8
                    if x != 0:
                        x -= 1   
        else:
                break

def endGame():
    for x in range(9):
        for y in range(9):
            if list[x][y].number == "" or list[x][y].colorText == (r, 0,0):
                return False
    return True

def init():
    for i in range(9):
        l = []
        for j in range(9):
            b = Block(i, j)
            l.append(b)
        list.append(l)

def test(i, j):
    for index in range(9):
        if index != j:
            if list[i][index].number == list[i][j].number:
                return False
        if index != i:
            if list[index][j].number == list[i][j].number:
                return False
    for x in range(3):
        for y in range(3):
            if x+(i//3)*3 != i and y+(j//3)*3 != j:
                if list[x+(i//3)*3][y+(j//3)*3].number == list[i][j].number:
                    return False
    return True
    
def grid():
    for i in range(9):
        for j in range(9):
            list[i][j].show()
            if list[i][j].lock == False and start:
                if test(i, j):
                    list[i][j].colorText = (0,g,0)
                else:
                    list[i][j].colorText = (r,0,0)
            text = myfont.render(list[i][j].number,False, list[i][j].colorText)
            screen.blit(text,(side*i+side//3, side*j+side//6))
    pygame.draw.line(screen, (0,255,0), (0, height), (width, height), 2)
    pygame.draw.line(screen, (0,255,0), (width, 0), (width, height), 2) 
    

class Block:
    def __init__(self, i, j):
        self.x = i
        self.y = j
        self.rect = pygame.Rect(side*i, side*j, side, side)
        self.color = (0,0,b)
        self.colorText = (255,255,255)
        self.number = ""
        self.lock = False
    def show(self):
        pygame.draw.rect(screen, self.color, self.rect, 1)
        if self.y % 3 == 0:
           pygame.draw.line(screen, (0,g,0), (0, side*self.y), (width, side*self.y), 2) 
        if self.x % 3 == 0:
           pygame.draw.line(screen, (0,g,0), (side*self.x, 0), (side*self.x, height), 2)     

if __name__ == "__main__":
    init()
    menu()
    pygame.mixer.init()
    while not endGame() and not pos == 3:
        screen.fill((0,0,0))
        grid()
        pygame.draw.line(screen, (0,g,0), (0, height), (width, height), 4) 
        pygame.draw.line(screen, (0,g,0), (width, 0), (width, height), 4)
        for event in pygame.event.get():
            if event.type == QUIT:
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse = pygame.mouse.get_pos()
                x = mouse[0]//side
                y = mouse[1]//side
            if case == 3 and not stop:
                generate(5)
            if event.type == pygame.KEYDOWN:
                if chr(event.key) in "1234567890" and list[x][y].lock == False:
                    if chr(event.key) == '0':
                        list[x][y].number = ""
                        grid()
                    else:
                        list[x][y].number = chr(event.key)
                        grid()
                        if [x,y] not in lock_list:
                            lock_list.append([x, y])
                elif start == False and (event.key == K_RETURN or case == 3):
                    for i in range(9):
                        for j in range(9):
                            if list[i][j].number == "":
                                break
                        else:
                            continue
                        break
                    start = True
                    for item in lock_list:
                        list[item[0]][item[1]].lock = True
                    if case == 2:
                        backtraking(i, j)
                    sleep(2)
                elif event.key == K_ESCAPE:
                    init()
                    exitMenu = False
                    pos = 1
                    menu()
                 
        pygame.display.flip()
    sleep(0.5)
    pygame.quit()
    
    
    
    
    