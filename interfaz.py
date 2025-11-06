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
        self.cesar_desp.insert(0, "")
        
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

        ctk.CTkButton(
            btn_frame, 
            text="DESCIFRAR", 
            command=self.cesar_descifrar,
            width=150,
            height=40,
            font=ctk.CTkFont(size=13, weight="bold"),
            fg_color="#f72585",
            hover_color="#d11a66"
        ).pack(side="left", padx=5)

        # RESULTADO
        ctk.CTkLabel(tab, text="Resultado:", font=ctk.CTkFont(size=14, weight="bold"), text_color="#00d4ff").pack(anchor="w", padx=20, pady=(10, 5))
        
        self.cesar_resultado = ctk.CTkTextbox(tab, height=100, font=ctk.CTkFont(size=12))
        self.cesar_resultado.pack(fill="both", expand=True, padx=20, pady=(5, 20))

    def crear_pestaña_hill(self):
        tab = self.tabview.tab("  HILL  ")
        
        # TEXTO DE ENTRADA
        ctk.CTkLabel(tab, text="Texto:", font=ctk.CTkFont(size=14, weight="bold")).pack(anchor="w", padx=20, pady=(10, 5))
        
        self.hill_texto = ctk.CTkTextbox(tab, height=80, font=ctk.CTkFont(size=12))
        self.hill_texto.pack(fill="x", padx=20, pady=5)
        
        # MATRIZ 2x2
        ctk.CTkLabel(tab, text="Matriz Clave 2x2:", font=ctk.CTkFont(size=14, weight="bold")).pack(anchor="w", padx=20, pady=(15, 5))
        
        matriz_frame = ctk.CTkFrame(tab, fg_color="transparent")
        matriz_frame.pack(pady=10)

        # FILA 1
        fila1_frame = ctk.CTkFrame(matriz_frame, fg_color="transparent")
        fila1_frame.pack(pady=5)
        
        ctk.CTkLabel(fila1_frame, text="[", font=ctk.CTkFont(size=24)).pack(side="left", padx=5)
        self.hill_a = ctk.CTkEntry(fila1_frame, width=60, justify="center", font=ctk.CTkFont(size=16))
        self.hill_a.pack(side="left", padx=5)
        self.hill_a.insert(0, "")
        
        self.hill_b = ctk.CTkEntry(fila1_frame, width=60, justify="center", font=ctk.CTkFont(size=16))
        self.hill_b.pack(side="left", padx=5)
        self.hill_b.insert(0, "")
        ctk.CTkLabel(fila1_frame, text="]", font=ctk.CTkFont(size=24)).pack(side="left", padx=5)
        
        # FILA 2
        fila2_frame = ctk.CTkFrame(matriz_frame, fg_color="transparent")
        fila2_frame.pack(pady=5)
        
        ctk.CTkLabel(fila2_frame, text="[", font=ctk.CTkFont(size=24)).pack(side="left", padx=5)
        self.hill_c = ctk.CTkEntry(fila2_frame, width=60, justify="center", font=ctk.CTkFont(size=16))
        self.hill_c.pack(side="left", padx=5)
        self.hill_c.insert(0, "")
        
        self.hill_d = ctk.CTkEntry(fila2_frame, width=60, justify="center", font=ctk.CTkFont(size=16))
        self.hill_d.pack(side="left", padx=5)
        self.hill_d.insert(0, "")
        ctk.CTkLabel(fila2_frame, text="]", font=ctk.CTkFont(size=24)).pack(side="left", padx=5)

        # BOTONES
        btn_frame = ctk.CTkFrame(tab, fg_color="transparent")
        btn_frame.pack(pady=15)
        
        ctk.CTkButton(
            btn_frame, 
            text="CIFRAR", 
            command=self.hill_cifrar,
            width=150,
            height=40,
            font=ctk.CTkFont(size=13, weight="bold"),
            fg_color="#00d4ff",
            hover_color="#00a8cc",
            text_color="black"
        ).pack(side="left", padx=5)
        
        ctk.CTkButton(
            btn_frame, 
            text="DESCIFRAR", 
            command=self.hill_descifrar,
            width=150,
            height=40,
            font=ctk.CTkFont(size=13, weight="bold"),
            fg_color="#f72585",
            hover_color="#d11a66"
        ).pack(side="left", padx=5)
        
        # RESULTADO
        ctk.CTkLabel(tab, text="Resultado:", font=ctk.CTkFont(size=14, weight="bold"), text_color="#00d4ff").pack(anchor="w", padx=20, pady=(10, 5))
        
        self.hill_resultado = ctk.CTkTextbox(tab, height=80, font=ctk.CTkFont(size=12))
        self.hill_resultado.pack(fill="both", expand=True, padx=20, pady=(5, 20))

    def crear_pestaña_rsa(self):
        tab = self.tabview.tab("  RSA  ")
        # FRAME DE GENERACIÓN DE CLAVES
        keys_frame = ctk.CTkFrame(tab)
        keys_frame.pack(fill="x", padx=20, pady=15)
        
        keys_title = ctk.CTkLabel(keys_frame, text="Generación de Claves", font=ctk.CTkFont(size=15, weight="bold"))
        keys_title.pack(pady=(10, 5))
        
        keys_control = ctk.CTkFrame(keys_frame, fg_color="transparent")
        keys_control.pack(pady=10)
        
        ctk.CTkLabel(keys_control, text="Bits:", font=ctk.CTkFont(size=13)).pack(side="left", padx=5)
        
        self.rsa_bits = ctk.CTkEntry(keys_control, width=60, justify="center")
        self.rsa_bits.pack(side="left", padx=5)
        self.rsa_bits.insert(0, "")

        # BOTONES GENERAR CLAVES
        ctk.CTkButton(
            keys_control,
            text="GENERAR CLAVES",
            command=self.rsa_generar_claves,
            width=150,
            font=ctk.CTkFont(size=12, weight="bold"),
            fg_color="#7209b7",
            hover_color="#5a0794"
        ).pack(side="left", padx=10)
        
        self.rsa_keys_label = ctk.CTkLabel(
            keys_frame,
            text="[!] No hay claves generadas",
            font=ctk.CTkFont(size=11),
            text_color="#fca311"
        )
        self.rsa_keys_label.pack(pady=(5, 10))
        
        # TEXTO DE ENTRADA
        ctk.CTkLabel(tab, text="Texto:", font=ctk.CTkFont(size=14, weight="bold")).pack(anchor="w", padx=20, pady=(10, 5))
        
        self.rsa_texto = ctk.CTkTextbox(tab, height=80, font=ctk.CTkFont(size=12))
        self.rsa_texto.pack(fill="x", padx=20, pady=5)
        
        # BOTONES CIFRAR/DESCIFRAR
        btn_frame = ctk.CTkFrame(tab, fg_color="transparent")
        btn_frame.pack(pady=15)
        
        ctk.CTkButton(
            btn_frame, 
            text="CIFRAR", 
            command=self.rsa_cifrar,
            width=150,
            height=40,
            font=ctk.CTkFont(size=13, weight="bold"),
            fg_color="#00d4ff",
            hover_color="#00a8cc",
            text_color="black"
        ).pack(side="left", padx=5)
        
        ctk.CTkButton(
            btn_frame, 
            text="DESCIFRAR", 
            command=self.rsa_descifrar,
            width=150,
            height=40,
            font=ctk.CTkFont(size=13, weight="bold"),
            fg_color="#f72585",
            hover_color="#d11a66"
        ).pack(side="left", padx=5)
        
        # RESULTADO
        ctk.CTkLabel(tab, text="Resultado:", font=ctk.CTkFont(size=14, weight="bold"), text_color="#00d4ff").pack(anchor="w", padx=20, pady=(10, 5))
        
        self.rsa_resultado = ctk.CTkTextbox(tab, height=100, font=ctk.CTkFont(size=11, family="Courier"))
        self.rsa_resultado.pack(fill="both", expand=True, padx=20, pady=(5, 20))

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
        if not texto:
            messagebox.showwarning("[!] ADVERTENCIA", "INGRESE UN TEXTO PARA CIFRAR")
            return
        
        try:
            matriz = [
                int(self.hill_a.get()),
                int(self.hill_b.get()),
                int(self.hill_c.get()),
                int(self.hill_d.get())
            ]
            resultado = hill_cifrado(texto, matriz)
            if resultado:
                self.hill_resultado.delete("1.0", "end")
                self.hill_resultado.insert("1.0", resultado)
            else:
                messagebox.showerror("[!] ERROR", 
                    f"MATRIZ NO INVERSIBLE EN mod {N}\n\n" +
                    "LA MATRIZ DEBE SER INVERSIBLE EN mod 27.\n" +
                    "INTENTE CON OTRA COMBINACIÓN DE VALORES.")
        except ValueError:
            messagebox.showerror("[!] ERROR", "INGRESE VALORES VÁLIDOS PARA LA MATRIZ")

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
            resultado = hill_descifrado(texto, matriz)
            if resultado:
                self.hill_resultado.delete("1.0", "end")
                self.hill_resultado.insert("1.0", resultado)
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