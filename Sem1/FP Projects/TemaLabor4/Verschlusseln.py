"""4. Verschlüsseln  Sie  die  Elemente  der  Liste,  indem  Sie das erste Element  als  Schlüssel benützen und die
Methode selbst wählen(+, *, XOR).
"""


def verschluss(lst):
    schlussel = lst[0]
    if schlussel == "+":
        s = lst[1]
        for i in range(2, len(lst)):
            s += lst[i]
        return s
    elif schlussel == "*":
        p = lst[1]
        for i in range(2, len(lst)):
            p *= lst[i]
        return p
    else:
        xor = lst[1]
        for i in range(2, len(lst)):
            xor = xor ^ lst[i]
        return xor
