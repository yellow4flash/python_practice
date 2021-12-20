#*La relación final entre cadenas está determinada por comparar el primer caracter 
#*diferente en ambas cadenas (ten en cuenta los puntos de código ASCII / UNICODE en todo momento).

#* Cuando se comparan dos cadenas de diferentes longitudes y la más corta es idéntica a la más larga, 
#* la cadena más larga se considera mayor.
# Justo como aquí:

print('alfa' < 'alfabeto') # is true
# La relación es True (verdadera).
#* La comparación de cadenas siempre distingue entre mayúsculas y minúsculas (las letras mayúsculas 
#* se consideran menores en comparación con las minúsculas).

print('beta' > 'Beta') # is true


#? Aún si una cadena contiene solo dígitos, todavía no es un número. 
# Se interpreta como lo que es, como cualquier otra cadena regular, y su aspecto numérico 
# (potencial) no se toma en cuenta, en ninguna manera.

# Mira los ejemplos:
'10' == '010'   # False
'10' > '010'    # True
'10' > '8'      # False
'20' < '8'      # True
'20' < '80'     # True

#? Comparar cadenas contra números generalmente es una mala idea.

#* Las únicas comparaciones que puede realizar con impunidad son aquellas simbolizadas 
#* por los operadores == y !=. El primero siempre devuelve False, mientras que el segundo siempre devuelve True.
'10' == 10  #False
'10' != 10  #True
'10' == 1   #False
'10' != 1   #True
'10' > 10   #TypeError exception