import pytest
import unittest

from HW17_pytest.HW13drop2 import Painting
from HW17_pytest.HW13drop2 import Painting
from HW17_pytest.HW13drop2 import ArtObject
from HW17_pytest.HW13drop2 import Exhibit
from HW17_pytest.HW13drop2 import Sculpture


@pytest.fixture
def painting():
    return Painting("Starry Night", "Vincent van Gogh", "Oil on canvas", "73.7 cm x 92.1 cm")


@pytest.fixture
def sculpture():
    return Sculpture("David", "Michelangelo", "Marble", "5.17 tons")


@pytest.fixture
def exhibit():
    return Exhibit("Famous Artworks")