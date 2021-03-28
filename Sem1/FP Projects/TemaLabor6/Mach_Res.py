from Res import Reservierung


def mach_reservierung(gast, nr_gaste, check_in, check_out, liste_gaste, liste_zimmern, liste_res):
    """functia face o rezervare:
-cauta prin lista de camere o camera in care sa incapa nr de clienti care vor sa se cazeze intr-o camera
-daca gaseste una cauta prin lista de rezervari a hotelului si verifica daca pe perioada dorita e libera camera
respectiva
- daca este libera atuncii face o rezervare si o variabila made devine true
-altfel nu se poate face rezervarea si se tipareste un mesaj corespunzator
"""
    made = False
    nr_ok = False
    period_ok = False
    check_in = datetime.datetime.strptime(check_in.strip(), '%Y-%d-%m').date()
    check_out = datetime.datetime.strptime(check_out.strip(), '%Y-%d-%m').date()
    for z in range(len(liste_zimmern)):
        # caut in lista de camere o camera libera pe perioada check_in - check_out pt gast

        if nr_gaste <= liste_zimmern[z].max_anz:  # trebuie sa fie si destul de incapatoare camera
            nr_ok = True

            if not liste_res:  # nu este nici o rezervare facuta ==> se face o rezervare instant

                neue_res = Reservierung(nr_gaste, liste_zimmern[z].nummer, check_in.strftime("%x"),
                                        check_out.strftime("%x"))
                liste_res.append(neue_res)
                made = True
                break

            else:
                period_ok = False   # presupunem ca pe perioada dorita nu e libera camera
                for r in range(len(liste_res)):
                    # in lista de rezervari verificam daca pe perioada dorita
                    # este sau nu vreo rezervare facuta pe camera liste_zimmern[z]

                    if liste_res[r].zimmer == liste_zimmern[z].nummer:

                        if (check_in >= liste_res[r].check_out) or (check_out <= liste_res[r].check_in):

                            neue_res = Reservierung(nr_gaste, liste_zimmern[z].nummer, check_in.strftime("%check_in"),
                                                    check_out.strftime("%check_out"))
                            liste_res.append(neue_res)
                            period_ok = True  # daca se poate face rezervarea atunci camera e libera pe perioada data
                            made = True
                            break
            break

    if made:
        # daca se poate face rezervarea verificam daca gast este un client vechi sau unul nou

        print(f"Reservierung für {gast.vorname, gast.nachname} gemacht")

        inlist = False

        for g in range(len(liste_gaste)):

            if (liste_gaste[g].vorname == gast.vorname) and (liste_gaste[g].nachname == gast.nachname):
                liste_gaste[g].add_reservierung(neue_res)
                inlist = True
                break

        if not inlist:

            liste_gaste.append(gast)
            gast.add_reservierung(neue_res)
        for gast in liste_gaste:
            print(gast)

    else:
        if not nr_ok:
            print('Ihr seid leider zu viele, wir haben kein Zimmer mit so viele Platze')
        if not period_ok:
            print('Dann sind keine Zimmer frei')
        print('Wir konnten leider keine Reservierung fur Sie machen://')
