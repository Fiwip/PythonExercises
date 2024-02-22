# -*- coding: latin-1 -*-
from exc115v3.arquivo import *


"""
    Nesse programa ser� mostrado um menu com tr�s op��es do que fazer, na op��o de ver as pessoas, ir� mostrar as
cadastradas, na op��o de cadastrar uma nova ir� pedir o nome e a idade ela ser� adicionada, e na op��o de sair,
ir� sair do sistema, contudo, os dados continuar�o salvos mesmo depois que encerrar o programa.
    O c�digo foi feito como o �ltimo projeto do curso de Python at� ent�o, tentei fazer com que o programa n�o desse 
erro independente do que a pessoa que estivesse executando fizesse. :)
"""


# Criando o arquivo de texto para caso ele n�o exista
arq = 'cursoemvideo.txt'
if not arquivo_existe(arq):
    criar_arquivo(arq)


def geral():
    """
    -> Fun��o que faz o loop do menu e que ativa as respectivas fun��es
    :return: Tudo aquilo que � para mostrar no programa
    """
    while True:
        # Mostrando o menu principal personalizado
        mostra_menu(["Ver pessoas cadastradas", "Cadastrar uma nova pessoa", "Sair do sistema"])
        op = valida_opt()
        if op == 1:
            # Mostrando as pessoas cadastradas
            mostra_pessoas()
        if op == 2:
            # Adicionando uma nova pessoa
            novo_cadastro()
        if op == 3:
            # Finalizando o programa
            lin('VOLTE SEMPRE!')
            break


geral()
