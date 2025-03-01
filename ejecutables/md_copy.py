import shutil
import os


def copiar_directorio(origen, destino, ignorar=None):
    if ignorar is None:
        ignorar = []  # Lista vacía si no hay archivos a ignorar

    if not os.path.exists(destino):
        shutil.copytree(origen, destino, ignore=shutil.ignore_patterns(*ignorar))
    else:
        for item in os.listdir(origen):
            origen_item = os.path.join(origen, item)
            destino_item = os.path.join(destino, item)

            if os.path.isdir(origen_item):
                if item in ignorar:
                    continue  # Ignorar directorio
                shutil.copytree(origen_item, destino_item, dirs_exist_ok=True, ignore=shutil.ignore_patterns(*ignorar))
            else:
                if any(shutil.fnmatch.fnmatch(item, pattern) for pattern in ignorar):
                    continue  # Ignorar archivo
                shutil.copy2(origen_item, destino_item)


# 🚀 **Ejemplo de uso:**
copiar_directorio("/Users/egarriga/Git/markdown-TOC/memento", "/Users/egarriga/Git/markdown-TOC/copy", ignorar=["README.md", "footage", "*.log"])
