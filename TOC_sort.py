import re

def ordenar_markdown(markdown):
    # Extraer encabezados con su contenido
    pattern = re.compile(r'^(#+\s+.*)(?:\n(.*?))?(?=^#+\s+|\Z)', re.DOTALL | re.MULTILINE)
    secciones = []

    for match in pattern.finditer(markdown):
        encabezado = match.group(1).strip()
        contenido = match.group(2).strip() if match.group(2) else ''
        nivel = len(re.match(r'^(#+)', encabezado).group(1))
        secciones.append({'nivel': nivel, 'texto': encabezado, 'contenido': contenido, 'hijos': []})

    # Construir estructura jerárquica
    estructura = []
    pila = []

    for seccion in secciones:
        while pila and pila[-1]['nivel'] >= seccion['nivel']:
            pila.pop()

        if pila:
            pila[-1]['hijos'].append(seccion)
        else:
            estructura.append(seccion)

        pila.append(seccion)

    # Ordenar de manera recursiva
    def ordenar_nodos(nodos):
        nodos.sort(key=lambda x: x['texto'].lower())
        for nodo in nodos:
            ordenar_nodos(nodo['hijos'])

    ordenar_nodos(estructura)

    # Reconstruir Markdown con contenido incluido
    def reconstruir_markdown(nodos):
        resultado = []
        for nodo in nodos:
            resultado.append(nodo['texto'])
            if nodo['contenido']:
                resultado.append(nodo['contenido'])
            resultado.extend(reconstruir_markdown(nodo['hijos']))
        return resultado

    lineas_ordenadas = reconstruir_markdown(estructura)
    return '\n\n'.join(lineas_ordenadas)

# 📥 Leer el contenido desde un archivo
def leer_markdown(nombre_archivo):
    with open(nombre_archivo, 'r', encoding='utf-8') as archivo:
        return archivo.read()

# 📤 Guardar el resultado en un archivo
def guardar_markdown(nombre_archivo, contenido):
    with open(nombre_archivo, 'w', encoding='utf-8') as archivo:
        archivo.write(contenido)

# 📌 Ejecutar el ordenamiento
entrada = '/home/egarriga/Documents/markdown-TOC/entrada.md'  # Archivo de entrada
salida = '/home/egarriga/Documents/markdown-TOC/salida.md'    # Archivo de salida

markdown = leer_markdown(entrada)
markdown_ordenado = ordenar_markdown(markdown)
guardar_markdown(salida, markdown_ordenado)

print(f"El Markdown ha sido ordenado y guardado en '{salida}'.")
