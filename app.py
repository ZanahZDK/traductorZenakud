from flask import Flask, render_template, request, jsonify

app = Flask(__name__, static_folder='static', template_folder='templates')

# Función para cargar los significados desde un archivo
def cargar_significados(archivo):
    significados = {}
    try:
        with open(archivo, 'r') as file:
            for line in file:
                parte = line.strip().split(' = ')
                if len(parte) == 2:
                    combinacion, significado = parte
                    significados[combinacion] = significado
    except Exception as e:
        print(f"Error al cargar el archivo: {e}")
    return significados

# Función para traducir el texto usando los significados cargados
def traducir_texto(texto, significados):
    letras_permitidas = {'A', 'D', 'E', 'J', 'K', 'M', 'N', 'O', 'S', 'W'}
    texto = texto.upper()  # Normalizar a mayúsculas para consistencia
    texto_set = set(texto)
    letras_no_permitidas = texto_set - letras_permitidas

    if letras_no_permitidas:
        letras_no_permitidas_str = ', '.join(sorted(letras_no_permitidas))
        return f"Zenakud solo usa las letras: A, D, E, J, K, M, N, O, S, W. Por favor, elimina las siguientes letras: {letras_no_permitidas_str}"

    traduccion = []
    i = 0
    while i < len(texto):
        parte = texto[i:min(i+5, len(texto))]  # Considerar hasta 5 caracteres
        encontrado = False

        # Intentar extraer combinaciones de acuerdo a la longitud máxima permitida y ajustando por tipos
        for j in range(len(parte), 0, -1):
            segmento = texto[i:i+j]
            if segmento in significados:
                if (len(segmento) == 1 or 
                    len(segmento) == 2 or 
                    (3 <= len(segmento) <= 5 and not (segmento[-1] == segmento[-2] == segmento[-3]))):
                    traduccion.append(significados[segmento])
                    i += j
                    encontrado = True
                    break

        if not encontrado:  # Si no encuentra ninguna combinación válida, avanzar un carácter
            i += 1

    return ' '.join(traduccion)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/traducir', methods=['POST'])
def traducir():
    data = request.get_json()
    texto = data.get('texto', '')
    significados = cargar_significados('words.txt')
    texto_set = set(texto.upper())
    traduccion = traducir_texto(texto, significados)
    return jsonify({'traduccion': traduccion})

if __name__ == '__main__':
    app.run(debug=True)
