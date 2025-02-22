# Jogo Desafios matematicos v003
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
import Interusuario
import DMUtil
import Eventos

# programa
#função main
def main():
    global ALTURA, botao, clicado, continuar, destino, demonstracao, etapa, font1, font2, font3, font4, font5 
    global indice_rank, LARGURA, lrank, mensagem, nome_jogador, num_questao, nivel, num_resposta, origem, pasta
    global posicao_resposta, raiz, ranking, relogio, respostas, runing, score, tela, tempo, tempo_parcial, texto_digitado
    pygame.init()
    ALTURA = 720
    botao = 0
    clicado = False
    continuar = 0
    destino =''
    demonstracao = 1
    etapa = 0
    font1 = pygame.font.SysFont('Arial', 120)
    font2 = pygame.font.SysFont('Arial',  40)
    font3 = pygame.font.SysFont('Arial',  30)
    font4 = pygame.font.SysFont('Arial',  20)
    font5 = pygame.font.SysFont('Arial', 18)
    indice_rank = 0
    LARGURA = 1280
    lrank = 0
    mensagem =''
    nome_jogador =''
    num_questao = 1
    nivel = 1
    num_resposta = 0
    origem =''
    pasta =''
    posicao_resposta =''
    raiz = os.getcwd()
    ranking = []
    respostas =[]
    tempo = 60
    tempo_parcial = 0
    texto_digitado =''
    runing = True
    score = 0
    tela = pygame.display.set_mode((LARGURA, ALTURA))
    pygame.display.set_caption('Desafios Matemáticos versão 0.03     Autor: Paulo Fernando Costa da Cruz')
    relogio = pygame.time.Clock()
    relogio.tick(60)
    while runing: # loop de eventos
        etapa = botao
        if etapa >= 0 and etapa <= 4:
            Interusuario.guidm(tela,etapa,pasta,score,texto_digitado,nivel,num_questao,tempo,tempo_parcial,ranking,lrank,indice_rank)
        elif etapa == 5: 
            Interusuario.guidm(tela,5,pasta,score,texto_digitado,nivel,num_questao,tempo,tempo_parcial,ranking,lrank,indice_rank)
            posicao_resposta = Interusuario.obter_posicao_resposta()
        elif etapa == 6:
            Interusuario.guidm(tela,6,pasta,score,texto_digitado,nivel,num_questao,tempo,tempo_parcial,ranking,lrank,indice_rank)
        elif etapa == 7: 
            Interusuario.guidm(tela,7,pasta,score,texto_digitado,nivel,num_questao,tempo,tempo_parcial,ranking,lrank,indice_rank)
            lrank = 1
        elif etapa == 8:
            Interusuario.guidm(tela,8,pasta,score,texto_digitado,nivel,num_questao,tempo,tempo_parcial,ranking,lrank,indice_rank)
            botao = Interusuario.obter_botao(etapa)
        elif etapa == 9:
            Interusuario.guidm(tela,9,pasta,score,texto_digitado,nivel,num_questao,tempo,tempo_parcial,ranking,lrank,indice_rank)
        pygame.mouse.set_visible(True)
        for event in pygame.event.get():
            if event.type == QUIT:
                Evento(1,0,0,0)
            if event.type == KEYDOWN:
                Evento(2,2,event,texto_digitado)
            if event.type == MOUSEBUTTONDOWN:
                mousex, mousey = event.pos
                if etapa == 0: Evento(3,0,mousex,mousey)
                if etapa == 1: Evento(4,1,mousex,mousey)
                if etapa == 2: Evento(5,2,mousex,mousey)
                if etapa == 3: Evento(6,3,mousex,mousey)
                if etapa == 4: Evento(7,4,mousex,mousey)
                if etapa == 5: Evento(8,5,mousex,mousey)
                if etapa == 6: Evento(9,6,mousex,mousey)
                if etapa == 7: Evento(10,7,mousex,mousey)
        if tempo_parcial == 0:
            tempo = tempo - 1
        elif tempo_parcial > 0:
            tempo = tempo_parcial            
        pygame.display.update()

def Evento(acao,par1,par2,par3):
    global botao, clicado, demonstracao, indice_rank, nivel, nome_jogador, pasta, num_questao, score, tempo, tempo_parcial, texto_digitado, raiz
    if acao == 1:
        Eventos.fechar_programa()
    if acao == 2:
        texto_digitado = Eventos.digitar(par1,par2,par3)
    if acao == 3:
        if par2 >= 550 and par2 <= 750:
            if par3 >= 550 and par3 <=635:
                clicado = Eventos.clicar_botao(tela,par2,par3,550,550,200,85,15,'      Iniciar')
                if clicado == True:
                    botao = 1
    if acao == 4:
        if par2 >= 550 and par2 <= 750:
            if par3 >= 550 and par3 <=635:
                clicado = Eventos.clicar_botao(tela,par2,par3,550,550,200,85,15,'     Avançar')
                if clicado == True:
                    botao = 2
    if acao == 5:
        if par2 >= 250 and par2 <= 450:
            if par3 >= 550 and par3 <=635:
                clicado = Eventos.clicar_botao(tela,par2,par3,250,550,200,85,15,'     Manual')
                if clicado == True:
                    Eventos.janela(200,200,tela,'Você vai visualizar o manual do jogo.','O manual está no formato pdf e pode ser impresso.',2)
                    DMUtil.ver_manual(origem,raiz)
        if par2 >= 850 and par2 <= 1050:
            if par3 >= 550 and par3 <=635:
                clicado = Eventos.clicar_botao(tela,par2,par3,850,550,200,85,15,'     Avançar')
                if clicado == True:
                    nome_jogador = texto_digitado
                    botao = 3
    if acao == 6:
        if par2 >= 50 and par2 <= 450:
            if par3 >= 200 and par3 <= 285:
                clicado = Eventos.clicar_botao(tela,par2,par3,50,200,400,85,5,'     Jogo Demonstraçao')
                if clicado == True:
                    Eventos.janela(200,200,tela,'Você escolheu o jogo de demonstração.','Este jogo não pode ser modificado',2)
                    demonstracao = 1
                    if demonstracao == 1:
                        raiz = os.getcwd()
                        pasta = raiz + '\\demonstracao'
        if par2 >= 50 and par2 <= 450:
            if par3 >= 500 and par3 <= 585:
                clicado = Eventos.clicar_botao(tela,par2,par3,50,500,400,85,5,'     Jogo do Professor')
                if clicado == True:
                    Eventos.janela(200,200,tela,'Você escolheu o jogo elaborado pelo professor.','Este jogo pode ser modificado.',2)
                    demonstracao = 0
                    if demonstracao == 0:
                        raiz = os.getcwd()
                        pasta = raiz + '\\jogo do professor'
        if par2 >= 800 and par2 <= 1142:
            if par3 >= 300 and par3 <= 485:
                clicado = Eventos.clicar_botao_nivel(tela,par2,par3,800,300,342,185)
                if clicado == True:
                    nivel = Eventos.valor_nivel()
                    num_questao = Eventos.valor_num_questao()
                    tempo = Eventos.tempo_inicial(pasta)
                    Eventos.janela(400,100,tela,'Você selecionou o  nível '+str(nivel),' ',1)
        if par2 >= 550 and par2 <= 750:
            if par3 >= 600 and par3 <= 685:
                clicado = Eventos.clicar_botao(tela,par2,par3,550,600,200,85,15,'     Avançar')
                if clicado == True:
                    botao = 4
    if acao == 7:
        if par2 >= 550 and par2 <= 750:
            if par3 >= 550 and par3 <= 635:
                clicado = Eventos.clicar_botao(tela,par2,par3,550,550,200,85,15,'     Avançar') 
                if clicado == True:
                    tempo = Eventos.tempo_inicial(pasta)
                    botao = 5  
    if acao == 8:
        if par2 >= 750 and par2 <= 1210:
            if par3 >= 100 and par3 <= 485:
                clicado = Eventos.clicar_resposta()
                if clicado == True:
                    num_resposta = Eventos.selecionar_reposta(tela,pasta,par2,par3,num_questao)
                    Eventos.janela(100,500,tela,'Confirme ou escolha outra opção de resposta.',' ',1)
            if par3 >= 500 and par3 <= 565:
                clicado = Eventos.clicar_botao_confirmar(tela,par2,par3)
                if clicado == True:
                    score,tempo = Eventos.comparar_resposta(tela,num_questao,pasta,tempo,score)
                    num_questao = num_questao + 1
                    if nivel == 1 and num_questao <= 10:
                        botao = 5 
                    elif nivel == 1 and num_questao > 10:
                        botao = 6   
                    if nivel == 2 and num_questao <= 20:
                        botao = 5
                    elif nivel == 2 and num_questao > 20:
                        botao = 6    
                    if nivel == 3 and num_questao <= 30:
                        botao = 5
                    elif nivel == 3 and num_questao > 30:
                        botao = 6    
                    if nivel == 4 and num_questao <= 40:
                        botao = 5
                    elif nivel == 4 and num_questao > 40:
                        botao = 6    
                    if nivel == 5 and num_questao <= 50:
                        botao = 5
                    elif nivel == 5 and num_questao > 50:
                        DMUtil.tocar_musica()
                        botao = 7    
        if par2 >= 730 and par2 <= 890:
            if par3 >= 620 and par3 <= 670:
                clicado = Eventos.clicar_botao_pausar(tela,par2,par3) 
                if clicado == True:
                    if tempo_parcial == 0:
                        tempo_parcial = tempo
                    elif tempo_parcial > 0:
                        tempo = tempo_parcial   
                        tempo_parcial = 0
    if acao == 9:
        if par2 >= 200 and par2 <= 402:
           if par3 >= 500 and par3 <= 585:
                clicado = Eventos.clicar_botao(tela,par2,par3,200,500,200,85,15,'       SIM')
                if clicado == True:
                    DMUtil.tocar_musica()
                    botao = 7
        if par2 >= 900 and par2 < 1102:
            if par3 > 500 and par3 < 585:
                clicado = Eventos.clicar_botao(tela,par2,par3,900,500,200,85,15,'       NÃO')
                if clicado == True:
                    tempo = Eventos.tempo_inicial(pasta)
                    nivel = nivel + 1
                    botao = 5
    if acao == 10:
        ranking=[]
        ranking = Interusuario.copiar_ranking(pasta,ranking)
        if par2 >= 450 and par2 <= 517:
            if par3 >= 550 and par3 <= 615:
                clicado = Eventos.clicar_botao(tela,par2,par3,450,550,67,65,10,'  '+chr(60))
                if clicado == True:
                    if indice_rank > 0:
                        indice_rank = indice_rank - 1
                        Interusuario.exibir_texto(500,450,tela,font3,(0,0,0),ranking[indice_rank][4:]+'   '+ranking[indice_rank][0:3])               
        if par2 >= 790 and par2 <= 857:
            if par3 >= 550 and par3 <= 615:
                clicado = Eventos.clicar_botao(tela,par2,par3,790,550,67,65,10,'  '+chr(62))
                if clicado == True:
                    indice_rank = indice_rank + 1
                    if indice_rank >= len(ranking):
                        indice_rank = 0
                        Interusuario.exibir_texto(500,450,tela,font3,(0,0,0),ranking[indice_rank][4:]+'   '+ranking[indice_rank][0:3])                
        if par2 >= 1000 and par2 <= 1200:
            if par3 >= 600 and par3 <= 685:
                clicado = Eventos.clicar_botao(tela,par2,par3,1000,600,200,85,15,'    Finalizar')
                if clicado == True:
                    botao = 8
   
if __name__ == "__main__":
    main() 
