def Nodos(nodov, izquierdo=None, derecho=None):
    return {'nvalor': nodov, 'izquierdo': izquierdo, 'derecho': derecho}


def ArbolBinario(nodo, minimo=None, maximo=None):
    if nodo is None:
        return True
    if minimo is not None and nodo['nvalor'] <= minimo:
        return False
    if maximo is not None and nodo['nvalor'] >= maximo:
        return False
    return (ArbolBinario(nodo['izquierdo'], minimo, nodo['nvalor']) and
            ArbolBinario(nodo['derecho'], nodo['nvalor'], maximo))


raiz = Nodos(3, Nodos(5, Nodos(1), Nodos(4)), Nodos(2, Nodos(6)))


if ArbolBinario(raiz):
    print("Es arbol binario")
else:
    print("no es arbol")


