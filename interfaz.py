import customtkinter as ctk
from tkinter import messagebox

# IMPORTAR TODAS LAS FUNCIONES DEL PROYECTO
from proyecto import *

class CypherGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("SISTEMA DE CRIPTOGRAFIA")
        self.root.geometry("900x700")


        # RSA
        self.rsa_public_key = None
        self.rsa_private_key = None
        self.rsa_cifrado_actual = None

        self.crear_widgets()

    def crear_widgets(self):
        # TITULO PRINCIPAL
        title_frame = ctk.CTkFrame(self.root, height=120, fg_color="#1a1a2e")
        title_frame.pack(fill="x", padx=20, pady=20)
        title_frame.pack_propagate(False)

        title_label = ctk.CTkLabel(
            title_frame,
            text="CYPHER",
            font=ctk.CTkFont(size=40, weight="bold"),
            text_color="#00d4ff"
        )
        title_label.pack(pady=(15,5))

        subtitle_label = ctk.CTkLabel(
            title_frame,
            text="SISTEMA DE CRIPTOGRAFIA • CESAR | HILL | RSA",
            font=ctk.CTkFont(size=14),
            text_color="#a8dadc"
        )
        subtitle_label.pack()

        # PESTANAS PREINCIPALES
        self.tabview = ctk.CTkTabview(self.root, height=450)
        self.tabview.pack(fill="both", expand=True, padx=20, pady=(0, 20))

        #PESTANAS DE CIFRADO
        self.tabview.add("  CESAR  ")
        self.tabview.add("  HILL  ")
        self.tabview.add("  RSA  ")

        # CONTENIDO DE CADA PESTANA
        self.crear_pestaña_cesar()
        self.crear_pestaña_hill()
        self.crear_pestaña_rsa()
    
    def crear_pestaña_cesar(self):
        tab = self.tabview.tab("  CESAR  ")
        # TEXTO DE ENTRADA
        ctk.CTkLabel(tab, text="Texto:", font=ctk.CTkFont(size=14, weight="bold")).pack(anchor="w", padx=20, pady=(10, 5))

        # CAJA DE TEXTO
        self.cesar_texto = ctk.CTkTextbox(tab, height=100, font=ctk.CTkFont(size=12))
        self.cesar_texto.pack(fill="x", padx=20, pady=5)

        # DESPALZAMIENTO
        desp_frame = ctk.CTkFrame(tab, fg_color="transparent")
        desp_frame.pack(fill="x", padx=20, pady=10)

        ctk.CTkLabel(desp_frame, text="Desplazamiento:", font=ctk.CTkFont(size=14, weight="bold")).pack(side="left", padx=(0,10))

        self.cesar_desp = ctk.CTkEntry(desp_frame, width=100, placeholder_text="0-26")
        self.cesar_desp.pack(side="left")
        self.cesar_desp.insert(0, "0")
        
        # BOTONES
        btn_frame = ctk.CTkFrame(tab, fg_color="transparent")
        btn_frame.pack(pady=15)

        ctk.CTkButton(
            btn_frame, 
            text="CIFRAR", 
            command=self.cesar_cifrar,
            width=150,
            height=40,
            font=ctk.CTkFont(size=13, weight="bold"),
            fg_color="#00d4ff",
            hover_color="#00a8cc",
            text_color="black"
        ).pack(side="left", padx=5)

    def crear_pestaña_hill(self):
        tab = self.tabview.tab("  HILL  ")

    def crear_pestaña_rsa(self):
        tab = self.tabview.tab("  RSA  ")

###############################################
#                  METODOS                    #
###############################################
    def cesar_cifrar(self):
        texto = self.cesar_texto.get("1.0", "end").strip()
        if not texto:
            messagebox.showwarning("[!] ADVERTENCIA", "INGRESE UN TEXTO PARA CIFRAR")
            return
        
        try:
            desp = int(self.cesar_desp.get())
            resultado = cifrado_cesar(texto, desp)
            self.cesar_resultado.delete("1.0", "end")
            self.cesar_resultado.insert("1.0", resultado)
        except ValueError:
            messagebox.showerror("[!] ERROR", "EL DESPLAZAMIENTO DEBE SER UN NÚMERO ENTERO")
    
    def cesar_descifrar(self):
        texto = self.cesar_texto.get("1.0", "end").strip()
        if not texto:
            messagebox.showwarning("[!] ADVERTENCIA", "INGRESE UN TEXTO PARA DESCIFRAR")
            return
        
        try:
            desp = int(self.cesar_desp.get())
            resultado = descifrar_cesar(texto, desp)
            self.cesar_resultado.delete("1.0", "end")
            self.cesar_resultado.insert("1.0", resultado)
        except ValueError:
            messagebox.showerror("[!] ERROR", "EL DESPLAZAMIENTO DEBE SER UN NÚMERO ENTERO")

    def hill_cifrar(self):
        texto = self.hill_texto.get("1.0", "end").strip()

    def hill_descifrar(self):
        texto = self.hill_texto.get("1.0", "end").strip()
        if not texto:
            messagebox.showwarning("[!] ADVERTENCIA", "INGRESE UN TEXTO PARA DESCIFRAR")
            return
        
        try:
            matriz = [
                int(self.hill_a.get()),
                int(self.hill_b.get()),
                int(self.hill_c.get()),
                int(self.hill_d.get())
            ]
            resultado = hill_cifrar(texto, matriz)
            if resultado:
                self.hill_resultado.delete("1.0", "end")
                self.hill_resultado.delete("1.0", resultado)
            else:
                messagebox.showerror("[!] ERROR",
                    f"MATRIZ NO INVERSIBLE EN mod {N}\n\n" +
                    "LA MATRIZ DEBE SER INVERSIBLE EN mod 27.\n" +
                    "INTENTE CON OTRA COMBINACION DE VALORES."
                )

        except ValueError:
            messagebox.showerror("[!] ERROR", "INGRESE VALORES VALIDOS PARA LA MATRIZ")

    
    def rsa_generar_claves(self):
        try:
            bits = int(self.rsa_bits.get())
            if bits < 8 or bits > 32:
                messagebox.showwarning("[!] ADVERTENCIA", "USE BITS ENTRE 8 Y 32 (16 RECOMENDADO)")
                return
            
            self.rsa_public_key, self.rsa_private_key = generar_claves_rsa(bits)
            
            self.rsa_keys_label.configure(
                text=f"[+] CLAVES GENERADAS | PÚBLICA: (e={self.rsa_public_key[0]}, n={self.rsa_public_key[1]})",
                text_color="#06ffa5"
            )
            
            messagebox.showinfo("[+] CLAVES GENERADAS", 
                f"CLAVES RSA GENERADAS EXITOSAMENTE:\n\n" +
                f"CLAVE PÚBLICA (e, n):\n   {self.rsa_public_key}\n\n" +
                f"CLAVE PRIVADA (d, n):\n   {self.rsa_private_key}\n\n" +
                f"GUARDE ESTAS CLAVES EN UN LUGAR SEGURO PARA FUTURO USO.")
        except ValueError:
            messagebox.showerror("[!] ERROR", "INGRESE UN NÚMERO VÁLIDO DE BITS")
        except Exception as e:
            messagebox.showerror("[!] ERROR", f"ERROR AL GENERAR CLAVES:\n{str(e)}")

    def rsa_cifrar(self):
        if not self.rsa_public_key:
            messagebox.showwarning("[!] ADVERTENCIA", "PRIMERO DEBE GENERAR LAS CLAVES RSA")
            return
        
        texto = self.rsa_texto.get("1.0", "end").strip()
        if not texto:
            messagebox.showwarning("[!] ADVERTENCIA", "INGRESE UN TEXTO PARA CIFRAR")
            return
        
        try:
            self.rsa_cifrado_actual = cifrar_rsa(texto, self.rsa_public_key)
            self.rsa_resultado.delete("1.0", "end")
            self.rsa_resultado.insert("1.0", f"TEXTO CIFRADO:\n\n{self.rsa_cifrado_actual}")
        except Exception as e:
            messagebox.showerror("[!] ERROR", f"ERROR AL CIFRAR:\n{str(e)}")

    def rsa_descifrar(self):
        if not self.rsa_private_key:
            messagebox.showwarning("[!] ADVERTENCIA", "PRIMERO DEBE GENERAR LAS CLAVES RSA")
            return
        
        if not self.rsa_cifrado_actual:
            messagebox.showwarning("[!] ADVERTENCIA", "PRIMERO DEBE CIFRAR UN TEXTO")
            return

        try:
            resultado = descifrar_rsa(self.rsa_cifrado_actual, self.rsa_private_key)
            self.rsa_resultado.delete("1.0", "end")
            self.rsa_resultado.insert("1.0", f"TEXTO DESCIFRADO:\n\n{resultado}")
        except Exception as e:
            messagebox.showerror("[!] ERROR", f"ERROR AL DESCIFRAR:\n{str(e)}")

###############################################
#                  MAIN                       #
###############################################
if __name__ == "__main__":
    root = ctk.CTk()
    app = CypherGUI(root)
    root.mainloop()