import sys
import os
import time
import matplotlib.pyplot as plt
from statistics import mean

current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)

try:
    from sufixArray_explicit import main as explicit_main
    from suffixArray_inexplicit import main as implicit_main
except ImportError as e:
    print(f"Error importando módulos: {e}")
    print(f"Directorio actual: {os.getcwd()}")
    print(f"Python path: {sys.path}")
    sys.exit(1)

def run_monte_carlo(num_iterations=30):
    # Configuración de tamaños y consultas
    text_sizes = [100_000, 1_000_000, 10_000_000]
    query_counts = [1_000, 10_000, 100_000]
    
    # Diccionarios para almacenar resultados
    results = {
        'explicit': {(s,q):[] for s in text_sizes for q in query_counts},
        'implicit': {(s,q):[] for s in text_sizes for q in query_counts}
    }
    
    # Ejecutar pruebas
    for iteration in range(num_iterations):
        print(f"Iteración {iteration + 1}/{num_iterations}")
        for size in text_sizes:
            for queries in query_counts:
                # Usar archivos existentes
                input_file = f"input_{size}.txt"
                query_file = f"subchain_query_{queries}.txt"
                
                # Ejecutar versión explícita
                os.system(f"copy {input_file} ../input.txt")
                os.system(f"copy {query_file} ../subchain_query.txt")
                start = time.time()
                explicit_main()
                explicit_time = time.time() - start
                results['explicit'][(size,queries)].append(explicit_time)
                
                # Ejecutar versión implícita
                start = time.time()
                implicit_main()
                implicit_time = time.time() - start
                results['implicit'][(size,queries)].append(implicit_time)
    
    # Calcular promedios
    averages = {
        'explicit': {k:mean(v) for k,v in results['explicit'].items()},
        'implicit': {k:mean(v) for k,v in results['implicit'].items()}
    }
    
    # Imprimir tabla de resultados
    print("\nResultados Promedio:")
    print("Tamaño del Texto\tNúmero de Consultas\tTiempo (Implícito)\tTiempo (Explícito)")
    print("-" * 80)
    for size in text_sizes:
        for queries in query_counts:
            print(f"{size}\t\t{queries}\t\t{averages['implicit'][(size,queries)]:.5f}s\t\t{averages['explicit'][(size,queries)]:.5f}s")
    
    # Crear gráfica de dispersión
    plt.figure(figsize=(12, 8))
    
    # Preparar datos para la gráfica
    x_implicit = []
    y_implicit = []
    x_explicit = []
    y_explicit = []
    
    for size in text_sizes:
        for queries in query_counts:
            # Datos para implícito
            x_implicit.extend([size] * len(results['implicit'][(size,queries)]))
            y_implicit.extend(results['implicit'][(size,queries)])
            
            # Datos para explícito
            x_explicit.extend([size] * len(results['explicit'][(size,queries)]))
            y_explicit.extend(results['explicit'][(size,queries)])
    
    plt.scatter(x_implicit, y_implicit, alpha=0.5, label='Implícito', color='blue')
    plt.scatter(x_explicit, y_explicit, alpha=0.5, label='Explícito', color='red')
    
    plt.xlabel('Tamaño del Texto')
    plt.ylabel('Tiempo de Ejecución (segundos)')
    plt.title('Comparación de Rendimiento: Implícito vs Explícito')
    plt.legend()
    plt.xscale('log')
    plt.yscale('log')
    plt.grid(True)
    plt.savefig('performance_comparison.png')
    plt.close()

    # 3D plot
        # Preparar datos para la gráfica 3D
    # Para cada prueba se almacenan: tamaño de texto, número de consultas y tiempo de ejecución.
    x_implicit, y_implicit, z_implicit = [], [], []
    x_explicit, y_explicit, z_explicit = [], [], []
    
    for size in text_sizes:
        for queries in query_counts:
            for t in results['implicit'][(size, queries)]:
                x_implicit.append(size)
                y_implicit.append(queries)
                z_implicit.append(t)
            for t in results['explicit'][(size, queries)]:
                x_explicit.append(size)
                y_explicit.append(queries)
                z_explicit.append(t)
    
    # Crear figura y eje 3D
    fig = plt.figure(figsize=(12, 8))
    ax = fig.add_subplot(111, projection='3d')
    
    # Graficar puntos para implícito y explícito
    ax.scatter(x_implicit, y_implicit, z_implicit, alpha=0.5, label='Implícito', color='blue')
    ax.scatter(x_explicit, y_explicit, z_explicit, alpha=0.5, label='Explícito', color='red')
    
    # Configurar etiquetas y título
    ax.set_xlabel('Tamaño del Texto')
    ax.set_ylabel('Número de Consultas')
    ax.set_zlabel('Tiempo de Ejecución (segundos)')
    ax.set_title('Comparación de Rendimiento 3D: Implícito vs Explícito')
    
    ax.legend()
    ax.grid(True)
    plt.savefig('performance_comparison_all.png')
    plt.show()
    plt.close()

if __name__ == "__main__":
    run_monte_carlo()