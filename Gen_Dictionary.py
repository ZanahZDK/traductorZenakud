import random
import os

# Las letras permitidas
letras = ['A', 'D', 'E', 'J', 'K', 'M', 'N', 'O', 'S', 'W']

# Significados especificados más algunos aleatorios generales
significados = ["no la mufes", "la mufaste", "lurker", "clutch", "xdd", "insano", "nadie nunca", "cachipun de pulpo","larga", "kru", "bora", "el deus", 
                "netu", "cuenta rut", "deposito a plazo", "tenso", "ban", "COMO", "que locura", "lineup", "mufa", "labura", "vandal", "phantom",
                "pino", "que veo", "quevedo", "mi compadre", "amaso", "amasar","poco se habla", "tay juguete", "vayan a twitter", "puras weas", "ctm","wn",
                "weon","aweonao", "no te lo creo", "apaga stream", "pero wn", "de la nada", "poco se habla wn", "poco se habla weon", "tay muy jugete", "trampolin de piojos", 
                "que buena Vela", "zapatitos de algodon"
]

# Función para generar combinaciones de letras sin más de dos repeticiones consecutivas
def generar_combinaciones(prefix, depth, max_depth):
    if depth == max_depth:
        return [prefix]
    combinaciones = []
    for letra in letras:
        # Asegurarse de no añadir más de dos letras iguales consecutivas
        if len(prefix) >= 2 and prefix[-1] == letra and prefix[-2] == letra:
            continue
        combinaciones.extend(generar_combinaciones(prefix + letra, depth + 1, max_depth))
    return combinaciones

# Generar combinaciones hasta una profundidad dada, por ejemplo 4 letras máximo
max_depth = 5
diccionario = {}
for depth in range(1, max_depth + 1):
    for palabra in generar_combinaciones('', 0, depth):
        if palabra not in diccionario:  # Asegurarse de no sobrescribir combinaciones
            diccionario[palabra] = random.choice(significados)

# Guardar el diccionario en un archivo de texto y mostrar la ruta
ruta_archivo = os.path.join(os.getcwd(), 'words.txt')
with open(ruta_archivo, 'w', encoding='utf-8') as file:
    for key, value in diccionario.items():
        file.write(f'{key} = {value}\n')

print(f'El archivo se ha guardado en: {ruta_archivo}')
