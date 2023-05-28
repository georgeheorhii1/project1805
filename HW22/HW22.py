import re
import xml.etree.ElementTree as ET


class XMLProcessor:
    def __init__(self, file_path):
        self.file_path = file_path

    def read_xml_file(self):
        """
        Read the XML data from the file.

        Returns:
            xml.etree.ElementTree.Element: XML data.
        """
        tree = ET.parse(self.file_path)
        return tree.getroot()

    def xml_to_string(self, xml_data):
        """
        Convert XML data to a string representation.

        Args:
            xml_data (xml.etree.ElementTree.Element): XML data.

        Returns:
            str: String representation of the XML data.
        """
        return ET.tostring(xml_data, encoding='utf-8').decode('utf-8')

    def string_to_xml(self, xml_string):
        """
        Convert a string representation of XML back to XML data.

        Args:
            xml_string (str): String representation of XML data.

        Returns:
            xml.etree.ElementTree.Element: XML data.
        """
        return ET.fromstring(xml_string)

    def perform_operations(self, xml_data):
        """
        Perform operations using the methods of the xml.etree library or any similar method of your choice.

        Args:
            xml_data (xml.etree.ElementTree.Element): XML data.

        Returns:
            str: Result of the operations performed.
        """
        result = ""
        for genre in xml_data:
            genre_category = genre.attrib.get('category')

            for decade in genre:
                decade_years = decade.attrib.get('years')

                for movie in decade:
                    movie_title = movie.attrib.get('title')
                    movie_favorite = movie.attrib.get('favorite')
                    movie_format = movie.find('format').text.strip()
                    movie_year = movie.find('year').text.strip()
                    movie_rating = movie.find('rating').text.strip()
                    movie_description = movie.find('description').text.strip()

                    # Example: Use regular expression to find movies with titles containing "man"
                    if re.search(r'man', movie_title, re.IGNORECASE):
                        result += f"Category: {genre_category}\n"
                        result += f"Decade: {decade_years}\n"
                        result += f"Movie Title: {movie_title}\n"
                        result += f"Favorite: {movie_favorite}\n"
                        result += f"Format: {movie_format}\n"
                        result += f"Year: {movie_year}\n"
                        result += f"Rating: {movie_rating}\n"
                        result += f"Description: {movie_description}\n\n"

        return result


# Create an instance of the XMLProcessor class
processor = XMLProcessor("example.xml")

# Read the XML data from the file
xml_data = processor.read_xml_file()

# Convert XML data to a string
xml_string = processor.xml_to_string(xml_data)
print("XML String:")
print(xml_string)

# Convert the string back to XML
decoded_xml = processor.string_to_xml(xml_string)
print("\nDecoded XML:")
print(decoded_xml)

# Perform operations on the XML data
result = processor.perform_operations(decoded_xml)
print("\nOperations Result:")
print(result)
