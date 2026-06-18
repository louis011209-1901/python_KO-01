import math
import pytest
from kreis_funktion import calc_diameter, flaeche, umfang


def test_calc_area():
    r = 3
    assert flaeche(r) == math.pi * r**2


def test_circumference():
    r = 3
    assert umfang(r) == 2 * math.pi * r


def test_diameter():
    r = 3
    assert calc_diameter(r) == 6