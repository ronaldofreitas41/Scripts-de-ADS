import math
    
def main():
    lambdaa = int(input("Informe a taxa de chegada lambda: "))
    mu = int(input("Informe a taxa de serviço mu: "))
    m = int(input("Informe a quantidade de servidores:"))

    opcao = 0
    while opcao != -1:
        opcao = int(input("O que deseja calcular: \n"
                            + "1 - Intensidade de trafego\n"
                            + "2 - Probabilidade de 0 jobs no sistema\n"
                            + "3 - Probabilidade de n jobs no sistema\n"
                            + "4 - Probabilidade de gerar uma fila\n"
                            + "5 - Numero medio de jobs no sistema\n"
                            + "6 - Varianca do numero de jobs no sistema\n"
                            + "7 - Numero medio de jobs na fila\n"
                            + "8 - Varianca do numero de jobs na fila\n"
                            + "9 - Utilizacao media por servidor\n"
                            + "10 - Distribuicao cumulativa do tempo de resposta\n"
                            + "11 - Tempo medio de resposta\n"
                            + "12 - Varianca do tempo de resposta\n"
                            + "13 - Distribuicao cumulativa do tempo de espera\n"
                            + "14 - Tempo medio de espera na fila\n"
                            + "15 - Varianca do tempo de espera\n"
                            + "16 - Q-percentual do tempo de resposta\n"
                            + "17 - 90-percentual do tempo de resposta\n"
                            +"-1 sair"))
        match opcao:
            case 1:
                rho = calculaUtilizacao(lambdaa, mu, m)
                print("Intensidade de trafego: ", rho)
            case 2:
                p0 = calculaProbZeroJobs(lambdaa, mu, m)
                print("Probabilidade de 0 jobs no sistema: ", p0)
            case 3:
                n = int(input("Informe a quantidade de jobs no sistema: "))
                pn = calculaProbNJobs(lambdaa, mu, m, n)
                print("Probabilidade de ", n, " jobs no sistema: ", pn)
            case 4:
                vr = calculaQueueing(lambdaa, mu, m)
                print("Probabilidade de gerar uma fila: ", vr)
            case 5:
                en = calculaNumeroMedioJobs(lambdaa, mu, m)
                print("Numero medio de jobs no sistema: ", en)
            case 6:
                var = calculaVariancaNumeroJobs(lambdaa, mu, m)
                print("Varianca do numero de jobs no sistema: ", var)
            case 7:
                enq = calculaNumeroMedioJobsFila(lambdaa, mu, m)
                print("Numero medio de jobs na fila: ", enq)
            case 8:
                varnq = calculaVariancaNumeroJobsFila(lambdaa, mu, m)
                print("Varianca do numero de jobs na fila: ", varnq)
            case 9:
                us = calculaUtilizacaoMediaServidor(lambdaa, mu, m)
                print("Utilizacao media por servidor: ", us)
            case 10:
                r = int(input("Informe o tempo de resposta: "))
                fr = calculaFr(lambdaa, mu, m, r)
                print("Distribuicao cumulativa do tempo de resposta: ", fr)
            case 11:
                er = calculaTempoMedioResposta(lambdaa, mu, m)
                print("Tempo medio de resposta: ", er)
            case 12:
                varer = calculaVariancaTempoResposta(lambdaa, mu, m)
                print("Varianca do tempo de resposta: ", varer)
            case 13:
                w = int(input("Informe o tempo de espera: "))
                fw = calculaFrEspera(lambdaa, mu, m, w)
                print("Distribuicao cumulativa do tempo de espera: ", fw)
            case 14:
                ew = calculaTempoMedioEspera(lambdaa, mu, m)
                print("Tempo medio de espera na fila: ", ew)
            case 15:
                varw = calculaVariancaTempoEspera(lambdaa, mu, m)
                print("Varianca do tempo de espera: ", varw)
            case 16:
                q = int(input("Informe o q-percentual: "))
                qr = calculaQr(lambdaa, mu, m, q)
                print("Q-percentual do tempo de resposta: ", qr)
            case 17:
                qr90 = calculaQr90(lambdaa, mu, m)
                print("90-percentual do tempo de resposta: ", qr90)
            case -1:
                print("Saindo...")
                
#Calcula a utilizacao do sistema 1
def calculaUtilizacao(lambdaa, mu, m):
    return lambdaa / (m * mu)

#Calcula a probabilidade de 0 jobs no sistema 2
def calculaProbZeroJobs(lambdaa, mu, m):
    rho = calculaUtilizacao(lambdaa, mu, m)
    somatorio = 0
    for n in range(m):
        somatorio += (((rho*m) ** n) / math.factorial(n)) 
    somatorio += 1 + (m*rho) ** m / math.factorial(m) * ((1 - rho))
    return 1 / somatorio

#Calcula a probabilidade de n jobs no sistema  3  
def calculaProbNJobs(lambdaa, mu, m, n):
    rho = calculaUtilizacao(lambdaa, mu, m)
    p0 = calculaProbZeroJobs(lambdaa, mu, m)
    if n < m:
        return p0 * ((m*rho) ** n) / math.factorial(n)
    else:
        return p0 * (m ** m)(rho ** n) / math.factorial(m)

#Probabilida de de gerar uma fila 4
def calculaQueueing(lambdaa, mu, m):
    rho = calculaUtilizacao(lambdaa, mu, m)
    p0 = calculaProbZeroJobs(lambdaa, mu, m)
    varrho = ((m * rho)**m )
    varrho = varrho / (math.factorial(m) * (1 - rho))
    varrho = p0 * varrho
    return varrho

#Calcula o numero medio de jobs no sistema 5
def calculaNumeroMedioJobs(lambdaa, mu, m):
    rho = calculaUtilizacao(lambdaa, mu, m)
    vr = calculaQueueing(lambdaa, mu, m)
    en = (m*rho) + ((rho*vr)/(1-rho))
    return en

#Variança do numero de jobs no sistema 6
def calculaVariancaNumeroJobs(lambdaa, mu, m):
    rho = calculaUtilizacao(lambdaa, mu, m)
    vr = calculaQueueing(lambdaa, mu, m)
    var = m*rho + ((rho*vr)*((1+rho-(rho*vr)/(1-rho)**2)+m))
    return var

#Calcula o numero medio de jobs na fila 7
def calculaNumeroMedioJobsFila(lambdaa, mu, m):
    rho = calculaUtilizacao(lambdaa, mu, m)
    vr = calculaQueueing(lambdaa, mu, m)
    enq = rho * vr / (1 - rho)
    return enq

#Calcula a varaiança do numero de jobs na fila 8
def calculaVariancaNumeroJobsFila(lambdaa, mu, m):
    rho = calculaUtilizacao(lambdaa, mu, m)
    vr = calculaQueueing(lambdaa, mu, m)
    varnq = vr * rho(1+rho-(rho*vr)/(1-rho)**2)
    return varnq

#Calcula a utilizacao media por servidor 9
def calculaUtilizacaoMediaServidor(lambdaa, mu, m):
    rho = calculaUtilizacao(lambdaa, mu, m)
    return rho

# Calcula distribuição cumulativa do tempo de resposta 10
def calculaFr(lambdaa, mu, m, r):
    rho = calculaUtilizacao(lambdaa, mu, m)
    p0 = calculaProbZeroJobs(lambdaa, mu, m)
    vr = calculaQueueing(lambdaa, mu, m)
    y = (m-1)/m
    if y != rho:
        return 1 - math.e(-mu * r) - ((vr/(1-m+(m*rho))) * math.e(-m * mu *(1-rho)) - math.e(-mu * r))
    else:
        return 1 - math.e(-mu * r) - (vr * mu * r * math.e(-mu * r))

#Calcula o tempo medio de resposta 11
def calculaTempoMedioResposta(lambdaa, mu, m):
    rho = calculaUtilizacao(lambdaa, mu, m)
    vr = calculaQueueing(lambdaa, mu, m)
    er = (1/mu) * (1 + (vr/(m*(1-rho))))
    return er

#Calcula varianca do tempo de resposta 12
def calculaVariancaTempoResposta(lambdaa, mu, m):
    rho = calculaUtilizacao(lambdaa, mu, m)
    vr = calculaQueueing(lambdaa, mu, m)
    varer = (1/(mu**2)) * (1 + ((vr * (2 - vr))/((m**2)*((1-rho)**2))))
    return varer

#Calcula distribuição cumulativa do tempo de espera 13
def calculaFrEspera(lambdaa, mu, m, w):
    rho = calculaUtilizacao(lambdaa, mu, m)
    vr = calculaQueueing(lambdaa, mu, m)
    fw = 1 - (vr* math.e(-m*mu*(1-rho)*w))
    return fw

#Calcula tempo medio de espera na fila 14
def calculaTempoMedioEspera(lambdaa, mu, m):
    rho = calculaUtilizacao(lambdaa, mu, m)
    vr = calculaQueueing(lambdaa, mu, m)
    ew = (vr/(m*mu*(1-rho)))
    return ew

#Calcula varianca do tempo de espera 15
def calculaVariancaTempoEspera(lambdaa, mu, m):
    rho = calculaUtilizacao(lambdaa, mu, m)
    vr = calculaQueueing(lambdaa, mu, m)
    varw = vr*(2 - vr)/(((m**2) * (mu**2)*(1-rho)**2))
    return varw

#Calcula q-percentual do tempo de resposta 16
def calculaQr(lambdaa, mu, m, q):
    ew = calculaTempoMedioEspera(lambdaa, mu, m)
    vr = calculaQueueing(lambdaa, mu, m)
    qr = math.max(0, (ew/vr)*math.log((100*vr)/(100 - q)))
    return qr

#Calcula 90-percentual do tempo de resposta 17
def calculaQr90(lambdaa, mu, m):
    
    ew = calculaTempoMedioEspera(lambdaa, mu, m)
    vr = calculaQueueing(lambdaa, mu, m)
    qr90 = (ew/vr)*math.log(10*vr)
    return qr90

if __name__ == "__main__":
    main()