#Importando a biblioteca random:
import random
#Declarando as variáveis que irão vigorar como globais no programa:
copo = []
dado_verde = ("CPCTPC")
dado_amarelo = ("TPCTPC")
dado_vermelho = ("TPTCPT")
cerebro = 0
tiro = 0
passos = 0

#Função sem parâmetros, retorna a lista que mostra os dados(respectivas faces) dentro do copo:
def dados_no_copo():
    copo = []
    i = 0
    while (i < 6):
        copo.append(dado_verde)
        i += 1

    i = 0
    while (i < 4):
        copo.append(dado_amarelo)
        i += 1

    i = 0
    while (i < 3):
        copo.append(dado_vermelho)
        i += 1
        return copo

print ("\nConferindo os dados dentro do copo: %s" %',' ' '.join(dados_no_copo()))

#Função que realiza a tarefa de lançar os dados, indicando a cor e face sorteadas. Mostra a pontuação ao final de cada lançamento de dados:
def lancar_dados():
    print("\nLançando os dados...\n")
    copo = dados_no_copo()
    #Usando a instrução "global" para alterar as variáveis globais:
    global cerebro
    cerebro = 0
    global tiro
    tiro = 0
    global passos
    passos = 0


    sorteio = random.randint(0, len(copo)-1)
    dado_sorteado = copo[sorteio]

    if (dado_sorteado == "CPCTPC"):
        print("Dado sorteado: verde!!!")
        copo.remove("CPCTPC")

        sorteio_face = random.randint(0, 5)
#        print(sorteio_face)
        face = dado_verde[sorteio_face]
#        print(face)
        if (face == "P"):
            print("Face: Passos!")
            passos += 1

        if (face == "C"):
            print("Face: Cérebro!")
            cerebro += 1

        if (face == "T"):
            print("Face: Tiro!")
            tiro += 1

    if (dado_sorteado == "TPCTPC"):
        print("Dado sorteado: amarelo!!!")
        copo.remove("TPCTPC")

        sorteio_face = random.randint(0, 5)
#        print(sorteio_face)
        face = dado_amarelo[sorteio_face]
#        print(face)
        if (face == "P"):
            print("Face: Passos!")
            passos += 1

        if (face == "C"):
            print("Face: Cérebro!")
            cerebro += 1

        if (face == "T"):
            print("Face: Tiro!")
            tiro += 1

    if (dado_sorteado == "TPTCPT"):
        print("Dado sorteado: vermelho!!!")
        copo.remove("TPTCPT")

        sorteio_face = random.randint(0, 5)
#        print(sorteio_face)
        face = dado_vermelho[sorteio_face]
#        print(face)
        if (face == "P"):
            print("Face: Passos!")
            passos += 1

        if (face == "C"):
            print("Face: Cérebro!")
            cerebro += 1

        if (face == "T"):
            print("Face: Tiro!")
            tiro += 1

    print ("\nConferindo os dados dentro do copo: %s" %',' ' '.join(copo))
#Pontuação usando tuplas:
    print("\nPontuação:")
    pontos = (cerebro, passos, tiro,)
    faces = ("Cérebro= ", "Tiro= ", "Passos= ",)
    for face, pontos in zip(faces,pontos):
        print (face, pontos)



#Função que interage com o usuário verificando se este deseja continuar lançando os dados:
def jogar_novamente():
    joga_novamente = int(input("Deseja jogar os dados novamente? Digite 1para continuar e 2 para encerrar: "))
    if (joga_novamente == 1):
        turno()
    if (joga_novamente == 2):
        print ("\nIniciando rodada com novo jogador...")

#Função que executa a sequencia das principais  funções do jogo:
def turno():
    dados_no_copo()
    lancar_dados()
    jogar_novamente()

