# Interusuarios
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
global botao,posicao_resposta

botao = 0
posicao_resposta = 0

# módulo de interface com o usuário

def guidm(tela,num,pasta,score,texto_digitado,nivel,num_questao,tempo,tempo_parcial,ranking,lrank,indice_rank):
    global botao,mensagem
    global ALTURA,font1,font2,font3,font4,font5,LARGURA
    ALTURA = 720
    font1 = pygame.font.SysFont('Arial', 120)
    font2 = pygame.font.SysFont('Arial',  40)
    font3 = pygame.font.SysFont('Arial',  30)
    font4 = pygame.font.SysFont('Arial',  20)
    font5 = pygame.font.SysFont('Arial', 18)
    LARGURA = 1280
    if num == 0:
        exibir_background(tela,'image001.jpg')
        exibir_texto(150,100,tela,font1,(255,255,255),'Desafios')
        exibir_texto(620,250,tela,font1,(255,255,255),'Matemáticos')
        exibir_texto(75,450,tela,font3,(255,255,255),'Jogo Educacional Digital de Avaliação. Professor: use o programa DMProf para customização do jogo')
        exibir_botao(tela,550,550,200,85,15,font2,'      Iniciar')
    if num == 1:
        preencher_tela(tela,(150,128,128))
        exibir_texto(450,50,tela,font2,(255,255,255),'Explicações gerais sobre o jogo')
        exibir_texto(50,150,tela,font3,(255,255,255),'Este jogo é uma ferramenta de avaliação. O estudante será submetido a uma avaliação na qual ele será')
        exibir_texto(50,200,tela,font3,(255,255,255),'intensamente exposto à visualzação matemática, ou seja, ao uso de visualizações para compreensão  da')
        exibir_texto(50,250,tela,font3,(255,255,255),'matemática. O jogo é um quiz com 5 níveis de dificuldade,  cada um com 10 questões. O professor pode')
        exibir_texto(50,300,tela,font3,(255,255,255),'usar a versão de demonstração que serve para alunos do último ano do ensino fundamental ou do ensino')
        exibir_texto(50,350,tela,font3,(255,255,255),'médio ou pode customizar o jogo, mudando instruções,  questões, respostas e o  tempo, em   segundos,')
        exibir_texto(50,400,tela,font3,(255,255,255),'para responder cada questão.')
        exibir_botao(tela,550,550,200,85,15,font2,'     Avançar')
    if num == 2:
        exibir_background(tela,'image002.jpg')
        exibir_texto(200,100,tela,font1,(255,255,255),'Cadastre o jogador')
        exibir_texto(200,330,tela,font2,(255,255,255),'Nome: ')
        exibir_texto(200,400,tela,font2,(255,255,255),'Score: '+str(score))
        exibir_retangulo_cheio(tela,(255,255,255),(300, 300,700,75))
        exibir_texto(310,320,tela,font2,(0,0,0),texto_digitado)
        exibir_botao(tela,250,550,200,85,15,font2,'     Manual')
        exibir_botao(tela,850,550,200,85,15,font2,'     Avançar')
    if num == 3: 
        preencher_tela(tela,(0,0,0))
        exibir_texto(500,50,tela,font2,(255,255,255),'Opções de jogo')
        exibir_texto(800,200,tela,font3,(255,255,255),'Escolha o nível inicial para jogar (1 a 5)')
        exibir_botao_nivel(tela,font2)
        exibir_botao(tela,50,200,400,85,5,font2,'     Jogo Demonstraçao')
        exibir_botao(tela,50,500,400,85,5,font2,'     Jogo do Professor')  
        exibir_botao(tela,550,600,200,85,15,font2,'     Avançar')
    if num == 4:
        preencher_tela(tela,(150,128,128))
        exibir_instrucoes(tela,pasta,font2,font3)
        exibir_botao(tela,550,550,200,85,15,font2,'     Avançar')
    if num == 5:
        if tempo == 0:
            mensagem = 'Tempo esgotado !' 
        else:
            mensagem = texto_digitado 
        exibir_background(tela,'image002.jpg')
        exibir_questao(num_questao,tela,pasta)
        exibir_retangulo_com_borda(tela,(0,255,0),(40,90,670,520),3)
        exibir_texto(60,20,tela,font2,(255,255,255),'Nível: '+str(nivel))
        exibir_retangulo_com_borda(tela,(0,255,0),(40,10,150,80),3)                
        exibir_texto(210,20,tela,font2,(255,255,255),'Questão '+str(num_questao))
        exibir_retangulo_com_borda(tela,(0,255,0),(190,10,220,80),3) 
        exibir_retangulo_cheio(tela,(0,0,0),(540,20,75,50))
        exibir_texto(430,20,tela,font2,(255,255,255),'Tempo: ') 
        exibir_tempo(tela,tempo)
        exibir_retangulo_com_borda(tela,(0,255,0),(410,10,300,80),3)
        exibir_retangulo_cheio(tela,(0,0,0),(160,620,75,50))
        exibir_texto(60,620,tela,font2,(255,255,255),'Score: '+str(score))                
        exibir_retangulo_com_borda(tela,(0,255,0),(40,605,220,80),3)
        exibir_retangulo_cheio(tela,(0,0,0),(410,620,290,50))
        exibir_texto(275,620,tela,font2,(255,255,255),'Conceito: ')                
        exibir_retangulo_com_borda(tela,(0,255,0),(260,605,450,80),3)
        exibir_texto(900,20,tela,font2,(255,255,255),'Respostas ') 
        exibir_texto(800,60,tela,font4,(255,255,255),'Escolha a alternativa correspondente ao gráfico')                
        exibir_retangulo_com_borda(tela,(0,255,0),(705,10,520,80),3)
        exibir_respostas(tela,pasta,num_questao)
        exibir_botao_confirmar(tela)           
        exibir_retangulo_com_borda(tela,(0,255,0),(705,90,520,520),3)
        exibir_botao_pausar(tela,tempo_parcial)
        exibir_retangulo_com_borda(tela,(0,255,0),(705,605,520,80),3)
        exibir_mensagem(tela,font2,(255,255,255),mensagem)
    if num == 6:
        nome_jogador = texto_digitado
        preencher_tela(tela,(0,0,100))
        if score < 30:
            texto_avalia ='Precisa melhorar!'
        elif score >= 30 and score <80:
            texto_avalia ='Regular!'
        elif score >=80:
            texto_avalia ='Excelente!' 
        exibir_texto(300,100,tela,font2,(255,255,255),'RESULTADO PARCIAL PARA O JOGADOR '+nome_jogador)                
        exibir_texto(400,200,tela,font2,(255,255,255),'Pontuação = '+str(score))                
        exibir_texto(400,250,tela,font2,(255,255,255),'Avaliação = '+texto_avalia+'  ')                
        exibir_texto(200,350,tela,font2,(255,255,255),'Deseja finalizar o jogo (Sim) ou avançar para o nível '+str(nivel+1)+ ' (Não)?')                
        if nivel < 5:
            exibir_botao(tela,200,500,200,85,15,font2,'       SIM')
            exibir_botao(tela,900,500,200,85,15,font2,'       NÃO')
        elif nivel == 5: botao = 6
    if num == 7:
        nome_jogador = texto_digitado
        ranking =[]
        acrescimo = 0
        preencher_tela(tela,(0,0,0))
        exibir_texto(550,50,tela,font2,(255,255,255),'R A N K I N G')                
        ranking = copiar_ranking(pasta,ranking)
        if lrank == 0: 
            adicionar_jog_rank(score,nome_jogador,ranking)
            ordenar_ranking(ranking)
        gravar_ranking(pasta,ranking)
        exibir_campeoes(tela,ranking)
        exibir_rank_completo(tela,ranking,indice_rank)
        exibir_botao(tela,450,550,67,65,10,font2,'  '+chr(60))
        exibir_botao(tela,790,550,67,65,10,font2,'  '+chr(62))
        exibir_botao(tela,1000,600,200,85,15,font2,'    Finalizar')
    if num == 8:
        preencher_tela(tela,(0,210,0))
        exibir_texto(550,100,tela,font2,(255,255,255),'CRÉDITOS')                
        exibir_texto(200,200,tela,font2,(255,255,255),'Música: Newer Wave by Kevin MacLeod via https://incompetech.com')                
        exibir_texto(200,300,tela,font2,(255,255,255),'Imagem: Estrada by Valentim (Valiphotos) via https:// pixabay.com')                
        exibir_texto(200,400,tela,font2,(255,255,255),'Imagem: Astronomia by Pexels via https:// pixabay.com')                
        i = 0
        while i < 5:
            pygame.display.update()
            time.sleep(1)
            i = i + 1
    if num == 9: 
        nome_jogador = texto_digitado
        exibir_background(tela,'image001.jpg')
        exibir_texto(400,300,tela,font1,(255,255,255),'Game Over')                
        exibir_texto(50,600,tela,font2,(255,255,255),'Muito obrigado por jogar Desafios Matemáticos!')                
        exibir_texto(800,600,tela,font2,(255,255,255),'Score: '+str(score))
        exibir_texto(800,650,tela,font2,(255,255,255),'Jogador: '+nome_jogador)                
        if score < 30: texto_avalia ='Precisa melhorar!'
        elif score >= 30 and score < 80: texto_avalia ='Regular!'
        elif score >=80: texto_avalia ='Excelente!' 
        exibir_texto(1000,600,tela,font2,(255,255,255),texto_avalia)                

def exibir_background(tela,imagem):
    background = pygame.image.load(imagem).convert()
    tela.blit(background, (0,0))

def preencher_tela(tela,cor):
    tela.fill(cor)
          
def exibir_texto(x,y,tela,fonte,cor,texto): 
    texto1 = fonte.render(texto, True, cor)
    tela.blit(texto1,(x,y))

def exibir_botao(tela,x,y,larg,altura,cmalt,fonte,texto):
    texto_b = fonte.render(texto, True, (255,255,255))
    pygame.draw.rect(tela,(255,255,255),(x, y,larg+2,altura)) 
    pygame.draw.rect(tela,(128,128,128),(x+2, y+2,larg-2,altura-4)) 
    tela.blit(texto_b, (x, y+cmalt))

def exibir_retangulo_cheio(tela,cor,dimensoes):
    pygame.draw.rect(tela,cor,dimensoes)    

def exibir_retangulo_com_borda(tela,cor,dimensoes,borda):
    pygame.draw.rect(tela,cor,dimensoes,borda)    

def exibir_botao_nivel(tela,fonte):
    j = 800
    for i in range(3):
        pygame.draw.rect(tela,(255,255,255),(j, 300,102,85)) 
        pygame.draw.rect(tela,(0,150,255),(j+2, 302,98,81)) 
        num1 = fonte.render(str(i+1), True, (255,255,255))
        tela.blit(num1, (j+40,320))
        j = j + 120
    j = 800    
    for i in range(2):
        pygame.draw.rect(tela,(255,255,255),(j, 400,102,85)) 
        pygame.draw.rect(tela,(0,150,255),(j+2, 402,98,81)) 
        num2 = fonte.render(str(i+4), True, (255,255,255))
        tela.blit(num2, (j+40,420))
        j = j + 120

def exibir_instrucoes(tela,mpasta,fontea,fonteb):
    instrucoes = ler_arquivo(mpasta,'instrucoes','txt')
    j = 50
    for i in range(8):
        a = instrucoes[i]; b = len(a)-1; a = a[0:b]; instrucoes[i] = a
        if i == 0: exibir_texto(50,j,tela,fontea,(255,255,255),instrucoes[i])
        else: exibir_texto(50,j,tela,fonteb,(255,255,255),instrucoes[i])
        j = j + 50

def exibir_questao(num,tela,npasta):
    if num < 10:
        img_questao = npasta+'\\questoes\\questao00'+str(num)+'.png'
    if (num >= 10) and (num <= 50):
        img_questao = npasta+'\\questoes\\questao0'+str(num)+'.png'
    exibir_imagem(tela,50,100,650,500,img_questao) 

def exibir_tempo(tela,tempo):
    if tempo < 0:
        tempo = 0
    time.sleep(1)
    exibir_texto(555,20,tela,font2,(255,255,255),str(tempo))                

def exibir_respostas(tela,pasta,num):
    global posicao_resposta
    respostas = ler_arquivo(pasta,'\\respostas\\respostas'+str(num),'txt')
    j = 100
    for i in range(5):
        pygame.draw.rect(tela,(255,255,255),(745, j,460,65)) 
        pygame.draw.rect(tela,(0,150,255),(750, j+5,450,55)) 
        a = respostas[i+1]; b = len(a)-1; a = a[0:b]; respostas[i+1] = a
        exibir_texto(770,j+5,tela,font3,(255,255,255),respostas[i+1]) 
        j = j + 80
    a = respostas[6]; b = len(a)-1; a = a[0:b]; respostas[6] = a
    exibir_texto(415,630,tela,font3,(255,255,255),respostas[6]) 
    a = respostas[7]; b = len(a)-1; a = a[0:b]; respostas[7] = a
    posicao_resposta = respostas[7]    

def exibir_botao_pausar(tela,tempo_parcial):
    if tempo_parcial == 0:
        exibir_botao(tela,730,620,160,50,3,font2,'   Pausar')
    elif tempo_parcial > 0:
        exibir_botao(tela,730,620,160,50,3,font2,' Continuar')

def exibir_botao_confirmar(tela):
    pygame.draw.rect(tela,(255,255,255),(745, 500,460,65)) 
    pygame.draw.rect(tela,(0,150,255),(750, 505,450,55))
    exibir_texto(770,505,tela,font2,(255,255,255),'                Confirmar')                

def exibir_mensagem(tela,fonte,cor,mens): 
    pygame.draw.rect(tela,(0,0,0),(900, 620,300,50)) 
    exibir_texto(850,620,tela,fonte,cor,'      '+mens)

def exibir_imagem(tela,x,y,larg,altura,imagem):
    img = pygame.image.load(imagem).convert()
    img = pygame.transform.scale(img, (larg,altura))
    tela.blit(img,(x,y))

def janela(x,y,tela,info1,info2,tempar):
    pygame.draw.rect(tela,(255,255,255),(x,y,600,200),1)
    pygame.draw.rect(tela,(0,255,255),(x+1,y+1,599,199))
    texto_info1 = font4.render(info1, True, (0,0,0))
    texto_info2 = font4.render(info2, True, (0,0,0))
    tela.blit(texto_info1, (x+10, y+10))
    tela.blit(texto_info2, (x+10, y+35))
    pygame.display.flip()
    pygame.time.delay(1000*tempar)

def exibir_campeoes(tela,ranking):
    xb_pos = 20
    yb_pos = 250
    for j in range(3):
        pygame.draw.rect(tela,(255,255,255),(xb_pos, yb_pos,402,85)) 
        pygame.draw.rect(tela,(128,128,128),(xb_pos+2, yb_pos+2,398,81))
        if j == 0:
            textorank = font2.render(ranking[j][4:]+'   '+ranking[j][0:3], True, (255,0,0))
        if j == 1:
            textorank = font2.render(ranking[j][4:]+'   '+ranking[j][0:3], True, (0,255,0))
        if j == 2:
            textorank = font2.render(ranking[j][4:]+'   '+ranking[j][0:3], True, (0,0,255))
        tela.blit(textorank, (xb_pos+50, yb_pos+15))
        xb_pos = xb_pos + 420
    texto2 = font3.render('OS TRÊS PRIMEIROS DO RANKING', True, (255,255,255))
    tela.blit(texto2,(450,150))

def exibir_rank_completo(tela,ranking,indice_rank):
    texto3 = font3.render('RANKING COMPLETO', True, (255,255,255))
    tela.blit(texto3,(150,450))
    pygame.draw.rect(tela,(255,255,255),(450, 440,402,65)) 
    texto4 = font3.render(ranking[indice_rank][4:]+'   '+ranking[indice_rank][0:3], True, (0,0,0))
    tela.blit(texto4,(500,450))

def exibir_50botoes(tela):
    i = 100
    qnum = 1
    while i < 1100:
        pygame.draw.rect(tela,(255,255,255),(i,200,50,85))
        pygame.draw.rect(tela,(0,150,255),(i,200,40,75)) 
        num = font2.render(str(qnum), True, (255,255,255))
        if qnum < 10:
            tela.blit(num, (i+10,210))
        elif qnum > 9:
            tela.blit(num, (i+5,210))    
        qnum =qnum + 1
        i = i + 50 
    i = 100
    qnum = 21
    while i < 1100:
        pygame.draw.rect(tela,(255,255,255),(i,350,50,85))
        pygame.draw.rect(tela,(0,150,255),(i,350,40,75)) 
        num = font2.render(str(qnum), True, (255,255,255))
        tela.blit(num, (i+5,360))    
        qnum =qnum + 1
        i = i + 50 
    i = 100
    qnum = 41
    while i < 600:
        pygame.draw.rect(tela,(255,255,255),(i,500,50,85))
        pygame.draw.rect(tela,(0,150,255),(i,500,40,75)) 
        num = font2.render(str(qnum), True, (255,255,255))
        tela.blit(num, (i+5,510))    
        qnum =qnum + 1
        i = i + 50 

# funções auxiliares

def ler_arquivo(npasta,nome,tipo):
    with open(npasta+'\\'+nome+'.'+tipo,'r', encoding='utf-8') as leitura:
        arq_lido = leitura.readlines()
        leitura.close()
    return arq_lido    

def gravar_arquivo(npasta,nome,tipo,nlista):
    with open(npasta+'\\'+nome+'.'+tipo,'w', encoding='utf-8') as gravado:
        for h in nlista:
            gravado.writelines(h+'\n')
        gravado.close() 

def tempo_inicial(pasta):
    global tempo, tempo_parcial
    tempo1 = ler_arquivo(pasta,'tempo','txt')
    tempo = int(tempo1[0])
    if tempo_parcial > 0:
        tempo = tempo_parcial
        tempo_parcial = 0
    return tempo    

def copiar_ranking(npasta,ranking):
    ranking = []
    ranking = ler_arquivo(npasta,'score','txt')
    c = len(ranking)
    for j in range(c):
        a = ranking[j]; b = len(a)-1; a = a[0:b]
        ranking[j] = a
    return ranking

def adicionar_jog_rank(score,nome_jogador,ranking):
    if score < 10:
        n1 = '00'+str(score)+' '+nome_jogador
    if score >= 10 and score < 100:
        n1 = '0'+str(score)+' '+nome_jogador
    if score >= 100:
        n1 = str(score)+' '+nome_jogador
    lr = len(ranking)    
    #ranking.append(n1) 
    ranking.insert(lr,n1)

def ordenar_ranking(ranking):
    ranking.sort(reverse=True)
    
def gravar_ranking(pasta,ranking):
    gravar_arquivo(pasta,'score','txt',ranking)

def obter_botao(botx):
    botx = botx + 1
    return botx

def obter_posicao_resposta():
    return posicao_resposta