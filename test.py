def es_caso_base(S:list)-> bool:
    if len(S) <= 1: return True
    return False

def resolver_caso_base(S:list, target)->bool:
    if S[0] == target: return True
    return False

def dividir(S:list)->tuple:
    mitad = len(S) //2
    izquierda = S[:mitad]
    derecha = S[mitad:]
    return izquierda, derecha

def combinar(S1:list, S2:list) ->list:
    return S1 or S2

def resolver(S: list, target) ->bool:
    if es_caso_base(S):
        return resolver_caso_base(S, target)
    S1,S2 = dividir(S)
    sol1 = resolver(S1, target)
    sol2 = resolver(S2, target)

    return combinar(sol1,sol2)

lista = [1,15,3,25,42,68,3,0]
print(resolver(lista, 3))