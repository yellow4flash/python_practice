
    #todo: Modo Lectura: un stream abierto en este modo permite solo operaciones de lectura; 
    # intentar escribir en la transmisión provocará una excepción (la excepción se llama 
    # UnsupportedOperation, la cual hereda el OSError y el ValueError, y proviene del módulo io).
    #todo: Modo Escritura: un stream abierto en este modo permite solo operaciones de escritura; 
    # intentar leer el stream provocará la excepción mencionada anteriormente.
    #todo: Modo Actualizar: un stream abierto en este modo permite tanto lectura como escritura.

#? operaciones básicas a realizar con el stream
    #* Lectura del stream: las porciones de los datos se recuperan del archivo y se colocan en un
    #*  área de memoria administrada por el programa (por ejemplo, una variable).
    #* Escritura del stream: Las porciones de los datos de la memoria (por ejemplo, una variable) 
    #* se transfieren al archivo.

#! modos de apertura de un stream ->> open()
#? Modo de apertura r: lectura

#     El stream será abierto en modo lectura.
#     El archivo asociado con el stream debe existir y tiene que ser legible, de lo contrario la 
#     función open() lanzará una excepción.

#? Modo de apertura w: escritura

#     El stream será abierto en modo escritura.
#     El archivo asociado con el stream no necesita existir. Si no existe, se creará; si existe, 
#     se truncará a la longitud de cero (se borrá); si la creación no es posible (por ejemplo, 
#     debido a los permisos del sistema) la función open() lanzará una excepción.

#? Modo de apertura a: adjuntar

#     El stream será abierto en modo adjuntar.
#     El archivo asociado con el stream no necesita existir; si no existe, se creará; si existe, el 
#     cabezal de grabación virtual se establecerá al final del archivo (el contenido anterior del archivo 
#     permanece intacto).

#? Modo de apertura r+: leer y actualizar

#     El stream será abierto en modo leer y actualizar.
#     El archivo asociado con el stream debe existir y tiene que ser escribible, de lo contrario la 
#     función open() lanzará una excepción.
#     Se permiten operaciones de lectura y escritura en el stream.

#? Modo de apertura w+: escribir y actualizar

#     El stream será abierto en modo escribir y actualizar.
#     El archivo asociado con el stream no necesita existir; si no existe, se creará; el contenido anterior 
#     del archivo permanece intacto.
#     Se permiten operaciones de lectura y escritura en el stream.

#todo: Si hay una letra b al final de la cadena del modo significa que el stream se debe abrir en el modo  binario

#! EXTRA

#* También puedes abrir un archivo para su creación exclusiva. Puedes hacer esto usando el modo de apertura x. 
#* Si el archivo ya existe, la función open() lanzará una excepción.


