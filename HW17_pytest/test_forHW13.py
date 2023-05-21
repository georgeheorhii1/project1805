import pytest
import unittest

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


@pytest.mark.artobject
class TestArtObject:
    def test_artobject_init(self):
        artobject = ArtObject("Title", "Artist")
        assert artobject.title == "Title"
        assert artobject.artist == "Artist"

    def test_artobject_display_info_not_implemented(self):
        artobject = ArtObject("Title", "Artist")
        with pytest.raises(NotImplementedError):
            artobject.display_info()


@pytest.mark.painting
class TestPainting:
    def test_painting_init(self, painting):
        assert painting.title == "Starry Night"
        assert painting.artist == "Vincent van Gogh"
        assert painting.medium == "Oil on canvas"
        assert painting.dimensions == "73.7 cm x 92.1 cm"

    def test_painting_display_info(self, painting, capsys):
        painting.display_info()
        captured = capsys.readouterr()
        assert captured.out == "Starry Night by Vincent van Gogh, Oil on canvas, 73.7 cm x 92.1 cm\n"


@pytest.mark.sculpture
class TestSculpture:
    def test_sculpture_init(self, sculpture):
        assert sculpture.title == "David"
        assert sculpture.artist == "Michelangelo"
        assert sculpture.material == "Marble"
        assert sculpture.weight == "5.17 tons"

    def test_sculpture_display_info(self, sculpture, capsys):
        sculpture.display_info()
        captured = capsys.readouterr()
        assert captured.out == "David by Michelangelo, Marble, 5.17 tons\n"


@pytest.mark.exhibit
class TestExhibit:
    def test_exhibit_init(self, exhibit):
        assert exhibit.exhibit_name == "Famous Artworks"
        assert exhibit.art_objects == []

    def test_exhibit_add_art_object(self, exhibit, painting):
        exhibit.add_art_object(painting)
        assert painting in exhibit.art_objects

    def test_exhibit_remove_art_object(self, exhibit, painting):
        exhibit.add_art_object(painting)
        exhibit.remove_art_object(painting)
        assert painting not in exhibit.art_objects

    def test_exhibit_display_info(self, exhibit, painting, sculpture, capsys):
        exhibit.add_art_object(painting)
        exhibit.add_art_object(sculpture)
        exhibit.display_info()
        captured = capsys.readouterr()
        expected_output = f"Exhibit: Famous Artworks\nStarry Night by Vincent van Gogh, Oil on canvas, 73.7 cm x 92.1 " \
                          f"cm\nDavid by Michelangelo, Marble, 5.17 tons\n"
        assert captured.out == expected_output


@pytest.mark.parametrize("title, artist, medium, dimensions",
                         [("Starry Night", "Vincent van Gogh", "Oil on canvas", "73.7 cm x 92.1 cm")])
def test_painting_parametrized(title, artist, medium, dimensions):
    painting = Painting(title, artist, medium, dimensions)
    assert painting.title == title
    assert painting.artist == artist
    assert painting.medium == medium
    assert painting.dimensions == dimensions



