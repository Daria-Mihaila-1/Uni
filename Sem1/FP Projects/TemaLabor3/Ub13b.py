def palindrom(n):
    """"
    Functia verifica daca un numar n este palindrom sau nu
    n este parametru de intrare
    aux este copie dupa n
    x initializam cu 0 si il folosim ca si oglindit a lui n
    Functia returneaza true daca n este palindrom si false in caz contrar
    """
    aux = n
    x = 0
    while (aux != 0):
        x = (x * 10) + aux%10
        aux = aux // 10
    if(x == n):
        return True
    else:
        return False

def sir_numere(v):
    """
    Functia printeaza toate numerele care sunt palindroame intr-un sir v sau "Nu exista palindroame"
    in caz contrar
    v: un vector oarecare
    ok: variabila pentru a verifica daca exista cel putin un palindrom
    i: element din vector
    """
    ok = 0
    for i in v:
        if palindrom(i):
            print(i)
            ok = 1
    if not ok:
        print("Nu exista palindroame")

def main():
    v = [8756, 183095, 100, 9,101]
    sir_numere(v)

main()
