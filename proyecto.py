#import tkinter as tk
#from tkinter import ttk, messagebox, scrolledtext
import math

ALFABETO = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
N = len(ALFABETO)

def limpiar_texto(texto):
    """LIMPIA EL TEXTO DE CARACTERES NO VALIDOS"""
    return ''.join([c.upper() for c in texto if c.upper() in ALFABETO])


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
    det = ((a*b)-(d*c))%N
    if math.gcd(det, N) != 1:
        raise ValueError(f"[!] ERROR! LA MATRIZ NO ES INVERTIBLE EN mod{N}. det={det}, mcd(det,{N})={math.gcd(det,N)}")

    if len(texto)%2!=0:
        texto+='X'
    
    resultado = ""
def hill_descifrado(texto, matriz_clave):
    """
    DESCIFRA USANDO MATRIZ DE 2X2 EN MOD 27
    P = K^(-1) × C (mod 27)
    """
    

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
            #COCK AQUI AÑADES EL METODO CESAR QUE VAS A HACER
            print("[!] CIFRADO CON EL METODO CESAR")
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