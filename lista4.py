#1
def order_selection(arr):
   for i in range(len(arr)):
      min_ind = i
      for j in range(i+1, len(arr)):
         if arr[j] < arr[min_ind]:
            min_ind = j


      arr[i], arr[min_ind] = arr[min_ind], arr[i]

   return arr


vetor = [50,30,10,15]
print("vetor ordenado", order_selection(vetor))

///////////////////////////////

#2
def ordenar_vetor(arr, ordem='crescente'):
    # Percorre todo o vetor
    for i in range(len(arr)):

        idx = i
        for j in range(i+1, len(arr)):
            if (ordem == 'crescente' and arr[j] < arr[idx]) or (ordem == 'decrescente' and arr[j] > arr[idx]):
                idx = j

        arr[i], arr[idx] = arr[idx], arr[i]

    return arr

vetor = [64, 25, 12, 22, 11]

print("Vetor ordenado em ordem crescente:", ordenar_vetor(vetor, ordem='crescente'))
print("Vetor ordenado em ordem decrescente:", ordenar_vetor(vetor, ordem='decrescente'))

//////////////////////////////

#3
def encontrar_maximo(arr):
   maximo = arr[0]

   for num in arr:
      if num > maximo:
         maximo = num
   return maximo

def encontrar_minimo(arr):
   minimo = arr[0]

   for num in arr:
      if num < minimo:
         minimo = num
   return minimo

array = [15,30,50,60]

valor_maximo = encontrar_maximo(array)
valor_minimo = encontrar_minimo(array)

print("o elemento maximo é ", valor_maximo)
print("o elemento com o valor minimo é ", valor_minimo)

//////////////////////////////////

#4
def segundo_menor(arr):
   arr_unico = list(set(arr))
   arr_unico.sort()

   return print("Segundo maior", arr_unico[1])



array = [10,29,39,15]
segundo_menor(array)

////////////////////////////////

#5
def remover_duplicatas(arr):
   return print(list(set(arr)))






array = [10,10,20,30,30]
remover_duplicatas(array)

/////////////////////////////////

#6
def ordenar_decrescente(arr):
   arr.sort()

   arr.reverse()

   quantidade_par = []
   quantidade_impar = []

   for i in arr:
      if i % 2 == 0:
         quantidade_par.append(i)
      else:
         quantidade_impar.append(i)

   return arr, quantidade_impar, quantidade_par


array = [20,10,50,30,33,25]
decrescente, impares, pares = ordenar_decrescente(array)

print("Vetor em ordem decrescente", decrescente)
print("Quantidade de números impares", len(impares))
print("Quantidade de números pares", len(pares))

/////////////////////////////////////

#7
def terceiro_maior(arr):
   arr_unico = list(set(arr))
   arr_unico.sort(reverse=True)



   return print("Terceiro maior", arr_unico[2])




array = [10,10,10,29,39,23,18,27]
terceiro_maior(array)

/////////////////////////////

#8
def calcular_mediana(arr):
   arr.sort()
   n = len(arr)
   soma = 0
   for num in arr:
      soma += num

   if n % 2 == 0:
      mediana = (arr[n // 2 -1] + arr[n // 2]) / 2
      return mediana
   else:
      mediana = arr[n // 2]
      return mediana


array = [ 3, 1, 4, 2, 5, 3, 5, 6, 7]

mediana =  calcular_mediana(array)
print(mediana)