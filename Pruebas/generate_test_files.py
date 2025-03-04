import random

# --- Función para generar un texto aleatorio de tamaño dado ---
def generate_text(length):
    return ''.join(random.choices("ACGT", k=length))  # Se usa A, C, G, T para similitud con datos genómicos

# --- Función para leer un archivo ---
def read_text(file_path):
    try:
        with open(file_path, 'r') as file:
            return file.read().strip()
    except FileNotFoundError:
        print(f"Error: No se encontró el archivo {file_path}")
        return None

# --- Función para generar consultas aleatorias dentro del texto ---
def generate_queries(text, num_queries, query_length=5):
    queries = []
    text_length = len(text)
    for _ in range(num_queries):
        start_idx = random.randint(0, text_length - query_length - 1)
        queries.append(text[start_idx:start_idx + query_length])
    return queries

# --- Generar archivos de texto ---
text_sizes = [100_000, 1_000_000, 10_000_000]  # Tamaños del texto
query_counts = [1_000, 10_000, 100_000, 1_000_000]  # Cantidad de consultas

# Paso 1: Generar archivos de texto
for size in text_sizes:
    text_file = f"input_{size}.txt"
    print(f"Generando archivo de texto: {text_file}...")
    
    text = generate_text(size)  # Genera el texto
    with open(text_file, "w") as f:
        f.write(text)  # Guarda el texto en un archivo

# Paso 2: Generar archivos de consulta
for num_queries in query_counts:
    text_file = "input_1000000.txt"  # Usamos el archivo de 1 millón de caracteres como base
    text = read_text(text_file)
    
    if text is None:  # Si el archivo no existe, no se generan consultas
        print(f"No se pudo generar el archivo de consultas porque no existe {text_file}")
        continue
    
    query_file = f"subchain_query_{num_queries}.txt"
    print(f"Generando archivo de consultas: {query_file}...")

    queries = generate_queries(text, num_queries)  # Genera las consultas
    with open(query_file, "w") as f:
        f.write("\n".join(queries))  # Guarda las consultas en un archivo

print("¡Todos los archivos han sido generados correctamente!")

