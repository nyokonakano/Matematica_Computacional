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
        

    def crear_pestaña_hill(self):
        tab = self.tabview.tab("  HILL  ")

    def crear_pestaña_rsa(self):
        tab = self.tabview.tab("  RSA  ")

###############################################
#                  MAIN                       #
###############################################
if __name__ == "__main__":
    root = ctk.CTk()
    app = CypherGUI(root)
    root.mainloop()