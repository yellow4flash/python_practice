try:
    # operaciones con streams
    exp
except IOError as exc:
    print(exc.errno)

#! Constantes seleccionadas útiles para detectar errores de flujo:

#* errno.EACCES → Permiso denegado

# El error se produce cuando intentas, por ejemplo, abrir un archivo con atributos de solo lectura para abrirlo.

#* errno.EBADF → Número de archivo incorrecto

# El error se produce cuando intentas, por ejemplo, operar un stream sin abrirlo.

#* errno.EEXIST → Archivo existente

# El error se produce cuando intentas, por ejemplo, cambiar el nombre de un archivo con su nombre anterior.

#*errno.EFBIG → Archivo demasiado grande

# El error ocurre cuando intentas crear un archivo que es más grande que el máximo permitido por el sistema 
# operativo.

#* errno.EISDIR → Es un directorio

# El error se produce cuando intentas tratar un nombre de directorio como el nombre de un archivo ordinario.

#* errno.EMFILE → Demasiados archivos abiertos

# El error se produce cuando intentas abrir simultáneamente más streams de los aceptables para el sistema 
# operativo.

#* errno.ENOENT → El archivo o directorio no existe

# El error se produce cuando intentas acceder a un archivo o directorio inexistente.

#* errno.ENOSPC → no queda espacio en el dispositivo

# El error ocurre cuando no hay espacio libre en el dispositivo.