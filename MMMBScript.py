import math


def main():
    lambdaa = int(input("Informe a taxa de chegada lambda: "))
    mu = int(input("Informe a taxa de serviço mu: "))
    m = int(input("Informe a quantidade de servidores:"))
    nb = int(input("Informe o numero de buffers:"))
    opcao = 0
    print("Resultado da B com M/M/10/10")
    while opcao != -1:
        opcao = int(input("O que deseja calcular: \n"
                          + "1 - Intensidade de trafego\n"
                          + "2 - Probabilidade de 0 jobs no sistema\n" 
                          + "3 - Probabilidade de n jobs no sistema\n"
                          + "4 - Numero medio de jobs no sistema\n"
                          + "5 - Numero medio de jobs na fila\n"
                          + "6 - Taxa de chegada efetiva\n"
                          + "7 - Utilizacao media por servidor\n"
                          + "8 - Tempo medio de Resposta\n"
                          + "9 - Tempo medio de espera na fila\n"
                          + "10 - Probabilidade de um sistema cheio\n" 
                          +"-1 sair"))
        match opcao:
            case 1:
                rho = calculaUtilizacao(lambdaa, mu, m)
                print("Intensidade de trafego: ", rho)
            case 2:
                p0 = calculaProbZeroJobs(lambdaa, mu, m, nb)
                print("Probabilidade de 0 jobs no sistema: ", p0)
            case 3:
                n = int(input("Informe o numero de jobs:"))
                pn = calculaProbNJobs(lambdaa, mu, m, n, nb)
                print("Probabilidade de ", n, " jobs no sistema: ", pn)
            case 4:
                en = calculaNumeroMedioJobs(lambdaa, mu, m, nb)
                print("Numero medio de jobs no sistema: ", en)
            case 5:
                enq = calculaNumeroMedioJobsFila(lambdaa, mu, m, nb)
                print("Numero medio de jobs na fila: ", enq)
            case 6:
                lambdal = calculaTaxaChegadaEfetiva(lambdaa, mu, m, nb)
                print("Taxa de chegada efetiva: ", lambdal)
            case 7:
                u = calculaUtilizacaoMediaServidor(lambdaa, mu, m, nb)
                print("Utilizacao media por servidor: ", u)
            case 8:
                t = calculaTempoMedioResposta(lambdaa, mu, m, nb)
                print("Tempo medio de Resposta: ", t)
            case 9:
                w = calculaTempoMedioEsperaFila(lambdaa, mu, m, nb)
                print("Tempo medio de espera na fila: ", w)
            case 10:
                pfull = calculaProbSistemaCheio(lambdaa, mu, m)
                print("Probabilidade de um sistema cheio: ", pfull)
            case 11:
                lr = calculaLossRate(lambdaa, mu, m, nb)
                print("Loss Rate: ", lr)
            case -1:
                print("Saindo...")

#Calcula a utilizacao do sistema
def calculaUtilizacao(lambdaa, mu, m):
    return lambdaa / (m * mu)

#Calcula probabilidade de 0 jobs no sistema
def calculaProbZeroJobs(lambdaa, mu, m, nb):
    rho = calculaUtilizacao(lambdaa, mu, m)
    somatorio = 0
    if m == 1:
        if rho != 1:
            return 1 - rho / 1 - rho ** (nb + 1)
        else:
            return 1 / (nb + 1)
            
    for i in range(m):
        somatorio += (m * rho) ** i / math.factorial(i)
    somatorio += (1-rho ** (nb - m + 1))*(m * rho) ** m / (math.factorial(m) * (1 - rho))
    return 1 / somatorio

#Calcula probabilidades de n jobs no sistema 
def calculaProbNJobs(lambdaa, mu, m, n, nb):
    rho = calculaUtilizacao(lambdaa, mu, m)
    p0 = calculaProbZeroJobs(lambdaa, mu, m, nb)
    if n >= 0 and n < m:
        return (((m * rho) ** n) / math.factorial(n))*p0
    if n >= m and n <= nb:
        return ((m ** m) * (rho ** n) / math.factorial(m))*p0

#Calcula numero medio de jobs no sistema
def calculaNumeroMedioJobs(lambdaa, mu, m, nb):
    rho = calculaUtilizacao(lambdaa, mu, m)
    if m == 1:
        en = (rho / (1 - rho) ) - (((nb + 1) * rho ** (nb + 1)) / (1 - rho ** (nb + 1)))
    else:
        somatorio = 0
        for i in range(1,nb+1):
            somatorio += i * calculaProbNJobs(lambdaa, mu, m, i, nb)
        en = somatorio
    return en

#Calcula quantidade de n jobs na fila
def calculaNumeroMedioJobsFila(lambdaa, mu, m, nb):
    rho = calculaUtilizacao(lambdaa, mu, m)
    if m == 1:
        enq = (rho / (1 - rho)) - (rho *  ((1 +(nb * ( rho ** (nb))))) / (1 - rho ** (nb + 1)))
    else:
        somatorio = 0
        for i in range(m+1,nb+1):
            somatorio += (i - m) * calculaProbNJobs(lambdaa, mu, m, i, nb)
        enq = somatorio
    return enq

#Calcula taxa de chegada efetiva
def calculaTaxaChegadaEfetiva(lambdaa, mu, m , nb):
    return lambdaa * (1 - calculaProbNJobs(lambdaa, mu, m, nb, nb))

#Calcula utilizacao media por servidor
def calculaUtilizacaoMediaServidor(lambdaa, mu, m, nb):
    u = calculaUtilizacao(lambdaa, mu, m)*(1 - calculaProbNJobs(lambdaa, mu, m, nb, nb))
    return u

#Calcula tempo medio de resposta
def calculaTempoMedioResposta(lambdaa, mu, m, nb):
    er = calculaNumeroMedioJobs(lambdaa, mu, m, nb) / calculaTaxaChegadaEfetiva(lambdaa, mu, m, nb) 
    return er

#Calcula tempo medio de espera na fila
def calculaTempoMedioEsperaFila(lambdaa, mu, m, nb):
    ew = calculaTempoMedioResposta(lambdaa, mu, m, nb) - (1 / mu)
    return ew

#Calcula Loss Rate
def calculaLossRate(lambdaa, mu, m, nb):
    pb = calculaProbNJobs(lambdaa, mu, m, nb, nb)
    lr = lambdaa*pb
    return lr
    

#Calcula probabilidade de um sistema cheio
def calculaProbSistemaCheio(lambdaa, mu, m):
    rho = calculaUtilizacao(lambdaa, mu, m)
    somatorio = 0
    for i in range(m):
        somatorio += (m * rho) ** i / math.factorial(i)
    pm = ((m * rho)/math.factorial(m))/somatorio
    return pm

if __name__ == "__main__":
    main()