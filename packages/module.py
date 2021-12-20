# print("I like to be a module. ")
# print(__name__) # la variable __name__ se establece a __main__
# from typing import Counter
#!/usr/bin/env python3
"""module.py - an example of Python module"""

__counter=0

def sum1(lista):
    global __counter
    __counter += 1
    sum = 0
    for e1 in lista:
        sum += e1
    return sum
def prod1(lista):
    global __counter
    __counter += 1
    prod = 1
    for e1 in lista:
        prod *= e1
    return prod

if __name__ == "__main__":
    print("I prefer to be a module(se ejcuta el mismo módulo), but I can do some tests for you")
    l=[i+1 for i in range(5)]
    print(sum(l)==15)
    print(prod1(l)==120)
else:
    print("I like to be a module, se invoca")