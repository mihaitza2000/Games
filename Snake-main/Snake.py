import pygame, random, glob, os, time
from sys import exit
from pygame import *
from time import sleep
from win32api import GetSystemMetrics

pygame.font.init()
length, width, height, running, levelBar, pause = 0, GetSystemMetrics(0), GetSystemMetrics(1), True, 7, True
block = 30
screen = pygame.display.set_mode([width,height])
myfont = pygame.font.SysFont('Comic Sans MS', block)

scoreValue = 0
scoreString = 'Score: ' + str(scoreValue)
color = 0

userLabel = "Username:"
username = ""
passwordLabel = "Password:"
password = ""
step, count = 1, 0
levelColor = (0,0,255)
oldLevelBar = levelBar
oldSong = ""
startGame = False

user = myfont.render(userLabel + " " + username, False, (0, 0, 0))
passW = myfont.render(passwordLabel + " " + password, False, (0, 0, 0))
playList = myfont.render("Play list", False, (0, 0, 0))


title = myfont.render('Snake', False, (color, color, color))
score = myfont.render(scoreString, False, (color, color, color))

select, nrSongs, options = 1, 0, 4
answer, start, resume, stop = False, True, False, False
index = 0
currentSong, stars = "", ""
typeName, duplicate, skipTest, change, change2 = True, False, False, True, True


musicBackground = pygame.image.load("./images/music.jpg")
musicBackground = pygame.transform.scale(musicBackground, (width, height))

userBackground = pygame.image.load("./images/user.jpg")
userBackground = pygame.transform.scale(userBackground, (width, height))

menuBackground = pygame.image.load("./images/menu.png")
menuBackground = pygame.transform.scale(menuBackground, (width, height))

fireBackground = pygame.image.load("./images/fire.jpg")
fireBackground = pygame.transform.scale(fireBackground, (width, height))

levelBackground = pygame.image.load("./images/level.png")
levelBackground = pygame.transform.scale(levelBackground, (width, height))

headBackground = pygame.image.load("./images/soldier.png")
headBackground = pygame.transform.scale(headBackground, (2*block, 2*block))

bloodBackground = pygame.image.load("./images/blood.png")
bloodBackground = pygame.transform.scale(bloodBackground, (10*block, 10*block))

tailBackground = pygame.image.load("./images/tail.png")
tailBackground = pygame.transform.scale(tailBackground, (2*block, 2*block))

skipBackground = pygame.image.load("./images/skip.png")
skipBackground = pygame.transform.scale(skipBackground, (6*block, 2*block))

skipBackground2 = pygame.image.load("./images/skip2.png")
skipBackground2 = pygame.transform.scale(skipBackground2, (6*block+4, 2*block+4))

gameBackground = pygame.image.load("./images/game.png")
gameBackground = pygame.transform.scale(gameBackground, (width, height-block))

portalBackground = pygame.image.load("./images/portal.jpg")
portalBackground = pygame.transform.scale(portalBackground, (block, block))

wallBackground = pygame.image.load("./images/wall.png")
wallBackground = pygame.transform.scale(wallBackground, (width, block))

redDiamond = pygame.image.load("./images/redDiamond.png")
redDiamond = pygame.transform.scale(redDiamond, (2*block, 2*block))

greenDiamond = pygame.image.load("./images/greenDiamond.png")
greenDiamond = pygame.transform.scale(greenDiamond, (block, block))

logo = pygame.image.load("./images/logo.jpg")
logo = pygame.transform.scale(logo, (6*block, 3*block))
   
clock = pygame.time.Clock() 
         
def userFunction(enterSound):
    global username, user, typeName, password, step, passW, stars, duplicate, count, skipTest
    mouse = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == QUIT:
            quit()
        if not skipTest:
            if event.type == KEYDOWN:
                pygame.mixer.Channel(4).play(enterSound)
                if event.key == K_BACKSPACE:
                    if username != "" and step == 1:
                        username = username[:-1]
                        user = myfont.render(userLabel + " " + username, False, (0, 0, 0))
                    elif password != "" and step == 2:
                        password = password[:-1]
                        stars = stars[:-1]
                        passW = myfont.render(passwordLabel + " " + stars, False, (0, 0, 0))
                elif event.key != K_RETURN:
                    if step == 1 and (len(username) < 12):
                        username = username + str(event.unicode)
                        user = myfont.render(userLabel + " " + username, False, (0, 0, 0))
                    elif step == 2 and (len(password) < 12):
                        password = password + str(event.unicode)
                        stars = stars + "*"
                        passW = myfont.render(passwordLabel + " " + stars, False, (0, 0, 0))   
                elif event.key == K_RETURN or event.key == '/t':
                    if step == 1 and len(username) > 0:
                        list = []
                        with open("Scors.txt","r") as f:
                            count = 0
                            for line in f:
                                if line != "\n":
                                    count += 1
                                list.append(line)
                        if len(list) != 0:
                            duplicate = False
                            for word in list:
                                count = list.index(word)
                                word = word[:word.find(" -")]
                                if username == word:
                                    duplicate = True
                                    break
                        step = 2
                    elif step == 2 and len(password) > 0:
                        if not duplicate:
                            with open("Passwords.txt", "a") as f:
                                f.write(password + "\n")
                            typeName = False
                        else:
                            list = []
                            with open("Passwords.txt","r") as f:
                                for line in f:
                                    if line != "\n":
                                        line = line[:-1]
                                        list.append(line)
                            if list[count] == password:
                                typeName = False
                            else:
                                step = 1
                                username = ""
                                user = myfont.render(userLabel + " " + username, False, (0, 0, 0))
                                password = ""
                                stars = ""
                                passW = myfont.render(passwordLabel + " " + stars, False, (0, 0, 0))
        if event.type == pygame.MOUSEBUTTONDOWN:
            if 3*width/8-12 <= mouse[0] <= 3*width/8-12 + 6*block and height/8+3*block-2 <= mouse[1] <= height/8+3*block-2 + 2*block:
                skipTest = True
    screen.blit(userBackground, (0, 0))                
    screen.blit(user, (3*width/8, height/8))
    screen.blit(passW, (3*width/8, height/8+block))
    screen.blit(skipBackground2,(3*width/8-12, height/8+3*block-2))
    screen.blit(skipBackground,(3*width/8-10, height/8+3*block))
    screen.blit(logo,(width - 6.5*block,0.5*block))
    
    
def initMusic(): 
    global nrSongs, nameSongs
    nameSongs = os.listdir("./songs")
    for name in nameSongs:
        extension = os.path.splitext(name)[1]
        if extension != ".mp3":
            nameSongs.remove(name)
            nrSongs -= 1
    nrSongs = len(glob.glob1("./songs","*.mp3"))

def changeMusic():
    global answer, color, index, nrSongs, nameSongs, currentSong, background_music, change2, oldSong
    color = 255
    screen.blit(musicBackground, (0,0))
    playList = myfont.render("Play list", False, (0, 0, 255))
    screen.blit(playList, (3*width//4-2*block, 2*block))
    if change2:
        oldSong = index
        change2 = False
    for i in range(nrSongs):
        tempName = nameSongs[i]
        if len(nameSongs[i]) > 37:
            tempName = tempName[:37] + "..."
        if i == index:
            screen.blit(myfont.render(str(i+1)+ ". " + tempName, False, (255, 0, 0)), (width//2 - 2*block, 4*block+block*i))
        else:
            screen.blit(myfont.render(str(i+1)+ ". " + tempName, False, (0, 255, 0)), (width//2 - 2*block, 4*block+block*i))
    for event in pygame.event.get():
        if event.type == QUIT:
            quit()
        elif event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                answer = False
                index = oldSong
            if event.key == pygame.K_UP:
                if index == 0:
                    index = nrSongs-1
                else:
                    index -= 1
            if event.key == pygame.K_DOWN:
                if index == nrSongs-1:
                    index = 0
                else:
                    index += 1
            if event.key == pygame.K_RETURN:
                answer = False
                currentSong = nameSongs[index]
                background_music = pygame.mixer.Sound("./songs/" + nameSongs[index])
                pygame.mixer.Channel(1).play(background_music, loops = -1)
                pygame.mixer.Channel(1).pause()
                change2 = True
            
def level():
    global levelBar, answer, levelColor, change, oldLevelBar, color
    color = 0
    title = myfont.render('Snake', False, (color, color, color))
    score = myfont.render(scoreString, False, (color, color, color))
    screen.blit(title, (width/2-block, -block/4))
    screen.blit(score, (5*block, -block/4))
    if change:
        oldLevelBar = levelBar
        change = False
    if levelBar <= 5:
        levelColor = (0,0,255)
    elif levelBar <= 10:
        levelColor = (0,255,0)
    else:
        levelColor = (255,0,0)
    screen.blit(levelBackground, (0,0))
    draw.rect(screen, levelColor, ((width-15*block)//2+2*block, 3*height//4+2*block, (levelBar-1)*block, 2*block))
    for i in range(levelBar):
        if i == 0:
            draw.circle(screen, levelColor,((width-15*block)//2+block*(i+1)+block, 3*height//4+3*block), block)
        elif i == levelBar-1:
            draw.circle(screen, levelColor, ((width-15*block)//2+block*(i+1)+block,3*height//4+3*block), block)
        else:
            draw.rect(screen, levelColor, ((width-15*block)//2+block*(i+1), 3*height//4+2*block, 2*block, 2*block))
    for event in pygame.event.get():
        if event.type == QUIT:
            quit()
        if event.type == KEYDOWN:
            if event.key == pygame.K_RIGHT and levelBar < 15:
                levelBar += 1
            elif event.key == pygame.K_LEFT and levelBar > 1:
                levelBar -= 1
            elif event.key == K_ESCAPE:
                levelBar = oldLevelBar
                answer = False
                color = 255
            elif event.key == K_RETURN:
                answer = False
                color = 255
                change = True

def game():
    screen.blit(wallBackground,(0,0))
    screen.blit(gameBackground,(0,block))
    for i in range(height//block):
        if i > 0: 
            screen.blit(portalBackground,(0, i*block))
            screen.blit(portalBackground,(width-block, i*block))
    for i in range(width//block): 
        screen.blit(portalBackground,(i*block, block))
        screen.blit(portalBackground,(i*block, height-block))

def menu():
    global select, answer, options, resume
    screen.blit(fireBackground, (0, 0))
    screen.blit(menuBackground, (0, 0))
    if start == False:
        if select == 1:
            startGame  = myfont.render("Start", False, (255,0,0))
            resumeGame = myfont.render("Resume", False, (0,255,0))
            levelGame  = myfont.render("Level", False, (0,255,0))
            musicGame  = myfont.render("Choose music", False, (0,255,0))
            exitGame   = myfont.render("Exit", False, (0,255,0))
        elif select == 2:
            startGame  = myfont.render("Start", False, (0,255,0))
            resumeGame = myfont.render("Resume", False, (255,0,0))
            levelGame  = myfont.render("Level", False, (0,255,0))
            musicGame  = myfont.render("Choose music", False, (0,255,0))
            musicGame  = myfont.render("Choose music", False, (0,255,0))
            exitGame   = myfont.render("Exit", False, (0,255,0))
        elif select == 3:
            startGame  = myfont.render("Start", False, (0,255,0))
            resumeGame = myfont.render("Resume", False, (0,255,0))
            levelGame  = myfont.render("Level", False, (255,0,0))
            musicGame  = myfont.render("Choose music", False, (0,255,0))
            exitGame   = myfont.render("Exit", False, (0,255,0))
        elif select == 4:
            startGame  = myfont.render("Start", False, (0,255,0))
            resumeGame = myfont.render("Resume", False, (0,255,0))
            levelGame  = myfont.render("Level", False, (0,255,0))
            musicGame  = myfont.render("Choose music", False, (255,0,0))
            exitGame   = myfont.render("Exit", False, (0,255,0))
        else:
            startGame  = myfont.render("Start", False, (0,255,0))
            resumeGame = myfont.render("Resume", False, (0,255,0))
            levelGame  = myfont.render("Level", False, (0,255,0))
            musicGame  = myfont.render("Choose music", False, (0,255,0))
            exitGame   = myfont.render("Exit", False, (255,0,0))
        screen.blit(startGame, (5, 5))
        screen.blit(resumeGame, (5, 5 + block))
        screen.blit(levelGame, (5, 5 + 2*block))
        screen.blit(musicGame, (5, 5 + 3*block))
        screen.blit(exitGame, (5, 5 + 4*block))
    else:
        if select == 1:
            startGame  = myfont.render("Start", False, (255,0,0))
            levelGame  = myfont.render("Level", False, (0,255,0))
            musicGame  = myfont.render("Choose music", False, (0,255,0))
            exitGame   = myfont.render("Exit", False, (0,255,0))
        elif select == 2:
            startGame  = myfont.render("Start", False, (0,255,0))
            levelGame  = myfont.render("Level", False, (255,0,0))
            musicGame  = myfont.render("Choose music", False, (0,255,0))
            exitGame   = myfont.render("Exit", False, (0,255,0))
        elif select == 3:
            startGame  = myfont.render("Start", False, (0,255,0))
            levelGame  = myfont.render("Level", False, (0,255,0))
            musicGame  = myfont.render("Choose music", False, (255,0,0))
            exitGame   = myfont.render("Exit", False, (0,255,0))
        else:
            startGame  = myfont.render("Start", False, (0,255,0))
            levelGame  = myfont.render("Level", False, (0,255,0))
            musicGame  = myfont.render("Choose music", False, (0,255,0))
            exitGame   = myfont.render("Exit", False, (255,0,0))
        screen.blit(startGame, (5, 5))
        screen.blit(levelGame, (5, 5 + block))
        screen.blit(musicGame, (5, 5 + 2*block))
        screen.blit(exitGame, (5, 5 + 3*block))
    for event in pygame.event.get():
        if event.type == QUIT:
            quit()
        elif event.type == KEYDOWN:
            if event.key == pygame.K_RETURN:
                answer = True
                pygame.mixer.pause()
                if select == 2 and start == False:
                    resume = True
            elif event.key == K_DOWN:
                if select == options:
                    select = 1
                else:
                    select += 1
            elif event.key == K_UP:
                if select == 1:
                    select = options
                else:
                    select -= 1
class Snake():
    def __init__(self, image):
        self.xHead, self.yHead, self.oldXHead, self.oldYHead, self.dirXHead, self.dirYHead, self.image = 10*block, 10*block, 10*block, 10*block, 1, 0, image
    def move(self, color):
        if pause == False:
            self.oldXHead, self.oldYHead = self.xHead, self.yHead
            self.xHead += self.dirXHead*block
            self.yHead += self.dirYHead*block
            if self.xHead > width-block:
                portalSound.play()
                self.xHead = block
            elif self.xHead < block:
                portalSound.play()
                self.xHead = width-block
            elif self.yHead > height-block:
                portalSound.play()
                self.yHead = 2*block
            elif self.yHead < 2*block:
                portalSound.play()
                self.yHead = height-block
        #pygame.draw.rect(screen, (255, 0 , 0), (self.xHead, self.yHead, block, block))
        if self.dirXHead != -1:
            screen.blit(self.image, (self.xHead-block/2,self.yHead-block/2))
        elif self.dirXHead != 0:
            screen.blit(pygame.transform.flip(self.image, True, False), (self.xHead-block/2,self.yHead-block/2))
    def changeDir(self, dirX, dirY):
        self.dirXHead = int(dirX)
        self.dirYHead = int(dirY)
            
   
class Food():
    def __init__(self):
        self.foodSet = 1
        self.xFood, self.yFood = random.randint(2, (width//block-2))*block, random.randint(2, (height//block-2))*block
        self.start_time = 0
    def show(self): 
        global foodSet
        if self.foodSet == 5:
            screen.blit(redDiamond,(self.xFood-block/2,self.yFood-block/2))
        else:
            screen.blit(greenDiamond,(self.xFood,self.yFood))
            #pygame.draw.rect(screen, (0, 255 , 0), (self.xFood, self.yFood, block, block))
    def get(self):    
        return self.foodSet
    def check(self, s): 
        if (abs(s.xHead - self.xFood) <= 3*block/4 and abs(s.yHead - self.yFood) <= 3*block/4 and self.foodSet == 5) or (abs(s.xHead - self.xFood) == 0 and abs(s.yHead - self.yFood) == 0 and self.foodSet != 5):
            if self.foodSet != 5:
                if self.foodSet == 4:
                    if self.start_time != 0:
                        dt = clock.tick()
                        self.start_time += dt
                        print(self.start_time)
                    if self.start_time > 3:
                        self.change()
                        self.start_time = 0;
                self.foodSet += 1
            else:
                self.foodSet = 1
            return True
        else:
            return False
    def change(self):
        self.xFood, self.yFood = random.randint(2, (width//block-2))*block, random.randint(2, (height//block-2))*block
        
class Tail():
    def __init__(self):
        self.tail = []
    def add(self, snake):
        s = Snake(tailBackground)
        self.tail.append(s)
        if len(self.tail) == 0:
            s.xHead, s.yHead = snake.xHead - block*snake.dirXHead, snake.yHead - block*snake.dirYHead
            s.changeDir(snake.dirXHead, snake.dirYHead)
        else:
            s.xHead, s.yHead = self.tail[-1].xHead - block*self.tail[-1].dirXHead, self.tail[-1].yHead - block*self.tail[-1].dirYHead
            s.changeDir(self.tail[-1].dirXHead, self.tail[-1].dirYHead)
    def move(self):
        if len(self.tail) > 0:
            if pause == False:
                self.tail[0].oldXHead, self.tail[0].oldYHead, self.tail[0].xHead, self.tail[0].yHead = self.tail[0].xHead, self.tail[0].yHead, snake.oldXHead, snake.oldYHead
            #pygame.draw.rect(screen, (255, 0 , 255), (self.tail[0].xHead, self.tail[0].yHead, block, block)
            if self.tail[0].dirXHead != -1:
                screen.blit(self.tail[0].image, (self.tail[0].xHead-block/2, self.tail[0].yHead-block/2))
            else:
                screen.blit(pygame.transform.flip(self.tail[0].image, True, False), (self.tail[0].xHead-block/2, self.tail[0].yHead-block/2))
            for i in range(1, len(self.tail)):
                if pause == False:
                    self.tail[i].oldXHead, self.tail[i].oldYHead, self.tail[i].xHead, self.tail[i].yHead = self.tail[i].xHead, self.tail[i].yHead, self.tail[i-1].oldXHead, self.tail[i-1].oldYHead
                screen.blit(self.tail[i].image, (self.tail[i].xHead-block/2, self.tail[i].yHead-block/2))
                #pygame.draw.rect(screen, (255, 0 , 255), (self.tail[i].xHead, self.tail[i].yHead, block, block))           
    def check(self, snake, count):
        for i in range(2, len(self.tail)):
            if self.tail[i].xHead == snake.xHead and self.tail[i].yHead == snake.yHead:
                return True
    
if __name__ == "__main__":
    nameSongs = []
    pygame.init()
    initMusic()
    pygame.mixer.init()
    fpsClock = time.Clock()
    snake, food, tail, count = Snake(headBackground), Food(), Tail(), 0
    pauseGame                = myfont.render("Pause", False, (255,255,255))
    fireSound = pygame.mixer.Sound("./sounds/fire.mp3")
    portalSound = pygame.mixer.Sound("./sounds/portal.mp3")
    eatSound = pygame.mixer.Sound("./sounds/eat.mp3")
    clickSound = pygame.mixer.Sound("./sounds/click.wav")
    enterSound = pygame.mixer.Sound("./sounds/enter.wav")
    if len(nameSongs) > 0:
        currentSong = nameSongs[index]
        background_music = pygame.mixer.Sound("./songs/" + nameSongs[index])
    pygame.mixer.Channel(0).play(fireSound)
    pygame.mixer.Channel(1).play(background_music, loops = -1)
    while typeName:
        if skipTest:
            pygame.mixer.Channel(3).play(clickSound)
            sleep(1)
            break
        display.flip()
        userFunction(enterSound)
        pygame.mixer.Channel(2).pause()
        pygame.mixer.Channel(1).pause()
        pygame.mixer.Channel(0).pause()
    while running:
        pygame.display.flip()
        if answer == False:
            pygame.mixer.Channel(0).unpause()
            pygame.mixer.Channel(1).pause()
            stop = False
            menu()
            startGame = True
        if answer == True:
            pygame.mixer.Channel(0).pause()
            if startGame:
                startGame = False
            if select == 1 and stop == False:
                pygame.init()
                fpsClock = time.Clock()
                snake, food, tail, count = Snake(headBackground), Food(), Tail(), 0
                stop = True
            if pause == True:
                pygame.mixer.Channel(1).pause()
                pauseGame   = myfont.render("Pause mode on", False, (0,0, 255))
            else:
                pygame.mixer.Channel(1).unpause()
                pauseGame   = myfont.render("", False, (255,0,0))
            if (select == 5 and start == False) or (select == 4 and start == True):
                running = False
            elif (select == 3 and start == False) or (select == 2 and start == True):
                level()
            elif (select == 4 and start == False) or (select == 3 and start == True):
                pygame.mixer.pause()
                changeMusic()
            else:
                game()
                food.show()
                for event in pygame.event.get():
                    if event.type == QUIT:
                        quit()
                        running = False
                    if event.type == KEYDOWN:
                        if event.key == K_ESCAPE:
                            start = False
                            options = 5
                            answer = False
                            resume = True
                            pause = True
                        if pause == False or event.key == K_LEFT or event.key == K_a or event.key == K_RIGHT or event.key == K_d or event.key == K_UP or event.key == K_w or event.key == K_DOWN or event.key == K_s:
                            if event.key == K_RIGHT or event.key == K_d:
                                if length == 0: 
                                    snake.changeDir(1,0)
                                elif snake.dirXHead != -1:
                                    snake.changeDir(1,0)
                            elif event.key == K_LEFT or event.key == K_a:
                                if length == 0: 
                                    snake.changeDir(-1,0)
                                elif snake.dirXHead != 1:
                                    snake.changeDir(-1,0)
                            elif event.key == K_DOWN or event.key == K_s:
                                if length == 0: 
                                    snake.changeDir(0,1)
                                elif snake.dirYHead != -1:
                                    snake.changeDir(0,1)
                            elif event.key == K_UP or event.key == K_w:
                                if length == 0: 
                                    snake.changeDir(0,-1)
                                elif snake.dirYHead != 1:
                                    snake.changeDir(0,-1)
                            if pause == True:
                                pause = False
                        if event.key == pygame.K_p:
                            if pause == True:
                                pause = False
                            else:
                                pause = True
                if food.check(snake):
                    pygame.mixer.Channel(2).play(eatSound)
                    length += 1
                    tail.add(snake)
                    food.change()
                    scoreString = 'Score: ' + str(scoreValue)
                    if food.get() != 5:
                        scoreValue += 10
                    else:
                        scoreValue += 50
                if tail.check(snake, count):
                    sleep(2)
                    exit()
                snake.move(255)
                tail.move()
                fpsClock.tick(levelBar+3)
                screen.blit(pauseGame, (200, -block/4))
            score = myfont.render(scoreString, False, (0, 0, 255))
            title = myfont.render('Snake', False, (0, 0, 255))
            screen.blit(title, (width-5*block, -block/4))
            screen.blit(score, (block, -block/4))
    if not skipTest:
        with open("Scors.txt", "a") as f:
            f.write(username + " - " + str(scoreValue) + " points" + "\n")
    pygame.quit()
    