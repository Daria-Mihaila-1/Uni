import datetime


def aktuelle_res(liste_gaste, liste_res):

    heute = datetime.datetime.now()
    nr = 0
    l = []
    for gast in range(len(liste_gaste)):

        if liste_gaste[gast].liste_res:  # verificam daca un client "gast" are sau nu rezervari facute

            liste_r = liste_gaste[gast].liste_res

            for r in range(len(liste_r)):  # cautam in lista lui de rezervari minim o rezervare actuala

                if (heute >= liste_r[r].check_in) and (heute <= liste_r[r].check_out):
                    nr += 1
                    l.append(liste_gaste[gast])
                    break
    print(nr, 'Gast/Gäste haben aktuelle Reservierungen:')
    print(l)
