"""
Laboratorio de Programación Básica en Python para Manejo de Datos
-----------------------------------------------------------------------------------------

Este archivo contiene las preguntas que se van a realizar en el laboratorio.

No puede utilizar pandas, numpy o scipy. Se debe utilizar solo las funciones de python
básicas.

Utilice el archivo `data.csv` para resolver las preguntas.


"""


def pregunta_01():
    # Inicializar la suma
    suma_segunda_columna = 0

    # Abrir el archivo en modo lectura
    with open('data.csv', 'r') as file:
        # Iterar sobre cada línea del archivo
        for line in file:
            # Dividir la línea en columnas usando el tabulador como delimitador
            columns = line.strip().split('\t')
            # Convertir el valor de la segunda columna a entero y sumarlo
            suma_segunda_columna += int(columns[1])

    return suma_segunda_columna

# Ejecutar la función y mostrar el resultado
print(pregunta_01())




def pregunta_02():
    # Diccionario para almacenar la cantidad de registros por letra
    registros_por_letra = {}

    # Abrir el archivo en modo lectura
    with open('data.csv', 'r') as file:
        # Iterar sobre cada línea del archivo
        for line in file:
            # Obtener la primera letra de la línea
            letra = line.strip().split('\t')[0]

            # Incrementar la cantidad de registros para la letra actual
            registros_por_letra[letra] = registros_por_letra.get(letra, 0) + 1

    # Convertir el diccionario a una lista de tuplas y ordenar alfabéticamente
    lista_registros_por_letra = sorted(registros_por_letra.items())

    return lista_registros_por_letra

# Ejecutar la función y mostrar el resultado
print(pregunta_02())




def pregunta_03():
    # Diccionario para almacenar la suma de la columna 2 por letra
    suma_por_letra = {}

    # Abrir el archivo en modo lectura
    with open('data.csv', 'r') as file:
        # Iterar sobre cada línea del archivo
        for line in file:
            # Obtener la primera letra y el valor de la columna 2
            letra, valor = line.strip().split('\t')[:2]
            valor = int(valor)

            # Sumar el valor al acumulado de la letra
            suma_por_letra[letra] = suma_por_letra.get(letra, 0) + valor

    # Convertir el diccionario a una lista de tuplas y ordenar alfabéticamente
    suma_por_letra_ordenada = sorted(suma_por_letra.items())

    return suma_por_letra_ordenada

# Ejecutar la función y mostrar el resultado
print(pregunta_03())



def pregunta_04():
    # Diccionario para almacenar la cantidad de registros por mes
    registros_por_mes = {}

    # Abrir el archivo en modo lectura
    with open('data.csv', 'r') as file:
        # Iterar sobre cada línea del archivo
        for line in file:
            # Obtener el mes de la fecha en la columna 3
            mes = line.strip().split('\t')[2].split('-')[1]

            # Incrementar la cantidad de registros para el mes actual
            registros_por_mes[mes] = registros_por_mes.get(mes, 0) + 1

    # Convertir el diccionario a una lista de tuplas y ordenar alfabéticamente por mes
    lista_registros_por_mes = sorted(registros_por_mes.items())

    return lista_registros_por_mes

# Ejecutar la función y mostrar el resultado
print(pregunta_04())



def pregunta_05():
    # Diccionario para almacenar el valor máximo y mínimo de la columna 2 por letra de la columna 1
    max_min_por_letra = {}

    # Abrir el archivo en modo lectura
    with open('data.csv', 'r') as file:
        # Iterar sobre cada línea del archivo
        for line in file:
            # Obtener la letra de la columna 1 y el valor de la columna 2
            letra, valor = line.strip().split('\t')[:2]
            valor = int(valor)

            # Actualizar el valor máximo y mínimo para la letra actual
            if letra not in max_min_por_letra:
                max_min_por_letra[letra] = [valor, valor]
            else:
                max_min_por_letra[letra][0] = max(max_min_por_letra[letra][0], valor)
                max_min_por_letra[letra][1] = min(max_min_por_letra[letra][1], valor)

    # Convertir el diccionario a una lista de tuplas y ordenar alfabéticamente por la letra de la columna 1
    lista_max_min_por_letra = [(letra, max_min[0], max_min[1]) for letra, max_min in max_min_por_letra.items()]
    lista_max_min_por_letra.sort(key=lambda x: x[0])  # Ordenar alfabéticamente por la letra de la columna 1

    return lista_max_min_por_letra

# Ejecutar la función y mostrar el resultado
print(pregunta_05())



def pregunta_06():
    # Diccionario para almacenar los valores asociados a cada clave
    valores_por_clave = {}

    # Abrir el archivo en modo lectura
    with open('data.csv', 'r') as file:
        # Iterar sobre cada línea del archivo
        for line in file:
            # Dividir la línea en columnas usando el tabulador como delimitador
            columns = line.strip().split('\t')
            # Obtener los valores de la columna 5
            valores_columna_5 = columns[4].split(',')

            # Iterar sobre cada valor de la columna 5
            for valor in valores_columna_5:
                clave, valor_asociado = valor.split(':')
                valor_asociado = int(valor_asociado)

                # Actualizar el valor mínimo y máximo asociado a la clave
                if clave not in valores_por_clave:
                    valores_por_clave[clave] = [valor_asociado, valor_asociado]
                else:
                    valores_por_clave[clave][0] = min(valores_por_clave[clave][0], valor_asociado)
                    valores_por_clave[clave][1] = max(valores_por_clave[clave][1], valor_asociado)

    # Convertir el diccionario a una lista de tuplas y ordenar alfabéticamente por la clave
    lista_valores_por_clave = [(clave, valores[0], valores[1]) for clave, valores in valores_por_clave.items()]
    lista_valores_por_clave.sort(key=lambda x: x[0])  # Ordenar alfabéticamente por la clave

    return lista_valores_por_clave

# Ejecutar la función y mostrar el resultado
print(pregunta_06())




def pregunta_07():
    # Diccionario para almacenar las letras asociadas a cada valor de la columna 2
    letras_por_valor = {}

    # Abrir el archivo en modo lectura
    with open('data.csv', 'r') as file:
        # Iterar sobre cada línea del archivo
        for line in file:
            # Dividir la línea en columnas usando el tabulador como delimitador
            columns = line.strip().split('\t')
            valor_columna_2 = int(columns[1])
            letra_columna_1 = columns[0]

            # Si el valor de la columna 2 no está en el diccionario, agregarlo con una lista vacía
            if valor_columna_2 not in letras_por_valor:
                letras_por_valor[valor_columna_2] = []

            # Agregar la letra de la columna 1 a la lista asociada al valor de la columna 2
            letras_por_valor[valor_columna_2].append(letra_columna_1)

    # Convertir el diccionario a una lista de tuplas y ordenarla por el valor de la columna 2
    lista_letras_por_valor = [(valor, letras) for valor, letras in letras_por_valor.items()]
    lista_letras_por_valor.sort(key=lambda x: x[0])  # Ordenar por el valor de la columna 2

    return lista_letras_por_valor

# Ejecutar la función y mostrar el resultado
print(pregunta_07())


def pregunta_08():
    # Diccionario para almacenar los conjuntos de letras asociadas a cada valor de la columna 2
    letras_por_valor = {}

    # Abrir el archivo en modo lectura
    with open('data.csv', 'r') as file:
        # Iterar sobre cada línea del archivo
        for line in file:
            # Dividir la línea en columnas usando el tabulador como delimitador
            columns = line.strip().split('\t')
            valor_columna_2 = int(columns[1])
            letra_columna_1 = columns[0]

            # Si el valor de la columna 2 no está en el diccionario, agregarlo con un conjunto vacío
            if valor_columna_2 not in letras_por_valor:
                letras_por_valor[valor_columna_2] = set()

            # Agregar la letra de la columna 1 al conjunto asociado al valor de la columna 2
            letras_por_valor[valor_columna_2].add(letra_columna_1)

    # Convertir el diccionario a una lista de tuplas
    lista_letras_por_valor = [(valor, sorted(letras)) for valor, letras in letras_por_valor.items()]

    # Ordenar la lista de tuplas por el valor de la columna 2
    lista_letras_por_valor.sort(key=lambda x: x[0])

    return lista_letras_por_valor

# Ejecutar la función y mostrar el resultado
print(pregunta_08())


def pregunta_09():
    # Diccionario para almacenar la cantidad de registros por clave de la columna 5
    conteo_claves = {}

    # Abrir el archivo en modo lectura
    with open('data.csv', 'r') as file:
        # Iterar sobre cada línea del archivo
        for line in file:
            # Dividir la línea en columnas usando el tabulador como delimitador
            columns = line.strip().split('\t')
            claves_columna_5 = columns[4].split(',')

            # Iterar sobre cada clave en la columna 5
            for clave in claves_columna_5:
                # Obtener la clave sin el valor numérico
                clave_sin_valor = clave.split(':')[0]

                # Incrementar el conteo para la clave actual
                conteo_claves[clave_sin_valor] = conteo_claves.get(clave_sin_valor, 0) + 1

    # Ordenar el diccionario por las claves alfabéticamente
    conteo_claves_ordenado = dict(sorted(conteo_claves.items(), key=lambda x: x[0]))

    return conteo_claves_ordenado

# Ejecutar la función y mostrar el resultado
print(pregunta_09())

def pregunta_10():
    # Lista para almacenar las tuplas con un índice de orden
    tuplas_con_indice = []

    # Abrir el archivo en modo lectura
    with open('data.csv', 'r') as file:
        # Iterar sobre cada línea del archivo
        for idx, line in enumerate(file):
            # Dividir la línea en columnas usando el tabulador como delimitador
            columns = line.strip().split('\t')
            letra_columna_1 = columns[0]
            elementos_columna_4 = columns[3].split(',')
            elementos_columna_5 = columns[4].split(',')

            # Obtener la cantidad de elementos de las columnas 4 y 5
            cantidad_elementos_columna_4 = len(elementos_columna_4)
            cantidad_elementos_columna_5 = len(elementos_columna_5)

            # Agregar la tupla con el índice de orden
            tuplas_con_indice.append((idx, letra_columna_1, cantidad_elementos_columna_4, cantidad_elementos_columna_5))

    # Ordenar la lista de tuplas según el índice de orden
    tuplas_con_indice.sort(key=lambda x: x[0])

    # Eliminar el índice de orden y devolver la lista de tuplas
    lista_tuplas = [(tupla[1], tupla[2], tupla[3]) for tupla in tuplas_con_indice]
    return lista_tuplas

# Ejecutar la función y mostrar el resultado
print(pregunta_10())





def pregunta_11():
    # Diccionario para almacenar la suma de la columna 2 para cada letra de la columna 4
    suma_por_letra = {}

    # Abrir el archivo en modo lectura
    with open('data.csv', 'r') as file:
        # Iterar sobre cada línea del archivo
        for line in file:
            # Dividir la línea en columnas usando el tabulador como delimitador
            columns = line.strip().split('\t')
            # Obtener la letra de la columna 4 y la suma de la columna 2
            letras_columna_4 = columns[3]

            # Iterar sobre cada letra de la columna 4
            for letra in letras_columna_4:
                # Verificar si la letra es del alfabeto
                if letra.isalpha():
                    # Actualizar la suma para la letra en el diccionario
                    suma_por_letra[letra] = suma_por_letra.get(letra, 0) + int(columns[1])

    # Ordenar el diccionario alfabéticamente por las claves
    suma_por_letra_ordenada = dict(sorted(suma_por_letra.items()))

    return suma_por_letra_ordenada

# Ejecutar la función y mostrar el resultado
print(pregunta_11())


def pregunta_12():
    # Diccionario para almacenar la suma de los valores de la columna 5 para cada letra de la columna 1
    suma_por_letra = {}

    # Abrir el archivo en modo lectura
    with open('data.csv', 'r') as file:
        # Iterar sobre cada línea del archivo
        for line in file:
            # Dividir la línea en columnas usando el tabulador como delimitador
            columns = line.strip().split('\t')
            # Verificar si la línea tiene al menos cinco elementos (incluyendo la columna 5)
            if len(columns) >= 5:
                # Obtener la letra de la columna 1
                letra_columna_1 = columns[0]
                # Decodificar el diccionario de la columna 5
                dictionary = columns[4].split(',')
                # Iterar sobre cada par clave-valor del diccionario
                for item in dictionary:
                    # Dividir el par clave-valor usando el carácter ':'
                    _, value = item.split(':')
                    # Sumar el valor al diccionario por letra de la columna 1
                    suma_por_letra[letra_columna_1] = suma_por_letra.get(letra_columna_1, 0) + int(value)

    # Ordenar el diccionario por las claves
    suma_por_letra_ordenada = dict(sorted(suma_por_letra.items()))

    return suma_por_letra_ordenada

# Ejecutar la función y mostrar el resultado
print(pregunta_12())
