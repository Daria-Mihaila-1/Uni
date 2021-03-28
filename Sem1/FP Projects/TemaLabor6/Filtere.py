def gefilterte_zimmern(liste_zimmern, lz):
    """
    functia lasa utilizatorul sa isi spuna criteriile pt o camera si returneaza o lista cu nr camerelor care
    indeplinesc criteriile
    :param liste_zimmern: lista de camere a hotelului
    :param lz: lista de camere din hotel care indeplinesc criteriile
    :return returneaza lista de camere din hotel care indeplinesc criteriile
    """
    mb = input('Meerblick: ').lower()
    print(mb)
    zpreis_found = False  # doar daca e gasita o camera care sa indeplineasca criteriul de pret,
    # in caz ca utilizatorul vrea o camera cu meerblick, se intreaba utilizatorul daca ar fi posibil sa renunte
    # la meerblick

    ok = False
    while not ok:
        if mb == 'nein':
            mb = False
            ok = True
        elif mb == 'ja':
            mb = True
            ok = True
        else:
            print('Sorry, ich kann Sie nicht verstehen, versuche noch einmal: ')
            mb = input('Meerblick: ').lower()
    print()
    p = int(input('gewunschter Preis: '))

    for zimmer in liste_zimmern:

        if zimmer.preis <= p:
            zpreis_found = True
            if zimmer.meerblick == mb:
                lz.append(zimmer)
    if not lz:

        print('Sorry, Ihre Kriterien konnen nicht erfullt werden')
        print()
        if mb and zpreis_found:

            maybe_without = input('Wollen Sie unbedingt ein Zimmer mit Meerblick? '
                                  '\n Schreiben Sie Ihre Antwort hier:  ').lower()
            ok = False
            while not ok:

                if maybe_without == 'nein':

                    ok = True
                    for zimmer in liste_zimmern:
                        if zimmer.preis <= p:
                            lz.append(zimmer)

                elif maybe_without == 'ja':
                    print('Sorry, Ihre Kriterien konnen nicht erfullt werden')
                    ok = True
                else:
                    print()
                    print("Sorry, ich verstehe Sie nicht, Ihre Antwort muss 'ja' oder 'nein' sein"
                          "\nVersuche noch einmal")
                    maybe_without = input('Wollen Sie unbedingt ein Zimmer mit Meerblick?'
                                          '\n Schreiben Sie Ihre Antwort hier: ').lower()

    return lz
