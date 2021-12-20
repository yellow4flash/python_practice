from platform import machine, platform, processor, system, version
# Entidad platform
print(platform())  # se invoca de manera estandar: aliased=false, terse=false
print(platform(1)) # aliased=1-> presenta los nombres de las capas subyacentes
print(platform(0, 1)) # aliased=0, terse=1-> convence a la función de presentar un resumen del resultado

# Entidad machine
print(machine()) # show the generic name processor to run SO together Python

# Entidad processor
print(processor())# show the real name of processor

# Entity system
print(system()) # show the generic name of the OS
# Entity version
print(version()) # show the version of the OS
