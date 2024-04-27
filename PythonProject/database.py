import sqlite3

class Database:
    def __init__(self, db_file="stock.db"):
        try:
            self.conn = sqlite3.connect(db_file, check_same_thread=False)
            self.c = self.conn.cursor()
            self.c.execute("PRAGMA foreign_keys = ON")  # Ativa suporte a chaves estrangeiras
            self.c.execute("CREATE TABLE IF NOT EXISTS produtos (id INTEGER PRIMARY KEY, nome TEXT, quantidade INTEGER)")
            self.c.execute("CREATE TABLE IF NOT EXISTS encomendas (id INTEGER PRIMARY KEY, id_produto INTEGER, nome_produto TEXT, quantidade INTEGER, FOREIGN KEY(id_produto) REFERENCES produtos(id))")

            # Adiciona a coluna nome_produto à tabela encomendas se não existir
            self.c.execute("PRAGMA table_info(encomendas)")
            columns = [column[1] for column in self.c.fetchall()]
            if 'nome_produto' not in columns:
                self.c.execute("ALTER TABLE encomendas ADD COLUMN nome_produto TEXT")

            self.conn.commit()
        except sqlite3.Error as e:
            print(f"Erro ao conectar ao banco de dados: {e}")


    # tabela produtos
    def adicionar_produto(self, nome, quantidade):
        try:
            self.c.execute("INSERT INTO produtos (nome, quantidade) VALUES (?, ?)", (nome, quantidade))
            self.conn.commit()
        except sqlite3.Error as e:
            print(f"Erro ao adicionar produto: {e}")

    def obter_produtos(self):
        try:
            self.c.execute("SELECT * FROM produtos")
            return self.c.fetchall()
        except sqlite3.Error as e:
            print(f"Erro ao obter produtos: {e}")
            return []
        
    def atualizar_produtos(self, id_produto, nova_quantidade):
        try:
            self.c.execute("UPDATE produtos SET quantidade=? WHERE id=?", (nova_quantidade, id_produto))
            self.conn.commit()
        except sqlite3.Error as e:
            print(f"Erro ao atualizar quantidade do produto: {e}")


    # Tabela encomendas
    def efetuar_encomenda(self, id_produto, referencia_produto, quantidade):
        try:
            self.c.execute("INSERT INTO encomendas (id_produto, nome_produto, quantidade) VALUES (?, ?, ?)", (id_produto, referencia_produto, quantidade))
            self.conn.commit()
        except sqlite3.Error as e:
            print(f"Erro ao efetuar encomenda: {e}")

    def obter_encomendas(self):
        try:
            self.c.execute("SELECT * FROM encomendas")
            return self.c.fetchall()
        except sqlite3.Error as e:
            print(f"Erro ao obter encomendas: {e}")
            return []
        
    def obter_detalhes_produto(self, ref_produto):
        try:
            self.c.execute("SELECT id, nome, quantidade FROM produtos WHERE id=?", (ref_produto,))
            return self.c.fetchone()
        except sqlite3.Error as e:
            print(f"Erro ao obter detalhes do produto: {e}")
            return None



    def apagar_produtos(self):
        self.c.execute("DELETE FROM produtos")
        self.conn.commit()

    def apagar_encomendas(self):
        self.c.execute("DELETE FROM encomendas")
        self.conn.commit()


    def fechar_conexao(self):
        try:
            self.conn.close()
        except sqlite3.Error as e:
            print(f"Erro ao fechar conexão: {e}")


if __name__ == "__main__":
    db = Database()

    #db.apagar_produtos()
    #db.apagar_encomendas()
    
    produtos = db.obter_produtos()
    print("Produtos:", produtos)
    
    encomendas = db.obter_encomendas()
    print("Encomendas:", encomendas)



    db.fechar_conexao()