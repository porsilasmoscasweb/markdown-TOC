import re

class MarkdownSortFiles:
    def __init__(self):
        self.patrones_bloques = [
            r'```.*?```',
            r"'''.*?'''",
            r'""".*?"""',
            r"'[^']*'",
            r'"[^"]*"',
            r'<!--.*?-->'
        ]
        self.bloques_ignorados = []

    def ordenar(self,
                markdown,
                ascendente=True):
        bloques_pattern = re.compile('|'.join(self.patrones_bloques), re.DOTALL)

        def reemplazar_bloque(match):
            self.bloques_ignorados.append(match.group(0))
            return f"__BLOQUE_IGNORADO_{len(self.bloques_ignorados) - 1}__"

        markdown_sin_bloques = bloques_pattern.sub(reemplazar_bloque, markdown)

        pattern = re.compile(r'^(#+\s+.*?)(?=\n#+\s+|\Z)', re.MULTILINE | re.DOTALL)
        secciones = []

        for match in pattern.finditer(markdown_sin_bloques):
            encabezado_bloque = match.group(1).strip()
            nivel = len(re.match(r'^(#+)', encabezado_bloque).group(1))
            secciones.append({
                'nivel': nivel,
                'texto': encabezado_bloque,
                'hijos': []
            })

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

        # Ordenar según el parámetro ascendente o descendente
        def ordenar_nodos(nodos):
            nodos.sort(key=lambda x: x['texto'].lower(), reverse=not ascendente)
            for nodo in nodos:
                ordenar_nodos(nodo['hijos'])

        ordenar_nodos(estructura)

        def reconstruir_markdown(nodos):
            resultado = []
            for nodo in nodos:
                resultado.append(nodo['texto'])
                resultado.extend(reconstruir_markdown(nodo['hijos']))
            return resultado

        markdown_ordenado = '\n\n'.join(reconstruir_markdown(estructura))

        def restaurar_bloques(texto):
            for i, bloque in enumerate(self.bloques_ignorados):
                texto = texto.replace(f"__BLOQUE_IGNORADO_{i}__", bloque)
            return texto

        return restaurar_bloques(markdown_ordenado)

    @staticmethod
    def leer_markdown(nombre_archivo):
        with open(nombre_archivo, 'r', encoding='utf-8') as archivo:
            return archivo.read()

    @staticmethod
    def guardar_markdown(nombre_archivo, contenido):
        with open(nombre_archivo, 'w', encoding='utf-8') as archivo:
            archivo.write(contenido)
