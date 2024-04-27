import os
import tkinter as tk
from tkinter import messagebox
from database import Database

class GestorStock:
    def __init__(self, root, db):
        self.root = root
        self.root.title("Gestor de Stock")
        self.db = db

        # Componentes da janela principal
        self.label_titulo = tk.Label(root, text="Lista de Produtos")
        self.label_titulo.pack(pady=10)

        self.lista_produtos = tk.Listbox(root, selectmode=tk.SINGLE, height=23, width=100)
        self.atualizar_lista_produtos()
        self.lista_produtos.pack(pady=10)

        self.botao_redirecionar = tk.Button(root, text="Inserir produto", command=self.redirecionar_pagina)
        self.botao_redirecionar.pack(pady=10)

        self.botao_redirecionar_e = tk.Button(root, text="Encomendas", command=self.redirecionar_pagina_e)
        self.botao_redirecionar_e.pack(pady=10)

        # Centralizar os botões na tela
        root.update_idletasks()
        largura_botao_redirecionar = self.botao_redirecionar.winfo_reqwidth()
        largura_botao_redirecionar_e = self.botao_redirecionar_e.winfo_reqwidth()
        largura_total = largura_botao_redirecionar + largura_botao_redirecionar_e + 10  # Adicionando algum espaçamento

        x = (root.winfo_width() - largura_total) // 2
        self.botao_redirecionar.pack_configure(side=tk.LEFT, anchor=tk.CENTER, padx=(x, 5))
        self.botao_redirecionar_e.pack_configure(side=tk.LEFT, anchor=tk.CENTER, padx=(5, x))

    def redirecionar_pagina(self):
        self.root.destroy()
        os.system("python inserir.py")

    def redirecionar_pagina_e(self):
        self.root.destroy()
        os.system("python encomendas.py")

    def atualizar_lista_produtos(self):
        # Limpar a lista de produtos
        self.lista_produtos.delete(0, tk.END)
        # Obter os produtos da base de dados
        produtos = self.db.obter_produtos()
        # Adicionar produtos à lista
        for produto in produtos:
            texto_produto = f"ref: {produto[0]} - {produto[1]} - qnt: {produto[2]}"
            self.lista_produtos.insert(tk.END, texto_produto)

if __name__ == "__main__":
    try:
        root = tk.Tk()
        # Ajustar o tamanho da pagina
        largura = 800
        altura = 500
        x = (root.winfo_screenwidth() - largura) // 2
        y = (root.winfo_screenheight() - altura) // 2
        root.geometry(f"{largura}x{altura}+{x}+{y}")

        # Criar a instância da classe Database
        db = Database()

        app = GestorStock(root, db)
        root.mainloop()

    except Exception as e:
        print(f"Erro: {e}")



