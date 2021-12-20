
#? Demostración de la función sorted()
#* la función sorted crea una nueva lista(esta ordenada) a partir de la lista parametro
firstGreek = ['omega', 'alfa', 'pi', 'gama']
firstGreek2 = sorted(firstGreek)

print(firstGreek)
print(firstGreek2)

print()

#? Demostración del método sort()
#* el metodo sort ordena la lista afectando a la misma
secondGreek = ['omega', 'alfa', 'pi', 'gama']
print(secondGreek)

secondGreek.sort()
print(secondGreek)