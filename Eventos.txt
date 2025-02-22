# Eventos
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

# variáveis globais
global nivel,num_questao,num_resposta,score,tempo_parcial
nivel = 1
num_questao = 1
num_resposta = 0
score = 0
tempo_parcial = 0

# funções dos eventos

def fechar_programa():
    pygame.quit()
    sys.exit()
    return False

def digitar(etapa,evento,texto_digitado):
    if etapa == 2:
        texto_digitado = texto_digitado + digitar2(evento)
    if evento.key == K_BACKSPACE:
        texto_digitado = texto_digitado[:-1]
    return texto_digitado

def digitar2(evento):
    Ch = evento.unicode
    if evento.key == K_BACKSPACE:
        Ch=''
    if evento.key == K_KP_ENTER:
        Ch=''
    return Ch

def clicar_botao(tela,xm,ym,x,y,larg,altura,cmalt,texto):
    font2 = pygame.font.SysFont('Arial',  40)
    ret_externo = pygame.draw.rect(tela,(255,255,255),(x, y,larg+2,altura)) 
    if ret_externo.collidepoint(xm,ym):
        texto_b = font2.render(texto, True, (0,0,0))
        pygame.draw.rect(tela,(255,255,0),(x+2, y+2,larg-2,altura-4),0,5) 
        tela.blit(texto_b, (x, y+cmalt))
        som = pygame.mixer.Sound('mouse-click-104737.mp3')
        som.play()
        pygame.time.delay(150)
        return True

def clicar_botao_nivel(tela,xm_pos,ym_pos,x,y,larg,altura):
    global nivel, num_questao
    font2 = pygame.font.SysFont('Arial',  40)
    som = pygame.mixer.Sound('mouse-click-104737.mp3')
    som.play()
    i = 1; j = 800; k = 1
    while i < 4:
        if xm_pos >= j and xm_pos <= j+102:
            if ym_pos >= 300 and ym_pos <= 385:
                nivel = i; num_questao = k
                pygame.draw.rect(tela,(255,255,0),(j+2, 302,98,81))
                num = font2.render(str(i), True, (0,0,0))
                tela.blit(num, (j+40,320))
        i = i + 1; j = j + 120; k = k + 10
    i = 4; j = 800; k = 31
    while i < 6:
        if xm_pos >= j and xm_pos <= j+102:
            if ym_pos >= 400 and ym_pos <= 485:
                nivel = i; num_questao = k
                pygame.draw.rect(tela,(255,255,0),(j+2, 402,98,81))
                num = font2.render(str(i), True, (0,0,0))
                tela.blit(num, (j+40,420))
        i = i + 1; j = j + 120; k = k + 10
    return True
    
def clicar_resposta():
    som = pygame.mixer.Sound('mouse-click-104737.mp3')
    som.play()
    return True

def selecionar_reposta(tela,pasta,xm_pos,ym_pos,num_questao):
    global num_resposta
    font3 = pygame.font.SysFont('Arial',  30)
    respostas = ler_arquivo(pasta,'\\respostas\\respostas'+str(num_questao),'txt')
    j = 100
    if xm_pos >= 750 and xm_pos <= 1210:
        if ym_pos >= 100 and ym_pos <= 165:
            num_resposta = 1    
        if ym_pos >= 180 and ym_pos <= 245:
            num_resposta = 2    
        if ym_pos >= 260 and ym_pos <= 325:
            num_resposta = 3    
        if ym_pos >= 340 and ym_pos <= 405:
            num_resposta = 4    
        if ym_pos >= 420 and ym_pos <= 485:
            num_resposta = 5 
    j = j + 80*(num_resposta - 1) 
    pygame.draw.rect(tela,(255,255,255),(745, j,460,65)) 
    pygame.draw.rect(tela,(255,255,0),(750, j+5,450,55)) 
    a = respostas[num_resposta]; b = len(a)-1; a = a[0:b]; respostas[num_resposta] = a
    exibir_texto(770,j+5,tela,font3,(0,0,0),respostas[num_resposta]) 
    return num_resposta

def clicar_botao_confirmar(tela,xm_pos,ym_pos):
    if clicar_botao(tela,xm_pos,ym_pos,745,505,460,65,5,'                Confirmar'):
        return True

def comparar_resposta(tela,numq,pasta,tempo,score):
    font2 = pygame.font.SysFont('Arial',  40)
    score1 = score
    respostas = ler_arquivo(pasta,'\\respostas\\respostas'+str(numq),'txt')
    a = respostas[7]; b = len(a)-1; a = a[0:b]; respostas[7] = a
    c = respostas[7]
    texto_resposta = ''
    if c == str(num_resposta):
        if tempo > 0:
            score1 = score1 + 10
            exibir_texto(60,620,tela,font2,(255,255,255),'Score: '+str(score1))                
            mensagem ='Resposta correta !'
            exibir_mensagem(tela,font2,(0,255,0),mensagem) 
    if c != str(num_resposta):
        if tempo > 0:
            exibir_texto(60,620,tela,font2,(255,255,255),'Score: '+str(score1))                
            mensagem ='Resposta errada !'
            exibir_mensagem(tela,font2,(255,0,0),mensagem) 
    tempo1 = tempo_inicial(pasta)
    return score1,tempo1

def clicar_botao_pausar(tela,xm_pos, ym_pos):
    som = pygame.mixer.Sound('mouse-click-104737.mp3')
    som.play()
    return True 

def janela(x,y,tela,info1,info2,tempar):
    font4 = pygame.font.SysFont('Arial',  20)
    pygame.draw.rect(tela,(255,255,255),(x,y,600,200),1)
    pygame.draw.rect(tela,(0,255,255),(x+1,y+1,599,199))
    texto_info1 = font4.render(info1, True, (0,0,0))
    texto_info2 = font4.render(info2, True, (0,0,0))
    tela.blit(texto_info1, (x+10, y+10))
    tela.blit(texto_info2, (x+10, y+35))
    pygame.display.flip()
    pygame.time.delay(1000*tempar)

# funções auxiliares

def ler_arquivo(npasta,nome,tipo):
    with open(npasta+'\\'+nome+'.'+tipo,'r', encoding='utf-8') as leitura:
        arq_lido = leitura.readlines()
        leitura.close()
    return arq_lido    

def exibir_texto(x,y,tela,fonte,cor,texto): 
    texto1 = fonte.render(texto, True, cor)
    tela.blit(texto1,(x,y))

def exibir_mensagem(tela,fonte,cor,mens): 
    pygame.draw.rect(tela,(0,0,0),(900, 620,300,50)) 
    exibir_texto(850,620,tela,fonte,cor,'      '+mens)

def tempo_inicial(pasta):
    global tempo,tempo_parcial
    tempo1 = ler_arquivo(pasta,'tempo','txt')
    tempo = int(tempo1[0])
    if tempo_parcial > 0:
        tempo = tempo_parcial
        tempo_parcial = 0
    return tempo    

def valor_nivel():
    return nivel

def valor_num_questao():
    return num_questao

def valor_num_resposta():
    return num_resposta

def valor_tempo():
    return tempo

def valor_tempo_parcial():
    return tempo_parcial

def valor_score():
    return score
