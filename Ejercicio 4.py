# costo constante, dado que la longitud de una de las palabras nunca sera mayor a 20.
def equal_prefix_len(word1, word2):
    len = 0
    for i in range(word1.__len__()):
        if i < word2.__len__() and word1[i] == word2[i]:
            len = len + 1
        else:
            break
    return len


class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None

    def insert(self, key):
        # se crea un nuevo nodo
        new_node = Node(key)
        # Si el árbol está vacío, el nuevo nodo será la raíz
        if self.root is None:
            self.root = new_node
        else:
            # Si el árbol no está vacío, se empieza a buscar dónde insertar el nuevo nodo
            current_node = self.root
            while True:
                # Si la palabra a insertar es menor que la del nodo actual, se sigue buscando por la izquierda
                if key < current_node.key:
                    # Si ya no hay nodo a la izquierda, se inserta el nuevo nodo allí
                    if current_node.left is None:
                        current_node.left = new_node
                        break
                    # Si hay un nodo a la izquierda, se busca por allí
                    else:
                        current_node = current_node.left
                # Si la palabra a insertar es mayor o igual que la del nodo actual, se busca por la derecha
                else:
                    # Si ya no hay nodo a la derecha, se inserta el nuevo nodo allí
                    if current_node.right is None:
                        current_node.right = new_node
                        break
                    # Si hay un nodo a la derecha, se busca por allí
                    else:
                        current_node = current_node.right

    def search(self, word):
        # Si el árbol está vacío, no hay nada que buscar
        if self.root is None:
            return ""
        else:
            # Si el árbol no está vacío, se busca el prefijo máximo
            current_node = self.root
            result = ""
            while current_node is not None:
                # Sì la longitud del prefijo coincidente entre la llave del nodo actual es mayor a la del resultado,
                # se guarda el resultado temporalmente
                if equal_prefix_len(current_node.key, word) > equal_prefix_len(result, word):
                    result = current_node.key
                # Sì la longitud del prefijo coincidente entre la llave del nodo actual es igual a la del resultado
                # actual, y la palabra del nodo actual es lexicográficamente menor, se actualiza el resultado.
                elif equal_prefix_len(current_node.key, word) == equal_prefix_len(result, word):
                    if current_node.key < result:
                        result = current_node.key
                # Sì la palabra del nodo actual es mayor a word, se busca por la izquierda
                if word < current_node.key:
                    current_node = current_node.left
                # Sì la palabra del nodo actual es menor a word, se busca por la derecha
                else:
                    current_node = current_node.right
            if equal_prefix_len(result, word) < (len(word) / 2):
                result = ""
            return result


def autocomplete(N, ops):
    # se crea una instancia de la clase BST, un arbol binario de búsqueda
    bst = BST()
    # se crea una lista para almacenar los resultados de las búsquedas
    results = []
    # Procesamos cada operación en ops
    for op, word in ops:
        # Sì la operación es de inserción, insertamos la palabra en el BST
        if op == 1:
            bst.insert(word)
        # Sì la operación es de búsqueda, buscamos la palabra con el prefijo máximo y la añadimos a la lista de
        # resultados
        else:
            results.append(bst.search(word))
    # se retorna la lista de resultados
    return results


print(autocomplete(5, [(1, "hola"), (1, "cabeza"), (1, "arroz"), (2, "aro"), (2, "pez")]))