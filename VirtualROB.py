# coding: utf-8
#Virtual ROB

import sys
import pygame
import time

class VirtualROB():
    def __init__(self):
        self.handsOpen = True
        self.field = [[None, None, None, None, None, None, None, None, None, None],
                      [None, None, None, None, None, None, None, None, None, None],
                      [ 'G',  'Y',  'B',  'W',  'R', None, None, None, None, None],
                      [None, None, None, None, None, None, None, None, None, None],
                      [None, None, None, None, None, None, None, None, None, None]]
        self.xposition = 2
        self.yposition = 5
        self.Illegal = False
        self.screen = pygame.display.set_mode((417,170)) #create a screen
        self.screen.fill((0,0,0))
        self.green = pygame.Surface((40,10))
        self.green.fill((0,255,0))
        self.yellow = pygame.Surface((40,10))
        self.yellow.fill((255,255,0))
        self.blue = pygame.Surface((40,10))
        self.blue.fill((0,0,255))
        self.white = pygame.Surface((40,10))
        self.white.fill((255,255,255))
        self.red = pygame.Surface((40,10))
        self.red.fill((255,0,0))
        self.left = pygame.Surface((15,10))
        self.left.fill((204,204,204))
        self.right = pygame.Surface((15,10))
        self.right.fill((204,204,204))
        self.illegal = pygame.Surface((417,170))
        self.illegal.fill((51,0,0))
        self.illegal.set_alpha(128)
        self.background = pygame.image.load("VirtualROB.png")
        self.background.set_alpha(128)
        self.Draw()

    def MoveUp(self):
        if self.yposition < 5:
            #print(self.handsOpen)
            #print(self.field[self.xposition][self.yposition])
            if self.handsOpen == False and self.field[self.xposition][self.yposition] != None:
                for i in reversed(range(self.yposition,10)):
                    #print(i)
                    self.field[self.xposition][i] = self.field[self.xposition][i-1]
                self.field[self.xposition][self.yposition] = None

            self.yposition += 1
        self.Draw()

    def MoveDown(self):
        if self.yposition > 0:
            if self.handsOpen == False and self.field[self.xposition][self.yposition-1] != None:
                self.IllegalMove()
                return
            if self.handsOpen == False and self.field[self.xposition][self.yposition] != None:
                for i in range(self.yposition-1,9):
                    #print(i)
                    self.field[self.xposition][i] = self.field[self.xposition][i+1]
                self.field[self.xposition][9] = None

            self.yposition -= 1
        self.Draw()

    def MoveLeft(self):
        if self.xposition > 0:
            if self.handsOpen == True:
                if self.field[self.xposition][self.yposition] != None or self.field[self.xposition-1][self.yposition] != None:
                    self.IllegalMove()
                    return
            else:
                if self.field[self.xposition][self.yposition] == None:
                    if self.field[self.xposition-1][self.yposition] != None:
                        self.IllegalMove()
                        return
                else:
                    if self.yposition == 0:
                        self.IllegalMove()
                        return
                    if self.field[self.xposition][self.yposition-1] != None:
                        self.IllegalMove()
                        return
                    if self.field[self.xposition-1][self.yposition-1] != None:
                        self.IllegalMove()
                        return

                    for i in range(self.yposition,10):
                        self.field[self.xposition-1][i] = self.field[self.xposition][i]
                        self.field[self.xposition][i] = None

            self.xposition -= 1
        self.Draw()

    def MoveRight(self):
        if self.xposition < 4:
            if self.handsOpen == True:
                if self.field[self.xposition][self.yposition] != None or self.field[self.xposition+1][self.yposition] != None:
                    self.IllegalMove()
                    return
            else:
                if self.field[self.xposition][self.yposition] == None:
                    if self.field[self.xposition+1][self.yposition] != None:
                        self.IllegalMove()
                        return
                else:
                    if self.yposition == 0:
                        self.IllegalMove()
                        return
                    if self.field[self.xposition][self.yposition-1] != None:
                        self.IllegalMove()
                        return
                    if self.field[self.xposition+1][self.yposition-1] != None:
                        self.IllegalMove()
                        return

                    for i in range(self.yposition,10):
                        self.field[self.xposition+1][i] = self.field[self.xposition][i]
                        self.field[self.xposition][i] = None

            self.xposition += 1
        self.Draw()

    def Open(self):
        if self.handsOpen == False:
            if self.field[self.xposition][self.yposition] != None:
                if self.yposition != 0 and self.field[self.xposition][self.yposition-1] == None:
                    self.IllegalMove()
                    return

            self.handsOpen = True
        self.Draw()

    def Close(self):
        self.handsOpen = False
        self.Draw()

    def IllegalMove(self):
        self.Illegal = True
        self.Draw()

    def Legal(self):
        self.Illegal = False
        self.Draw()

    def GetColor(self, x, y):
        if self.field[x][y] == 'G':
            return self.green
        if self.field[x][y] == 'Y':
            return self.yellow
        if self.field[x][y] == 'B':
            return self.blue
        if self.field[x][y] == 'W':
            return self.white
        if self.field[x][y] == 'R':
            return self.red

    def Draw(self):
        self.screen.fill((0,0,0))
        self.screen.blit(self.background, (0,0))

        if self.Illegal == True:
            self.screen.blit(self.illegal, (0,0))

        for i in range(0,5):
            for j in range(0,10):
                if self.field[i][j] != None:
                    self.screen.blit(self.GetColor(i,j), (i*83 + 2 + 21, 155 - j*15))

        if self.handsOpen == True:
            self.screen.blit(self.left, (self.xposition*83 + 2 + 21 - 20, 155 - self.yposition*15))
            self.screen.blit(self.right, (self.xposition*83 + 2 + 21 + 40 + 5, 155 - self.yposition*15))
        else:
            if self.field[self.xposition][self.yposition] != None:
                self.screen.blit(self.left, (self.xposition*83 + 2 + 21 - 15, 155 - self.yposition*15))
                self.screen.blit(self.right, (self.xposition*83 + 2 + 21 + 40, 155 - self.yposition*15))
            else:
                self.screen.blit(self.left, (self.xposition*83 + 2 + 21 + 5 - 2, 155 - self.yposition*15))
                self.screen.blit(self.right, (self.xposition*83 + 2 + 21 + 20 + 2, 155 - self.yposition*15))

        pygame.display.flip()

pygame.init()

clock = pygame.time.Clock()

virtualROB = VirtualROB()

while 1:
    clock.tick(8)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                quit()
            if event.key == pygame.K_w:
                virtualROB.MoveUp()
            if event.key == pygame.K_s:
                virtualROB.MoveDown()
            if event.key == pygame.K_q:
                virtualROB.MoveLeft()
            if event.key == pygame.K_e:
                virtualROB.MoveRight()
            if event.key == pygame.K_o or event.key == pygame.K_a:
                virtualROB.Open()
            if event.key == pygame.K_c or event.key == pygame.K_d:
                virtualROB.Close()
            if event.key == pygame.K_u:
                virtualROB.Legal()
            if event.key == pygame.K_r:
                virtualROB = VirtualROB()
