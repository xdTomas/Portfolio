import os
import tkinter as tk
from tkinter import messagebox
from database import Database  # Importe da classe Database do ficheiro database.py

class AdicionarProduto:
    def __init__(self, root, db):
        self.root = root
        self.root.title("Gestor de Stock")
        self.db = db

        self.label_titulo = tk.Label(root, text="Adicionar Produto")
        self.label_titulo.pack(pady=10)

        self.label_nome = tk.Label(root, text="Nome do Produto:")
        self.label_nome.pack()
        self.entry_nome = tk.Entry(root)
        self.entry_nome.pack()

        self.label_qnt = tk.Label(root, text="Quantidade:")
        self.label_qnt.pack()
        self.entry_qnt = tk.Entry(root)
        self.entry_qnt.pack()

        self.botao_adicionar = tk.Button(root, text="Adicionar", command=self.adicionar_produto)
        self.botao_adicionar.pack(pady=10)

        self.botao_adicionar = tk.Button(root, text="cancelar", command=self.cancelar)
        self.botao_adicionar.pack(pady=10)

    def adicionar_produto(self):
        nome_produto = self.entry_nome.get()
        qnt_produto = self.entry_qnt.get()
        if nome_produto:
            self.db.adicionar_produto(nome_produto, qnt_produto)
            messagebox.showinfo("Sucesso", f"Produto adicionado: {nome_produto}")
            self.root.destroy()
            os.system("python inventory.py")
        else:
            messagebox.showwarning("Aviso", "Por favor, insira o nome do produto.")

    def cancelar(self):
        self.root.destroy()
        os.system("python inventory.py")

if __name__ == "__main__":
    root = tk.Tk()

    # Ajustar o tamanho da pagina
    largura = 800
    altura = 500
    x = (root.winfo_screenwidth() - largura) // 2
    y = (root.winfo_screenheight() - altura) // 2
    root.geometry(f"{largura}x{altura}+{x}+{y}")

    # Criar uma instância da classe Database
    db = Database()

    app = AdicionarProduto(root, db)
    root.mainloop()