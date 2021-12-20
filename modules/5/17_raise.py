# Raise: exc
# ? sirve para ssimular una exepción como en el siguente fragmaneto
def badFun(n):
    raise ZeroDivisionError #* se crea una exepción ZeroDivisionError
try:
    badFun(0) # se ocaciona la excepción
except ArithmeticError:#por lo que se ejecuta #*except
    print("¿Que pasó? ¿Un error?")

print("FIN.")

#? en este caso ocacionamos una excepción al invocar 
#*raise en el except
def badFun(n):
    try:
        return n / 0
    except:
        print("¡Lo hice otra vez!")
        raise#*ocacionará una excepcion
    #! en esta variante solo debe ser usado dentro
    #! de la instrucción except, fuera ocacionará error
try:
    badFun(0)
except ArithmeticError:
    print("¡Ya veo!")

print("FIN.")