import collections
from itertools import groupby
from operator import itemgetter
import random


Carta = collections.namedtuple('Carta', ['palo', 'valor'])

class SpanishDeck:
    palos = 'espada basto oro copa'.split()
    valores = [1, 2, 3, 4, 5, 6, 7, 10, 11, 12]
    puntajes = {
        1: 11,
        2: 12,
        3: 13,
        4: 14,
        5: 15,
        6: 16,
        7: 17,
        10: 10,
        11: 10,
        12: 10
    }

    def __init__(self):
        self._cards = [Carta(palo, valor)
                       for valor in self.valores
                       for palo in self.palos]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]

    def calcular_puntos(self, tirada):
        grupo = groupby(tirada, itemgetter(0))
        grupos = [[item for item in data] for (key, data) in grupo]
        cartas_mismo_palo = [grupo for grupo in grupos if len(grupo) > 1]

        if len(cartas_mismo_palo) >= 1:
            if len(cartas_mismo_palo[0]) >= 2:
                cartas_puntaje = [self.puntajes[carta.valor] for carta in cartas_mismo_palo[0]]
                ordenados = sorted(cartas_puntaje, reverse=True)[0:2]
                return sum(ordenados)
        else:
            return 0

    def repartir(self):
        return random.sample(self._cards, 3)


N = 10
deck = SpanishDeck()
listado_cartas = [deck.repartir() for i in range(N)]
puntos = [(deck.calcular_puntos(cartas), cartas)
          for cartas in listado_cartas]

[print(punto) for punto in puntos]

