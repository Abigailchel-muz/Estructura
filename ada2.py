import random
import time


# ==================================
# CONFIGURACIÓN
# ==================================

cantidad_alumnos = 500
cantidad_materias = 6


# ==================================
# GENERAR DATOS
# Alumno -> Materia -> Calificación
# ==================================

alumnos = {}


for i in range(1, cantidad_alumnos + 1):

    nombre = "Alumno" + str(i)

    alumnos[nombre] = {}


    for j in range(1, cantidad_materias + 1):

        materia = "Materia" + str(j)

        alumnos[nombre][materia] = random.randint(1,10)



# ==================================
# MOSTRAR TABLA COMPLETA
# ==================================

print("\nTABLA DE CALIFICACIONES")
print("=" * 90)


print(
    "Alumno\t",
    end=""
)


for j in range(1, cantidad_materias + 1):

    print(
        "Materia" + str(j) + "\t",
        end=""
    )


print()


for alumno, materias in alumnos.items():

    print(
        alumno,
        "\t",
        end=""
    )


    for calificacion in materias.values():

        print(
            calificacion,
            "\t",
            end=""
        )


    print()



# ==================================
# BUSCAR ALUMNO Y MATERIA
# ==================================

alumno_buscar = input(
    "\nIngrese alumno a consultar (Ejemplo Alumno321): "
)


materia_buscar = input(
    "Ingrese materia a consultar (Ejemplo Materia5): "
)



inicio = time.perf_counter()



calificacion = alumnos[alumno_buscar][materia_buscar]



fin = time.perf_counter()



# ==================================
# RESULTADO
# ==================================

print("\nRESULTADO DE BÚSQUEDA")
print("=" * 40)

print("Alumno:", alumno_buscar)
print("Materia:", materia_buscar)
print("Calificación:", calificacion)


print(
    "Tiempo de búsqueda:",
    fin - inicio,
    "segundos"
)