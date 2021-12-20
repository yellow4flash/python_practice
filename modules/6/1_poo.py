
#* Casi todos los programas que vimos hasta ahora, pertenecen al estilo de programación procedimental

#?La programación procedimental 
#* fue el enfoque dominante para el desarrollo de software durante décadas de TI, 
#* y todavía se usa en la actualidad. Además, no va a desaparecer en el futuro, ya que funciona muy bien para 
#* proyectos específicos (en general, no muy complejos y no grandes, pero existen muchas excepciones a esa regla).

#?El enfoque orientado a objetos 
#* es bastante joven (mucho más joven que el enfoque procedimental) y es particularmente útil cuando 
#* se aplica a proyectos grandes y complejos llevados a cabo por grandes equipos formados por muchos 
#* desarrolladores.

#? Python es una herramienta universal para la programación procedimental y orientada a objetos. 
#? Se puede utilizar con éxito en ambas.

#todo:_ Cada clase es como una receta que se puede usar cuando quieres crear un objeto útil.
#* Nota: la jerarquía crece de arriba hacia abajo, como raíces de árboles, no ramas.

#* Ten en cuenta la dirección de las flechas: siempre apuntan a la superclase. La clase de nivel 
#* superior es una excepción: no tiene su propia superclase.

#? Un objeto 
#* es una encarnación de los requisitos, rasgos y cualidades asignados a una clase específica.
#? herencia. 
#* Cualquier objeto vinculado a un nivel específico de una jerarquía de clases hereda todos los rasgos 
#* (así como los requisitos y cualidades) definidos dentro de cualquiera de las superclases.

# La programación orientada a objetos supone que cada objeto existente puede estar equipado con tres 
# grupos de atributos:

    # Un objeto tiene un nombre que lo identifica de forma exclusiva dentro de su namespace
            #  (aunque también puede haber algunos objetos anónimos).
    # Un objeto tiene un conjunto de propiedades individuales que lo hacen original, 
            # único o sobresaliente (aunque es posible que algunos objetos no tengan propiedades).
    # Un objeto tiene un conjunto de habilidades para realizar actividades específicas, capaz de cambiar 
            # el objeto en sí, o algunos de los otros objetos.
    #!tips

    #* Un sustantivo: probablemente se este definiendo el nombre del objeto.   (nombre propio)
    #* Un adjetivo: probablemente se este definiendo una propiedad del objeto. (califica el sustantivo)
    #* Un verbo: probablemente se este definiendo una actividad del objeto.    (acción del sustantivo)

#? Dos ejemplos deberían servir como un buen ejemplo:

#!     Max es un gato grande que duerme todo el día.

#*     Nombre del objeto = Max
#*     Clase de inicio = Gato
#*     Propiedad = Tamaño (grande)
#*     Actividad = Dormir (todo el día)

#!     Un Cadillac rosa pasó rápidamente.

#*     Nombre del objeto = Cadillac
#*     Clase de inicio = Vehículo terrestre
#*     Propiedad = Color (rosa)
#*     Actividad = Pasar (rápidamente)

# Creación de una simple clase
class ClaseSimple:
    pass
# La palabra clave reservada #*pass 
# llena la clase con nada. No contiene ningún método ni propiedades.

#*creación de un objeto

miPrimerObjeto = ClaseSimple()

#? El acto de crear un objeto de la clase seleccionada también se llama 
#! instanciación 
#? (ya que el objeto se convierte en una instancia de la clase).