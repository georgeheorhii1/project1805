from abc import ABC, abstractmethod


# Describe the art objects for the museum.
# use all 5 principles: abstraction, imitation, polymorphism, hiding, encapsulation.
# add property, setter.
# Create at least one instance of each class and call the methods


class ArtObject(ABC):
    def __init__(self, title, artist):
        self.title = title
        self.artist = artist

    @abstractmethod
    def display_info(self):
        pass


class Painting(ArtObject):

    def __init__(self, title, artist, medium, dimensions):
        super().__init__(title, artist)
        self.medium = medium
        self.dimensions = dimensions

    def display_info(self):
        print(f"{self.title} by {self.artist}, {self.medium}, {self.dimensions}")


class Sculpture(ArtObject):
    def represent_the_article(self):
        pass

    def __init__(self, title, artist, material, weight):
        super().__init__(title, artist)
        self.material = material
        self.weight = weight

    def display_info(self):
        print(f"{self.title} by {self.artist}, {self.material}, {self.weight}")


class Exhibit:
    def __init__(self, exhibit_name):
        self.__exhibit_name = exhibit_name
        self.__art_objects = []

    @property
    def exhibit_name(self):
        return self.__exhibit_name

    @property
    def art_objects(self):
        return self.__art_objects

    def add_art_object(self, art_object):
        self.__art_objects.append(art_object)

    def remove_art_object(self, art_object):
        self.__art_objects.remove(art_object)

    def display_info(self):
        print(f"Exhibit: {self.exhibit_name}")
        for art_object in self.art_objects:
            art_object.display_info()


painting = Painting("Starry Night", "Vincent van Gogh", "Oil on canvas", "73.7 cm x 92.1 cm")
sculpture = Sculpture("David", "Michelangelo", "Marble", "5.17 tons")
exhibit = Exhibit("Famous Artworks")

exhibit.add_art_object(painting)
exhibit.add_art_object(sculpture)

exhibit.display_info()
