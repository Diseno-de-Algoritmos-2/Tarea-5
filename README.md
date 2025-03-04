# **Tarea 5**

Este repositorio contiene la implementación de dos algoritmos para la construcción de arreglos de sufijos (Suffix Arrays), uno utilizando sufijos explícitos y otro implícitos. El programa implementa un arreglo de sufijos para buscar múltiples cadenas en un texto dado. Debe recibir un archivo con el texto y otro con las cadenas de consulta, devolviendo las posiciones de cada consulta en el texto, separadas por tabulador, en un archivo de salida estándar. Para resolverlo, se: (1) construyo un arreglo de sufijos sin almacenar explícitamente los sufijos, ordenando directamente las posiciones de inicio en el texto; (2) se desarrollo una función que use búsqueda binaria para encontrar las posiciones de cada consulta en el texto.

## **Autores**

- Vargas Ulloa, Daniel Felipe - d.vargasu@uniandes.edu.co
- Bobadilla Suarez, Santiago - s.bobadilla@uniandes.edu.co
- Ariza Lopez, Lina Marcela - l.arizal@uniandes.edu.co

---

## **Descripción del Problema**

El objetivo es implementar dos versiones de arreglos de sufijos para buscar sub-cadenas de un texto dado. La primera versión utiliza sufijos explícitos, mientras que la segunda utiliza sufijos implícitos, permitiendo comparar la eficiencia de ambos enfoques.

## **Estructura del Problema**

El repositorio contiene los siguientes archivos:

1. **Algoritmos de Solución:**

   - `sufixArray_explicit.py`: Implementación del arreglo de sufijos usando sufijos explícitos
   - `suffixArray_inexplicit.py`: Implementación del arreglo de sufijos usando sufijos implícitos

2. **Archivos de Entrada y Salida:**
   - `input.txt`: Contiene el texto donde se realizará la búsqueda
   - `subchain_query.txt`: Contiene los patrones a buscar
   - `output.txt`: Contiene los resultados de las búsquedas

---

## **Formato de los Archivos**

### **Archivo de Entrada (`input.txt`)**

Contiene el texto donde se realizarán las búsquedas. Ejemplo:

```
AGACTACGATGGCGCCAACTCAATCGCAGCTC...
```

### **Archivo de Consultas (`subchain_query.txt`)**

Contiene los patrones a buscar, uno por línea. Ejemplo:

```
AGC
CTA
GCT
```

### **Archivo de Salida (`output.txt`)**

Muestra los resultados de las búsquedas en el formato:

```
Results of subchain queries:
The results are in the format 'pattern    start_position'.

AGC    346
CTA    3
GCT    295
```

---

## **Ejemplo de Ejecución**

### **Comando de Ejecución - Versión Explícita**

```bash
python sufixArray_explicit.py
```

### **Comando de Ejecución - Versión Implícita**

```bash
python suffixArray_inexplicit.py
```

---

## **Estrategia de Solución**

1. **Versión Explícita**:

   - Genera una lista de todos los sufijos del texto como cadenas completas
   - Ordena los sufijos lexicográficamente
   - Mantiene un registro de las posiciones originales

2. **Versión Implícita**:

   - Trabaja directamente con las posiciones de inicio de los sufijos
   - Utiliza comparaciones parciales de cadenas durante el ordenamiento
   - Reduce el uso de memoria al no almacenar los sufijos completos

3. **Búsqueda de Patrones**:

   - Implementa búsqueda binaria sobre el arreglo de sufijos
   - Retorna la posición donde se encuentra el patrón o -1 si no existe

4. **Análisis Experimental**:

   | Tamaño del Texto | Número de Consultas | Tiempo (Implícito) | Tiempo (Explícito) |
   | ---------------- | ------------------- | ------------------ | ------------------ |
   | 100000           | 1000                | 0.00000 seconds    | 0.01028 seconds    |
   | 1000000          | 10000               | 0.00719 seconds    | 0.00603 seconds    |
   | 10000000         | 100000              | 0.01140 seconds    | 0.00690 seconds    |

## **Instalación/Configuración**

### **Requisitos**

- Python 3.x
- Módulos estándar de Python (sys, time)

### **Instalación en Windows**

1. **Instalar Python 3**:
   - Descargar Python desde [python.org](https://www.python.org/downloads/)
   - Durante la instalación, seleccionar "Add Python to PATH"

### **Instalación en Ubuntu**

```bash
sudo apt update
sudo apt install python3
```

## **Ejecución del Programa**

1. Preparar los archivos de entrada:

   - Crear `input.txt` con el texto a analizar
   - Crear `subchain_query.txt` con los patrones a buscar

2. Ejecutar el programa deseado:

```bash
python sufixArray_explicit.py
# o
python suffixArray_inexplicit.py
```

3. Revisar los resultados en `output.txt`

---

## **Análisis de Complejidad**

### **Versión Explícita**

- Construcción del arreglo: O(n² log n) // El método sort() de Python usa Timsort.
- Búsqueda de patrones: O(m log n) donde n es la longitud del texto y m la longitud del patrón

### **Versión Implícita**

- Construcción del arreglo: O(n log n)
- Búsqueda de patrones: O(m log n) donde n es la longitud del texto y m la longitud del patrón
