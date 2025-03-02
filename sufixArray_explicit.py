import sys
import time

# ---
# Leer el texto de entrada desde un archivo
# ---
def read_text(file_path):
    # Abre el archivo en modo lectura y lee todo el contenido
    with open(file_path, 'r') as file:
        # Retorna el contenido del archivo sin espacios en blanco al inicio y al final
        return file.read().strip()

# ---
# Construir una lista de cadenas con todos los sufijos del texto original
# ---
def generate_suffixes(text):
    # Genera una lista de tuplas con cada sufijo del texto y su posición inicial
    return [(text[i:], i) for i in range(len(text))]

# ---
# Ordenar la lista de sufijos (lexicográficamente)
# ---
def sort_suffixes(suffixes):
    # Ordena la lista de sufijos en orden lexicográfico
    suffixes.sort()
    return suffixes

# ---
# Retornar un arreglo de enteros con las posiciones de inicio de los diferentes sufijos
# ---
def build_suffix_array(text):
    # Genera la lista de sufijos
    suffixes = generate_suffixes(text)
    # Ordena la lista de sufijos
    sorted_suffixes = sort_suffixes(suffixes)
    # Extrae y retorna las posiciones iniciales de los sufijos ordenados
    suffix_array = [suffix[1] for suffix in sorted_suffixes]
    return suffix_array

# ---
# Busca un patrón en el texto usando el array de sufijos.
# ---
def search_pattern(text, pattern, suffix_array):
    
    
    left, right = 0, len(suffix_array)
    # Realiza una búsqueda binaria en el array de sufijos
    while left < right:
        mid = (left + right) // 2
        # Verifica si el patrón coincide con el sufijo en la posición actual
        if text[suffix_array[mid]:].startswith(pattern):
            return suffix_array[mid]
        # Ajusta los límites de la búsqueda binaria
        elif text[suffix_array[mid]:] < pattern:
            left = mid + 1
        else:
            right = mid
    # Retorna -1 si el patrón no se encuentra
    return -1

# ---
# Escribir los resultados en un archivo de salida
# ---
def write_results(output_file, results):
    # Abre el archivo en modo escritura
    with open(output_file, 'w') as file:
        # Escribe una pequeña descripción de los resultados y el formato de salida
        file.write("Results of subchain queries:\n")
        file.write("The results are in the format 'pattern\tstart_position'.\n\n")
        
        
        # Escribe cada resultado en una nueva línea del archivo
        for result in results:
            file.write(result + '\n')

# ---
# Función principal que lee el texto y las consultas de patrones desde archivos,
# construye el arreglo de sufijos, busca los patrones y escribe los resultados en un archivo de salida.
# ---
def main():
    # comienza a contar el tiempo de ejecución
    start_time = time.time()
    
    # Lee el texto desde el archivo 'input.txt'
    text = read_text('input.txt')
    # Construye el arreglo de sufijos para el texto leído
    suffix_array = build_suffix_array(text)
    
    # Lee las consultas de patrones desde el archivo 'subchain_query.txt'
    with open('subchain_query.txt', 'r') as file:
        queries = file.readlines()
    
    results = []
    # Busca cada patrón en el texto usando el arreglo de sufijos
    for query in queries:
        query = query.strip()
        position = search_pattern(text, query, suffix_array)
        # Guarda el resultado de la búsqueda en la lista de resultados
        if position != -1:
            results.append(f"{query}\t{position}")
        else:
            results.append(f"{query}\tNot Found")
    
    output_file = 'output.txt'
    if len(sys.argv) > 1:
        output_file = sys.argv[1]
        print(f"Writing results to '{output_file}'.")
    else:
        print("Output file name not provided. Writing results to 'output.txt'.")

    # Escribe los resultados en el archivo de salida
    write_results(output_file, results)
    
    # imprime el tiempo de ejecución redondeado a 5 decimales
    end_time = time.time()
    
    print()
    print("Execution time: {:.5f} seconds".format(end_time - start_time))

if __name__ == "__main__":
    main()