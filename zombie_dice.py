#Aluna Rafaela Souza Plachta, Curso GTI

#Introdução.
print ("Jogo ZOMBIE DICE (V2) \n")

#Iniciando a interação com o usuário:
print ("Seja bem-vindo(a) ao jogo ZOMBIE DICE!!! \n")

numero = int(input("Informe o número de jogadores: "))
#Informando a regra ao jogador caso ele digite menos de dois jogadores:
while True:
    if (numero < 2):
        numero = int(input("Informe pelo menos  2 jogadores: "))
    else:
        break
#Solicitando o nome de cada jogador de acordo com a quantidade de jogadorese imprimindo na tela:
lista_jogador = []
for i in range(numero):
    nome = input("Digite o nome do jogador: ")
    lista_jogador.append(nome)

for key, value in enumerate(lista_jogador):
    print("\nJogador", key, value)

print("\nOk! Vamos lá %s! Iniciando o jogo..." % ',' ' '.join(lista_jogador).upper())

jogador_atual = lista_jogador[0]
print("\nO jogador da rodada é: ", jogador_atual.upper())

#Importando o arquivo com as funções criadas para o jogo.
import func_z_dice
func_z_dice.turno()

jogador_atual = lista_jogador[0 + 1]
print("\nO jogador da rodada é: ", jogador_atual.upper())
#Chamando a function turno novamente para continuação do jogo com o próximo jogador:
func_z_dice.turno()

