import unittest
from random import shuffle
from copy import deepcopy

def sort_quicksort(lista, *, key=lambda x:x, reverse=False):
    if lista == []:
        return []
    else:
        pivot = lista[0]

        if not reverse:
            lesser = sort_quicksort([x for x in lista[1:] if key(x) < key(pivot)], key=key, reverse=reverse)
            greater = sort_quicksort([x for x in lista[1:] if not key(x) < key(pivot)], key=key, reverse=reverse)
            return lesser + [pivot] + greater
        else:
            lesser = sort_quicksort([x for x in lista[1:] if not key(x) < key(pivot)], key=key, reverse=reverse)
            greater = sort_quicksort([x for x in lista[1:] if key(x) < key(pivot)], key=key, reverse=reverse)
            return lesser + [pivot] + greater


def sort_gnomesort(lista_p, *, key=lambda x:x, reverse=False):
    lista = deepcopy(lista_p)
    pos = 1
    while pos < len(lista):
        q = not reverse
        p = key(lista[pos]) < key(lista[pos-1])

        if (p or q) and not (p and q):
            pos += 1
        else:
            lista[pos], lista[pos-1] = lista[pos-1], lista[pos]
            if pos > 1:
                pos -= 1

    return lista
class TestQuickSort(unittest.TestCase):
    def setUp(self):
        self.lista = list(range(0,50))
        shuffle(self.lista)

    def testNoKey(self):
        ordon = sort_quicksort(self.lista)

        for i in range(1, len(ordon)):
            self.assertLessEqual(ordon[i-1], ordon[i])

    def testReverse(self):
        ordon = sort_quicksort(self.lista, reverse=True)

        for i in range(1, len(ordon)):
            self.assertGreaterEqual(ordon[i-1], ordon[i])

    def testWithKey(self):
        ordon = sort_quicksort(self.lista, key=lambda x:x+10)

        for i in range(1, len(ordon)):
            self.assertLessEqual(ordon[i-1], ordon[i])

class TestGnomeSort(unittest.TestCase):
    def setUp(self):
        self.lista = list(range(0,50))
        shuffle(self.lista)

    def testNoKey(self):
        ordon = sort_gnomesort(self.lista)

        for i in range(1, len(ordon)):
            self.assertLessEqual(ordon[i-1], ordon[i])

    def testReverse(self):
        ordon = sort_gnomesort(self.lista, reverse=True)

        for i in range(1, len(ordon)):
            self.assertGreaterEqual(ordon[i-1], ordon[i])

    def testWithKey(self):
        ordon = sort_gnomesort(self.lista, key=lambda x:x+10)

        for i in range(1, len(ordon)):
            self.assertLessEqual(ordon[i-1], ordon[i])

if __name__ == "__main__":
    unittest.main()

