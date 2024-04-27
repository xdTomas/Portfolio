import os
import tkinter as tk
from tkinter import messagebox
from database import Database

class EfetuarEncomenda:

    def __init__(self, root, db):
        self.root = root
        self.root.title("Gestor de Stock")
        self.db = db

        self.label_titulo = tk.Label(root, text="Nova Encomenda")
        self.label_titulo.pack(pady=10)

        self.label_ref = tk.Label(root, text="Referencia do produto")
        self.label_ref.pack()
        self.entry_ref = tk.Entry(root)
        self.entry_ref.pack()

        self.label_qnt = tk.Label(root, text="Quantidade:")
        self.label_qnt.pack()
        self.entry_qnt = tk.Entry(root)
        self.entry_qnt.pack()

        self.botao_adicionar = tk.Button(root, text="Confirmar", command=self.adicionar_encomenda)
        self.botao_adicionar.pack(pady=10)

        self.botao_adicionar = tk.Button(root, text="Cancelar", command=self.cancelar)
        self.botao_adicionar.pack(pady=10)

    def adicionar_encomenda(self):
        try:
            ref_produto = self.entry_ref.get()
            quantidade = int(self.entry_qnt.get())

            detalhes_produto = self.db.obter_detalhes_produto(ref_produto)

            if detalhes_produto:
                id_produto, nome_produto, quantidade_produto = detalhes_produto
                if quantidade <= quantidade_produto:
                    
                    self.db.efetuar_encomenda(id_produto, nome_produto, quantidade)
                    messagebox.showinfo("Sucesso", "Encomenda efetuada com sucesso!")

                    nova_quantidade = quantidade_produto - quantidade
                    self.db.atualizar_produtos(id_produto, nova_quantidade)

                    self.root.destroy()
                    os.system("python encomendas.py")
                else:
                    messagebox.showerror("Erro", "Quantidade insuficiente.")
            else:
                messagebox.showerror("Erro", "Produto não encontrado!")

        except ValueError:
            messagebox.showerror("Erro", "Quantidade deve ser um número inteiro.")

    def cancelar(self):
        self.root.destroy()
        os.system("python encomendas.py")

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

    app = EfetuarEncomenda(root, db)
    root.mainloop()