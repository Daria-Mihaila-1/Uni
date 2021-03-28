def prim(p):
    """
    functia verifica daca un nr p dat ca parametru este prim
    :param p: un nr oarecare
    :return: True daca p e prim, False in caz contrar
    t: un posibil divizor al lui p
    pri: variabila de tip boolean care isi schimba valoarea daca p este divizibil cu t
    """
    if p > 1:
        if (p == 2) or (p == 3):
            return True
        else:
            pri = True
            for t in range(2, int(p**(1/2)+1)):
                if p % t == 0:
                    pri = False
                    break
            return pri


def primz_auf_primindexe(n):
    """
    functia tipareste primele n nr care sunt prime si sunt in sirul numerelor prim pe pozitii prime
    :param n: nr de numere care trebuiesc printate, acestea indeplinid conditiile
    :return: o lista cu primele n nr care indeplinesc conditiile
    lst: lista care se formeaza din nr care indeplinesc conditiile
     i:variabila contor pt nr prime is sirul nr-lor prime
     nr:un nr care e verificat daca indeplinesc conditiile
     """
    lst = []
    nr = 2
    i  = 1
    while len(lst) < n:
        if prim(nr):            #prima data se verifica daca nr-ul i este prim
            if prim(i):         #daca da atunci verificam daca este si pe pozitie prima in sirul nr-lor prime
                lst.append(nr)  #daca da atunci se adauga nr-ul i in lista lst
            i += 1              #pozitia creste cu 1
        if nr > 2:              #daca nr-ul e mai mare decat 2 atunci creste cu 2
            nr += 2
        else:
            nr += 1             #in caz contrar cu 1
    print(lst)

def main():
    n = int(input('n='))
    primz_auf_primindexe(n)

main()
