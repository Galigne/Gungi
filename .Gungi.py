#ALL import
import pygame
from pygame.locals import *
from random import *
import time
import os
import sys
import platform
pygame.init()

#-------------------------------------------------------------------------------------------------------------------
#ALL Global Variables
global posx, posy, x, y, z, piece, choose, select, statik, turn, color, color_2, move, nbTurn, X, Y
Board = [[[0 for k in range(3)]for i in range(9)]for j in range(9)]
Piece = [0] * 20
#-------------------------------------------------------------------------------------------------------------------
def initialisation():
    for i in range(9):
        for j in range(9):
            for k in range(3):
                Board[i][j][k] = 0
    Piece[0] = -10
    Piece[1] = 1
    Piece[11] = 1
    Piece[2] = 1
    Piece[12] = 1
    Piece[3] = 9
    Piece[13] = 9
    Piece[4] = 6
    Piece[14] = 6
    Piece[5] = 2
    Piece[15] = 2
    Piece[6] = 2
    Piece[16] = 2
    Piece[7] = 2
    Piece[17] = 2
    Piece[8] = 2
    Piece[18] = 2
    Piece[9] = 2
    Piece[19] = 2
#-------------------------------------------------------------------------------------------------------------------
initialisation()
x = 0
y = 0
z = 0
move = 0
loop = 1
choose = 0
select = 0
statik = 0
turn = 0
nbTurn = 0
piece = 0
color = (200,50,50)
color_2 = (255,255,255)
color_3 = (0,0,0)
#-------------------------------------------------------------------------------------------------------------------
#ALL image and Screen
screen = pygame.display.set_mode((1200, 900))
board = pygame.image.load(".Board.jpg").convert()
background = pygame.image.load(".Background.jpg").convert()
myfont = pygame.font.SysFont("comicsansms", 30)
thefont = pygame.font.SysFont("arial", 17)
font = pygame.font.SysFont("arial", 80)

#Pieces
MarshallB = pygame.image.load("MarshallB.png").convert_alpha()
MarshallW = pygame.image.load("MarshallW.png").convert_alpha()
GeneralB = pygame.image.load("GeneralB.png").convert_alpha()
GeneralW = pygame.image.load("GeneralW.png").convert_alpha()
PawnB = pygame.image.load("PawnB.png").convert_alpha()
PawnW = pygame.image.load("PawnW.png").convert_alpha()
KnightB = pygame.image.load("KnightB.png").convert_alpha()
KnightW = pygame.image.load("KnightW.png").convert_alpha()
SamouraiB = pygame.image.load("SamouraiB.png").convert_alpha()
SamouraiW = pygame.image.load("SamouraiW.png").convert_alpha()
CannonB = pygame.image.load("CannonB.png").convert_alpha()
CannonW = pygame.image.load("CannonW.png").convert_alpha()
ArcherB = pygame.image.load("ArcherB.png").convert_alpha()
ArcherW = pygame.image.load("ArcherW.png").convert_alpha()
NinjaB = pygame.image.load("NinjaB.png").convert_alpha()
NinjaW = pygame.image.load("NinjaW.png").convert_alpha()
FortressB = pygame.image.load("FortressB.png").convert_alpha()
FortressW = pygame.image.load("FortressW.png").convert_alpha()

#Logos
Marshall_W = pygame.image.load("Marshall_W.png").convert_alpha()
Marshall_B = pygame.image.load("Marshall_B.png").convert_alpha()
General_B = pygame.image.load("General_B.png").convert_alpha()
General_W = pygame.image.load("General_W.png").convert_alpha()
Pawn_B = pygame.image.load("Pawn_B.png").convert_alpha()
Pawn_W = pygame.image.load("Pawn_W.png").convert_alpha()
Knight_W = pygame.image.load("Knight_W.png").convert_alpha()
Knight_B = pygame.image.load("Knight_B.png").convert_alpha()
Samourai_B = pygame.image.load("Samourai_B.png").convert_alpha()
Samourai_W = pygame.image.load("Samourai_W.png").convert_alpha()
Cannon_B = pygame.image.load("Cannon_B.png").convert_alpha()
Cannon_W = pygame.image.load("Cannon_W.png").convert_alpha()
Archer_B = pygame.image.load("Archer_B.png").convert_alpha()
Archer_W = pygame.image.load("Archer_W.png").convert_alpha()
Ninja_B = pygame.image.load("Ninja_B.png").convert_alpha()
Ninja_W = pygame.image.load("Ninja_W.png").convert_alpha()
Fortress_B = pygame.image.load("Fortress_B.png").convert_alpha()
Fortress_W = pygame.image.load("Fortress_W.png").convert_alpha()


#-------------------------------------------------------------------------------------------------------------------
#Swap Turn
def Turn():
    global turn, nbTurn, choose, select, piece
    #Reinitialise all important variables
    choose = 0
    select = 0
    piece = 0
    #Display the changes
    display()
    #Add a turn
    nbTurn += 1
    turn = nbTurn%2
    i = 0
    j = 0
    k = 0
    #Change side of the Board
    if nbTurn!=30:
        Board2 = [[[0 for k in range(3)]for i in range(9)]for j in range(9)]
        black = 0
        white = 0
        for i in range(9):
            for j in range(9):
                for k in range(3):
                    Board2[8-i][8-j][k] = Board[i][j][k]
                    if Board[i][j][k] == 11:
                        black = 1
                    if Board[i][j][k] == 1:
                        white = 1
        for i in range(9):
            for j in range(9):
                for k in range(3):
                    Board[i][j][k] = Board2[i][j][k]
        while black == 0 and nbTurn>1:
            win(1)
            
        while white == 0 and nbTurn>1:
            win(0)
        
    #If it's the 30's turn, whites play again
    if nbTurn == 30:
        nbTurn += 1
        turn = nbTurn%2
    #Wait a little
    time.sleep(0.5)
    #Redisplay everything after the Board have been turned
    display()

#-------------------------------------------------------------------------------------------------------------------
#Refresh the screen
def display():
    global piece, choose, select, move, turn, nbTurn

    #Display all background elements
    Marshall__W = myfont.render(str(Piece[1]), 1, (0,0,0))
    Marshall__B = myfont.render(str(Piece[11]), 1, (0,0,0))
    General__W = myfont.render(str(Piece[2]), 1, (0,0,0))
    General__B = myfont.render(str(Piece[12]), 1, (0,0,0))
    Pawn__W = myfont.render(str(Piece[3]), 1, (0,0,0))
    Pawn__B = myfont.render(str(Piece[13]), 1, (0,0,0))
    Knight__W = myfont.render(str(Piece[4]), 1, (0,0,0))
    Knight__B = myfont.render(str(Piece[14]), 1, (0,0,0))
    Samourai__W = myfont.render(str(Piece[5]), 1, (0,0,0))
    Samourai__B = myfont.render(str(Piece[15]), 1, (0,0,0))
    Cannon__W = myfont.render(str(Piece[6]), 1, (0,0,0))
    Cannon__B = myfont.render(str(Piece[16]), 1, (0,0,0))
    Archer__W = myfont.render(str(Piece[7]), 1, (0,0,0))
    Archer__B = myfont.render(str(Piece[17]), 1, (0,0,0))
    Ninja__W = myfont.render(str(Piece[8]), 1, (0,0,0))
    Ninja__B = myfont.render(str(Piece[18]), 1, (0,0,0))
    Fortress__W = myfont.render(str(Piece[9]), 1, (0,0,0))
    Fortress__B = myfont.render(str(Piece[19]), 1, (0,0,0))
    screen.blit(background, (0,0))
    screen.blit(board, (150,0))
    if turn==0 and nbTurn!=4:
        pygame.draw.line(screen,color_3,(150,600),(1050,600), 5)
        pygame.draw.line(screen,color_2,(150,300),(1050,300), 5)
    if turn==1 or nbTurn==4:
        pygame.draw.line(screen,color_2,(150,600),(1050,600), 5)
        pygame.draw.line(screen,color_3,(150,300),(1050,300), 5)
    screen.blit(Marshall_W, (0,0))
    screen.blit(Marshall__W, (100, 30))
    screen.blit(Marshall_B, (1050,0))
    screen.blit(Marshall__B, (1150, 30))
    screen.blit(General_W, (0,100))
    screen.blit(General__W, (100, 130))
    screen.blit(General_B, (1050,100))
    screen.blit(General__B, (1150, 130))
    screen.blit(Pawn_W, (0,200))
    screen.blit(Pawn__W, (100, 230))
    screen.blit(Pawn_B, (1050,200))
    screen.blit(Pawn__B, (1150, 230))
    screen.blit(Knight_W, (0,300))
    screen.blit(Knight__W, (100, 330))
    screen.blit(Knight_B, (1050,300))
    screen.blit(Knight__B, (1150, 330))
    screen.blit(Samourai_W, (0,400))
    screen.blit(Samourai__W, (100, 430))
    screen.blit(Samourai_B, (1050,400))
    screen.blit(Samourai__B, (1150, 430))
    screen.blit(Cannon_W, (0,500))
    screen.blit(Cannon__W, (100, 530))
    screen.blit(Cannon_B, (1050,500))
    screen.blit(Cannon__B, (1150, 530))
    screen.blit(Archer_W, (0,600))
    screen.blit(Archer__W, (100, 630))
    screen.blit(Archer_B, (1050,600))
    screen.blit(Archer__B, (1150, 630))
    screen.blit(Ninja_W, (0,700))
    screen.blit(Ninja__W, (100, 730))
    screen.blit(Ninja_B, (1050,700))
    screen.blit(Ninja__B, (1150, 730))
    screen.blit(Fortress_W, (0,800))
    screen.blit(Fortress__W, (100, 830))
    screen.blit(Fortress_B, (1050,800))
    screen.blit(Fortress__B, (1150, 830))
    
    #Selected new piece
    if choose == 1:
        if piece == 1:
            pygame.draw.rect(screen, color_3, (17,15,65,65), 3)
        if piece == 11:
            pygame.draw.rect(screen, color_2, (1066,15,65,65), 3)
        if piece == 2:
            pygame.draw.rect(screen, color_3, (17,115,65,65), 3)
        if piece == 12:
            pygame.draw.rect(screen, color_2, (1066,115,65,65), 3)
        if piece ==3:
            pygame.draw.rect(screen, color_3, (17,215,65,65), 3)
        if piece == 13:
            pygame.draw.rect(screen, color_2, (1066,215,65,65), 3)
        if piece == 4:
            pygame.draw.rect(screen, color_3, (17,315,65,65), 3)
        if piece == 14:
            pygame.draw.rect(screen, color_2, (1066,315,65,65), 3)
        if piece == 5:
            pygame.draw.rect(screen, color_3, (17,415,65,65), 3)
        if piece == 15:
            pygame.draw.rect(screen, color_2, (1066,415,65,65), 3)
        if piece == 6:
            pygame.draw.rect(screen, color_3, (17,515,65,65), 3)
        if piece == 16:
            pygame.draw.rect(screen, color_2, (1066,515,65,65), 3)
        if piece == 7:
            pygame.draw.rect(screen, color_3, (17,615,65,65), 3)
        if piece == 17:
            pygame.draw.rect(screen, color_2, (1066,615,65,65), 3)
        if piece == 8:
            pygame.draw.rect(screen, color_3, (17,715,65,65), 3)
        if piece == 18:
            pygame.draw.rect(screen, color_2, (1066,715,65,65), 3)
        if piece == 9:
            pygame.draw.rect(screen, color_3, (17,815,65,65), 3)
        if piece == 19:
            pygame.draw.rect(screen, color_2, (1066,815,65,65), 3)
            
    #Display the possible movements of pieces
    if move == 1:
        #Marshall
        if piece == 1 or piece == 11:
            pygame.draw.rect(screen, color, ((150+x*100),(y*100),100,100), 5)
            pygame.draw.rect(screen, color, ((150+x*100)+100,(y*100),100,100), 5)
            pygame.draw.rect(screen, color, ((150+x*100)-100,(y*100),100,100), 5)
            pygame.draw.rect(screen, color, ((150+x*100),(y*100)+100,100,100), 5)
            pygame.draw.rect(screen, color, ((150+x*100),(y*100)-100,100,100), 5)
            pygame.draw.rect(screen, color, ((150+x*100)+100,(y*100)+100,100,100), 5)
            pygame.draw.rect(screen, color, ((150+x*100)+100,(y*100)-100,100,100), 5)
            pygame.draw.rect(screen, color, ((150+x*100)-100,(y*100)+100,100,100), 5)
            pygame.draw.rect(screen, color, ((150+x*100)-100,(y*100)-100,100,100), 5)
        #General
        if piece == 2 or piece == 12:
            pygame.draw.rect(screen, color, ((150+x*100),(y*100),100,100), 5)
            pygame.draw.rect(screen, color, ((150+x*100)+100,(y*100),100,100), 5)
            pygame.draw.rect(screen, color, ((150+x*100)+200,(y*100),100,100), 5)
            pygame.draw.rect(screen, color, ((150+x*100)-100,(y*100),100,100), 5)
            pygame.draw.rect(screen, color, ((150+x*100)-200,(y*100),100,100), 5)
            pygame.draw.rect(screen, color, ((150+x*100),(y*100)+100,100,100), 5)
            pygame.draw.rect(screen, color, ((150+x*100),(y*100)+200,100,100), 5)
            pygame.draw.rect(screen, color, ((150+x*100),(y*100)-100,100,100), 5)
            pygame.draw.rect(screen, color, ((150+x*100),(y*100)-200,100,100), 5)
            pygame.draw.rect(screen, color, ((150+x*100)+100,(y*100)+100,100,100), 5)
            pygame.draw.rect(screen, color, ((150+x*100)+100,(y*100)-100,100,100), 5)
            pygame.draw.rect(screen, color, ((150+x*100)-100,(y*100)+100,100,100), 5)
            pygame.draw.rect(screen, color, ((150+x*100)-100,(y*100)-100,100,100), 5)
            if z >= 1:
                pygame.draw.rect(screen, color, ((150+x*100)+200,(y*100)+200,100,100), 5)
                pygame.draw.rect(screen, color, ((150+x*100)+200,(y*100)-200,100,100), 5)
                pygame.draw.rect(screen, color, ((150+x*100)-200,(y*100)+200,100,100), 5)
                pygame.draw.rect(screen, color, ((150+x*100)-200,(y*100)-200,100,100), 5)
            if z == 2:
                pygame.draw.rect(screen, color, ((150+x*100)+300,(y*100)+300,100,100), 5)
                pygame.draw.rect(screen, color, ((150+x*100)+300,(y*100)-300,100,100), 5)
                pygame.draw.rect(screen, color, ((150+x*100)-300,(y*100)+300,100,100), 5)
                pygame.draw.rect(screen, color, ((150+x*100)-300,(y*100)-300,100,100), 5)
                pygame.draw.rect(screen, color, ((150+x*100)+300,(y*100),100,100), 5)
                pygame.draw.rect(screen, color, ((150+x*100),(y*100)-300,100,100), 5)
                pygame.draw.rect(screen, color, ((150+x*100),(y*100)+300,100,100), 5)
                pygame.draw.rect(screen, color, ((150+x*100)-300,(y*100),100,100), 5)
        #Pawn
        if piece == 3 or piece == 13:
            if y == 0:
                pygame.draw.rect(screen, (0,0,255), ((150+x*100),(y*100),100,100), 5)
            else:
                pygame.draw.rect(screen, color, ((150+x*100),(y*100),100,100), 5)
            pygame.draw.rect(screen, color, ((150+x*100),(y*100)-100,100,100), 5)
            if z>=1:
                pygame.draw.rect(screen, color, ((150+x*100)+100,(y*100)-100,100,100), 5)
                pygame.draw.rect(screen, color, ((150+x*100)-100,(y*100)-100,100,100), 5)
            if z==2:
                pygame.draw.rect(screen, color, ((150+x*100)+100,(y*100),100,100), 5)
                pygame.draw.rect(screen, color, ((150+x*100)-100,(y*100),100,100), 5)
        #Knight
        if piece == 4 or piece == 14:
            pygame.draw.rect(screen, color, ((150+x*100),(y*100),100,100), 5)
            pygame.draw.rect(screen, color, ((150+x*100),(y*100)-100,100,100), 5)
            pygame.draw.rect(screen, color, ((150+x*100)+100,(y*100)+100,100,100), 5)
            pygame.draw.rect(screen, color, ((150+x*100)-100,(y*100)+100,100,100), 5)
            pygame.draw.rect(screen, color, ((150+x*100)-100,(y*100)-100,100,100), 5)
            pygame.draw.rect(screen, color, ((150+x*100)+100,(y*100)-100,100,100), 5)
            if z >= 1:
                pygame.draw.rect(screen, color, ((150+x*100),(y*100)-200,100,100), 5)
            if z == 2:
                pygame.draw.rect(screen, color, ((150+x*100)+100,(y*100)-200,100,100), 5)
                pygame.draw.rect(screen, color, ((150+x*100)-100,(y*100)-200,100,100), 5)
        #Samourai
        if piece == 5 or piece == 15:
            pygame.draw.rect(screen, color, ((150+x*100),(y*100),100,100), 5)
            pygame.draw.rect(screen, color, ((150+x*100)+100,(y*100)+100,100,100), 5)
            pygame.draw.rect(screen, color, ((150+x*100)-100,(y*100)+100,100,100), 5)
            pygame.draw.rect(screen, color, ((150+x*100)-100,(y*100)-100,100,100), 5)
            pygame.draw.rect(screen, color, ((150+x*100)+100,(y*100)-100,100,100), 5)
            if z >= 1:
                pygame.draw.rect(screen, color, ((150+x*100)+200,(y*100)+200,100,100), 5)
                pygame.draw.rect(screen, color, ((150+x*100)-200,(y*100)+200,100,100), 5)
                pygame.draw.rect(screen, color, ((150+x*100)-200,(y*100)-200,100,100), 5)
                pygame.draw.rect(screen, color, ((150+x*100)+200,(y*100)-200,100,100), 5)
            if z == 2:
                pygame.draw.rect(screen, color, ((150+x*100)+300,(y*100)+300,100,100), 5)
                pygame.draw.rect(screen, color, ((150+x*100)-300,(y*100)+300,100,100), 5)
                pygame.draw.rect(screen, color, ((150+x*100)-300,(y*100)-300,100,100), 5)
                pygame.draw.rect(screen, color, ((150+x*100)+300,(y*100)-300,100,100), 5)
        #Cannon
        if piece == 6 or piece == 16:
            pygame.draw.rect(screen, color, ((150+x*100),(y*100),100,100), 5)
            pygame.draw.rect(screen, color, ((150+x*100)+100,(y*100),100,100), 5)
            pygame.draw.rect(screen, color, ((150+x*100)-100,(y*100),100,100), 5)
            pygame.draw.rect(screen, color, ((150+x*100),(y*100)+100,100,100), 5)
            pygame.draw.rect(screen, color, ((150+x*100),(y*100)-100,100,100), 5)
            if z >= 1:
                pygame.draw.rect(screen, color, ((150+x*100)+200,(y*100),100,100), 5)
                pygame.draw.rect(screen, color, ((150+x*100)-200,(y*100),100,100), 5)
                pygame.draw.rect(screen, color, ((150+x*100),(y*100)+200,100,100), 5)
                pygame.draw.rect(screen, color, ((150+x*100),(y*100)-200,100,100), 5)
            if z == 2:
                pygame.draw.rect(screen, color, ((150+x*100)+300,(y*100),100,100), 5)
                pygame.draw.rect(screen, color, ((150+x*100)-300,(y*100),100,100), 5)
                pygame.draw.rect(screen, color, ((150+x*100),(y*100)+300,100,100), 5)
                pygame.draw.rect(screen, color, ((150+x*100),(y*100)-300,100,100), 5)
        #Archer
        if piece == 7 or piece == 17:
            if z<2:
                pygame.draw.rect(screen, color, ((150+x*100)+200,(y*100),100,100), 5)
                pygame.draw.rect(screen, color, ((150+x*100)-200,(y*100),100,100), 5)
                pygame.draw.rect(screen, color, ((150+x*100),(y*100)+200,100,100), 5)
                pygame.draw.rect(screen, color, ((150+x*100),(y*100)-200,100,100), 5)
            if z>=1:
                pygame.draw.rect(screen, color, ((150+x*100)+100,(y*100)-200,100,100), 5)
                pygame.draw.rect(screen, color, ((150+x*100)-100,(y*100)-200,100,100), 5)
                pygame.draw.rect(screen, color, ((150+x*100)+100,(y*100)+200,100,100), 5)
                pygame.draw.rect(screen, color, ((150+x*100)-100,(y*100)+200,100,100), 5)
                pygame.draw.rect(screen, color, ((150+x*100)+200,(y*100)-100,100,100), 5)
                pygame.draw.rect(screen, color, ((150+x*100)+200,(y*100)+100,100,100), 5)
                pygame.draw.rect(screen, color, ((150+x*100)-200,(y*100)-100,100,100), 5)
                pygame.draw.rect(screen, color, ((150+x*100)-200,(y*100)+100,100,100), 5)
            if z==2:
                pygame.draw.rect(screen, color, ((150+x*100)+300,(y*100),100,100), 5)
                pygame.draw.rect(screen, color, ((150+x*100)-300,(y*100),100,100), 5)
                pygame.draw.rect(screen, color, ((150+x*100),(y*100)+300,100,100), 5)
                pygame.draw.rect(screen, color, ((150+x*100),(y*100)-300,100,100), 5)
            pygame.draw.rect(screen, (0,255,0), ((150+x*100)+100,(y*100),100,100), 5)
            pygame.draw.rect(screen, (0,255,0), ((150+x*100)-100,(y*100),100,100), 5)
            pygame.draw.rect(screen, (0,255,0), ((150+x*100),(y*100)+100,100,100), 5)
            pygame.draw.rect(screen, (0,255,0), ((150+x*100),(y*100)-100,100,100), 5)
        #Ninja
        if piece == 8 or piece == 18:
            pygame.draw.rect(screen, color, ((150+x*100),(y*100),100,100), 5)
            if z == 0:
                pygame.draw.rect(screen, color, ((150+x*100)+100,(y*100),100,100), 5)
                pygame.draw.rect(screen, color, ((150+x*100)-100,(y*100),100,100), 5)
                pygame.draw.rect(screen, color, ((150+x*100),(y*100)+100,100,100), 5)
                pygame.draw.rect(screen, color, ((150+x*100),(y*100)-100,100,100), 5)
                pygame.draw.rect(screen, color, ((150+x*100)+100,(y*100)+100,100,100), 5)
                pygame.draw.rect(screen, color, ((150+x*100)+100,(y*100)-100,100,100), 5)
                pygame.draw.rect(screen, color, ((150+x*100)-100,(y*100)+100,100,100), 5)
                pygame.draw.rect(screen, color, ((150+x*100)-100,(y*100)-100,100,100), 5)
            if z == 1:
                pygame.draw.rect(screen, color, ((150+x*100)+200,(y*100),100,100), 5)
                pygame.draw.rect(screen, color, ((150+x*100)-200,(y*100),100,100), 5)
                pygame.draw.rect(screen, color, ((150+x*100),(y*100)+200,100,100), 5)
                pygame.draw.rect(screen, color, ((150+x*100),(y*100)-200,100,100), 5)
                pygame.draw.rect(screen, color, ((150+x*100)+200,(y*100)+200,100,100), 5)
                pygame.draw.rect(screen, color, ((150+x*100)+200,(y*100)-200,100,100), 5)
                pygame.draw.rect(screen, color, ((150+x*100)-200,(y*100)+200,100,100), 5)
                pygame.draw.rect(screen, color, ((150+x*100)-200,(y*100)-200,100,100), 5)
            if z == 2:
                pygame.draw.rect(screen, color, ((150+x*100)+300,(y*100),100,100), 5)
                pygame.draw.rect(screen, color, ((150+x*100)-300,(y*100),100,100), 5)
                pygame.draw.rect(screen, color, ((150+x*100),(y*100)+300,100,100), 5)
                pygame.draw.rect(screen, color, ((150+x*100),(y*100)-300,100,100), 5)
                pygame.draw.rect(screen, color, ((150+x*100)+300,(y*100)+300,100,100), 5)
                pygame.draw.rect(screen, color, ((150+x*100)+300,(y*100)-300,100,100), 5)
                pygame.draw.rect(screen, color, ((150+x*100)-300,(y*100)+300,100,100), 5)
                pygame.draw.rect(screen, color, ((150+x*100)-300,(y*100)-300,100,100), 5)
        #Fortress
        if piece == 9 or piece == 19:
            pygame.draw.rect(screen, color, ((150+x*100),(y*100),100,100), 5)

    #Display all Pieces on Board
    for u in range(0,9):
        for c in range(0,9):
            #First floor
            if Board[u][c][0] == 1:
                screen.blit(MarshallW, (150+c*100, (u*100)+5))
            if Board[u][c][0] == 11:
                screen.blit(MarshallB, (150+c*100, (u*100)+5))
            if Board[u][c][0] == 2:
                screen.blit(GeneralW, (150+c*100, (u*100)+5))
            if Board[u][c][0] == 12:
                screen.blit(GeneralB, (150+c*100, (u*100)+5))
            if Board[u][c][0] == 3:
                screen.blit(PawnW, (150+c*100, (u*100)+5))
            if Board[u][c][0] == 13:
                screen.blit(PawnB, (150+c*100, (u*100)+5))
            if Board[u][c][0] == 4:
                screen.blit(KnightW, (150+c*100, (u*100)+5))
            if Board[u][c][0] == 14:
                screen.blit(KnightB, (150+c*100, (u*100)+5))
            if Board[u][c][0] == 5:
                screen.blit(SamouraiW, (150+c*100, (u*100)+5))
            if Board[u][c][0] == 15:
                screen.blit(SamouraiB, (150+c*100, (u*100)+5))
            if Board[u][c][0] == 6:
                screen.blit(CannonW, (150+c*100, (u*100)+5))
            if Board[u][c][0] == 16:
                screen.blit(CannonB, (150+c*100, (u*100)+5))
            if Board[u][c][0] == 7:
                screen.blit(ArcherW, (150+c*100, (u*100)+5))
            if Board[u][c][0] == 17:
                screen.blit(ArcherB, (150+c*100, (u*100)+5))
            if Board[u][c][0] == 8:
                screen.blit(NinjaW, (150+c*100, (u*100)+5))
            if Board[u][c][0] == 18:
                screen.blit(NinjaB, (150+c*100, (u*100)+5))
            if Board[u][c][0] == 9:
                screen.blit(FortressW, (150+c*100, (u*100)+5))
            if Board[u][c][0] == 19:
                screen.blit(FortressB, (150+c*100, (u*100)+5))
            
            #Second floor
            if Board[u][c][1] == 1:
                screen.blit(MarshallW, (150+c*100, (u*100)-3))
            if Board[u][c][1] == 11:
                screen.blit(MarshallB, (150+c*100, (u*100)-3))
            if Board[u][c][1] == 2:
                screen.blit(GeneralW, (150+c*100, (u*100)-3))
            if Board[u][c][1] == 12:
                screen.blit(GeneralB, (150+c*100, (u*100)-3))
            if Board[u][c][1] == 3:
                screen.blit(PawnW, (150+c*100, (u*100)-3))
            if Board[u][c][1] == 13:
                screen.blit(PawnB, (150+c*100, (u*100)-3))
            if Board[u][c][1] == 4:
                screen.blit(KnightW, (150+c*100, (u*100)-3))
            if Board[u][c][1] == 14:
                screen.blit(KnightB, (150+c*100, (u*100)-3))
            if Board[u][c][1] == 5:
                screen.blit(SamouraiW, (150+c*100, (u*100)-3))
            if Board[u][c][1] == 15:
                screen.blit(SamouraiB, (150+c*100, (u*100)-3))
            if Board[u][c][1] == 6:
                screen.blit(CannonW, (150+c*100, (u*100)-3))
            if Board[u][c][1] == 16:
                screen.blit(CannonB, (150+c*100, (u*100)-3))
            if Board[u][c][1] == 7:
                screen.blit(ArcherW, (150+c*100, (u*100)-3))
            if Board[u][c][1] == 17:
                screen.blit(ArcherB, (150+c*100, (u*100)-3))
            if Board[u][c][1] == 8:
                screen.blit(NinjaW, (150+c*100, (u*100)-3))
            if Board[u][c][1] == 18:
                screen.blit(NinjaB, (150+c*100, (u*100)-3))
                
            #Thrid floor
            if Board[u][c][2] == 1:
                screen.blit(MarshallW, (150+c*100, (u*100)-11))
            if Board[u][c][2] == 11:
                screen.blit(MarshallB, (150+c*100, (u*100)-11))
            if Board[u][c][2] == 2:
                screen.blit(GeneralW, (150+c*100, (u*100)-11))
            if Board[u][c][2] == 12:
                screen.blit(GeneralB, (150+c*100, (u*100)-11))
            if Board[u][c][2] == 3:
                screen.blit(PawnW, (150+c*100, (u*100)-11))
            if Board[u][c][2] == 13:
                screen.blit(PawnB, (150+c*100, (u*100)-11))
            if Board[u][c][2] == 4:
                screen.blit(KnightW, (150+c*100, (u*100)-11))
            if Board[u][c][2] == 14:
                screen.blit(KnightB, (150+c*100, (u*100)-11))
            if Board[u][c][2] == 5:
                screen.blit(SamouraiW, (150+c*100, (u*100)-11))
            if Board[u][c][2] == 15:
                screen.blit(SamouraiB, (150+c*100, (u*100)-11))
            if Board[u][c][2] == 6:
                screen.blit(CannonW, (150+c*100, (u*100)-11))
            if Board[u][c][2] == 16:
                screen.blit(CannonB, (150+c*100, (u*100)-11))
            if Board[u][c][2] == 7:
                screen.blit(ArcherW, (150+c*100, (u*100)-11))
            if Board[u][c][2] == 17:
                screen.blit(ArcherB, (150+c*100, (u*100)-11))
            if Board[u][c][2] == 8:
                screen.blit(NinjaW, (150+c*100, (u*100)-11))
            if Board[u][c][2] == 18:
                screen.blit(NinjaB, (150+c*100, (u*100)-11))

    #Refresh the screen
    pygame.display.flip()

#-------------------------------------------------------------------------------------------------------------------
#Select a piece
def select_piece():
    global posx, posy, x, y, z, piece, choose, select, move, turn, nbTurn
    select = 0
    P = 0
    #Choose a new piece
    if (posx<150 and turn == 1 and move == 0) or (posx>1050 and turn == 0 and move == 0):
        #Marshall W
        if posx<100 and posy<100:
            P = 1
        #Marshall B
        if posx>1050 and posy<100:
            P = 11
        #General W
        if posx<100 and posy>100 and posy<200 and nbTurn > 1:      
            P = 2
        #General B
        if posx>1050 and posy>100 and posy<200 and nbTurn > 1:
            P = 12
        #Pawn W
        if posx<100 and posy>200 and posy<300 and nbTurn > 1:      
            P = 3
        #Pawn B
        if posx>1050 and posy>200 and posy<300 and nbTurn > 1:
            P = 13
        #Knight W
        if posx<100 and posy>300 and posy<400 and nbTurn > 1:      
            P = 4
        #Knight B
        if posx>1050 and posy>300 and posy<400 and nbTurn > 1:
            P = 14
        #Samourai W
        if posx<100 and posy>400 and posy<500 and nbTurn > 1:      
            P = 5
        #Samourai B
        if posx>1050 and posy>400 and posy<500 and nbTurn > 1:
            P = 15
        #Cannon W
        if posx<100 and posy>500 and posy<600 and nbTurn > 1:      
            P = 6
        #Cannon B
        if posx>1050 and posy>500 and posy<600 and nbTurn > 1:
            P = 16
        #Archer W
        if posx<100 and posy>600 and posy<700 and nbTurn > 1:      
            P = 7
        #Archer B
        if posx>1050 and posy>600 and posy<700 and nbTurn > 1:
            P = 17
        #Ninja W
        if posx<100 and posy>700 and posy<800 and nbTurn > 1:      
            P = 8
        #Ninja B
        if posx>1050 and posy>700 and posy<800 and nbTurn > 1:
            P = 18
        #Fortress W
        if posx<100 and posy>800 and posy<900 and nbTurn > 1:      
            P = 9
        #Fortress B
        if posx>1050 and posy>800 and posy<900 and nbTurn > 1:
            P = 19
        #Take a Piece
        if choose == 0 and Piece[P] > 0:
                    choose = 1
                    piece = P
                    Piece[P] -= 1 
        elif choose == 1 and piece == P:
                    choose = 0
                    piece = 0
                    Piece[P] += 1  

        
            
    #Choose an empty square or piece
    if posx>150 and posx<1050:
        select = 1
        #position in 'x' of cursor
        if posx>=150 and posx<250:
            x = 0
        if posx>=250 and posx<350:
            x = 1
        if posx>=350 and posx<450:
            x = 2
        if posx>=450 and posx<550:
            x = 3
        if posx>=550 and posx<650:
            x = 4
        if posx>=650 and posx<750:
            x = 5
        if posx>=750 and posx<850:
            x = 6
        if posx>=850 and posx<950:
            x = 7
        if posx>=950 and posx<1050:
            x = 8
        
        #position in 'y' of cursor
        if posy<100:
            y = 0
        if posy>=100 and posy<200:
            y = 1
        if posy>=200 and posy<300:
            y = 2
        if posy>=300 and posy<400:
            y = 3
        if posy>=400 and posy<500:
            y = 4
        if posy>=500 and posy<600:
            y = 5
        if posy>=600 and posy<700:
            y = 6
        if posy>=700 and posy<800:
            y = 7
        if posy>=800 and posy<900:
            y = 8

    #Placement of new piece
    if choose == 1 and select == 1 and move == 0:
        if Board[y][x][0] == 0 or Board[y][x][1] == 0 or Board[y][x][2] == 0:
            if ((y>2 and nbTurn>30) or (y>5 and nbTurn<=30)):
                if Board[y][x][0] == 0:
                    Board[y][x][0] = piece
                    Turn()
                elif Board[y][x][1] == 0 and Board[y][x][0] != 1 and Board[y][x][0] != 11 and piece!=9 and piece!=19:
                    Board[y][x][1] = piece
                    Turn()
                elif Board[y][x][2] == 0 and Board[y][x][0] != 1 and Board[y][x][0] != 11 and Board[y][x][1] != 1 and Board[y][x][1] != 11 and piece!=9 and piece!=19:
                    Board[y][x][2] = piece
                    Turn()
                    
                
    #Select a piece on Board 
    i = 2
    while i >= 0 and choose == 0 and move == 0 and select == 1 and Board[y][x][0] != 0 and nbTurn>30:
        if (Board[y][x][i]<11 and Board[y][x][i]>0 and turn == 1) or (Board[y][x][i]>10 and turn == 0):
            
            #piece on ground and nothing on top
            if i == 0 and Board[y][x][i+1] == 0:
                piece = Board[y][x][i]
                z = i
                move_piece()
                z = 0
                i = 0
                
            #piece on ground and a piece on top
            elif i == 0 and Board[y][x][i+1] != 0:
                if (turn == 1 and Board[y][x][i+1] > 10) or (turn == 0 and Board[y][x][i+1]<11 and Board[y][x][i+1]>0):
                    piece = Board[y][x][i]
                    z = i
                    if (Board[y][x][i+1] == 8 and turn==0) or (Board[y][x][i+1] == 18 and turn==1):
                        move_piece()
                    else:
                        static_attack()
                    z = 0
                    i = 0
                    
            #piece tier 1 and no piece on top     
            elif i == 1 and Board[y][x][i+1] == 0:
                if (turn == 1 and Board[y][x][i-1] > 10) or (turn == 0 and Board[y][x][i-1]<11 and Board[y][x][i-1]>0):
                    piece = Board[y][x][i]
                    z = i
                    static_move()
                    z = 0
                    i = 0
                else:
                    piece = Board[y][x][i]
                    z = i
                    move_piece()
                    z = 0
                    i = 0
                    
            #piece tier 1 and piece on top       
            elif i == 1 and Board[y][x][i+1] != 0:
                if (turn == 1 and Board[y][x][i-1] > 10) or (turn == 0 and Board[y][x][i-1]<11 and Board[y][x][i-1]>0) or (turn == 1 and Board[y][x][i+1] > 10) or (turn == 0 and Board[y][x][i+1]<11 and Board[y][x][i+1]>0):
                    piece = Board[y][x][i]
                    z = i
                    if (Board[y][x][i+1] == 8 and turn==0) or (Board[y][x][i+1] == 18 and turn==1):
                        move_piece()
                    else:
                        static_attack()
                    z = 0
                    i = 0
                    
            #piece tier 2 
            elif i == 2:
                if (turn == 1 and Board[y][x][i-1] > 10) or (turn == 0 and Board[y][x][i-1]<11 and Board[y][x][i-1]>0):
                    piece = Board[y][x][i]
                    z = i
                    static_move()
                    z = 0
                    i = 0
                else:
                    piece = Board[y][x][i]
                    z = i
                    move_piece()
                    z = 0
                    i = 0
        i = i-1



#-------------------------------------------------------------------------------------------------------------------
#Move a Piece on the board
def move_piece():
    global x, y, z, piece, select, turn, move, X, Y, Z, posx, posy
    move = 1         
    display()
    X = x
    Y = y
    Z = z
    while select == 1:
        for event in pygame.event.get():
            #Quit
            if event.type == QUIT:
                pygame.quit()
            #Left Click
            if event.type == MOUSEBUTTONDOWN and event.button == 1:
                posx = event.pos[0]
                posy = event.pos[1]
                select_piece()
                #Check deplacement
                
                #Marshall
                if piece == 1 or piece == 11:
                    if y>=Y-1 and y<=Y+1 and x>=X-1 and x<=X+1:
                        if y!=Y or x!=X:
                            change_emplacement()
                    select = 0
                #General
                if piece == 2 or piece == 12:
                    if y!=Y or x!=X:
                        if (y>=Y-1 and y<=Y+1 and x>=X-1 and x<=X+1) or (y>=Y-2 and y<=Y+2 and x==X) or (y==Y and x>=X-2 and x<=X+2) or (z >= 1 and y==Y+2 and x==X+2) or (z >= 1 and y==Y-2 and x==X+2) or (z >= 1 and y==Y+2 and x==X-2) or (z >= 1 and y==Y-2 and x==X-2):
                            change_emplacement()
                        elif z == 2 and y==Y+3:
                            if x==X-3 or x==X or x==X+3:
                                change_emplacement()
                        elif z == 2 and y==Y:
                            if x==X-3 or x==X+3:
                                change_emplacement()
                        elif z == 2 and y==Y-3:
                            if x==X-3 or x==X or x==X+3:
                                change_emplacement()
                    select = 0
                #Pawn
                if piece == 3 or piece == 13:
                    if y!=Y or x!=X:
                        if(y==Y-1 and x==X) or (z>=1 and y==Y-1 and (x==X+1 or x==X-1)) or (z==2 and y==Y and (x==X+1 or x==X-1)):
                            change_emplacement()
                    else:
                        if Y==0 and (Z==2 or (Board[Y][X][Z+1] != 8 and Board[Y][X][Z] != 18)):
                            y = Y
                            Board[Y][X][Z] = 0
                            if piece == 3:
                                Piece[3]+= 1
                            if piece == 13:
                                Piece[13]+= 1
                            Turn()
                    select = 0
                #Knight
                if piece == 4 or piece == 14:
                    if y!=Y or x!=X:
                        if (y==Y-1 and x>=X-1 and x<=X+1) or (y==Y+1 and x==X+1) or (y==Y+1 and x==X-1) or (z==1 and y==Y-2 and x==X) or (z==2 and y==Y-2 and x>=X-1 and x<=X+1):
                            change_emplacement()
                    select = 0
                #Samourai
                if piece == 5 or piece == 15:
                    if y!=Y or x!=X:
                        if ((y==Y-1 or y==Y+1) and (x==X+1 or x==X-1)) or ((z >= 1) and (y==Y-2 or y==Y+2) and (x==X+2 or x==X-2)) or ((z == 2) and (y==Y-3 or y==Y+3) and (x==X+3 or x==X-3)):
                            change_emplacement()
                    select = 0
                #Cannon
                if piece == 6 or piece == 16:
                    if y!=Y or x!=X:
                        if (y==Y and (x==X+1 or x==X-1)) or (x==X and (y==Y+1 or y==Y-1)) or (z>=1 and y==Y and (x==X+2 or x==X-2)) or (z>=1 and x==X and (y==Y+2 or y==Y-2)) or (z==2 and y==Y and (x==X+3 or x==X-3)) or (z==2 and x==X and (y==Y+3 or y==Y-3)):
                            change_emplacement()
                    select = 0
                #Archer
                if piece == 7 or piece==17:
                    if y!=Y or x!=X:
                        if (z<2 and y==Y and (x==X+2 or x==X-2)) or (z<2 and x==X and (y==Y+2 or y==Y-2)) or (z>=1 and y==Y+2 and(x==X+1 or x==X-1)) or (z>=1 and y==Y-2 and (x==X+1 or x==X-1)) or (z>=1 and x==X+2 and (y==Y+1 or y==Y-1)) or (z>=1 and x==X-2 and (y==Y+1 or y==Y-1)) or (z==2 and y==Y and (x==X+3 or x==X-3)) or (z==2 and x==X and (y==Y+3 or y==Y-3)):
                            move_Archer(1)
                        if (y==Y+1 and x==X) or (y==Y-1 and x==X) or (y==Y and x==X+1) or (y==Y and x==X-1):
                            move_Archer(0)
                    select = 0
                #Ninja
                if piece == 8 or piece == 18:
                    if y!=Y or x!=X:
                        if (z==0 and x<=X+1 and x>= X-1 and y<=Y+1 and y>=Y-1) or (z==1 and y==Y-2 and (x==X or x==X+2 or x==X-2)) or (z==1 and y==Y and (x==X+2 or x==X-2)) or (z==1 and y==Y+2 and (x==X or x==X+2 or x==X-2)) or (z==2 and y==Y-3 and (x==X or x==X+3 or x==X-3)) or (z==2 and y==Y and (x==X+3 or x==X-3)) or (z==2 and y==Y+3 and (x==X or x==X+3 or x==X-3)):
                            change_emplacement()
                    select = 0
                #Fortress
                if piece == 9 or piece == 19:
                    select = 0

    move = 0

#-------------------------------------------------------------------------------------------------------------------                                 
#Change emplacement of a piece
def change_emplacement():
    global x, y, z, piece, select, turn, move, X, Y, Z, posx, posy
    emplacement = 0
    #moving on a empty square
    if Board[y][x][0] == 0:
        emplacement = 1

    #moving on what
    z = 3
    while emplacement == 0 and z >= 0:
        z -= 1
        #White Pieces 
        if piece < 11:
            if Board[y][x][z] < 11 and Board[y][x][z] > 0:
                emplacement = 2
            if Board[y][x][z] > 10:
                emplacement = 3
        #Black Pieces
        if piece > 10:
            if Board[y][x][z] < 11 and Board[y][x][z] > 0:
                emplacement = 3
            if Board[y][x][z] > 10:
                emplacement = 2
    #Direction             
    a = 0
    b = 0
    c = 0
    u = 0
    DX = x-X
    DY = y-Y
    if DX < 0:
        a = -1
    if DX > 0:
        a = 1
    if DY < 0:
        b = -1
    if DY > 0:
        b = 1
    nothing = 1
    
    #See if there is a piece that block the way
    while c!=DX+a or u!=DY+b:
        if (u!=0 or c!=0) and (c!=DX or u!=DY):
            if Board[Y+u][X+c][0] != 0:
                nothing = 0
        c = c + a
        u = u + b
    
    #Spécial Knight         
    if piece == 14 or piece==4:
        if y == Y-2:
            if x == X+1:     
                if Board[Y-1][X][0]!=0 and Board[Y-1][X+1][0]!=0:
                    nothing = 0
                else:
                    nothing = 1
            if x == X-1:
                if Board[Y-1][X][0]!=0 and Board[Y-1][X-1][0]!=0:
                    nothing = 0
                else:
                    nothing = 1
                    
    #Spécial Ninja
    if emplacement!=1 and (piece == 8 or piece == 18):
        emplacement = 2
        nothing = 1

    #can it move 
    if (x<=X+1 and x>=X-1 and y<=Y+1 and y>=Y-1) or (nothing == 1):
    #moving on a empty square
        if emplacement == 1:
            Board[y][x][0] = piece
            Board[Y][X][Z] = 0
            #Special ninja
            if Z<2 and (Board[Y][X][Z+1] == 8 or Board[Y][X][Z+1] == 18):
                Board[y][x][1] = Board[Y][X][Z+1]
                Board[Y][X][Z+1] = 0
            Turn()
        #moving on an ally
        if emplacement == 2 and z<2 and Board[y][x][z] != 1 and Board[y][x][z] != 11:
            Board[y][x][z+1] = piece
            Board[Y][X][Z] = 0
            #Special ninja
            if Z<2 and (Board[Y][X][Z+1] == 8 or Board[Y][X][Z+1] == 18):
                if z+1<2:
                    Board[y][x][z+2] = Board[Y][X][Z+1]
                    Board[Y][X][Z+1] = 0
                else:
                    Board[Y][X][Z] = Board[Y][X][Z+1]
                    Board[Y][X][Z+1] = 0
            Turn()
        #moving on an ennemy
        if emplacement == 3:
            #Special Fortress
            if z>0 and ((Board[y][x][0] == 9 and turn == 0) or (Board[y][x][0] == 19 and turn == 1)):
                if z >= 1:
                    Board[y][x][0] = Board[y][x][1]
                    Board[y][x][1] = 0
                if z == 2:
                    Board[y][x][1] = Board[y][x][2]
            #Normal   
            else:
                Board[y][x][z] = piece
                Board[Y][X][Z] = 0
                #Special ninja
                if Z<2 and (Board[Y][X][Z+1] == 8 or Board[Y][X][Z+1] == 18):
                    if z+1<2:
                        Board[y][x][z+2] = Board[Y][X][Z+1]
                        Board[Y][X][Z+1] = 0
                    else:
                        Board[Y][X][Z] = Board[Y][X][Z+1]
                        Board[Y][X][Z+1] = 0
            Turn()


#-------------------------------------------------------------------------------------------------------------------
def static_attack():
    global x, y, z, piece, turn, posx, posy, move, X, Y, Z, statik
    loop = 1
    Piece1 = 0
    Piece2 = 0
    #Draw proposition
    pygame.draw.rect(screen, (200,200,200), (posx, posy, 100, 50), 0)
    pygame.draw.rect(screen, (0,0,0), (posx, posy, 100, 50), 1)
    pygame.draw.line(screen, (0,0,0), (posx, posy+25), (posx+100, posy+25), 1)
    piece1 = thefont.render("", 1, (0,0,0))
    piece2 = thefont.render("", 1, (0,0,0))
    
    #See what Piece can be attacked
    if z == 0 and piece!=9 and piece!=19 and Board[y][x][z+1]!=8 and Board[y][x][z+1]!=18:
        Piece1 = Board[y][x][z+1]
    if z == 1 and statik == 1:
        Piece2 = Board[y][x][z-1]
    if z == 1 and statik == 0:
        if Board[y][x][z+1]!=8 and Board[y][x][z+1]!=18:
            Piece1 = Board[y][x][z+1]
        if (Board[y][x][z]>10 and Board[y][x][z-1]<11) or (Board[y][x][z]<11 and Board[y][x][z-1]>10):
            Piece2 = Board[y][x][z-1]
    if z == 2:
        Piece2 = Board[y][x][z-1]
        
    #Write the piece that can be attacked
    if Piece1 != 0:
        if Piece1 == 1 or Piece1 == 11:
            piece1 = thefont.render("Marshall", 1, (0,0,0))
        if Piece1 == 2 or Piece1 == 12:
            piece1 = thefont.render("General", 1, (0,0,0))
        if Piece1 == 3 or Piece1 == 13:
            piece1 = thefont.render("Pawn", 1, (0,0,0))
        if Piece1 == 4 or Piece1 == 14:
            piece1 = thefont.render("Knight", 1, (0,0,0))
        if Piece1 == 5 or Piece1 == 15:
            piece1 = thefont.render("Samourai", 1, (0,0,0))
        if Piece1 == 6 or Piece1 == 16:
            piece1 = thefont.render("Cannon", 1, (0,0,0))
        if Piece1 == 7 or Piece1 == 17:
            piece1 = thefont.render("Archer", 1, (0,0,0))
        if Piece1 == 8 or Piece1 == 18:
            piece1 = thefont.render("Ninja", 1, (0,0,0))
        if Piece1 == 9 or Piece1 == 19:
            piece1 = thefont.render("Fortress", 1, (0,0,0))
    
    if Piece2 != 0:
        if Piece2 == 1 or Piece2 == 11:
            piece2 = thefont.render("Marshall", 1, (0,0,0))
        if Piece2 == 2 or Piece2 == 12:
            piece2 = thefont.render("General", 1, (0,0,0))
        if Piece2 == 3 or Piece2 == 13:
            piece2 = thefont.render("Pawn", 1, (0,0,0))
        if Piece2 == 4 or Piece2 == 14:
            piece2 = thefont.render("Knight", 1, (0,0,0))
        if Piece2 == 5 or Piece2 == 15:
            piece2 = thefont.render("Samourai", 1, (0,0,0))
        if Piece2 == 6 or Piece2 == 16:
            piece2 = thefont.render("Cannon", 1, (0,0,0))
        if Piece2 == 7 or Piece2 == 17:
            piece2 = thefont.render("Archer", 1, (0,0,0))
        if Piece2 == 8 or Piece2 == 18:
            piece2 = thefont.render("Ninja", 1, (0,0,0))
        if Piece2 == 9 or Piece2 == 19:
            piece2 = thefont.render("Fortress", 1, (0,0,0))
            
    screen.blit(piece1, (posx+5, posy))
    screen.blit(piece2, (posx+5, posy+25))
    pygame.display.flip()
    
    X = posx
    Y = posy
    #See on what the player click
    while loop == 1:
        for event in pygame.event.get():
            if event.type == MOUSEBUTTONDOWN and event.button == 1:
                posx = event.pos[0]
                posy = event.pos[1]
                #Attack the piece on top
                if posx>=X and posx<= X+100 and posy>=Y and posy<=Y+25 and Piece1 != 0:
                    Board[y][x][z+1] = 0
                    if z == 0:
                        Board[y][x][1] = Board[y][x][2]
                        Board[y][x][2] = 0
                    Turn()
                #Attack the piece under
                elif posx>=X and posx<= X+100 and posy>=Y+25 and posy<=Y+50 and Piece2 != 0:
                    Board[y][x][z-1] = Board[y][x][z]
                    Board[y][x][z] = 0
                    if z == 1:
                        Board[y][x][1] = Board[y][x][2]
                        Board[y][x][2] = 0
                    Turn()
                else:
                    display()
                loop = 0
                


        
#-------------------------------------------------------------------------------------------------------------------
def static_move():
    global x, y, z, piece, turn, posx, posy, move, X, Y, statik
    statik = 1
    loop = 1
    #Draw the proposition
    pygame.draw.rect(screen, (200,200,200), (posx, posy, 50, 50), 0)
    pygame.draw.rect(screen, (0,0,0), (posx, posy, 50, 50), 1)
    pygame.draw.line(screen, (0,0,0), (posx, posy+25), (posx+50, posy+25), 1)
    static = thefont.render(" static", 1, (0,0,0))
    movement = thefont.render("move", 1, (0,0,0))
    screen.blit(static, (posx+5, posy))
    screen.blit(movement, (posx+5, posy+25))
    pygame.display.flip()
        
    X = posx
    Y = posy
    while loop == 1:
        #See on what the player click
        for event in pygame.event.get():
            #Quit
            if event.type == QUIT:
                pygame.quit()
                
            if event.type == MOUSEBUTTONDOWN and event.button == 1:
                posx = event.pos[0]
                posy = event.pos[1]
                #The player choose static attack
                if posx>=X and posx<= X+50 and posy>=Y and posy<=Y+25:
                    static_attack()
                #The player choose to move the piece
                elif posx>=X and posx<= X+50 and posy>=Y+25 and posy<=Y+50:
                    move_piece()
                loop = 0
    display()    
    statik = 0

#-------------------------------------------------------------------------------------------------------------------
def move_Archer(AM):
    global x, y, z, piece, turn, posx, posy, move, X, Y, Z
    emplacement = 0
    if Board[y][x][0] == 0 and AM==0:
        emplacement = 1
    z = 3
    while emplacement == 0 and z >= 0:
        z -= 1
        if Board[y][x][z]>10 and turn==0 and AM==0:
            emplacement = 2
        if Board[y][x][z]<11 and Board[y][x][z]!=0 and turn==1 and AM==0:
            emplacement = 2 
        if Board[y][x][z]>10 and turn==1 and AM==1:
            emplacement = 3
        if Board[y][x][z]<11 and Board[y][x][z]!=0 and turn==0 and AM==1:
            emplacement = 3
            
    if emplacement==1:
        Board[y][x][0] = piece
        Board[Y][X][Z] = 0
        Turn()
    if emplacement==2:
        if z<2 and Board[y][x][z]!=1 and Board[y][x][z]!=11:
            Board[y][x][z+1] = piece
            Board[Y][X][Z] = 0
            Turn()
    if emplacement==3:
        #Special Fortress
        if z>0 and ((Board[y][x][0] == 9 and turn == 0) or (Board[y][x][0] == 19 and turn == 1)):
            if z >= 1:
                Board[y][x][0] = Board[y][x][1]
                Board[y][x][1] = 0
            if z == 2:
                Board[y][x][1] = Board[y][x][2]
        #Normal   
        else:
            Board[y][x][z] = 0
        Turn()

                            
#-------------------------------------------------------------------------------------------------------------------
def win(winner):
    global turn, nbTurn
    loop = 1
    if winner==0:
        winer = font.render("BLACK WIN !", 3, (255,255,255))
    if winner==1:
        winer = font.render("WHITE WIN !", 3, (255,255,255))
    screen.blit(winer, (450,450))
    pygame.display.flip()
    initialisation()
    turn = 0
    nbTurn = 0
    while loop==1:
        for event in pygame.event.get():
            if event.type == MOUSEBUTTONDOWN and event.button == 1:
                loop = 0

                            
#-------------------------------------------------------------------------------------------------------------------
loop = 1
display()
#Main Loop
while loop==1:
    #Detect Event
    for event in pygame.event.get():
            #Quit
            if event.type == QUIT:
                loop = 0
            #Help
            if event.type == KEYDOWN and event.key == K_h:
                rules = pygame.image.load("help_1.png").convert()
                screen.blit(rules, (0,0))
                pygame.display.flip()
                page = 1
                while page<=6:
                    #Click to continue
                    for event in pygame.event.get():  
                        if event.type == MOUSEBUTTONDOWN and event.button == 1:
                            posx = event.pos[0]
                            posy = event.pos[1]
                            if posx>1080 and posy<120:
                                page = 7
                            else:
                                page += 1
                                if page == 2:
                                    rules = pygame.image.load("help_2.png").convert()
                                if page == 3:
                                    rules = pygame.image.load("help_3.png").convert()
                                if page == 4:
                                    rules = pygame.image.load("help_4.png").convert()
                                if page == 5:
                                    rules = pygame.image.load("help_5.png").convert()
                                if page == 6:
                                    rules = pygame.image.load("help_6.png").convert()
                                screen.blit(rules, (0,0))
                                pygame.display.flip()
                display()
            #Left Mouse Click
            if event.type == MOUSEBUTTONDOWN and event.button == 1:
                #Cursor position
                posx = event.pos[0]
                posy = event.pos[1]
                #Detect on what the player clicked
                select_piece()
                #if the player isn't trying to move a piece
                if select == 0:
                    #Display everything again
                    display()
        

    
                        



