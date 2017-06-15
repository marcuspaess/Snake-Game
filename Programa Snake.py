#Introdução a Programação de Computadores - IPC
# Universidade do Estado do Amazonas - UEA
# Prof. Jucimar Jr
# 
# Aracille de Souza Barbosa                     1315120206
# Diego Reis Figueira                           1515070169
# João Victor de Cordeiro                       1515140036
# Kethelen Tamara Braga Barbosa                 1525212002
# Marcus Vinicius Paes da Silva Santos          1515070060
# Ulisses Antonio Antonino da Costa             1515090555

#-----------------------------------------------------------------





import pygame
import random
import sys
from pygame.locals import *

pygame.init()

velocidade = 2

largura_tela = 800
altura_tela = 600

black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 200, 0)
bright_red = (255, 0, 0)
bright_green = (0, 255, 0)
block_color = (53, 115, 255)

base = 10

fonte = pygame.font.SysFont('freesansbold.ttf', 30)
tela = pygame.display.set_mode((largura_tela, altura_tela)
