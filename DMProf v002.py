# DMProf v001
# Autor: Paulo Fernando Costa da Cruz Data: 31/08/2024
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
import shutil
import webbrowser

# programa
#função main
def main():
    global ALTURA, a1, a2, a3, a4, a5, a6, a7, botao, cesp, clicado, copia, destino, etapa, font1, font2, font3, font4, font5, LARGURA, num_questao
    global num_resposta, origem, pasta, raiz, relogio, respostas, runing, tela, texto_digitacao
    pygame.init()
    a1 =''
    a2 =''
    a3 =''
    a4 =''
    a5 =''
    a6 =''
    a7 =''
    ALTURA = 720
    botao = 0
    cesp =''
    clicado = False
    copia =''
    destino =''
    etapa = 0
    font1 = pygame.font.SysFont('Arial', 120)
    font2 = pygame.font.SysFont('Arial',  40)
    font3 = pygame.font.SysFont('Arial',  30)
    font4 = pygame.font.SysFont('Arial',  20)
    font5 = pygame.font.SysFont('Arial', 18)
    LARGURA = 1280
    num_questao = 1
    num_resposta = 0
    origem =''
    pasta =''
    raiz=''
    respostas =[]
    texto_digitacao =''
    runing = True
    tela = pygame.display.set_mode((LARGURA, ALTURA))
    pygame.display.set_caption('DMProf versão 0.02     Autor: Paulo Fernando Costa da Cruz')
    relogio = pygame.time.Clock()
    relogio.tick(60)
    while runing:
        etapa = botao
        if etapa == 0:
           Tela(0)
           #Interusuario.guidmprof(tela,0)
           pygame.mouse.set_visible(True)
        if etapa == 1:
           Tela(1)
           #Interusuario.guidmprof(tela,1)
        if etapa == 2:
           Tela(2)
           #Interusuario.guidmprof(tela,2)
        if etapa == 3:
           Tela(3)
           #Interusuario.guidmprof(tela,3)
        if etapa == 4:
            Tela(4)
            #Interusuario.guidmprof(tela,4)  
        if etapa == 5:
            Tela(5)  
        if etapa == 6:
            Tela(6)  
        if etapa == 7:
            Tela(7) 
        if etapa == 8:
            Tela(8)             
        if etapa == 9:
           Tela(9)
        for event in pygame.event.get():
            if event.type == QUIT:
                runing = False
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if etapa == 8:
                    if num_resposta == 1:
                        a1 = a1 + Digitar2(event)
                        if event.key == K_BACKSPACE:
                            a1 = a1[:-1]
                    if num_resposta == 2:
                        a2 = a2 + Digitar2(event) 
                        if event.key == K_BACKSPACE:
                            a2 = a2[:-1]
                    if num_resposta == 3:
                        a3 = a3 + Digitar2(event) 
                        if event.key == K_BACKSPACE:
                            a3 = a3[:-1]
                    if num_resposta == 4:
                        a4 = a4 + Digitar2(event) 
                        if event.key == K_BACKSPACE:
                            a4 = a4[:-1]
                    if num_resposta == 5:
                        a5 = a5 + Digitar2(event)
                        if event.key == K_BACKSPACE:
                            a5 = a5[:-1]
                    if num_resposta == 6:
                        a6 = a6 + Digitar2(event) 
                        if event.key == K_BACKSPACE:
                            a6 = a6[:-1]
                    if num_resposta == 7:
                        a7 = a7+ Digitar2(event) 
                        if event.key == K_BACKSPACE:
                            a7 = a7[:-1]
            if event.type == MOUSEBUTTONDOWN:
                mousex, mousey = event.pos
                if etapa == 0:
                    if mousex >= 550 and mousex <= 750:
                        if mousey >= 550 and mousey <=635:
                            clicado = Clicar_Botao(mousex,mousey,550,550,200,85,15,'      Iniciar')
                            if clicado == True:
                                botao = 1
                if etapa == 1:
                    if mousex >= 550 and mousex <= 750:
                        if mousey >= 550 and mousey <=635:
                            clicado = Clicar_Botao(mousex,mousey,550,550,200,85,15,'     Avançar')
                            if clicado == True:
                                botao = 2
                if etapa == 2:
                    if mousex >= 250 and mousex <= 450:
                        if mousey >= 550 and mousey <=635:
                            clicado = Clicar_Botao(mousex,mousey,250,550,200,85,15,'     Manual')
                            if clicado == True:
                                Janela(200,200,tela,'Você vai visualizar o manual do jogo.','O manual está no formato pdf e pode ser impresso.',3)
                                Ver_manual()
                    if mousex >= 850 and mousex <= 1050:
                        if mousey >= 550 and mousey <=635:
                            clicado = Clicar_Botao(mousex,mousey,850,550,200,85,15,'     Avançar')
                            if clicado == True:
                                botao = 3
                if etapa == 3:
                    if mousex >= 50 and mousex <= 290:
                        if mousey >= 200 and mousey <=285:
                            clicado = Clicar_Botao(mousex,mousey,50,200,240,85,15,'  Manter o jogo')
                            if clicado == True:
                                Janela(400,200,tela,'Você optou por não alterar o jogo do professor.','O programa vai encerrar.',3)
                                botao = 9 
                    if mousex >= 500 and mousex <= 740:
                        if mousey >= 200 and mousey <=285:
                            clicado = Clicar_Botao(mousex,mousey,500,200,240,85,15,' Backup do jogo')
                            if clicado == True:
                                Janela(400,300,tela,'Você optou por fazer o backup do jogo do professor.',' ',1)
                                Fazer_backup()
                    if mousex >= 500 and mousex <= 740:
                        if mousey >= 350 and mousey <=435:
                            clicado = Clicar_Botao(mousex,mousey,500,350,240,85,15,'     Restaurar')
                            if clicado == True:
                                Janela(400,100,tela,'Você optou por restaurar o jogo do professor.','do backup.',1)
                                Restaurar_backup()
                    if mousex >= 950 and mousex <= 1190:
                        if mousey >= 200 and mousey <=285:
                            clicado = Clicar_Botao(mousex,mousey,950,200,240,85,15,'   Alterar o jogo')
                            if clicado == True:
                                botao = 4
                if etapa == 4:
                    if mousex >= 50 and mousex <= 350:
                        if mousey >= 350 and mousey <= 435:
                            clicado = Clicar_Botao(mousex,mousey,50,350,300,85,15,'   Alterar instruções')  
                            if clicado == True:
                                Alterar_instrucoes()
                    if mousex >= 500 and mousex <= 800:
                        if mousey >= 350 and mousey <= 435:
                            clicado = Clicar_Botao(mousex,mousey,500,350,300,85,15,'    Alterar Tempo')
                            if clicado == True: 
                                Alterar_tempo_resposta()  
                    if mousex >= 900 and mousex <= 1200:
                        if mousey >= 350 and mousey <= 435:
                            clicado = Clicar_Botao(mousex,mousey,900,350,300,85,15,'   Alterar Questões') 
                            if clicado == True:
                                botao = 5  
                if etapa == 5:
                    if mousex >= 100 and mousey <= 1100:
                        if mousey >= 200 and mousey <= 585:
                            clicado = Clicar_50botoes(mousex,mousey)
                            if clicado == True: 
                                botao = 6
                    if mousex >= 800 and mousex <= 1100:
                        if mousey >= 600 and mousey <= 685:
                            clicado = Clicar_Botao(mousex,mousey,800,600,300,85,15,'          Finalizar') 
                            if clicado == True:
                                botao = 9  
                if etapa == 6:
                    if mousex >= 900 and mousey <= 1200:
                        if mousey >= 100 and mousey <= 185:
                            clicado = Clicar_Botao(mousex,mousey,900,100,300,85,15,'  Procure na internet')
                            if clicado == True:
                                Janela(600,100,tela,'Procure nova imagem na internet e salve no computador. Em seguida converta','para o tipo *.png, renomeie para "questao(número)" e copie',5)
                                Procurar_internet()
                    if mousex >= 900 and mousey <= 1200:
                        if mousey >= 200 and mousey <= 285:
                            clicado = Clicar_Botao(mousex,mousey,900,200,300,85,15,'     Computador')
                            if clicado == True:
                                Janela(600,100,tela,'Procure nova imagem no seu computador.','converta para *.png, renomeie para "questao(número)" e copie',5)
                                Procurar_computador()
                    if mousex >= 900 and mousey <= 1200:
                        if mousey >= 300 and mousey <= 385:
                            clicado = Clicar_Botao(mousex,mousey,900,300,300,85,15,'    Substituir (*.png)')
                            if clicado == True:
                                Janela(600,200,tela,'Cole a nova imagem na pasta do jogo do professor.',' ',2)
                                Procurar_jogo_professor_questoes()
                    if mousex >= 900 and mousey <= 1200:
                        if mousey >= 400 and mousey <= 485:
                            clicado = Clicar_Botao(mousex,mousey,900,400,300,85,15,'       Respostas')
                            if clicado == True:
                                botao = 7
                    if mousex >= 900 and mousey <= 1200:
                        if mousey >= 500 and mousey <= 585:
                            clicado = Clicar_Botao(mousex,mousey,900,500,300,85,15,'            Voltar')
                            if clicado == True:
                                botao = 5
                if etapa == 7:
                    if mousex >= 950 and mousex <= 1250:
                        if mousey >= 300 and mousey <= 385:    
                            clicado = Clicar_Botao(mousex,mousey,900,300,300,85,15,'           Editor')
                            if clicado == True:
                                botao = 8
                    if mousex >= 950 and mousey <= 1250:
                        if mousey >= 400 and mousey <= 485:
                            clicado = Clicar_Botao(mousex,mousey,950,400,300,85,15,'           Alterar')
                            if clicado == True:
                                Janela(600,200,tela,'Use o bloco de notas para alterar as respostas . Conteúdo das respostas: 00,','5 respostas (máx. 25 caracteres), conceito, número da questão correta',6)
                                Alterar_respostas()
                    if mousex >= 950 and mousex <= 1250:
                        if mousey >= 500 and mousey <= 585:    
                            clicado = Clicar_Botao(mousex,mousey,900,500,300,85,15,'            Voltar')
                            if clicado == True:
                                botao = 5
                if etapa == 8:
                    if mousex >= 950 and mousex <= 1250:
                        if mousey >= 300 and mousey <= 385:    
                            clicado = Clicar_Botao(mousex,mousey,950,300,300,85,15,'         Editar > '+str(num_resposta))
                            if clicado == True:
                                num_resposta = num_resposta + 1
                                if num_resposta > 7:
                                    num_resposta = 1
                                Janela(600,200,tela,'Edite a resposta '+str(num_resposta),' ',2)
                    if mousex >= 950 and mousex <= 1250:
                        if mousey >= 400 and mousey <= 485:    
                            if num_resposta == 1:
                                a1 = a1 + Clicar_Btn_Cesp(mousex,mousey)
                            elif num_resposta == 2:
                                a2 = a2 + Clicar_Btn_Cesp(mousex,mousey)  
                            elif num_resposta == 3:
                                a3 = a3 + Clicar_Btn_Cesp(mousex,mousey)
                            elif num_resposta == 4:
                                a4 = a4 + Clicar_Btn_Cesp(mousex,mousey)
                            elif num_resposta == 5:
                                a5 = a5 + Clicar_Btn_Cesp(mousex,mousey)
                            elif num_resposta == 6:
                                a6 = a6 + Clicar_Btn_Cesp(mousex,mousey)
                            elif num_resposta == 7:
                                a7 = a7 + Clicar_Btn_Cesp(mousex,mousey)                             
                    if mousex >= 950 and mousex <= 1250:
                        if mousey >= 500 and mousey <= 585:    
                            clicado = Clicar_Botao(mousex,mousey,950,500,300,85,15,'            Salvar')
                            if clicado == True:
                                Salvar_Respostas(num_questao)
                    if mousex >= 950 and mousex <= 1250:
                        if mousey >= 600 and mousey <= 685:    
                            clicado = Clicar_Botao(mousex,mousey,950,600,300,85,15,'            Voltar')
                            if clicado == True:
                                botao = 5


        pygame.display.update()

def Tela(num):
        if num == 0:
            Preencher_Tela((150,128,128))  
            Exibir_Texto(200,100,tela,font1,(255,255,255),'Módulo do Professor')                
            Exibir_Texto(50,250,tela,font1,(255,255,255),'Jogo Desafios Matemáticos')                
            Exibir_Texto(300,450,tela,font3,(255,255,255),'Jogo Educacional Digital de Avaliação. Módulo para customização do jogo')                
            Exibir_Botao(550,550,200,85,15,'      Iniciar')
        if num == 1:
            Preencher_Tela((150,128,128))  
            Exibir_Texto(450,50,tela,font2,(255,255,255),'Explicações gerais sobre o jogo')                
            Exibir_Texto(50,150,tela,font3,(255,255,255),'Este jogo é uma ferramenta de avaliação. O estudante será submetido a uma avaliação na qual ele será')                
            Exibir_Texto(50,200,tela,font3,(255,255,255),'intensamente exposto à visualzação matemática, ou seja, ao uso da visualização matemática para       a')                
            Exibir_Texto(50,250,tela,font3,(255,255,255),'compreensão da matemática. jogo é um quiz com 5 níveis de dificuldade, cada um com 10 questões.   O')                
            Exibir_Texto(50,300,tela,font3,(255,255,255),'professor pode usar a versão de demonstração que serve para alunos do último ano do ensino fundamen-')                
            Exibir_Texto(50,350,tela,font3,(255,255,255),'tal e do ensino médio ou pode customizar o jogo por meio deste módulo, mudando instruções,   questões,')                
            Exibir_Texto(50,400,tela,font3,(255,255,255),'respostas e o tempo para responder cada questão em segundos.')                
            Exibir_Texto(50,450,tela,font3,(255,255,255),'')                
            Exibir_Texto(50,500,tela,font3,(255,255,255),'')                
            Exibir_Botao(550,550,200,85,15,'     Avançar')
        if num == 2:
            Preencher_Tela((150,128,128))  
            Exibir_Texto(450,50,tela,font2,(255,255,255),'Instruções gerais sobre este módulo')                
            Exibir_Texto(50,150,tela,font3,(255,255,255),'Existem duas versões do jogo: a de demostração e a do professor. Este módulo permite a  customização')                
            Exibir_Texto(50,200,tela,font3,(255,255,255),'do jogo do professor. Você pode mudar as instruções, questões (imagens) e as repostas para        cada')                
            Exibir_Texto(50,250,tela,font3,(255,255,255),'questão e o tempo para responder uma questão.')                
            Exibir_Texto(50,300,tela,font3,(255,255,255),'Caso deseje manter o jogo do professor como está clique no botão "Manter" na próxima tela e o programa')                
            Exibir_Texto(50,350,tela,font3,(255,255,255),'será encerrado. Caso deseje alterar o jogo do professor faça primeiro um backup do jogo atual e    depois')                
            Exibir_Texto(50,400,tela,font3,(255,255,255),'clique no botão "Alterar" para iniciar as alterações nas instruções, questões (imagens) e respostas.')                
            Exibir_Texto(50,450,tela,font3,(255,255,255),'Boa Sorte!')                
            Exibir_Botao(250,550,200,85,15,'     Manual')
            Exibir_Botao(850,550,200,85,15,'     Avançar')
        if num == 3:    
            Preencher_Tela((0,0,0))  
            Exibir_Texto(400,30,tela,font2,(255,255,255),'Jogo do professor - Escolher opções')                
            Exibir_Texto(250,500,tela,font3,(255,255,255),'Escolha entre manter o jogo do professor ou fazer backup e alterações ')                
            Exibir_Botao(50,200,240,85,15,'  Manter o jogo')
            Exibir_Botao(500,200,240,85,15,' Backup do jogo')
            Exibir_Botao(500,350,240,85,15,'     Restaurar')
            Exibir_Botao(950,200,240,85,15,'   Alterar o jogo')
        if num == 4:
            Preencher_Tela((0,0,0))  
            Exibir_Texto(400,30,tela,font2,(255,255,255),'Jogo do professor - Alterações')                
            Exibir_Texto(50,100,tela,font2,(255,255,255),'Instruções  ')
            Exibir_Imagem(50,150,150,75,'image003.png')
            Exibir_Texto(500,100,tela,font2,(255,255,255),'Questões  ')
            Exibir_Imagem(500,150,150,75,'image004.png')
            Exibir_Texto(900,100,tela,font2,(255,255,255),'Respostas')
            Exibir_Imagem(900,150,150,75,'image005.png')
            Exibir_Botao(50,350,300,85,15,'   Alterar instruções')
            Exibir_Texto(50,500,tela,font4,(255,255,255),'Use o bloco de notas para alterar as instruções do jogo ')
            Exibir_Texto(50,525,tela,font4,(255,255,255),'Texto com no máximo  8 linhas. Não esqueça de salvar')
            Exibir_Texto(500,500,tela,font4,(255,255,255),'Use o bloco de notas para alterar')
            Exibir_Texto(500,525,tela,font4,(255,255,255),'o tempo para responder uma questão.')
            Exibir_Texto(850,500,tela,font4,(255,255,255),'Também use o bloco de notas para alterar as respostas.')
            Exibir_Texto(850,525,tela,font4,(255,255,255),'Conteúdo: 00, 5 repostas (20 caracteres), Conceito,')
            Exibir_Texto(850,550,tela,font4,(255,255,255),'número da resposta correta. Use o explorer')
            Exibir_Texto(850,575,tela,font4,(255,255,255),'para substituir as imagens')
            Exibir_Botao(500,350,300,85,15,'    Alterar Tempo')
            Exibir_Botao(900,350,300,85,15,'   Alterar Questões')
        if num == 5:
            Preencher_Tela((0,0,0))
            Exibir_Texto(200,30,tela,font2,(255,255,255),'Jogo do professor - Alterar questões (imagens) e respostas')                
            Exibir_Texto(200,100,tela,font3,(255,255,255),'Clique no botão numerado para alterar a questão e respostas correspondentes')                
            Exibir_50botoes()
            Exibir_Botao(800,600,300,85,15,'          Finalizar')
        if num == 6:
            Preencher_Tela((0,0,0))
            Exibir_Texto(230,50,tela,font2,(255,255,255),'Questão (gráfico)  '+str(num_questao))                
            Exibir_Questao(num_questao)
            Exibir_Texto(50,625,tela,font4,(255,255,255),'Use somente imagens do tipo *.png. Converta  antes a imagem que estiver em outro formato. Dimensã0 650x500 pixels.')                
            Exibir_Texto(50,650,tela,font4,(255,255,255),'Renomeie a nova imagem para "questao(numero)" e copie para a pasta \jogo do professor\questoes')                
            Exibir_Botao(900,100,300,85,15,'  Procure na internet')
            Exibir_Botao(900,200,300,85,15,'     Computador')
            Exibir_Botao(900,300,300,85,15,'    Substituir (*.png)')
            Exibir_Botao(900,400,300,85,15,'       Respostas')
            Exibir_Botao(900,500,300,85,15,'            Voltar')
        if num == 7:
            Preencher_Tela((0,0,0))
            Exibir_Texto(50,50,tela,font2,(255,255,255),'Respostas para a questão '+str(num_questao))                
            Exibir_Texto(530,50,tela,font2,(255,255,255),'Conceito ')                
            Exibir_Texto(530,200,tela,font2,(255,255,255),'Num. da resposta correta ')                
            Exibir_Texto(50,650,tela,font4,(255,255,255),'Use o bloco de notas ou o editor para alterar as respostas. Não esqueça de salvar.')                
            Exibir_Respostas(num_questao)
            Exibir_Botao(950,300,300,85,15,'           Editor')
            Exibir_Botao(950,400,300,85,15,' Alterar(bl. de notas)')
            Exibir_Botao(950,500,300,85,15,'            Voltar')
        if num == 8:
            Preencher_Tela((0,0,0))
            Exibir_Texto(400,30,tela,font2,(255,255,255),'Edite as respostas da questão '+str(num_questao))                
            pygame.draw.rect(tela,(255,255,255),(250, 100,400,75)) 
            Exibir_Texto(20,120,tela,font2,(255,255,255),'Resposta 1') 
            Exibir_Texto(260,120,tela,font2,(0,0,0),a1) 
            pygame.draw.rect(tela,(255,255,255),(250, 200,400,75)) 
            Exibir_Texto(20,220,tela,font2,(255,255,255),'Resposta 2') 
            Exibir_Texto(260,220,tela,font2,(0,0,0),a2) 
            pygame.draw.rect(tela,(255,255,255),(250, 300,400,75)) 
            Exibir_Texto(20,320,tela,font2,(255,255,255),'Resposta 3') 
            Exibir_Texto(260,320,tela,font2,(0,0,0),a3) 
            pygame.draw.rect(tela,(255,255,255),(250, 400,400,75)) 
            Exibir_Texto(20,420,tela,font2,(255,255,255),'Resposta 4') 
            Exibir_Texto(260,420,tela,font2,(0,0,0),a4) 
            pygame.draw.rect(tela,(255,255,255),(250, 500,400,75)) 
            Exibir_Texto(20,520,tela,font2,(255,255,255),'Resposta 5') 
            Exibir_Texto(260,520,tela,font2,(0,0,0),a5) 
            pygame.draw.rect(tela,(255,255,255),(850, 100,400,75)) 
            Exibir_Texto(700,120,tela,font2,(255,255,255),'Conceito') 
            Exibir_Texto(860,120,tela,font2,(0,0,0),a6) 
            pygame.draw.rect(tela,(255,255,255),(850, 200,400,75)) 
            Exibir_Texto(700,220,tela,font2,(255,255,255),'Número') 
            Exibir_Texto(860,220,tela,font2,(0,0,0),a7) 
            Exibir_Botao(950,300,300,85,15,'         Editar > '+str(num_resposta))
            Exibir_Btn_Cesp()
            Exibir_Botao(950,500,300,85,15,'            Salvar')
            Exibir_Botao(950,600,300,85,15,'            Voltar')
        if num == 9:
            Preencher_Tela((150,128,128))  
            Exibir_Texto(200,100,tela,font1,(255,255,255),'Módulo do Professor')                
            Exibir_Texto(500,250,tela,font1,(255,255,255),'F  I  M')                
            Exibir_Texto(300,450,tela,font3,(255,255,255),'Jogo Educacional Digital de Avaliação. Módulo para customização do jogo')                
    
def Preencher_Tela(cor):
    tela.fill(cor)
          
def Exibir_Texto(x,y,tela,fonte,cor,texto): 
    texto1 = fonte.render(texto, True, cor)
    tela.blit(texto1,(x,y))

def Exibir_Imagem(x,y,larg,altura,imagem):
    img = pygame.image.load(imagem).convert()
    img = pygame.transform.scale(img, (larg,altura))
    tela.blit(img,(x,y))

def Exibir_Botao(x,y,larg,altura,cmalt,texto):
    texto_b = font2.render(texto, True, (255,255,255))
    pygame.draw.rect(tela,(255,255,255),(x, y,larg+2,altura)) 
    pygame.draw.rect(tela,(128,128,128),(x+2, y+2,larg-2,altura-4)) 
    tela.blit(texto_b, (x, y+cmalt))

def Clicar_Botao(xm,ym,x,y,larg,altura,cmalt,texto):
    ret_externo = pygame.draw.rect(tela,(255,255,255),(x, y,larg+2,altura)) 
    if ret_externo.collidepoint(xm,ym):
        texto_b = font2.render(texto, True, (0,0,0))
        pygame.draw.rect(tela,(255,255,0),(x+2, y+2,larg-2,altura-4),0,5) 
        tela.blit(texto_b, (x, y+cmalt))
        som = pygame.mixer.Sound('mouse-click-104737.mp3')
        som.play()
        pygame.time.delay(150)
        return True

def Exibir_50botoes():
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

def Clicar_50botoes(xm_pos,ym_pos):
    global  num_questao
    if ym_pos > 200 and ym_pos < 285:
        if xm_pos > 100 and xm_pos < 1100: 
            num_questao = int((xm_pos - 100)/50) + 1     
    if ym_pos > 350 and ym_pos < 435:
        if xm_pos > 100 and xm_pos < 1100: 
            num_questao = int((xm_pos - 100)/50) + 21     
    if ym_pos > 500 and ym_pos < 585:
        if xm_pos > 100 and xm_pos < 600: 
            num_questao = int((xm_pos - 100)/50) + 41 
    return True

def Exibir_Btn_Cesp():
    i = 950
    while i < 1250:
        pygame.draw.rect(tela,(255,255,255),(i,400,50,85))
        pygame.draw.rect(tela,(128,128,128),(i+2,402,46,81)) 
        if i == 950:
            texto = font2.render('\u00b6', True, (255,255,255))
            tela.blit(texto, (i+20,410))
        elif i == 1000:
            texto = font2.render('\u00b2', True, (255,255,255))
            tela.blit(texto, (i+20,410))
        elif i == 1050:
            texto = font2.render('\u00b3', True, (255,255,255))
            tela.blit(texto, (i+20,410))
        elif i == 1100:
            texto = font2.render('\u00b1', True, (255,255,255))
            tela.blit(texto, (i+20,410))
        elif i == 1150:
            texto = font2.render('\u221a', True, (255,255,255))
            tela.blit(texto, (i+20,410))
        elif i == 1200:
            texto = font2.render('\u00f8', True, (255,255,255))
            tela.blit(texto, (i+15,410))
        i = i + 50 

def Clicar_Btn_Cesp(xm_pos,ym_pos):
    global a1, a2, a3, a4, a5, a6, a7, cesp
    if ym_pos >= 400 and ym_pos <= 485:
        if xm_pos >= 950 and xm_pos < 1000: 
            cesp = '\u00b6'
        if xm_pos >= 1000 and xm_pos < 1050: 
            cesp = '\u00b2'
        if xm_pos >= 1050 and xm_pos < 1100: 
            cesp = '\u00b3'
        if xm_pos >= 1100 and xm_pos < 1150: 
            cesp = '\u00b1'
        if xm_pos >= 1150 and xm_pos < 1200: 
            cesp = '\u221a'
        if xm_pos >= 1200 and xm_pos < 1250: 
            cesp = '\u00f8'
        return cesp    
             
def Exibir_questao(num):
    global origem, raiz          
    raiz = os.getcwd()
    if num < 10:
        origem = raiz +'\\jogo do professor\\questoes\\questao00'+str(num)+'.png'
        os.system('explorer.exe '+raiz +'\\jogo do professor\\questoes')
    if num > 9:
        origem = raiz +'\\jogo do professor\\questoes\\questao0'+str(num)+'.png'
        os.system('explorer.exe '+raiz +'\\jogo do professor\\questoes')
     
def Ver_manual():
    global origem, raiz
    raiz = os.getcwd()
    origem = raiz +'\\Manual do jogo'+'.pdf'
    os.startfile(origem)

def Janela(x,y,tela,info1,info2,tempar):
    pygame.draw.rect(tela,(255,255,255),(x,y,600,200),1)
    pygame.draw.rect(tela,(0,255,255),(x+1,y+1,599,199))
    texto_info1 = font4.render(info1, True, (0,0,0))
    texto_info2 = font4.render(info2, True, (0,0,0))
    tela.blit(texto_info1, (x+10, y+10))
    tela.blit(texto_info2, (x+10, y+35))
    pygame.display.flip()
    pygame.time.delay(1000*tempar)

def Fazer_backup():  
    global destino, origem, raiz        
    raiz = os.getcwd()
    origem = raiz +'\\jogo do professor'
    destino = raiz +'\\backup'
    if os.path.exists(destino):
        shutil.rmtree(destino)
    arqgrav = shutil.copytree(origem, destino)
    Exibir_Texto(50,600,tela,font5,(255,255,255),'Backup do jogo do professor realizado com sucesso na pasta '+ destino) 
    Exibir_Texto(200,625,tela,font5,(255,255,255),'Inicie as alterações.') 
    pygame.display.flip()
    pygame.time.delay(4000)
      
def Restaurar_backup():
    global copia, destino, origem, raiz          
    raiz = os.getcwd()
    origem = raiz +'\\jogo do professor'
    copia =  raiz +'\\jogo do professor_copia'
    destino = raiz +'\\backup'
    if os.path.exists(origem):
        if not os.path.exists(copia):
            arqgrav1 = shutil.copytree(origem, copia)
    if os.path.exists(destino):
        if os.path.exists(origem):
            shutil.rmtree(origem)
        arqgrav2 = shutil.copytree(destino, origem)
    Exibir_Texto(450,600,tela,font5,(255,255,255),'Restauração do jogo do professor com sucesso ') 
    pygame.display.flip()
    pygame.time.delay(4000)

def Alterar_instrucoes():
    global origem, raiz      
    raiz = os.getcwd()
    origem = raiz +'\\jogo do professor\\instrucoes.txt'
    os.startfile(origem)
    
def Alterar_tempo_resposta():
    global origem, raiz      
    raiz = os.getcwd()
    origem = raiz +'\\jogo do professor\\tempo.txt'
    os.startfile(origem)

def Exibir_Questao(num):
    global pasta, raiz
    raiz = os.getcwd()
    pasta = raiz +'\\jogo do professor'
    if num < 10:
        img_questao = pasta+'\\questoes\\questao00'+str(num)+'.png'
    if (num >= 10) and (num <= 50):
        img_questao = pasta+'\\questoes\\questao0'+str(num)+'.png'
    Exibir_Imagem(50,100,650,500,img_questao) 

def Procurar_internet():
    webbrowser.open('http://www.google.com')

def Procurar_computador():
    os.system('explorer.exe '+'C:\\')

def Procurar_jogo_professor_questoes():
    os.system('explorer.exe '+raiz +'\\jogo do professor\\questoes')    

def Exibir_Respostas(num):
    global a1, a2, a3, a4, a5, a6, a7, pasta, respostas, raiz
    pygame.draw.rect(tela,(255,255,255),(45, 100,460,85)) 
    pygame.draw.rect(tela,(255,255,255),(45, 200,460,85)) 
    pygame.draw.rect(tela,(255,255,255),(45, 300,460,85)) 
    pygame.draw.rect(tela,(255,255,255),(45, 400,460,85)) 
    pygame.draw.rect(tela,(255,255,255),(45, 500,460,85)) 
    pygame.draw.rect(tela,(0,150,255),(50, 105,450,75)) 
    pygame.draw.rect(tela,(0,150,255),(50, 205,450,75)) 
    pygame.draw.rect(tela,(0,150,255),(50, 305,450,75)) 
    pygame.draw.rect(tela,(0,150,255),(50, 405,450,75)) 
    pygame.draw.rect(tela,(0,150,255),(50, 505,450,75))
    pygame.draw.rect(tela,(255,255,255),(530, 100,360,85)) 
    pygame.draw.rect(tela,(255,255,255),(530, 250,360,85)) 
    pygame.draw.rect(tela,(0,150,255),(535, 105,350,75)) 
    pygame.draw.rect(tela,(0,150,255),(535, 255,350,75)) 
    Ler_Respostas(num)    
    a1 = respostas[1]; b = len(a1)-1; a1 = a1[0:b]
    a2 = respostas[2]; b = len(a2)-1; a2 = a2[0:b] 
    a3 = respostas[3]; b = len(a3)-1; a3 = a3[0:b]
    a4 = respostas[4]; b = len(a4)-1; a4 = a4[0:b] 
    a5 = respostas[5]; b = len(a5)-1; a5 = a5[0:b]
    a6 = respostas[6]; b = len(a6)-1; a6 = a6[0:b]
    a7 = respostas[7]; b = len(a7)-1; a7 = a7[0:b]
    resp1 = font3.render(a1, True, (255,255,255))
    resp2 = font3.render(a2, True, (255,255,255))
    resp3 = font3.render(a3, True, (255,255,255))
    resp4 = font3.render(a4, True, (255,255,255))
    resp5 = font3.render(a5, True, (255,255,255))
    resp6 = font3.render(a6, True, (255,255,255))
    resp7 = font3.render(a7, True, (255,255,255))
    tela.blit(resp1, (60,105))
    tela.blit(resp2, (60,205))
    tela.blit(resp3, (60,305))
    tela.blit(resp4, (60,405))
    tela.blit(resp5, (60,505))
    tela.blit(resp6,(540,105))
    tela.blit(resp7,(540,255))
    texto_conceito = font2.render('Conceito: '+a6, True, (255,255,255))
    pygame.draw.rect(tela,(0,0,0),(330, 10,320,50)) 
    tela.blit(texto_conceito,(50,10))
    
def Ler_Respostas(numero):
    global pasta, respostas, raiz
    raiz = os.getcwd()
    pasta = raiz +'\\jogo do professor'
    respostas = []
    with open(pasta+'\\respostas\\respostas'+str(numero)+'.txt','r', encoding='utf-8') as arquivo:
        respostas = arquivo.readlines()
        arquivo.close()

def Alterar_respostas():
    global origem, raiz
    raiz = os.getcwd()
    origem = raiz +'\\jogo do professor\\respostas\\respostas'+str(num_questao)+'.txt'
    os.startfile(origem)

def Digitar(x,y,evento,texto):  
    global texto_digitacao
    texto_digitacao = texto
    if evento.type == KEYDOWN:
        if evento.key == K_BACKSPACE:
            if len(texto_digitacao) > 0:
                texto_digitacao = texto_digitacao[:-1]
        else:
            texto_digitacao = texto_digitacao + evento.unicode
        Exibir_Texto(x,y,tela,font2,(0,0,0),texto_digitacao) 
        pygame.time.delay(600)

def Digitar2(evento):
    Ch = evento.unicode
    if evento.key == K_BACKSPACE:
        Ch=''
    if evento.key == K_KP_ENTER:
        Ch=''
    return Ch

def Salvar_Respostas(numero):
    global pasta, respostas, raiz
    raiz = os.getcwd()
    pasta = raiz +'\\jogo do professor'
    respostas[0] ='00'
    respostas[1] = a1
    respostas[2] = a2
    respostas[3] = a3
    respostas[4] = a4
    respostas[5] = a5
    respostas[6] = a6
    respostas[7] = a7
    with open(pasta+'\\respostas\\respostas'+str(numero)+'.txt','w', encoding='utf-8') as arquivo:
        for h in respostas:
            arquivo.writelines(h+'\n')
        arquivo.close()

if __name__ == "__main__":
    main()  
