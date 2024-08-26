#parametros de entrada
import math


#intensidade de trafego 1
def calculaRho(lambdaa, mu):
    rho = lambdaa/mu
    return rho

#probabilidade de 0 jobs no sistema 2
def calculaP0(rho):
    p0 = 1 - rho
    return p0

#probabilidade de n jobs no sistema 3
def calculaPn(rho, n):
    p0 = calculaP0(rho)
    pN = p0 * pow(rho,n)
    return pN

#calcula numero medio de jobs no sistema 4
def calculaEn(rho):
    en = rho/(1-rho)
    return en

#Calcula Variançca do numero de jobs no sistema 5
def calculaVar(rho):
    var = rho/(1-pow(rho,2))
    return var

#Calcula a probabilidade de k jobs na fila 6
def calculaPk(rho, k):
    p0 = calculaP0(rho)
    if k == 0:
        return 1 - rho**2
    else:
        pk = p0 * pow(rho,k+1)
        return pk

#Calcula o numero medio de jobs na fila 7
def calculaEnq(rho):
    enq = rho**2/(1-rho)    
    return enq

#Calcula a Varianca do numero de jobs na fila 8
def calculaVarnq(rho):
    Vnq = (rho**2)*(1+rho-rho**2)/(1-rho)**2
    return Vnq

#Calcula Distribuição Acumulada do tempo de resposta 9
def calculaFr(mu,rho,r):
    fr = 1 - math.e**(-r*mu*(1-rho))
    return fr

#Calcula tempo medio de resposta 10
def calculaEr(mu,rho):
    er = (1/mu)/(1-rho)
    return er

#Calcula a variancia do tempo de resposta 11
def calculaVarEr(mu,rho):
    varEr = (1/(mu**2))/(1-rho)**2
    return varEr

#Calcula a q-Percentual do tempo de resposta 12
def calculaQr(mu,rho,q):
    qr = calculaEr(mu,rho)*math.log(100/100-q)
    return qr

#Calcula 90-Percentual do tempo de resposta 13
def calculaQr90(mu,rho):
    qr90 = calculaEr(mu,rho)*2.3
    return qr90

#Calcula Distribuição Acumulada do tempo de espera 14
def calculaFw(mu,rho,w):
    fw = 1 - math.e**(-w*mu*rho)
    return fw

#Calcula tempo medio de espera 15
def calculaEw(mu,rho):
    ew = rho*((1/mu)/(1-rho))
    return ew

#Calcula a variancia do tempo de espera 16 
def calculaVarEw(mu,rho):
    varEw = ((2 - rho)*rho)/(mu**2 * (1-rho)**2)
    return varEw

#Calcula a probabilidade de encontrar n ou mais jobs no sistema 17
def calculaPnMais(rho,n):
    pnMais = rho**(n+1)
    return pnMais

# #Calcula a probalilidade de atender n jobs no periodo ocupado 18
# def calculaPnAtendidos(rho,n):
#     pnAtendidos = (1-rho)*rho**n
#     return pnAtendidos

#Calcula o numero medio de jobs atendidos no periodo ocupado 19
def calculaEnAtendidos(rho):
    enAtendidos = 1/(1-rho)
    return enAtendidos

#Calcula a variancia do numero de jobs atendidos no periodo ocupado 20
def calculaVarEnAtendidos(rho):
    varEnAtendidos = (rho*(1+rho))/(1-rho)**3
    return varEnAtendidos

#calcula media da duração do perioodo ocupado 21
def calculaDuracaoOcupado(mu,rho):
    duracaoOcupado = 1/(mu*(1-rho))
    return duracaoOcupado

#Calcula variancia da duração do periodo ocupado 22
def calculaVarDuracaoOcupado(mu,rho):
    varDuracaoOcupado = 1/(mu**2*(1-rho)**3) - 1/(mu**2*(1-rho)**2)
    return varDuracaoOcupado

#calcula 90-percentual do tempo de espera 23
def CalculaQw90(mu,rho):
    qw90 = calculaEw(mu,rho)*math.log(10*rho)
    return qw90

def main():
    opcao = 0
    mu = float(input("Informe o valor de mu: "))
    lambdaa = float(input("Informe o valor de lambda: "))
    rho = calculaRho(lambdaa, mu)
       
    while opcao != -1:
        opcao = int(input("Informe o que você deseja calcular:\n" 
            + "1 - Utilização\n"
            + "2 - Probabilidade de 0 jobs no sistema P0\n"
            + "3 - Probabilidade de n jobs no sistema Pn\n"
            + "4 - Número médio de jobs no sistema En\n"
            + "5 - Variância do número de jobs no sistema\n"
            + "6 - Probabilidade de k jobs na fila Pk\n"
            + "7 - Número médio de jobs na fila Enq\n"
            + "8 - Variância do número de jobs na fila Vnq\n"
            + "9 - Distribuição Acumulada do tempo de resposta Fr\n"
            + "10 - Tempo médio de resposta Er\n"
            + "11 - Variância do tempo de resposta VarEr\n"
            + "12 - q-Percentual do tempo de resposta Qr\n"
            + "13 - 90-Percentual do tempo de resposta Qr90\n"
            + "14 - Distribuição Acumulada do tempo de espera Fw\n"
            + "15 - Tempo médio de espera Ew\n"
            + "16 - Variância do tempo de espera VarEw\n"
            + "17 - Probabilidade de encontrar n ou mais jobs no sistema PnMais\n"
            + "18 - Número médio de jobs atendidos no período ocupado EnAtendidos\n"
            + "19 - Variância do número de jobs atendidos no período ocupado VarEnAtendidos\n"
            + "20 - Média da duração do período ocupado DuracaoOcupado\n"
            + "21 - Variância da duração do período ocupado VarDuracaoOcupado\n"
            + "22 - 90-Percentual do tempo de espera Qw90\n"
            + "-1 - Sair\n"))

        match opcao:
            case 1:
                print(rho)
            case 2:
                rho = calculaRho(lambdaa, mu)
                P0 = calculaP0(rho)
                print(P0)
            case 3:
                n = int (input("Informe o valor de n: "))
                pn = calculaPn(rho, n)
                print("Pn: ", pn)
            case 4:
                en = calculaEn(rho)
                print("En: ", en)
            case 5:
                var = calculaVar(rho)
                print("Var: ", var) 
            case 6:
                k = int(input("Informe o valor de k: "))
                pk = calculaPk(rho, k)
                print("Pk: ", pk)
            case 7:
                enq = calculaEnq(rho)
                print("Enq: ", enq)
            case 8:
                vnq = calculaVarnq(rho)
                print("Vnq: ", vnq)
            case 9:
                r = int(input("Informe o valor de r: "))
                fr = calculaFr(mu, rho, r)
                print("Fr: ", fr)
            case 10:
                er = calculaEr(mu, rho)
                print("Er: ", er)
            case 11:
                varEr = calculaVarEr(mu, rho)
                print("VarEr: ", varEr)
            case 12:
                q = int(input("Informe o valor de q: "))
                qr = calculaQr(mu, rho, q)
                print("Qr: ", qr)
            case 13:
                qr90 = calculaQr90(mu, rho)
                print("Qr90: ", qr90)
            case 14:
                w = int(input("Informe o valor de w: "))
                fw = calculaFw(mu, rho, w)
                print("Fw: ", fw)  
            case 15:         
                ew = calculaEw(mu, rho)
                print("Ew: ", ew)
            case 16:
                varEw = calculaVarEw(mu, rho)
                print("VarEw: ", varEw)
            case 17:
                n = int(input("Informe o valor de n: "))
                pnMais = calculaPnMais(rho, n)
                print("PnMais: ", pnMais)
            case 18:
                enA = calculaEnAtendidos(rho)
                print("EnAtendidos: ", enA)
            case 19:
                varEnA = calculaVarEnAtendidos(rho)
                print("VarEnAtendidos: ", varEnA)
            case 20:
                duracaoOcupado = calculaDuracaoOcupado(mu, rho)
                print("DuracaoOcupado: ", duracaoOcupado)
            case 21:
                varDuracaoOcupado = calculaVarDuracaoOcupado(mu, rho)
                print("VarDuracaoOcupado: ", varDuracaoOcupado)
            case -1:
                print("Saindo...")
            case _:
                print("Opção inválida, tente novamente.")

if __name__ == "__main__":
    main()