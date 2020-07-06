def questao1(nums, alvo):
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if (nums[i] + nums[j]) == alvo:
                return [i,j]
    return None

##Questão 2
def bracket(sequence):
    pilha = []
    for x in range(len(sequence)):
        if sequence[x] in ["(", "[", "{"]:
            pilha.append(sequence[x])
            print(pilha)
        else:
            if len(pilha) == 0:
                return False
            if sequence[x] == ")":
                if pilha.pop() != "(":
                    return False
            elif sequence[x] == "]":
                if pilha.pop() != "[":
                    return False
            elif sequence[x] == "}":
                if pilha.pop() != "{":
                    return False

    return len(pilha) == 0

##Questão 3
def acaoDoDia(valores):
    lucro = 0
    for i in range(len(valores)):
        bud = valores[i]

        for j in range(i+1, len(valores)):
            atual = valores[j]
            if atual > bud and (atual - bud) > lucro:
                lucro = atual - bud

    return lucro

##Questão 4
def retencaoAgua(elevacoes):

    ##pegamos o valor do índice de altura máxima
    ind_max = 0
    for i in range(1, len(elevacoes)):
        if elevacoes[i] > elevacoes[ind_max]:
            ind_max = i

    altura_max = elevacoes[ind_max]
    print("Altura maxima: " + str(altura_max))
    quantidade = 0
    for i in range(altura_max):
        #indices
        ini = 0
        fim = 0
        arr_ind = []
        flag_ini = True
        for j in range(len(elevacoes)):
            if elevacoes[j] == (altura_max - i):
                arr_ind.append(j)
                if flag_ini:
                    flag_ini = False
                    ini = j
                else:
                    fim = j

            if fim > ini:
                quantidade = quantidade + (fim - ini - 1)
                ini = fim
        #decrementando a altura máxima
        for k in range(len(arr_ind)):
            elevacoes[arr_ind[k]] = elevacoes[arr_ind[k]] - 1

    return quantidade

##Testes

arr = [2, 7, 11, 15]
arr2 = [1, 2, 3, 7, 11]
alvo = 9

print(questao1(arr2, alvo))

print(bracket("{[()[()]]}"))

print(acaoDoDia([7,1,5,3,6,4]))
print(acaoDoDia([7,1,5,3,6,4,1,5]))
print(acaoDoDia([7,6,4,3,1]))

print(retencaoAgua([0,1,0,2,1,0,1,3,2,1,2,1]))
print(retencaoAgua([0,3,0,2,1,0,1,3,2,1,2,1]))