import pandas as pd 
"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta.
"""

# pylint: disable=import-outside-toplevel


def pregunta_01():
    """
    Construya y retorne un dataframe de Pandas a partir del archivo
    'files/input/clusters_report.txt'. Los requierimientos son los siguientes:

    - El dataframe tiene la misma estructura que el archivo original.
    - Los nombres de las columnas deben ser en minusculas, reemplazando los
      espacios por guiones bajos.
    - Las palabras clave deben estar separadas por coma y con un solo
      espacio entre palabra y palabra.


    """
    from pathlib import Path
    import re
    
    clusters = []
    file_path = Path(__file__).parent.parent / "files/input/clusters_report.txt"
    with open(file_path, "r", encoding="utf-8") as f:
        lines = f.readlines()
        
    for line in lines:
        if not line.strip() or line.strip().startswith("---") or "Cluster" in line or "palabras" in line:
            continue
            
        match = re.match(r'^\s*(\d+)\s+(\d+)\s+([\d,]+)\s*%\s+(.*)', line)
        if match:
            cluster_num = int(match.group(1))
            cantidad = int(match.group(2))
            porcentaje = float(match.group(3).replace(",", "."))
            words = match.group(4).strip()
            
            clusters.append({
                "cluster": cluster_num,
                "cantidad_de_palabras_clave": cantidad,
                "porcentaje_de_palabras_clave": porcentaje,
                "principales_palabras_clave": words
            })
        else:
            if clusters:
                clusters[-1]["principales_palabras_clave"] += " " + line.strip()
                
    for cluster in clusters:
        text = cluster["principales_palabras_clave"]
        if text.endswith("."):
            text = text[:-1]
        keywords = [re.sub(r'\s+', ' ', k.strip()) for k in text.split(",")]
        cluster["principales_palabras_clave"] = ", ".join(keywords)
        
    df = pd.DataFrame(clusters)
    return df