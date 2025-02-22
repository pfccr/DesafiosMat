# DMUtil
# Autor: Paulo Fernando Costa da Cruz Data: 30/06/2024 a 31/08/2024
#
#Copyright (C) 2024  Paulo Fernando Costa da Cruz
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <https://www.gnu.org/licenses/>.
#
# bibliotecas
import pygame, sys
from pygame.locals import *
import time
import os


# funções auxiliares

def Ler_arquivo(npasta,nome,tipo):
    with open(npasta+'\\'+nome+'.'+tipo,'r', encoding='utf-8') as leitura:
        arq_lido = leitura.readlines()
        leitura.close()
    return arq_lido    

def Gravar_arquivo(npasta,nome,tipo,nlista):
    with open(npasta+'\\'+nome+'.'+tipo,'w', encoding='utf-8') as gravado:
        for h in nlista:
            gravado.writelines(h+'\n')
        gravado.close() 

def TempoInicial(pasta):
    global tempo, tempo_parcial
    tempo1 = Ler_arquivo(pasta,'tempo','txt')
    tempo = int(tempo1[0])
    if tempo_parcial > 0:
        tempo = tempo_parcial
        tempo_parcial = 0
    return tempo    

def tempo_esgotado():
    texto ='Tempo esgotado !'
    return texto

def Janela(x,y,tela,info1,info2,tempar):
    font4 = pygame.font.SysFont('Arial',  20)
    pygame.draw.rect(tela,(255,255,255),(x,y,600,200),1)
    pygame.draw.rect(tela,(0,255,255),(x+1,y+1,599,199))
    texto_info1 = font4.render(info1, True, (0,0,0))
    texto_info2 = font4.render(info2, True, (0,0,0))
    tela.blit(texto_info1, (x+10, y+10))
    tela.blit(texto_info2, (x+10, y+35))
    pygame.display.flip()
    pygame.time.delay(1000*tempar)

# funções uteis

def tocar_musica():
    pygame.mixer.music.load('Newer Wave.mp3')
    pygame.mixer.music.play(0) 

def ver_manual(origem,raiz):
    raiz = os.getcwd()
    origem = raiz +'\\Manual do jogo'+'.pdf'
    os.startfile(origem)

def som():
    som = pygame.mixer.Sound('mouse-click-104737.mp3')
    som.play()
