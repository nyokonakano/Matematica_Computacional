# Matematica_Computacional
# CYPHER - Sistema de Criptografía

<div align="center">

![Version](https://img.shields.io/badge/version-1.0-blue)
![Python](https://img.shields.io/badge/python-3.8+-green)
![License](https://img.shields.io/badge/license-MIT-orange)

**Sistema completo de criptografía con tres algoritmos clásicos: César, Hill y RSA**

[Características](#-características) • [Instalación](#-instalación) • [Uso](#-uso) • [Compilar](#-compilar-a-exe)

</div>

---

## Descripción

**CYPHER** es un sistema de criptografía educativo y funcional que implementa tres algoritmos de cifrado:

- **Cifrado César**: Cifrado por sustitución simple con desplazamiento
- **Cifrado Hill**: Cifrado por bloques usando álgebra matricial (2x2)
- **Cifrado RSA**: Criptografía asimétrica de clave pública

El proyecto incluye dos interfaces:
- **Consola**: Menú interactivo en terminal
- **Interfaz Gráfica**: GUI moderna con CustomTkinter

---

## Características

### Cifrado César
- Desplazamiento configurable (0-27)
- Alfabeto español
- Cifrado y descifrado instantáneo

### Cifrado Hill
- Matriz de cifrado 2x2
- Validación de invertibilidad en MOD 27
- Manejo automático de texto impar (padding con 'X')

### Cifrado RSA
- Generación automática de claves
- Tamaño de bits configurable (8-32)
- Test de primalidad de Miller-Rabin
- Visualización de claves pública y privada

### Interfaz Gráfica
- Tema oscuro moderno
- Pestañas organizadas por algoritmo
- Validación de entrada en tiempo real
- Mensajes de error descriptivos

---

## Estructura del Proyecto

```
MATEMATICA_COMPUTACIONAL/
│
├── cifrado-de-datos.ico    # Ícono de la aplicación
├── interfaz.py              # Interfaz gráfica (CustomTkinter)
├── proyecto.py              # Módulo principal con algoritmos
└── README.md                # Documentación
```

---

## Instalación

### Requisitos Previos
- Python 3.8 o superior
- pip (gestor de paquetes de Python)

### 1. Clonar o descargar el proyecto
```bash
git clone https://github.com/tu-usuario/cypher.git
cd MATEMATICA_COMPUTACIONAL
```

### 2. Instalar dependencias

#### Para usar la interfaz gráfica:
```bash
pip install customtkinter
```

#### Para compilar a .exe (opcional):
```bash
pip install pyinstaller
```

---

## Uso

### Opción 1: Interfaz de Consola
```bash
python proyecto.py
```

**Menú interactivo:**
```
╔════════════════════════════════════════════════════════════╗
║   ██████╗██╗   ██╗██████╗ ██╗  ██╗███████╗██████╗        ║
║  ██╔════╝╚██╗ ██╔╝██╔══██╗██║  ██║██╔════╝██╔══██╗       ║
║  ██║      ╚████╔╝ ██████╔╝███████║█████╗  ██████╔╝       ║
║  ██║       ╚██╔╝  ██╔═══╝ ██╔══██║██╔══╝  ██╔══██╗       ║
║  ╚██████╗   ██║   ██║     ██║  ██║███████╗██║  ██║       ║
║   ╚═════╝   ╚═╝   ╚═╝     ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝       ║
╚════════════════════════════════════════════════════════════╝

1. CIFRADO CÉSAR
2. CIFRADO HILL
3. CIFRADO RSA
0. SALIR
```

### Opción 2: Interfaz Gráfica
```bash
python interfaz.py
```

**Características de la GUI:**
- Pestañas separadas para cada algoritmo
- Campos de entrada y resultado claramente identificados
- Botones de cifrar/descifrar con íconos
- Validación automática de entradas

---

## Ejemplos de Uso

### Cifrado César
```python
# Importar módulo
from proyecto import cifrado_cesar, descifrar_cesar

# Cifrar
texto = "HOLA MUNDO"
cifrado = cifrado_cesar(texto, 3)
print(cifrado)  # Output: KROD PXQGR

# Descifrar
descifrado = descifrar_cesar(cifrado, 3)
print(descifrado)  # Output: HOLA MUNDO
```

### Cifrado Hill
```python
from proyecto import hill_cifrado, hill_descifrado

# Matriz clave [3, 3]
#              [2, 5]
matriz = [3, 3, 2, 5]

# Cifrar
texto = "HOLA"
cifrado = hill_cifrado(texto, matriz)
print(cifrado)  # Output: ZEQE

# Descifrar
descifrado = hill_descifrado(cifrado, matriz)
print(descifrado)  # Output: HOLA
```

### Cifrado RSA
```python
from proyecto import generar_claves_rsa, cifrar_rsa, descifrar_rsa

# Generar claves
clave_publica, clave_privada = generar_claves_rsa(bits=16)

# Cifrar
texto = "HOLA"
cifrado = cifrar_rsa(texto, clave_publica)
print(cifrado)  # Output: [12345, 67890, 11223, 44556]

# Descifrar
descifrado = descifrar_rsa(cifrado, clave_privada)
print(descifrado)  # Output: HOLA
```

---

## Compilar a .exe

### Paso 1: Asegurar que tienes PyInstaller
```bash
pip install pyinstaller
```

### Paso 2: Compilar con ícono
```bash
pyinstaller --onefile --windowed --icon=cifrado-de-datos.ico --name=CYPHER interfaz.py
```

### Paso 3: Incluir el módulo principal
```bash
pyinstaller --onefile --windowed --icon=cifrado-de-datos.ico --name=CYPHER --add-data "proyecto.py;." interfaz.py
```

### Parámetros explicados:
- `--onefile`: Genera un único archivo .exe
- `--windowed`: Oculta la consola (solo GUI)
- `--icon`: Usa tu ícono personalizado
- `--name`: Nombre del ejecutable
- `--add-data`: Incluye archivos adicionales

### Resultado:
```
dist/
└── CYPHER.exe  ← ¡Tu aplicación lista para distribuir!
```

---

## Solución de Problemas

### Error: "No module named 'customtkinter'"
```bash
pip install customtkinter
```

### Error: "No module named 'proyecto'"
Asegúrate de que `proyecto.py` esté en la misma carpeta que `interfaz.py`

### El .exe no abre
- Verifica que usaste `--windowed` para aplicaciones GUI
- Usa `--hidden-import=customtkinter` si hay problemas con CustomTkinter:
```bash
pyinstaller --onefile --windowed --hidden-import=customtkinter --icon=cifrado-de-datos.ico --name=CYPHER interfaz.py
```

### Matriz Hill no es invertible
La matriz debe cumplir: `det(matriz) mod 27 ≠ 0` y `gcd(det, 27) = 1`

**Matrices válidas de ejemplo:**
- [3, 3, 2, 5]
- [5, 8, 7, 11]
- [9, 4, 5, 7]

---

## Algoritmos Implementados

### Cifrado César
```
C = (P + k) mod 27
P = (C - k) mod 27
```
- `C`: Texto cifrado
- `P`: Texto plano
- `k`: Desplazamiento (clave)

### Cifrado Hill
```
C = (K × P) mod 27
P = (K⁻¹ × C) mod 27
```
- `K`: Matriz clave 2×2
- `K⁻¹`: Inversa de K en mod 27

### RSA
```
Cifrado: C = M^e mod n
Descifrado: M = C^d mod n
```
- `(e, n)`: Clave pública
- `(d, n)`: Clave privada
- `n = p × q` (producto de dos primos)

---

## Alfabeto Utilizado

```python
ALFABETO = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"  # 27 caracteres
```

**Nota:** El sistema incluye el alfabeto español.

---

## Autor

Desarrollado por el Grupo 6 para el curso de **Matemática Computacional**



<div align="center">


</div>
