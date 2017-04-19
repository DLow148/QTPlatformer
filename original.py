#Derek Low <dl9525@bard.edu>
#5/11/15
#cmsc143
#Assignment 5: A Commencement Program
#Collaboration Statement: I worked alone on this assignment with help from the internet and a highschool friend

from Graphics import *
from Myro import *
import random
import time

#finish monster
#Arrow
#sword swing?
#Dying
#traps?
#boss?
#level structure
#powerups?

class physicsCharacter:

    JUMPING = 2
    NOT_JUMPING = 3
    ON_GROUND = True
    GRAVITY = 300
    
    def __init__(self, win):
        self.win = win
        self.state = character.LIVE

        self.velocityX = 0
        self.velocityY = 0
        self.onGround = True
        self.jump = character.NOT_JUMPING

    def update(self, step):
        self.appearance.x += self.velocityX * step
        self.appearance.y += self.velocityY * step
        self.velocityY += character.GRAVITY * step
        
        if self.velocityX > 0:
            self.velocityX -= 8
            
        if self.velocityX < 0:
            self.velocityX += 8

    def setOnGround(self, platform):
        self.velocityY = 0
        self.onGround = True
        self.jump = character.NOT_JUMPING
        self.appearance.y = platform.appearance.y - self.appearance.getHeight()/2 - 5
    
    def setOffLeft(self,platform):
        self.velocityX = 0
        self.onGround = False
        self.jump = character.JUMPING
        self.appearance.x = platform.appearance.x - platform.width/2 - self.appearance.getWidth()/2

    def setOffRight(self, platform):
        self.velocityX = 0
        self.onGround = False
        self.jump = character.JUMPING
        self.appearance.x = platform.appearance.x + platform.width/2 + self.appearance.getWidth()/2

    def setUnderGround(self,platform):
        self.velocityY = 0
        self.onGround = False
        self.jump = character.JUMPING
        self.appearance.y = platform.appearance.y + 1

    def collidedWith(self, other):
        return

def isCollision (self, other):
    myx1 = self.x - self.width/2 #left
    myy1 = self.y - self.height/2 #top
    myx2 = self.x + self.width/2 #right
    myy2 = self.y + self.height/2    #bottom

    otherx1 = other.appearance.x - other.appearance.getWidth()/2 #left
    othery1 = other.appearance.y - other.appearance.getHeight()/2 #top
    otherx2 = other.appearance.x + other.appearance.getWidth()/2 #right
    othery2 = other.appearance.y + other.appearance.getHeight()/2 #bottom 
    return  myy1 < othery2 and myy2 > othery1 and myx1 < otherx2 and myx2 > otherx1

def checkCollision (self,other):
    myx1 = self.appearance.x - self.appearance.width/2 #left
    myy1 = self.appearance.y - self.appearance.height/2 #top
    myx2 = self.appearance.x + self.appearance.width/2 #right
    myy2 = self.appearance.y + self.appearance.height/2    #bottom

    otherx1 = other.appearance.x - other.appearance.getWidth()/2 #left
    othery1 = other.appearance.y - other.appearance.getHeight()/2 #top
    otherx2 = other.appearance.x + other.appearance.getWidth()/2 #right
    othery2 = other.appearance.y + other.appearance.getHeight()/2 #bottom

    return  myy1 < othery2 and myy2 > othery1 and myx1 < otherx2 and myx2 > otherx1
class collisionDetection(object):
    def __init__(self, platforms):
        self.platforms = platforms
        
    def detectCollisions(self):
        # do collision detection here
        for Platform in self.platforms:
            for Entity in Entities:
                if platforms.checkCollision(Platform, Entity):
                    if Platform.correctCollision(Entity) ==1 :
                        Entity.setOnGround(Platform)   
                    if Platform.correctCollision(Entity) ==2:
                        Entity.setUnderGround(Entity)                                 
                    if Platform.correctCollision(Entity) ==3:
                        if Entity.appearance.y > Platform.appearance.y:
                            Entity.setOffLeft(Platform)
                        else:
                            Entity.setOnGround(Platform)
                    if Platform.correctCollision(Entity) ==4 :
                        if Entity.appearance.y > Platform.appearance.y:
                            Entity.setOffRight(Platform)
                        else:
                            Entity.setOnGround(Platform)
        for idx, entityA in enumerate(Entities):
            for idx2,entityB in enumerate(Entities, start = idx+1):
                if checkCollision(entityA, entityB):
                    entityA.collidedWith(entityB)
                    entityB.collidedWith(entityA)
                    
    def updatePhysics(self, step):
        for Entity in Entities:
            Entity.update(step)
        
class monster(physicsCharacter):
    GRAVITY = 300
    def __init__(self, win):
        physicsCharacter.__init__(self, win)
        self.startTime = currentTime()
        self.win = win
        #self.state = character.LIVE
        
        self.appearance = makePicture('enemy.gif')
        self.appearance.x = random.choice(Platforms).appearance.x
        self.appearance.y = random.choice(Platforms).appearance.y - 30
        self.appearance.draw(win)
        self.velocityX = -70
   
    def update(self,step):
        self.appearance.x += self.velocityX * step
        self.appearance.y += self.velocityY * step
        self.velocityY += character.GRAVITY * step

    def setOnGround(self, platform):
        self.velocityY = 0
        self.onGround = True
        self.jump = character.NOT_JUMPING
        self.appearance.y = platform.appearance.y - self.appearance.getHeight()/2 - 5
        if self.appearance.x < platform.appearance.x - platform.width/2 + 15:
            self.velocityX = 70
        if self.appearance.x > platform.appearance.x + platform.width/2 - 15:      
            self.velocityX = -70

            
            
            
class platforms(object):
    MIN_SIZE = 50
    MAX_SIZE = 1000
    def __init__(self, x , y, width, win):
        self.win = win
        self.width = width 
        self.height = 10
        self.appearance = Rectangle(Point(x - self.width/2, y - self.height/2),
                                    Point(x + self.width/2, y + self.height/2))
        # The left rectangle's top left corner
        lefttopLeftX = self.appearance.x - self.width/2
        lefttopLeftY = self.appearance.y - self.height/2
        
        # The left rectangle's bottom right corner
        leftbottomrightx = self.appearance.x - self.width/2 + 4
        leftbottomrighty = self.appearance.y +self.height/2
        
        # The right rectangle's top left corner
        righttopleftx = self.appearance.x + self.width/2 - 4
        righttoplefty = self.appearance.y - self.height/2
        
        # The right rectangle's bottom right corner
        rightbottomrightx = self.appearance.x + self.width/2
        rightbottomrighty = self.appearance.y + self.height/2

        # The top rectangle's top left corner
        toptopleftx = self.appearance.x - self.width/2 + 4
        toptoplefty = self.appearance.y - self.height/2
        
        # The top rectangle's bottom right corner
        topbottomrightx = self.appearance.x + self.width/2 - 4
        topbottomrighty = self.appearance.y
        
        # The bottom rectangle's top left corner
        bottomtopleftx = self.appearance.x -self.width/2 + 4
        bottomtoplefty = self.appearance.y
        
        # The bottom rectangle's bottom right corner
        bottombottomrightx= self.appearance.x + self.width/2 - 4
        bottombottomrighty = self.appearance.y + self.height/2

        # topRightX =
        self.leftRect = Rectangle( Point(lefttopLeftX, lefttopLeftY), 
                                  Point (leftbottomrightx, leftbottomrighty))
        
        self.rightRect = Rectangle( Point(righttopleftx, righttoplefty) ,
                                  Point (rightbottomrightx,rightbottomrighty ))
        self.bottom = Rectangle( Point(bottomtopleftx,bottomtoplefty) ,
                                  Point (bottombottomrightx,bottombottomrighty))
        self.top =  Rectangle( Point(toptopleftx, toptoplefty) ,
                                  Point (topbottomrightx, topbottomrighty))
        
        
        self.appearance.draw(win)
        self.leftRect.draw(win)
        self.rightRect.draw(win)
        self.bottom.draw(win)
        self.top.draw(win)
        #self.appearance.setFill(Color(random.choice(["blue", "orange", "red"])))

    def checkCollision (self,other):
      myx1 = self.appearance.x - self.width/2 #left
      myy1 = self.appearance.y - self.height/2 #top
      myx2 = self.appearance.x + self.width/2 #right
      myy2 = self.appearance.y + self.height/2    #bottom

      otherx1 = other.appearance.x - other.appearance.getWidth()/2 #left
      othery1 = other.appearance.y - other.appearance.getHeight()/2 #top
      otherx2 = other.appearance.x + other.appearance.getWidth()/2 #right
      othery2 = other.appearance.y + other.appearance.getHeight()/2 #bottom

      return  myy1 < othery2 and myy2 > othery1 and myx1 < otherx2 and myx2 > otherx1

  
    def correctCollision (self, other):
        if isCollision(self.top, other):
            return 1
        if isCollision(self.bottom,other):
            return 2
        if isCollision(self.leftRect, other):
            return 3
        if isCollision(self.rightRect, other):
            return 4
            
        return False   
class character(physicsCharacter):

    DEAD = 0
    LIVE = 1
    JUMPING = 2
    NOT_JUMPING = 3
    ON_GROUND = True
    GRAVITY = 300
    WIN = 6
    
    def __init__(self, win):
        physicsCharacter.__init__(self, win)

        self.startTime = currentTime()
        self.win = win
        self.state = character.LIVE
        
        self.appearance = makePicture('Bob.png')
        self.appearance.y = getHeight(win) - 50
        self.appearance.draw(win)

        self.hp = 100
        
    def collidedWith(self, other):
        if other in Monsters:
            self.hp = self.hp - 25
            if self.velocityX > 0:
                self.velocityX = -500
            if self.velocityX < 0:
                self.velocityX = 500
            self.velocityY = -100
            self.onGround = False
            self.jump = character.JUMPING
        if other in Treasure:
            self.state = character.WIN        
    def update(self, step):
        physicsCharacter.update(self,step)
            
        if self.hp <= 0:
            self.state = character.DEAD
#class ladder(object):




class treasureChest(physicsCharacter):
    def __init__(self, win):
        physicsCharacter.__init__(self,win)
        self.appearance = makePicture('chest.png')
        self.appearance.x = 50
        self.appearance.y = 50
        self.appearance.draw(win)

Platforms = []
Monsters = []
Entities = []
Treasure = []
def mainLevel1():
    win = Window('Explore!', 900,900)

    caves = makePicture("background.png")
    caves.draw(win)

    #win.mode = 'physics'
    Platforms.append(platforms(450, getHeight(win) - 10, getWidth(win),win))
    Platforms.append(platforms(250, 700, 100,win))
    Platforms.append(platforms(500, 650, 300,win))
    Platforms.append(platforms(850, 700, 100, win))
    Platforms.append(platforms(650, 700, 100,win))
    Platforms.append(platforms(800, 550, 200,win))
    Platforms.append(platforms(300,500,600,win))
    Platforms.append(platforms(450, 400, 200, win))
    Platforms.append(platforms(200, 325, 200, win))
    Platforms.append(platforms(700, 325, 200, win))
    Platforms.append(platforms(100, 250, 200, win))
    Platforms.append(platforms(800, 250, 200,win))
    Platforms.append(platforms(450, 200, 200, win))
    Platforms.append(platforms(200, 100, 400, win))
    
    
    Bob = character(win)
    Entities.append(Bob)
    treasureWin = Treasure.append(treasureChest(win))
    for i in range(10):
        Monsters.append(monster(win))
    Entities.extend(Monsters)
    Entities.extend(Treasure)
    CollisionDetection = collisionDetection(Platforms)
    
    frameRate = 0
    fps = 25
    time_delta = 1/fps
    while Bob.state == character.LIVE:

        t0 = time.clock()
        time.sleep(time_delta)
        t1 = time.clock()
        delta = t1 - t0
        
        # The Game Loop
        CollisionDetection.detectCollisions()
        CollisionDetection.updatePhysics(delta)
        
        if win.getKeyPressed('Left') == True:
            Bob.velocityX = -100
            
        if win.getKeyPressed('Right') == True:
            Bob.velocityX = 100
            
        if win.getKeyPressed('Up') == True:
            # only when bob isn't jumping does the up
            # button actually do anything
            
            if Bob.jump != character.JUMPING:
                Bob.velocityY = -250
                Bob.jump = character.JUMPING
                Bob.onGround = False
            
        if win.getKeyPressed('Down') == True:
            Bob.velocityY+= 50

        if win.getKeyPressed('x') == True:
            print("shoot")
        #print(1/(t1 - t0))
    if Bob.state == character.DEAD:
        caves.undraw()
        win.setBackground(Color("black"))
        loser = Text((300,100), "YOU LOSE :(")
        loser.setColor(Color("white"))
        loser.fontSize = 60
        loser.draw(win)
    if Bob.state == character.WIN:
        caves.undraw()
        win.setBackground(Color("gold"))
        winner = Text((300,100),"YOU WIN!!!" )
        winner.fontSize = 60
        winner.draw(win)
mainLevel1()