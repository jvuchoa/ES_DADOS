def ordernacao(vetor,ordem):
    num=len(vetor)
    if (ordem==0):
        for i in range(num):
            indice_min=i
       
        for j in range(i + 1,num):
            if vetor[j] < vetor[indice_min]:
                indice_min=j
        vetor[i],vetor[indice_min] = vetor[indice_min],vetor[i]
    else:
        for j in range(i + 1,num):
            if vetor[j] > vetor[indice_min]:
                indice_min=j
        vetor[i],vetor[indice_min] = vetor[indice_min],vetor

        
vetor=[5,8,4,2,7]
ordernacao(vetor)
print(vetor)
    