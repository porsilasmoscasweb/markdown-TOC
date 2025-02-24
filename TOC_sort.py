import re

class MarkdownOrdenador:
    def __init__(self):
        # Patrones de bloques de código, comillas y comentarios HTML que deben ser ignorados
        self.patrones_bloques = [
            r'```.*?```',   # Bloques de código con backticks
            r"'''.*?'''",   # Bloques con comillas simples triples
            r'""".*?"""',   # Bloques con comillas dobles triples
            r"'[^']*'",     # Comillas simples
            r'"[^"]*"',     # Comillas dobles
            r'<!--.*?-->',   # Comentarios HTML
        ]
        self.bloques_ignorados = []

    def ordenar(self, markdown):
        # Combinar todos los patrones en una sola expresión regular
        bloques_pattern = re.compile('|'.join(self.patrones_bloques), re.DOTALL)

        # Reemplazar temporalmente los bloques con marcadores
        def reemplazar_bloque(match):
            self.bloques_ignorados.append(match.group(0))
            return f"__BLOQUE_IGNORADO_{len(self.bloques_ignorados) - 1}__"

        markdown_sin_bloques = bloques_pattern.sub(reemplazar_bloque, markdown)

        # Extraer encabezados con su contenido fuera de los bloques ignorados
        pattern = re.compile(r'^(#+\s+.*)(?:\n(.*?))?(?=^#+\s+|\Z)', re.DOTALL | re.MULTILINE)
        secciones = []

        for match in pattern.finditer(markdown_sin_bloques):
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
        markdown_ordenado = '\n\n'.join(lineas_ordenadas)

        # Restaurar los bloques ignorados en su posición original
        def restaurar_bloques(texto):
            for i, bloque in enumerate(self.bloques_ignorados):
                texto = texto.replace(f"__BLOQUE_IGNORADO_{i}__", bloque)
            return texto

        return restaurar_bloques(markdown_ordenado)

    # 📥 Leer el contenido desde un archivo
    @staticmethod
    def leer_markdown(nombre_archivo):
        with open(nombre_archivo, 'r', encoding='utf-8') as archivo:
            return archivo.read()

    # 📤 Guardar el resultado en un archivo
    @staticmethod
    def guardar_markdown(nombre_archivo, contenido):
        with open(nombre_archivo, 'w', encoding='utf-8') as archivo:
            archivo.write(contenido)


# # 📌 Uso de la clase
# entrada = '/home/egarriga/Documents/markdown-TOC/entrada.md'  # Archivo de entrada
# salida = '/home/egarriga/Documents/markdown-TOC/salida.md'    # Archivo de salida
#
# # Crear instancia de la clase
# ordenador = MarkdownOrdenador()
#
# # Leer, ordenar y guardar el Markdown
# markdown = MarkdownOrdenador.leer_markdown(entrada)
# markdown_ordenado = ordenador.ordenar(markdown)
# MarkdownOrdenador.guardar_markdown(salida, markdown_ordenado)
#
# print(f"El Markdown ha sido ordenado (ignorando encabezados en bloques de código, comillas y comentarios HTML) y guardado en '{salida}'.")
