from entferne_Wiederholungen import entferne
from Anz_sym_Paare import *
from maxZahl_aus_Liste import *
from Verschlusseln import *
from Dominos import *
from Beziehungen import *
from kgv_zw_Indexe import *

"""
3.Generieren Sie die größtemögliche Zahl, die aus der Konkatenation der Elemente der Liste gebildet ist.
"""

"""4. Verschlüsseln  Sie  die  Elemente  der  Liste,
indem  Sie das erste Element  als  Schlüssel benützen und die Methode selbst wählen(+, *, XOR).
"""

"""
5. Filtern Sie die Zahlen, die eine bestimmte Beziehung zwischen Zahlen haben,
die in einem String angegeben wird.(z.B:“x=y*3”, “x/y=2“, ...)
"""

"""6. Finden Sie die längste zusammenhängendeDominoTeilfolge. 
Eine Domino Teilfolge ist definiert als x1y1, x2y2, wo y1=x2. (z.B: 89, 95, 54)
"""

"""7. Finden Sie den kleinsten gemeinsamen Vielfachenzwischen Index from und to, welche gegeben sind.
"""


def lesen_liste():
    List = input("Liste von Elementen:")

    liste = List.split(sep=' ')

    for i in range(len(liste)):
        liste[i] = int(liste[i])

    return liste


def main():
    Option = int(input("die Aufgabe: "))
    liste = lesen_liste()
    if Option == 1:
        entferne(list)

    elif Option == 2:
        anz_von_sym(liste)

    elif Option == 3:
        print(max_zahl(liste))

    elif Option == 4:
        print("die Liste verschlusselt", verschluss(liste))

    elif Option == 5:
        bez = input("meine Beziehung:")
        l_neu = []
        for i in liste:
            filtere(bez, i, l_neu)
        print(l_neu)

    elif Option == 6:
        domino(liste)

    elif Option == 7:
        frm = int(input("from: "))
        to = int(input("to: "))
        print(kleinste_gemeinsamer_vielfach(liste, frm, to))


main()
