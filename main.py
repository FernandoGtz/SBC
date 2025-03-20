import pandas as pd

def generar_reglas(excel_file, output_file):
    # Leer el archivo de Excel (ignorar columnas vacías)
    df = pd.read_excel(excel_file, index_col=0).dropna(how='all').dropna(axis=1, how='all')

    reglas = []

    # Iterar sobre cada columna (regiones)
    for region in df.columns:
        condiciones = []

        # Iterar sobre cada fila (preguntas)
        for pregunta, valor in df[region].items():
            if str(valor).strip().lower() == 'x':  # Verifica si hay una 'x'
                condiciones.append(str(pregunta))  # Asegura que la pregunta sea texto

        # Generar la regla si hay condiciones
        if condiciones:
            regla = f"IF {' & '.join(condiciones)} THEN '{region}'"
            reglas.append(regla)

    # Escribir las reglas en un archivo .txt
    with open(output_file, 'w') as f:
        for regla in reglas:
            f.write(regla + '\n')

    print(f"Reglas generadas exitosamente en '{output_file}'")

# Ejemplo de uso
generar_reglas("tabla10.xlsx", "reglas_turismo.txt")
