#import tkinter as tk
#from tkinter import ttk, messagebox, scrolledtext
import math

ALFABETO = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
N = len(ALFABETO)
###############################################
#             FUNCIONES AUXILIARES            #
###############################################
def mod_inverse(a,m):
    """HALLA EL INVERSO MULTIPLICATIVO DE a EN MOD m"""
    if math.gcd(a,m)!=1:
        raise ValueError(f"[!] ERROR! NO EXISTE EL INVERSO MODULAR DE {a} EN mod {m}")
    m0,x0,x1=m,0,1
    while a>1:
        q=a//m
        m,a=a%m,m
        x0,x1=x1-q*x0,x0
    return x1%m0

def num_to_char(num):
    """CONVIERTE UN NUMERO A SU EQUIVALENTE CARACTER"""
    return ALFABETO[num%N]

def char_to_num(char):
    """CONVIERTE UN CARACTER A SU EQUIVALENTE NUMERICO"""
    char=char.upper()
    for char in ALFABETO:
        return ALFABETO.index(char)
    return -1

def limpiar_texto(texto):
    """LIMPIA EL TEXTO DE CARACTERES NO VALIDOS"""
    return ''.join([c.upper() for c in texto if c.upper() in ALFABETO])

def cifrado_cesar(texto, desplazamiento):
    resultado = ""
    
    for char in texto.upper(): 
        if char in ALFABETO:

            indice = ALFABETO.index(char)

            nuevo_indice = (indice + desplazamiento)  
            nuevo_indice1 = nuevo_indice % len(ALFABETO)

            if nuevo_indice >= len(ALFABETO):
                print(f"La letra '{char}' de la posición {indice} se pasa del alfabeto (mayor que 27).")
                print(f"Por lo tanto, aplicamos el módulo: {nuevo_indice} % 27 = {nuevo_indice1}\n")

            resultado += ALFABETO[nuevo_indice1]
        else:
            resultado += char

    return resultado


def descifrar_cesar(texto, desplazamiento):
    return cifrado_cesar(texto, -desplazamiento)


print("=== Cifrado César  ===")     

texto = input("Ingrese el texto a cifrar: ").upper()
clave = int(input("Ingrese el desplazamiento: "))

cifrado = cifrado_cesar(texto, clave)
descifrado = descifrar_cesar(cifrado, clave)

print("\n  Texto original:  ", texto)
print(" Texto cifrado:   ", cifrado)
print(" Texto descifrado:", descifrado)

def hill_cifrado(texto, matriz_clave):
    """
    CIFRA USANDO MATRIZ DE 2X2 EN MOD 27
    C = (K*P) MOD 27
    matriz_clave: LISTA DE 4 ELEMENTOS [a,b,c,d]
     _  _ 
    |a  b|
    |c  d|
     -  -
    """
    texto = limpiar_texto(texto)

    #VALIDAR LA MATRIZ
    if len(matriz_clave) != 4:
        raise ValueError("[!] ERROR! LA MATRIZ DEBE CONTENER 4 EELEMTOS: [a,b,c,d]")
    a,b,c,d=matriz_clave

    #HALLAR LA EDTERMINNTE PARA VER SI ES INVERTIBLE LA MARTRIZ
    det = ((a*b)-(d*c))%N # RETORNA EL ENTERO SEGUN LA CANT DE LETRAS EN EL ALFABETO
    if math.gcd(det, N) != 1:
        raise ValueError(f"[!] ERROR! LA MATRIZ NO ES INVERTIBLE EN mod{N}. det={det}, mcd(det,{N})={math.gcd(det,N)}")

    if len(texto)%2!=0:
        texto+='X'
    
    resultado = ""

    #PROCESAR DE 2 EN 2
    for i in range(0,len(texto),2):
        p1=char_to_num(texto[i])
        p2=char_to_num(texto[i+1])

        #MULTIPLICAR LA MATRIZ POR EL VECTOR
        c1=(a*p1+b*p2)%N
        c2=(c*p1+d*p2)%N
        resultado+=num_to_char(c1)+num_to_char(c2)

def hill_descifrado(texto, matriz_clave):
    """
    DESCIFRA USANDO MATRIZ DE 2X2 EN MOD 27
    P = K^(-1) × C (mod 27)
    """
def menu_cesar():
    print("\n"+"="*80)
    
def menu_hill():
    print("\n"+"="*80)

def menu_principal():
    #menu
    opcion = input("SELECCIONE UNA OPCION: ")
    print("SISTEMA DE CRIPTOGRAFIA")
    print("1. CIFRAR CON EL METODO CESAR")
    print("2. CIFRAR CON EL METODO HILL")
    print("3. SALIR")
    
    match opcion:
        case "1":
            print("[!] CIFRADO CON EL METODO CESAR")
            menu_cesar()
        case "2":
            print("[!] CIFRADO CON EL METODO HILL")
            menu_hill()
        case "3":
            print("[!] SALIENDO...")
            exit(1)
        case _:
            print("[!] OPCION NO VALIDA")
            menu_principal()
    input("\n[*] PRESIONES ENTER PARA CONTINUAR...")

if __name__ == "__main__":
    menu_principal() 