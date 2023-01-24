# Algoritmo de ordenamiento mergeSort O(n log(n))
def mergeSort(lista):
    if len(lista) < 2:
        return lista

    mid = len(lista) // 2
    left = lista[:mid]
    right = lista[mid:]

    left = mergeSort(left)
    right = mergeSort(right)

    return merge(left, right)

def merge(left, right):
    result = []
    while left and right:
        if left[0] < right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))

    result.extend(left)
    result.extend(right)

    return result


def apartamentosMaximos(m, n, k, precioAptos, tentativoAplicantes):
    mergeSort(precioAptos)          #mlog(m) -> O(NlogN)
    mergeSort(tentativoAplicantes)  #nlog(n) -> O(NlogN)
    aptos_arrendados = 0
    aux_indice_aplicantes = 0

    # m*n
    for i in range(m):
        for j in range(aux_indice_aplicantes, n):
            # Si el precio del aplicante está dentro del rango de tolerancia del precio
            # del apartamento, se arrienda el apartamento y pasamos al siguiente solicitante
            if precioAptos[i] - k <= tentativoAplicantes[j] <= precioAptos[i] + k:
                aptos_arrendados += 1
                aux_indice_aplicantes = j + 1
                break
    return aptos_arrendados

print(apartamentosMaximos(3, 4, 5, [30, 60, 75],  [60, 45, 80, 60]))  # 2
print(apartamentosMaximos(3, 4, 5, [75, 10, 20],  [60, 45, 80, 60]))  # 1
print(apartamentosMaximos(3, 4, 5, [75, 30, 600],  [60, 45, 80, 60]))  # 1
print(apartamentosMaximos(3, 5, 10, [100, 150, 200], [90, 140, 210, 260, 310]))  # 3
print(apartamentosMaximos(3, 5, 20, [100, 150, 200], [140, 210, 260, 310, 400]))  # 2
print(apartamentosMaximos(2, 5, 20, [100, 150], [90, 140, 210, 260, 310]))  # 2
print(apartamentosMaximos(5, 5, 20, [100, 150, 200, 250, 300], [90, 140, 210, 260, 310]))  # 5
print(apartamentosMaximos(5, 5, 50, [100, 200, 250, 250, 300], [90, 140, 210, 260, 310]))  # 4
