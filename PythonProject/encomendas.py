import tkinter as tk
import os
from database import Database

class Encomendas:

    def __init__(self, root, db):
        self.root = root
        self.root.title("Gestor de Stock")
        self.db = db

        self.label_titulo = tk.Label(root, text="Encomendas")
        self.label_titulo.pack(pady=10)

        self.lista_encomendas = tk.Listbox(root, selectmode=tk.SINGLE, height=20, width=100)
        self.lista_encomendas.pack(pady=10)

        self.atualizar_lista_encomendas()

        self.botao_redirecionar = tk.Button(root, text="Efetuar encomenda", command=self.redirecionar_pagina)
        self.botao_redirecionar.pack(pady=10)

        self.botao_voltar = tk.Button(root, text="Voltar", command=self.voltar_pagina)
        self.botao_voltar.pack(pady=10)

    def atualizar_lista_encomendas(self):

        self.lista_encomendas.delete(0, tk.END)
        encomendas = self.db.obter_encomendas()
        for encomendas in encomendas:
            texto_encomendas = f"{encomendas[0]} - ref: {encomendas[1]} - qnt: {encomendas[2]}"
            self.lista_encomendas.insert(tk.END, texto_encomendas)

    def voltar_pagina(self):
        self.root.destroy()
        os.system("python inventory.py")

    def redirecionar_pagina(self):
        self.root.destroy()
        os.system("python efetuar_encomenda.py")


if __name__ == "__main__":

    try:
        root = tk.Tk()
        largura = 800
        altura = 500
        x = (root.winfo_screenwidth() - largura) // 2
        y = (root.winfo_screenheight() - altura) // 2
        root.geometry(f"{largura}x{altura}+{x}+{y}")
        db = Database()
        app = Encomendas(root, db)
        root.mainloop()

    except Exception as e:
        print(f"Erro: {e}")