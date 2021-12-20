from platform import python_implementation, python_version_tuple

print(python_implementation()) # String que denota la implementación de python

for atributo  in python_version_tuple():
    print(atributo)