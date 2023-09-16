def ordernacao(vetor):
    num=len(vetor)
   
    for i in range(num):
        indice_min=i
       
        for j in range(i + 1,num):
            if vetor[j] < vetor[indice_min]:
                indice_min=j
       
        aux= vetor[i]
        vetor[i] = vetor[indice_min]
        vetor[indice_min]=aux

vetor=[5,8,4,2,7]
ordernacao(vetor)
print(vetor)