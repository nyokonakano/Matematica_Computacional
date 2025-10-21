#import tkinter as tk
#from tkinter import ttk, messagebox, scrolledtext
import math

ALFABETO = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
N = len(ALFABETO)

###############################################
#             FUNCIONES AUXILIARES            #
###############################################
def mod_inverse(a, m):
    """HALLA EL INVERSO MULTIPLICATIVO DE a EN MOD m"""
    if math.gcd(a, m) != 1:
        raise ValueError(f"[!] ERROR! NO EXISTE EL INVERSO MODULAR DE {a} EN MOD {m}")
    m0, x0, x1 = m, 0, 1
    while a > 1:
        q = a // m
        m, a = a % m, m
        x0, x1 = x1 - q * x0, x0
    return x1 % m0

def num_to_char(num):
    """CONVIERTE UN NUMERO A SU EQUIVALENTE CARACTER"""
    return ALFABETO[num % N]

def char_to_num(char):
    """CONVIERTE UN CARACTER A SU EQUIVALENTE NUMERICO"""
    char = char.upper()
    if char in ALFABETO:
        return ALFABETO.index(char)
    return -1

def limpiar_texto(texto):
    """LIMPIA EL TEXTO DE CARACTERES NO VALIDOS"""
    return ''.join([c.upper() for c in texto if c.upper() in ALFABETO])

###############################################
#             FUNCIONES PRINCIPALES           #
###############################################
def cifrado_cesar(texto, desplazamiento):
    """CIFRA USANDO EL MÉTODO CÉSAR"""
    resultado = ""
    for char in texto.upper():
        if char in ALFABETO:
            indice = ALFABETO.index(char)
            nuevo_indice = (indice + desplazamiento) % N
            resultado += ALFABETO[nuevo_indice]
        else:
            resultado += char
    return resultado

def descifrar_cesar(texto, desplazamiento):
    """DESCIFRA USANDO EL MÉTODO CÉSAR"""
    return cifrado_cesar(texto, -desplazamiento)

def hill_cifrado(texto, matriz_clave):
    """CIFRA USANDO MATRIZ DE 2x2 EN MOD 27"""
    texto = limpiar_texto(texto)
    if len(matriz_clave) != 4:
        raise ValueError("[!] ERROR! LA MATRIZ DEBE CONTENER 4 ELEMENTOS [A,B,C,D]")
    a, b, c, d = matriz_clave

    det = (a * d - b * c) % N
    if math.gcd(det, N) != 1:
        raise ValueError(f"[!] ERROR! LA MATRIZ NO ES INVERTIBLE EN MOD {N}")

    if len(texto) % 2 != 0:
        texto += 'X'

    resultado = ""
    for i in range(0, len(texto), 2):
        p1 = char_to_num(texto[i])
        p2 = char_to_num(texto[i + 1])
        c1 = (a * p1 + b * p2) % N
        c2 = (c * p1 + d * p2) % N
        resultado += num_to_char(c1) + num_to_char(c2)
    return resultado

def hill_descifrado(texto, matriz_clave):
    """DESCIFRA USANDO MATRIZ DE 2x2 EN MOD 27"""
    texto = limpiar_texto(texto)
    if len(matriz_clave) != 4:
        raise ValueError("[!] LA MATRIZ DEBE TENER 4 ELEMENTOS [A,B,C,D]")
    a, b, c, d = matriz_clave

    det = (a * d - b * c) % N
    if math.gcd(det, N) != 1:
        raise ValueError(f"[!] LA MATRIZ NO ES INVERTIBLE EN MOD {N}")

    det_inv = mod_inverse(det, N)
    a_inv = (det_inv * d) % N
    b_inv = (det_inv * (-b)) % N
    c_inv = (det_inv * (-c)) % N
    d_inv = (det_inv * a) % N

    resultado = ""
    for i in range(0, len(texto), 2):
        c1 = char_to_num(texto[i])
        c2 = char_to_num(texto[i + 1])
        p1 = (a_inv * c1 + b_inv * c2) % N
        p2 = (c_inv * c1 + d_inv * c2) % N
        resultado += num_to_char(p1) + num_to_char(p2)
    return resultado

###############################################
#                    MENÚS                    #
###############################################
def menu_cesar():
    print("\n========== CIFRADO CÉSAR ==========")
    print("1. CIFRAR TEXTO")
    print("2. DESCIFRAR TEXTO")
    opcion = input("SELECCIONE UNA OPCIÓN: ").strip().upper()

    texto = input("INGRESE EL TEXTO: ").upper()
    desplazamiento = int(input("INGRESE EL DESPLAZAMIENTO: "))

    if opcion == "1":
        cifrado = cifrado_cesar(texto, desplazamiento)
        print(f"\n[+] TEXTO CIFRADO: {cifrado}")
    elif opcion == "2":
        descifrado = descifrar_cesar(texto, desplazamiento)
        print(f"\n[+] TEXTO DESCIFRADO: {descifrado}")
    else:
        print("[!] OPCIÓN NO VÁLIDA.")

def menu_hill():
    print("\n========== CIFRADO HILL ==========")
    texto = input("INGRESE EL TEXTO: ").strip().upper()
    matriz_str = input("INGRESE LOS 4 ELEMENTOS DE LA MATRIZ CLAVE (A,B,C,D): ").strip()
    matriz = [int(x) for x in matriz_str.split(',')]

    print("\n1. CIFRAR")
    print("2. DESCIFRAR")
    opcion = input("SELECCIONE UNA OPCIÓN: ").strip().upper()

    if opcion == "1":
        resultado = hill_cifrado(texto, matriz)
        print(f"\n[+] TEXTO CIFRADO: {resultado}")
    elif opcion == "2":
        resultado = hill_descifrado(texto, matriz)
        print(f"\n[+] TEXTO DESCIFRADO: {resultado}")
    else:
        print("[!] OPCIÓN NO VÁLIDA.")

def menu_principal():
    while True:
        print("\n" + "="*45)
        print("      SISTEMA DE CRIPTOGRAFÍA EN PYTHON")
        print("="*45)
        print("1. CIFRADO CÉSAR")
        print("2. CIFRADO HILL")
        print("0. SALIR")

        opcion = input("SELECCIONE UNA OPCIÓN: ").strip().upper()
        if opcion == "1":
            menu_cesar()
        elif opcion == "2":
            menu_hill()
        elif opcion == "0":
            print("[!] SALIENDO DEL PROGRAMA...")
            break
        else:
            print("[!] OPCIÓN NO VÁLIDA.")

###############################################
#                  MAIN                       #
###############################################
if __name__ == "__main__":
    menu_principal()