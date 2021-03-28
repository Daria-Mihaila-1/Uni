from bag import bag
from iteratorbag import iterator


def main():
    lst = bag()

    lst.add(49)
    lst.add(56)
    lst.add(56)
    lst.add(56)
    lst.add(8)
    lst.add(9)

    print(lst)

    lst.remove(56)
    print(lst)
    # lst =[49, 56, 56, 8, 9]
    print(lst.search(7))
    print(lst.search(8))

    print(lst.size())

    lst.add(56)
    print(lst.nrOccurrences(56))

    i = iterator(lst)
    print(i.valid())

    i.first()
    print(i)

    i.next()
    i.next()
    i.next()
    i.next()
    i.next()
    i.next()
    i.next()


main()