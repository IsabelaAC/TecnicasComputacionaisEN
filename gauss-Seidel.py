#Método de Gauss-Seidel

from sympy.core.symbol import Symbol

b1 = Symbol('b1')
b2 = Symbol('b2')
b3 = Symbol('b3')
b4 = Symbol('b4')
b5 = Symbol('b5'),

def gaussSeidel(A,b,vetorSolucao,iteracoes):
    iteracao = 0

    while iteracao < iteracoes:
        for i in range(len(A)):
            x = b[i]
            for j in range(len(A)):
                if i!= j:
                 x -=A[i][j]*vetorSolucao[j]
            x /= A[i][i]
            vetorSolucao[i] = x
        iteracao += 1
    print(vetorSolucao)
#Questão 2
gaussSeidel([[8,2,-1,0],[2,-4,0,0],[0,-2,8,-1],[-0,0,-1,4]],[1,1,1,1],[0,0,0,0],100)

#Questão 3
#A = [[7,-3,0,0,0], [-3,7,-3,0,0], [0,-3,7,-3,0],[0,0,-3,7,-3],[0,0,0,-3,7]]
#b = [b1,b2,b3,b4,b5] ou [1,1,1,1,1]
#vetorS= [10,45,100,45,10]
#Para questão 3 descomentar apenas a linha abaixo
#gaussSeidel([[7,-3,0,0,0], [-3,7,-3,0,0], [0,-3,7,-3,0],[0,0,-3,7,-3],[0,0,0,-3,7]],[1,1,1,1,1],[10,45,100,45,10],200)
            
