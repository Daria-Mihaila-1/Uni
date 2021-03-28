def erste_nat_primz(lst):
    """
    die Funktion erste_nat_primz gibt eine Liste, die die ersten 10 naturliche Primzahlen enthalt, zuruck durch den Parameter lst
    lst:die Liste die gebaut wird
    i: eine beliebige Zahl die untersucht wird ob sie eine Primzahl ist
    t:nimmt die Werte der moglichen Teiler von i
    """
    i = 3
    while len(lst) < 10:
       if i == 3:
           lst.append(i)
       else:
           for t in range(2, int(i ** (1 / 2)) + 1): #die for-Schleife fur i's Teiler geht nur bis zum Radikal der Zahl damit man nicht unnotige Teiler uberpruft
               if i % t == 0:
                   break
           else:
                lst.append(i)
       i += 1
    return(lst)

def main():
    lst = []
    erste_nat_primz(lst)
    print(lst)

main()

