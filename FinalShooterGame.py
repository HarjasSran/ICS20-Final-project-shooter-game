#Harjas Sran
#June 2019 ICS2O
#Final Shooter game Project
#June 14, 2019

import pygame
import math
import shelve
pygame.init()


size = (1000,700)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Rando Atar.io")

surface = pygame.image.load("ball.png")
pygame.display.set_icon(surface)


done = False

#Fonts
font = pygame.font.SysFont('Calibri', 60, False, True)
font2 = pygame.font.SysFont('Calibri', 20, False, True)
font3 = pygame.font.SysFont('Calibri', 90, False, True)

#Music
pygame.mixer.music.load("atarimusic.ogg")
pygame.mixer.music.play(-1,0.0)

#Heart Image
heartImg = pygame.image.load("heart.png")
heartImg = pygame.transform.scale(heartImg, [25,25])

#Starting off display Booleans
rect1 = True
rect2 = True
rect3 = True
rect4 = True
rect5 = True

#Round has not been won yet
roundwon = False

#Sreen Layout
layout = 1

#Round Start
start_round = False

#Round Counter
round_ = 0

#Score Counter
score = 0

#Starting number of lives
lives = 3

#User has not lost lives yet
life_loss = False

#Ball speeds
ballspeedx = 2
ballspeedy = 2

#Ball Starting Positions
ballx = 500
bally = 650

#Rectangle formation
rects = 1

#Rectangle starting
rect1_x = 50
rect1_y = 100
rect2_x = 250
rect2_y = 100
rect3_x = 450
rect3_y = 100
rect4_x = 650
rect4_y = 100
rect5_x = 850
rect5_y = 100

#Rectable Couonter
rect_count = 1

#Colours
BLACK = [0,0,0]
WHITE = [255,255,255]
RED = [255,0,0]
BLUE = [0,0,255]

#Load up highscore file
highscore = shelve.open("highscore")
#Initially creates highscore file, then recalls it everytime the program is replayed
try:
    int_highscore = highscore["hs"]
except:
    highscore["hs"] = 0
    int_highscore = highscore["hs"]
while not done:

    #Welcome screen
    if layout == 1:
        #Starting of game with black screen and text to quide user
        screen.fill(BLACK)
        startText = font.render("Welcome to Rando Atar.io", True, WHITE)
        screen.blit(startText, [220,200])
        exitText = font2.render("Press \"q\" at any point to exit the game", True, WHITE)
        screen.blit(exitText, [0,650])
        spaceText = font.render("Press SPACE to start playing Atar.io", True, WHITE)
        screen.blit(spaceText, [150,400])
        lives = 3
        #Updates user input
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    done = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    layout = 2
    #2nd Layout, Start of game screen    
    if layout == 2:
        screen.fill(BLACK)
        
        #Start up game
        if start_round == False and life_loss != True:
            roundText = font.render("Press SPACE to begin round", True, WHITE)
            screen.blit(roundText, [150,300])
            highscoreText = font3.render("Highscore: " + str(int_highscore), True, WHITE)
            screen.blit(highscoreText, [200,350])
            
        #Score
        scoreText = font.render(str(score), True, WHITE)
        screen.blit(scoreText, [930,0])
        
        #Bouncer pad
        pos = pygame.mouse.get_pos()
        x = pos[0]
        if x < 800:
            pygame.draw.rect(screen, RED, [x,680,200,25])
        else:
            x -= 200
            pygame.draw.rect(screen, RED, [x,680,200,25])
        
        #Bouncy Ball
        if start_round == True:
            ballx += ballspeedx
            bally -= ballspeedy
        pygame.draw.circle(screen, WHITE, [int(ballx), int(bally)], 10)
        
        #Ball boucing off the walls (Not ground)
        if ballx >= 990:
            ballspeedx = -ballspeedx
        if ballx <= 10:
            ballspeedx = -ballspeedx
        if bally <= 10:
            ballspeedy = -ballspeedy
            
        #Rects and ball interaction
        dist_ball = ballx - x
        if dist_ball <=220 and dist_ball >= -20 and bally >= 670:
            ballspeedy = abs(ballspeedy)
            rects += 1
            
        #Max 5 rectangles per round
        if rects >= 6:
            rects = 1
            
        #Center of Bouncy pad
        pad_center = x + 100
        
        #Ball direction based of pad center
        if ballx <= pad_center and bally >= 670 and ballspeedx >= 1:
            ballspeedx = - ballspeedx
        if ballx >= pad_center and bally >= 670:
            ballspeedx = abs(ballspeedx)
				#If the ball does not hit the pad
        if bally >= 690:
            lives -= 1
            ballx = 500
            bally = 650
            ballspeedx = abs(ballspeedx)
            ballspeedy = -ballspeedy
            start_round = False
            life_loss = True 
            
        #Life loss
        if life_loss == True:
            lifeText = font.render("Click SPACE to continue with " + str(lives) + " lives left!", True, WHITE)
            screen.blit(lifeText, [20,350])
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        done = True 
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        start_round = True
                        life_loss = False
        #Once all lives are lost, death screen appers
        if lives <= 0:
            layout = 3
            
        #Random rectangle positions (Trapeziod shape)
        if rect_count == 1 or rect_count == 6:
            rect1_x = 100
            rect1_y = 100
			rect_count = random.randrange(2,6)
            
            rect2_x = 250
            rect2_y = 250
            
            rect3_x = 450
            rect3_y = 100
            
            rect4_x = 650
            rect4_y = 250
            
            rect5_x = 800
            rect5_y = 100
            
        if rect_count == 2:
            rect1_x = 100
            rect1_y = 150
            
            rect2_x = 400
            rect2_y = 200
            
            rect3_x = 450
            rect3_y = 100
            
            rect4_x = 650
            rect4_y = 100
            
            rect5_x = 800
            rect5_y = 300
            
        if rect_count == 3:
            rect1_x = 150
            rect1_y = 100
            
            rect2_x = 450
            rect2_y = 100
            
            rect3_x = 250
            rect3_y = 400
            
            rect4_x = 600
            rect4_y = 200
            
            rect5_x = 850
            rect5_y = 200  
            
        if rect_count == 4:
            rect1_x = 650
            rect1_y = 100
            
            rect2_x = 900
            rect2_y = 100
            
            rect3_x = 420
            rect3_y = 500
            
            rect4_x = 650
            rect4_y = 200
            
            rect5_x = 100
            rect5_y = 100   
            
        if rect_count == 5:
            rect1_x = 550
            rect1_y = 200
            
            rect2_x = 250
            rect2_y = 100
            
            rect3_x = 850
            rect3_y = 500
            
            rect4_x = 650
            rect4_y = 100
            
            rect5_x = 150
            rect5_y = 250  
            
        #Distance between rectangles and ball
        dist_rect1_x = ballx - (rect1_x + 50)
        dist_rect1_y = bally - (rect1_y + 25)
        
        dist_rect2_x = ballx - (rect2_x + 50)
        dist_rect2_y = bally - (rect2_y + 25)
        
        dist_rect3_x = ballx - (rect3_x + 50)
        dist_rect3_y = bally - (rect3_y + 25)
        
        dist_rect4_x = ballx - (rect4_x + 50)
        dist_rect4_y = bally - (rect4_y + 25)
        
        dist_rect5_x = ballx - (rect5_x + 50)
        dist_rect5_y = bally - (rect5_y + 25)  
        
        #Destruction of blocks with ball
        if dist_rect1_x <= 50 and dist_rect1_x >= -50 and dist_rect1_y <= 50 and dist_rect1_y >= -50 and rect1 == True:
            rect1 = False
            ballspeedx = -ballspeedx
            ballspeedy = -ballspeedy
            score += 5
            
        if dist_rect2_x <= 50 and dist_rect2_x >= -50 and dist_rect2_y <= 50 and dist_rect2_y >= -50 and rect2 == True:
            rect2 = False
            ballspeedx = -ballspeedx
            ballspeedy = -ballspeedy
            score += 5 
            
        if dist_rect3_x <= 50 and dist_rect3_x >= -50 and dist_rect3_y <= 50 and dist_rect3_y >= -50 and rect3 == True:
            rect3 = False
            ballspeedx = -ballspeedx
            ballspeedy = -ballspeedy
            score += 5         
        
        if dist_rect4_x <= 50 and dist_rect4_x >= -50 and dist_rect4_y <= 50 and dist_rect4_y >= -50 and rect4 == True:
            rect4 = False
            ballspeedx = -ballspeedx
            ballspeedy = -ballspeedy
            score += 5              
    
        if dist_rect5_x <= 50 and dist_rect5_x >= -50 and dist_rect5_y <= 50 and dist_rect5_y >= -50 and rect5 == True:
            rect5 = False
            ballspeedx = -ballspeedx
            ballspeedy = -ballspeedy
            score += 5    
            
        #Rectangle 1
        if rect1 == True:
            pygame.draw.rect(screen, BLUE, [rect1_x, rect1_y, 100,50])
        #Rectangle 2
        if rect2 == True:
            pygame.draw.rect(screen, BLUE, [rect2_x, rect2_y, 100,50])
        #Rectangle 3
        if rect3 == True:
            pygame.draw.rect(screen, BLUE, [rect3_x, rect3_y, 100,50])
        #Rectangle 4
        if rect4 == True:
            pygame.draw.rect(screen, BLUE, [rect4_x, rect4_y, 100,50])
        #Rectangle 5
        if rect5 == True:
            pygame.draw.rect(screen, BLUE, [rect5_x, rect5_y, 100,50])  
        
        #Once all the rectangles are gone user wins
        if rect1 == False and rect2 == False and rect3 == False and rect4 == False and rect5 == False:
            layout = 4
            round_ += 1
            lives = 3
            
        if lives > 0:
            lifeText = font2.render(str(lives), True, WHITE)
            screen.blit(lifeText, [x + 100, 685])
        
        #Heart Image Draw
        screen.blit(heartImg, [x + 75, 675])
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    done = True
                if event.key == pygame.K_SPACE:
                    start_round = True
                    life_loss = False
                    
    #Losing screen
    if layout == 3:
        screen.fill(BLACK)
        #Display
        loseText = font.render("You just lost!", True, WHITE)
        screen.blit(loseText, [380,300])
        quitText = font2.render("Press \"q\" to quit the game at any point", True, WHITE)
        screen.blit(quitText, [0, 680])
        #Input Update
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    done = True
            
            
    if layout == 4:
        screen.fill(BLACK)
        #Display
        roundText = font.render("Round " + str(round_) + " finished", True, WHITE)
        screen.blit(roundText, [280,300])
        exitText = font2.render("Press \"q\" at any point to exit the game", True, WHITE)
        screen.blit(exitText, [0,680])
        spaceText = font.render("Press SPACE to start playing Atar.io" , True, WHITE)
        screen.blit(spaceText, [150,400])
        scoreText = font3.render("Score: " + str(score), True, WHITE)
        screen.blit(scoreText, [295, 100])            
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    done = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    layout = 2
                    rect1 = True
                    rect2 = True
                    rect3 = True
                    rect4 = True
                    rect5 = True
                    ballx = 500
                    bally = 650
                    rect_count += 1
                    round_start = False
                    ballspeedx = abs(ballspeedx) + 0.75
                    ballspeedy = abs(ballspeedy) + 0.75
    if (score > int_highscore):
        highscore["hs"] = score
        int_highscore = highscore["hs"]
                
    pygame.display.flip()
pygame.quit()