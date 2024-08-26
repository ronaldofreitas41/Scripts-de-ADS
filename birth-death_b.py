def produto(lambdas, mus, k):
    produto = 1  
    for i in range(k):
        produto *= lambdas[i] / mus[i]
    return produto

def calculaP0(lambdas, mus):
    soma = 1  # Ajuste inicial para considerar o estado vazio (k=0)
    n = len(lambdas)
    
    for k in range(1, n + 1):
        soma += produto(lambdas, mus, k)
    
    P0 = 1 / soma
    return P0

def calcula_probabilidades_estacionarias(lambdas, mus, n):
    # Calcula as probabilidades de estado estacionário
    p0 = calculaP0(lambdas, mus)
    ps = []
    for i in range(n + 1):
        if i == 0:
            ps.append(p0)
        else:
            ps.append(produto(lambdas, mus, i) * p0)
    return ps

def main():
    # Definir taxas de nascimento (λ) e morte (μ)
    lambdas = [175, 175, 175, 175, 175, 175, 175, 175, 175, 175]
    mus = [30, 60, 90, 120, 150, 180, 210, 240, 270, 300]

    # Calcular probabilidades de estado estacionário
    probabilidades = calcula_probabilidades_estacionarias(lambdas, mus, 10)
    
    print("Probabilidades item B via Birth-Death:")
    # Exibir resultados
    for i, p in enumerate(probabilidades):
        print(f"P{i} = {p:.4f}")

if __name__ == "__main__":
    main()
