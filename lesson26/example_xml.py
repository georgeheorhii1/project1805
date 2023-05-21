from xml.etree import ElementTree

tree = ElementTree.parse('example.xml')
collection = tree.getroot()
for genre in collection.iter('decade'):
    print(genre.items())


#print(collection)
#with open('example.xml', 'r') as e:


#for genre in collection:
#    for decade in genre:
#        print(decade.tag)
#print(ElementTree.tostring(collection).decode())