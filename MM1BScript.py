#Para calcular utilização

def utilizacao(lambdaa, mu):
    rho = lambdaa/mu
    return rho

#Para calcular a probabilidade de 0 jobs no sistema
def calculaP0(rho, nB):
    if(rho == 1):
        p0 = 1/(nB + 1)
    else:
        p0 = (1 - rho)/(1 - pow(rho, nB + 1))
    return p0
#Para calcular a probabilidade de n jobs no sistema
def calculaPn(rho, nB , n):
    if(n > nB):
        return 0
    else:
        if(rho == 1):
            pn = 1/(nB + 1)
        else:
            pn = calculaP0(rho, nB) * pow(rho, n)
    return pn

#Para calcular o numero medio de jobs no sistema
def calculaEn(rho,nB,n):
    en = rho/(1-rho) - (nB + 1) * pow(rho, nB + 1)/(1 - pow(rho, nB + 1))
    return en

#Para calcular o numero medio de jobs na fila
def calculaEnq(rho,nB,n):
    enq = rho/(1-rho) - rho*(1 + nB * pow(rho, nB))/(1 - pow(rho, nB + 1))
    return enq

#Para calcular a taxa de chegada efetiva
def calculaLambdaLinha(lambdaa, nB, rho):
    lambdal = lambdaa * (1 - calculaPn(rho, nB, nB))
    return lambdal

#Para calcular o tempo medio de resposta
def calculaEr(lambdal, nB,rho):
    er = calculaEnq(rho, nB, nB)/lambdal
    return er

#Para calcular o tempo medio de espera
def calculaEw(er, mu):
    ew = er - (1/mu)
    return ew

def main():
    #parametros
    lambdaa = int(input("Informe a taxa de chegada lambda ")) #taxa de chegada
    mu = int(input("Informe a taxa de servico mu ")) #taxa de serviço
    nB = int(input("Informe o numero de buffers B ")) #numero de buffers 
    opcao = 0

    while(opcao != -1):
        opcao = int(input("Informe o que você deseja calcular:\n" 
            + "1 - Utilização\n"
            + "2 - Probabilidade de 0 jobs no sistema P0\n"
            + "3 - Probabilidade de n jobs no sistema Pn\n"
            + "4 - Número médio de jobs no sistema En\n"
            + "5 - Número médio de jobs na fila Enq\n"
            + "6 - Taxa de chegada efetiva λ'\n"
            + "7 - Tempo médio de resposta Er\n"
            + "8 - Tempo médio de espera Ew\n"
            + "-1 - Sair\n"))
        match opcao:
            case 1:
                rho = utilizacao(lambdaa, mu)
                print(rho)
            case 2:
                rho = utilizacao(lambdaa, mu)
                p0 = calculaP0(rho, nB)
                print(p0)
            case 3:
                rho = utilizacao(lambdaa, mu)
                n = int(input("Informe o valor de n: "))
                pn = calculaPn(rho, nB, n)
                print(pn)
            case 4:
                rho = utilizacao(lambdaa, mu)
                n = int(input("Informe o valor de n: "))
                en = calculaEn(rho, nB, n)
                print(en)
            case 5:
                rho = utilizacao(lambdaa, mu)
                n = int(input("Informe o valor de n: "))
                enq = calculaEnq(rho, nB, n)
                print(enq)
            case 6:
                rho = utilizacao(lambdaa, mu)
                lambdal = calculaLambdaLinha(lambdaa, nB, rho)
                print(lambdal)
            case 7:
                rho = utilizacao(lambdaa, mu)
                lambdal = calculaLambdaLinha(lambdaa, nB, rho)
                er = calculaEr(lambdal, nB, rho)
                print(er)
            case 8:
                rho = utilizacao(lambdaa, mu)
                lambdal = calculaLambdaLinha(lambdaa, nB, rho)
                er = calculaEr(lambdal, nB, rho)
                ew = calculaEw(er, mu)
                print(ew)
            case -1:
                print("Saindo...")
            case _:
                print("Opção inválida")

if __name__ == "__main__":
    main()
