import pytest
from linear_board import * # Esto importa todo de linear_board
from settings import BOARD_LENGTH, VICTORY_STRIKE

def test_empty_board(): # Comprobar si está vacío el tablero
    empty = LinearBoard()
    assert empty != None # Aqui hay algo, algún objeto
    assert empty.is_full() == False # Afirmamos que el board está vacío
    assert empty.is_victory('x') == False # Determinar si hay alguna victoria

def test_add(): # Añadir cosas al tablero
    b = LinearBoard()
    for i in range(BOARD_LENGTH):
        b.add('x')
    assert b.is_full() == True

def test_victory():
    b = LinearBoard()
    for i in range(VICTORY_STRIKE):
        b.add('x')

        assert b.is_victory('o') == False
        assert b.is_victory('x') == True

def test_tie(): # Comprobar si hay un empate
    b = LinearBoard()

    b.add('o')
    b.add('o')
    b.add('x')
    b.add('o')

    assert b.is_tie('x', 'o')


def test_add_to_full():
    full = LinearBoard()
    for i in range(BOARD_LENGTH):
        full.add('x')

    full.add('x')
    assert full.is_full()
