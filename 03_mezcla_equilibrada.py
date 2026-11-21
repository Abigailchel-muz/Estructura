# Mezcla equilibrada natural de dos vías con archivos auxiliares.
# Cada línea de un archivo JSONL representa una secuencia ordenada.
import json
from pathlib import Path
from tempfile import TemporaryDirectory

def secuencias_naturales(datos):
    if not datos:
        return []
    secuencias = [[datos[0]]]
    for valor in datos[1:]:
        if valor >= secuencias[-1][-1]:
            secuencias[-1].append(valor)
        else:
            secuencias.append([valor])
    return secuencias

def fusionar(a, b):
    salida = []
    i = j = 0
    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            salida.append(a[i]); i += 1
        else:
            salida.append(b[j]); j += 1
    return salida + a[i:] + b[j:]

def escribir(ruta, secuencias):
    with ruta.open('w', encoding='utf-8') as archivo:
        for secuencia in secuencias:
            archivo.write(json.dumps(secuencia) + '\n')

def leer(ruta):
    with ruta.open(encoding='utf-8') as archivo:
        return [json.loads(linea) for linea in archivo if linea.strip()]

def mezcla_equilibrada(datos):
    secuencias = secuencias_naturales(datos)
    with TemporaryDirectory() as carpeta:
        a = Path(carpeta) / 'auxiliar_a.jsonl'
        b = Path(carpeta) / 'auxiliar_b.jsonl'
        pasada = 0
        while len(secuencias) > 1:
            pasada += 1
            escribir(a, secuencias[::2])
            escribir(b, secuencias[1::2])
            izquierda, derecha = leer(a), leer(b)
            secuencias = []
            for indice, bloque in enumerate(izquierda):
                if indice < len(derecha):
                    secuencias.append(fusionar(bloque, derecha[indice]))
                else:
                    secuencias.append(bloque)
            print(f'Pasada {pasada}:', secuencias)
    return secuencias[0] if secuencias else []

if __name__ == '__main__':
    folios = [101, 105, 110, 103, 107, 115, 102, 109, 120]
    print('Original:', folios)
    print('Ordenado:', mezcla_equilibrada(folios))
