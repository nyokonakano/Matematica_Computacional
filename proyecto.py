#import tkinter as tk
#from tkinter import ttk, messagebox, scrolledtext
import math
import random
import sys

ALFABETO = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
N = len(ALFABETO)
###############################################
#                    LOGO                     #
###############################################

def mostrar_logo():
    """MUESTRA EL LOGO ASCII DEL SISTEMA"""
    logo = """
    ╔════════════════════════════════════════════════════════════╗
    ║                                                            ║
    ║     ██████╗██╗   ██╗██████╗ ██╗  ██╗███████╗██████╗        ║
    ║    ██╔════╝╚██╗ ██╔╝██╔══██╗██║  ██║██╔════╝██╔══██╗       ║
    ║    ██║      ╚████╔╝ ██████╔╝███████║█████╗  ██████╔╝       ║
    ║    ██║       ╚██╔╝  ██╔═══╝ ██╔══██║██╔══╝  ██╔══██╗       ║
    ║    ╚██████╗   ██║   ██║     ██║  ██║███████╗██║  ██║       ║
    ║     ╚═════╝   ╚═╝   ╚═╝     ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝       ║
    ║                                                            ║
    ║                SISTEMA DE CRIPTOGRAFÍA v1.0                ║
    ║                                                            ║
    ╚════════════════════════════════════════════════════════════╝
    """
    print(logo)

###############################################
#             FUNCIONES AUXILIARES            #
###############################################
def mod_inverse(a, m):
    """HALLA EL INVERSO MULTIPLICATIVO DE a EN MOD m"""
    if math.gcd(a, m) != 1:
        return None
    m0, x0, x1 = m, 0, 1
    while a > 1:
        q = a // m
        m, a = a % m, m
        x0, x1 = x1 - q * x0, x0
    return x1 % m0

def num_to_char(num):
    """CONVIERTE UN NÚMERO A SU EQUIVALENTE CARACTER"""
    return ALFABETO[num % N]

def char_to_num(char):
    """CONVIERTE UN CARACTER A SU EQUIVALENTE NUMÉRICO"""
    char = char.upper()
    if char in ALFABETO:
        return ALFABETO.index(char)
    return -1

def limpiar_texto(texto):
    """LIMPIA EL TEXTO DE CARACTERES NO VÁLIDOS"""
    return ''.join([c.upper() for c in texto if c.upper() in ALFABETO])

###############################################
#             FUNCIONES CÉSAR                 #
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

###############################################
#             FUNCIONES HILL                  #
###############################################
def hill_cifrado(texto, matriz_clave):
    """CIFRA USANDO MATRIZ DE 2x2 EN MOD 27"""
    texto = limpiar_texto(texto)
    if len(matriz_clave) != 4:
        print("[!] ERROR: LA MATRIZ DEBE TENER 4 ELEMENTOS [A,B,C,D]")
        return None

    a, b, c, d = matriz_clave
    det = (a * d - b * c) % N

    if math.gcd(det, N) != 1:
        print(f"[!] ALERTA: LA MATRIZ NO ES INVERTIBLE EN MOD {N}. INTENTE CON OTRA CLAVE.")
        return None

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
        print("[!] ERROR: LA MATRIZ DEBE TENER 4 ELEMENTOS [A,B,C,D]")
        return None

    a, b, c, d = matriz_clave
    det = (a * d - b * c) % N
    if math.gcd(det, N) != 1:
        print(f"[!] ALERTA: LA MATRIZ NO ES INVERTIBLE EN MOD {N}. NO SE PUEDE DESCIFRAR.")
        return None

    det_inv = mod_inverse(det, N)
    if det_inv is None:
        print("[!] ERROR: NO EXISTE INVERSO MODULAR.")
        return None

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
#             FUNCIONES RSA                   #
###############################################
def es_primo(n, k=5):
    """TEST DE PRIMALIDAD DE MILLER-RABIN"""
    if n < 2:
        return False
    if n == 2 or n == 3:
        return True
    if n % 2 == 0:
        return False
    
    r, d = 0, n - 1
    while d % 2 == 0:
        r += 1
        d //= 2
    
    for _ in range(k):
        a = random.randrange(2, n - 1)
        x = pow(a, d, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True

def generar_primo(bits=16):
    """GENERA UN NÚMERO PRIMO DE bits BITS"""
    while True:
        num = random.randrange(2**(bits-1), 2**bits)
        if es_primo(num):
            return num

def generar_claves_rsa(bits=16):
    """GENERA PAR DE CLAVES RSA (PÚBLICA Y PRIVADA)"""
    print("[*] GENERANDO NÚMEROS PRIMOS...")
    p = generar_primo(bits)
    q = generar_primo(bits)
    
    n = p * q
    phi = (p - 1) * (q - 1)
    
    e = 65537
    while math.gcd(e, phi) != 1:
        e = random.randrange(3, phi, 2)
    
    d = mod_inverse(e, phi)
    
    print(f"[+] CLAVE PÚBLICA (e, n): ({e}, {n})")
    print(f"[+] CLAVE PRIVADA (d, n): ({d}, {n})")
    
    return (e, n), (d, n)

def cifrar_rsa(texto, clave_publica):
    """CIFRA TEXTO USANDO RSA"""
    e, n = clave_publica
    texto = limpiar_texto(texto)
    
    cifrado = []
    for char in texto:
        m = char_to_num(char)
        c = pow(m, e, n)
        cifrado.append(c)
    
    return cifrado

def descifrar_rsa(cifrado, clave_privada):
    """DESCIFRA TEXTO USANDO RSA"""
    d, n = clave_privada
    
    descifrado = ""
    for c in cifrado:
        m = pow(c, d, n)
        descifrado += num_to_char(m)
    
    return descifrado

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
        if resultado:
            print(f"\n[+] TEXTO CIFRADO: {resultado}")
    elif opcion == "2":
        resultado = hill_descifrado(texto, matriz)
        if resultado:
            print(f"\n[+] TEXTO DESCIFRADO: {resultado}")
    else:
        print("[!] OPCIÓN NO VÁLIDA.")

def menu_rsa():
    print("\n========== CIFRADO RSA ==========")
    print("1. GENERAR NUEVAS CLAVES Y CIFRAR")
    print("2. USAR CLAVES EXISTENTES PARA CIFRAR")
    print("3. DESCIFRAR CON CLAVE PRIVADA")
    opcion = input("SELECCIONE UNA OPCIÓN: ").strip()

    if opcion == "1":
        bits = int(input("INGRESE TAMAÑO DE BITS PARA PRIMOS (16-32 RECOMENDADO): ") or "16")
        clave_publica, clave_privada = generar_claves_rsa(bits)
        
        texto = input("\nINGRESE EL TEXTO A CIFRAR: ").upper()
        cifrado = cifrar_rsa(texto, clave_publica)
        print(f"\n[+] TEXTO CIFRADO: {cifrado}")
        
        respuesta = input("\n¿DESEA DESCIFRAR AHORA? (S/N): ").strip().upper()
        if respuesta == "S":
            descifrado = descifrar_rsa(cifrado, clave_privada)
            print(f"[+] TEXTO DESCIFRADO: {descifrado}")
    
    elif opcion == "2":
        e = int(input("INGRESE e (EXPONENTE PÚBLICO): "))
        n = int(input("INGRESE n (MÓDULO): "))
        clave_publica = (e, n)
        
        texto = input("INGRESE EL TEXTO A CIFRAR: ").upper()
        cifrado = cifrar_rsa(texto, clave_publica)
        print(f"\n[+] TEXTO CIFRADO: {cifrado}")
    
    elif opcion == "3":
        d = int(input("INGRESE d (EXPONENTE PRIVADO): "))
        n = int(input("INGRESE n (MÓDULO): "))
        clave_privada = (d, n)
        
        cifrado_str = input("INGRESE EL TEXTO CIFRADO (LISTA DE NÚMEROS SEPARADOS POR COMAS): ")
        cifrado = [int(x.strip()) for x in cifrado_str.strip('[]').split(',')]
        
        descifrado = descifrar_rsa(cifrado, clave_privada)
        print(f"\n[+] TEXTO DESCIFRADO: {descifrado}")
    else:
        print("[!] OPCIÓN NO VÁLIDA.")

def menu_principal():
    mostrar_logo()
    while True:
        print("\n" + "="*45)
        print("      SISTEMA DE CRIPTOGRAFÍA EN PYTHON")
        print("="*45)
        print("1. CIFRADO CÉSAR")
        print("2. CIFRADO HILL")
        print("3. CIFRADO RSA")
        print("0. SALIR")

        opcion = input("SELECCIONE UNA OPCIÓN: ").strip().upper()
        if opcion == "1":
            menu_cesar()
        elif opcion == "2":
            menu_hill()
        elif opcion == "3":
            menu_rsa()
        elif opcion == "0":
            print("[!] SALIENDO DEL PROGRAMA...")
            sys.exit(0) # ESTADO DE SALIDA EXITOSA
            # sys.exit(1) # ESTADO DE SALIDA CON ERROR
        else:
            print("[!] OPCIÓN NO VÁLIDA.")

###############################################
#                  MAIN                       #
###############################################
if __name__ == "__main__":
    menu_principal()
