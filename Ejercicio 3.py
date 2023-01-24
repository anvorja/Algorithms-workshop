# Algoritmo de ordenamiento mergeSort O(n log(n))
def mergeSort(list):
    if len(list) < 2:
        return list

    mid = len(list) // 2
    left = list[:mid]
    right = list[mid:]

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


def mesasOcupadas(n, T):
    # Se ordena la lista de tuplas por tiempo de entrada
    T = mergeSort(T)
    maxMesas = 0

    # Se crea una lista para llevar el registro del # de mesas ocupadas en cada momento
    momentos = [0] * max(tupla[1] for tupla in T)
    # Se recorre cada una de las tuplas en T
    for e, s in T:
        # Se recorre el intervalo de tiempo en el que el grupo actual esta en una mesa
        for t in range(e, s):
            # Se aumenta en 1 el número de mesas ocupadas en el momento actual
            momentos[t] += 1
            maxMesas = max(maxMesas, momentos[t])

    return maxMesas


print("1. " + str(mesasOcupadas(3, [(5, 8), (2, 4), (3, 9)])))  # 2
print("2. " + str(mesasOcupadas(5, [(5, 8), (2, 4), (3, 9), (2, 4), (3, 9)])))  # 4
print("3. " + str(mesasOcupadas(7, [(5, 8), (2, 4), (3, 9), (2, 4), (3, 9), (3, 9), (5, 6)])))  # 5
print("4. " + str(mesasOcupadas(4, [(1, 3), (4, 6), (2, 5), (7, 9)])))  # 2
print("5. " + str(mesasOcupadas(4, [(1, 3), (4, 6), (2, 5), (5, 7)])))  # 2
print("6. " + str(mesasOcupadas(3, [(2, 4), (2, 4), (2, 4)])))  # 3
print("7. " + str(mesasOcupadas(3, [(2, 4), (5, 7), (8, 10)])))  # 1
print("8. " + str(mesasOcupadas(3, [(2, 4), (4, 6), (7, 8)])))  # 1
print("9. " + str(mesasOcupadas(3, [(2, 4), (1, 3), (1, 5)])))  # 3
print("10. " + str(mesasOcupadas(8, [(1, 4), (5, 9), (10, 12), (1, 3), (1, 5), (14, 16), (13, 15), (15, 18)])))  # 3
