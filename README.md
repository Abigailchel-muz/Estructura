#  Programa de Ventas Mensuales

##  Descripción

Este proyecto consiste en un programa desarrollado en **Python** para administrar las ventas mensuales de una tienda.

El programa utiliza un **arreglo bidimensional de 12 meses × 3 departamentos**, donde se almacenan las ventas correspondientes a:

*  Ropa
*  Deportes
*  Juguetería
El archivo principal del proyecto es:
```text
arreglo_tarea.py
```
El programa cuenta con un menú interactivo que permite al usuario registrar, buscar, eliminar y visualizar las ventas.

##  Objetivo

El objetivo de este proyecto es practicar el uso de **arreglos bidimensionales en Python**, además de aplicar diferentes conceptos básicos de programación como:

* Listas
* Arreglos bidimensionales
* Funciones
* Ciclos `for`
* Ciclos `while`
* Condicionales
* Entrada de datos
* Índices
* Manejo de valores numéricos

## Estructura del arreglo

El programa utiliza un arreglo bidimensional llamado `ventas`.

```python
ventas = [
    [0, 0, 0],  # Enero
    [0, 0, 0],  # Febrero
    [0, 0, 0],  # Marzo
    [0, 0, 0],  # Abril
    [0, 0, 0],  # Mayo
    [0, 0, 0],  # Junio
    [0, 0, 0],  # Julio
    [0, 0, 0],  # Agosto
    [0, 0, 0],  # Septiembre
    [0, 0, 0],  # Octubre
    [0, 0, 0],  # Noviembre
    [0, 0, 0]   # Diciembre
]
```

El arreglo tiene:

**12 filas × 3 columnas**

Las filas representan los meses y las columnas representan los departamentos.

| Mes        | Ropa | Deportes | Juguetería |
| ---------- | ---: | -------: | ---------: |
| Enero      |    0 |        0 |          0 |
| Febrero    |    0 |        0 |          0 |
| Marzo      |    0 |        0 |          0 |
| Abril      |    0 |        0 |          0 |
| Mayo       |    0 |        0 |          0 |
| Junio      |    0 |        0 |          0 |
| Julio      |    0 |        0 |          0 |
| Agosto     |    0 |        0 |          0 |
| Septiembre |    0 |        0 |          0 |
| Octubre    |    0 |        0 |          0 |
| Noviembre  |    0 |        0 |          0 |
| Diciembre  |    0 |        0 |          0 |

Los valores comienzan en `0` porque inicialmente no hay ninguna venta registrada.
#  Lista de meses

El programa también utiliza una lista llamada `meses` para almacenar los nombres de los 12 meses:

```python
meses = [
    "Enero",
    "Febrero",
    "Marzo",
    "Abril",
    "Mayo",
    "Junio",
    "Julio",
    "Agosto",
    "Septiembre",
    "Octubre",
    "Noviembre",
    "Diciembre"
]
```

Esta lista permite mostrar el nombre del mes al usuario.

Por ejemplo:

```python
meses[0]
```

corresponde a:

```text
Enero
```

#  Lista de departamentos

Los departamentos se almacenan en otra lista:

```python
departamentos = [
    "Ropa",
    "Deportes",
    "Juguetería"
]
```

Cada departamento corresponde a una columna del arreglo:

| Índice | Departamento |
| -----: | ------------ |
|      0 | Ropa         |
|      1 | Deportes     |
|      2 | Juguetería   |



#  1. Insertar una venta

La función:

```python
def insertar_venta():
```

permite registrar una nueva venta.

Primero se muestran los meses disponibles:

```text
1 - Enero
2 - Febrero
3 - Marzo
4 - Abril
5 - Mayo
6 - Junio
7 - Julio
8 - Agosto
9 - Septiembre
10 - Octubre
11 - Noviembre
12 - Diciembre
```

Después el usuario selecciona el número del mes.

También se muestran los departamentos:

```text
1 - Ropa
2 - Deportes
3 - Juguetería
```

Finalmente se solicita el valor de la venta.

La información se guarda dentro del arreglo mediante:

```python
ventas[opcion_mes - 1][opcion_departamento - 1] = venta
```

Se utiliza `-1` porque en Python los índices comienzan desde `0`, mientras que las opciones que ve el usuario comienzan desde `1`.

### Ejemplo

Si el usuario selecciona:

```text
Mes: 1 - Enero
Departamento: 1 - Ropa
Venta: $1500
```

El programa guarda:

```python
ventas[0][0] = 1500
```

Esto significa:

**Enero → Ropa → $1500**

#  2. Buscar una venta

La función:

```python
def buscar_venta():
```

permite consultar una venta específica.

El usuario selecciona el mes y el departamento que desea consultar.

Después el programa obtiene el valor almacenado:

```python
venta = ventas[opcion_mes - 1][opcion_departamento - 1]
```

Por ejemplo, si se selecciona:

```text
Mes: Enero
Departamento: Ropa
```

el programa puede mostrar:

```text
Resultado de la búsqueda:

Mes: Enero
Departamento: Ropa
Venta: $1500.0
```

# 🗑️ 3. Eliminar una venta

La función:

```python
def eliminar_venta():
```

permite eliminar una venta registrada.

Primero se guarda temporalmente el valor de la venta:

```python
venta = ventas[opcion_mes - 1][opcion_departamento - 1]
```

Después se cambia el valor por `0`:

```python
ventas[opcion_mes - 1][opcion_departamento - 1] = 0
```

En este programa, `0` representa que no existe una venta registrada en esa posición.

Finalmente, el programa muestra la venta que fue eliminada.


#  4. Mostrar todas las ventas

La función:

```python
def mostrar_ventas():
```

permite visualizar todas las ventas registradas.

La información se presenta en forma de tabla:

```text
==============================================================
                    TABLA DE VENTAS
==============================================================
Mes                  Ropa       Deportes        Juguetería
-----------------------------------------------------------
Enero             $1500.00       $2500.00          $800.00
Febrero           $2000.00       $1800.00         $1200.00
Marzo             $1750.00       $2200.00          $950.00
-----------------------------------------------------------
```

Para recorrer los meses se utiliza:

```python
for i in range(12):
```

Y para acceder a cada departamento:

```python
ventas[i][0]
ventas[i][1]
ventas[i][2]
```

Donde:

```text
[0] → Ropa
[1] → Deportes
[2] → Juguetería
```

#  5. Menú principal

El programa utiliza un ciclo `while` para mantener activo el menú:

```python
while True:
```

El menú cuenta con cinco opciones:

```text
========================================
       SISTEMA DE VENTAS MENSUALES
========================================
1. Insertar una venta
2. Buscar una venta
3. Eliminar una venta
4. Mostrar todas las ventas
5. Salir
========================================
```

Dependiendo de la opción seleccionada, se ejecuta una función diferente.

```python
if opcion == "1":
    insertar_venta()

elif opcion == "2":
    buscar_venta()

elif opcion == "3":
    eliminar_venta()

elif opcion == "4":
    mostrar_ventas()

elif opcion == "5":
    print("\nPrograma finalizado.")
    break
```

La instrucción `break` permite salir del ciclo `while` y finalizar el programa.


#  Conceptos de programación utilizados

##  Listas

Las listas permiten almacenar los meses y los departamentos.

```python
meses = [...]
departamentos = [...]
```

##  Arreglo bidimensional

El arreglo `ventas` permite almacenar información utilizando filas y columnas.

```python
ventas[fila][columna]
```

##  Funciones

Las funciones permiten dividir el programa en diferentes tareas:

```python
insertar_venta()
buscar_venta()
eliminar_venta()
mostrar_ventas()
```

##  Ciclo `for`

Se utiliza para recorrer los meses y departamentos.

```python
for i in range(12):
```

##  Ciclo `while`

Se utiliza para mantener activo el menú principal:

```python
while True:
```

##  Condicionales

Se utilizan para determinar qué opción seleccionó el usuario:

```python
if
elif
else
```

##  Entrada de datos

Se utiliza `input()` para recibir información del usuario:

```python
opcion = input("Selecciona una opción: ")
```

##  Conversión de datos

Se utiliza `int()` para convertir datos a números enteros:

```python
int(input())
```

Y `float()` para introducir valores de ventas con decimales:

```python
float(input())
```

---

#  Ejemplo de funcionamiento

Primero aparece el menú:

```text
========================================
       SISTEMA DE VENTAS MENSUALES
========================================
1. Insertar una venta
2. Buscar una venta
3. Eliminar una venta
4. Mostrar todas las ventas
5. Salir
========================================
```

Si seleccionamos:

```text
1
```

podemos registrar una venta.

Por ejemplo:

```text
Selecciona el número del mes: 1
Selecciona el departamento: 1
Ingresa el valor de la venta: $1500
```

El programa guarda:

```python
ventas[0][0] = 1500
```

Después podemos utilizar la opción `4` para mostrar todas las ventas y comprobar que la información fue almacenada correctamente.


#  Cómo ejecutar el programa

Primero se debe descargar o clonar el repositorio.

Después entrar a la carpeta del proyecto:

```bash
cd estructura
```

Finalmente ejecutar:

```bash
python arreglo_tarea.py
```

En algunos equipos puede ser necesario utilizar:

```bash
python3 arreglo_tarea.py
```

#  Estructura del repositorio

```text
estructura/
│
├── arreglo_tarea.py
│
└── README.md
```

###  arreglo_tarea.py

Contiene el código fuente del programa.

###  README.md

Contiene la documentación y explicación del proyecto.

#  Conclusión

Este proyecto permitió desarrollar un sistema sencillo para administrar las ventas mensuales de una tienda.

La parte principal del programa es el uso de un **arreglo bidimensional de 12 × 3**, donde las filas representan los meses y las columnas representan los departamentos.

También se practicó el uso de funciones, listas, ciclos, condicionales, índices y entrada de datos.

El programa cuenta con un menú interactivo que permite **insertar, buscar, eliminar y mostrar las ventas**, haciendo que la información pueda ser administrada de una manera sencilla.

Este ejercicio ayuda a comprender de manera práctica cómo funcionan los **arreglos bidimensionales en Python** y cómo pueden utilizarse para organizar información.

#  Autora

**Abigail Chel**

 **Gracias por visitar este repositorio.**
