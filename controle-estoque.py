import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

class Produto:
    def __init__(self, nome, quantidade):
        self.nome = nome
        self.quantidade = quantidade

class Estoque:
    def __init__(self):
        self.produtos = {}
        self.carregar_estoque()

    def carregar_estoque(self):
        """Carrega o estoque do arquivo 'estoque.txt'."""
        try:
            with open('estoque.txt', 'r') as arquivo:
                for linha in arquivo:
                    nome, quantidade = linha.strip().split(": ")
                    quantidade = int(quantidade)
                    self.produtos[nome] = Produto(nome, quantidade)
        except FileNotFoundError:
            pass

    def adicionar_produto(self, nome, quantidade):
        if nome in self.produtos:
            self.produtos[nome].quantidade += quantidade
        else:
            self.produtos[nome] = Produto(nome, quantidade)

    def remover_produto(self, nome, quantidade):
        if nome in self.produtos:
            if self.produtos[nome].quantidade >= quantidade:
                self.produtos[nome].quantidade -= quantidade
                if self.produtos[nome].quantidade == 0:
                    del self.produtos[nome]
            else:
                messagebox.showerror("Erro", "Não há quantidade suficiente para remover.")
        else:
            messagebox.showerror("Erro", "Produto não encontrado no estoque.")

    def atualizar_quantidade(self, nome, quantidade):
        if nome in self.produtos:
            self.produtos[nome].quantidade = quantidade
        else:
            messagebox.showerror("Erro", "Produto não encontrado no estoque.")

    def listar_produtos(self):
        return sorted(self.produtos.values(), key=lambda x: x.nome)

    def salvar_em_arquivo(self):
        with open('estoque.txt', 'w') as arquivo:
            for produto in self.produtos.values():
                arquivo.write(f"{produto.nome}: {produto.quantidade}\n")

class ControleEstoque:
    def __init__(self, root):
        self.root = root
        self.root.title("Controle de Estoque")
        self.root.geometry("600x500")
        self.root.config(bg="#f2f2f2")
        self.estoque = Estoque()
        self.criar_widgets()

    def criar_widgets(self):
        # Frame para entrada de dados
        self.frame_entrada = tk.Frame(self.root, bg="#f2f2f2")
        self.frame_entrada.pack(pady=20)

        # Labels e entradas
        tk.Label(self.frame_entrada, text="Nome do Produto:", font=("Arial", 12), bg="#f2f2f2").grid(row=0, column=0, padx=10)
        self.entrada_nome = ttk.Entry(self.frame_entrada, font=("Arial", 12))
        self.entrada_nome.grid(row=0, column=1, padx=10, pady=5)

        tk.Label(self.frame_entrada, text="Quantidade:", font=("Arial", 12), bg="#f2f2f2").grid(row=1, column=0, padx=10)
        self.entrada_quantidade = ttk.Entry(self.frame_entrada, font=("Arial", 12))
        self.entrada_quantidade.grid(row=1, column=1, padx=10, pady=5)

        # Botões de ação
        self.frame_botoes = tk.Frame(self.root, bg="#f2f2f2")
        self.frame_botoes.pack(pady=10)

        self.botao_adicionar = ttk.Button(self.frame_botoes, text="Adicionar", command=self.adicionar_produto)
        self.botao_adicionar.grid(row=0, column=0, padx=10, pady=10)

        self.botao_remover = ttk.Button(self.frame_botoes, text="Remover", command=self.remover_produto)
        self.botao_remover.grid(row=0, column=1, padx=10, pady=10)

        self.botao_atualizar = ttk.Button(self.frame_botoes, text="Atualizar", command=self.atualizar_quantidade)
        self.botao_atualizar.grid(row=0, column=2, padx=10, pady=10)

        self.botao_excluir = ttk.Button(self.frame_botoes, text="Excluir", command=self.excluir_produto)
        self.botao_excluir.grid(row=0, column=3, padx=10, pady=10)

        # Listbox para listar produtos
        self.texto_lista = tk.Listbox(self.root, height=10, width=50, font=("Arial", 12), selectmode=tk.SINGLE, bg="#ffffff", fg="#333333", bd=2)
        self.texto_lista.pack(pady=20)

        # Campo de pesquisa
        self.frame_pesquisa = tk.Frame(self.root, bg="#f2f2f2")
        self.frame_pesquisa.pack(pady=10)

        tk.Label(self.frame_pesquisa, text="Pesquisar:", font=("Arial", 12), bg="#f2f2f2").grid(row=0, column=0, padx=10)
        self.entrada_pesquisa = ttk.Entry(self.frame_pesquisa, font=("Arial", 12))
        self.entrada_pesquisa.grid(row=0, column=1, padx=10)

        self.botao_pesquisar = ttk.Button(self.frame_pesquisa, text="Pesquisar", command=self.pesquisar_produto)
        self.botao_pesquisar.grid(row=0, column=2, padx=10)

        # Carregar a lista de produtos do estoque no início
        self.listar_produtos()

    def adicionar_produto(self):
        nome = self.entrada_nome.get()
        if not nome:
            messagebox.showerror("Erro", "O nome do produto não pode estar vazio.")
            return
        try:
            quantidade = int(self.entrada_quantidade.get())
            selecionado = self.texto_lista.curselection()
            if selecionado:
                produto_nome = self.texto_lista.get(selecionado[0]).split(":")[0].strip()
                self.estoque.adicionar_produto(produto_nome, quantidade)
            else:
                self.estoque.adicionar_produto(nome, quantidade)
            self.entrada_nome.delete(0, tk.END)
            self.entrada_quantidade.delete(0, tk.END)
            self.listar_produtos()
            self.estoque.salvar_em_arquivo()
        except ValueError:
            messagebox.showerror("Erro", "Quantidade deve ser um número inteiro.")

    def remover_produto(self):
        try:
            selecionado = self.texto_lista.curselection()
            if not selecionado:
                messagebox.showerror("Erro", "Selecione um produto para remover.")
                return
            produto_nome = self.texto_lista.get(selecionado[0]).split(":")[0].strip()
            quantidade = int(self.entrada_quantidade.get()) if self.entrada_quantidade.get() else 1
            self.estoque.remover_produto(produto_nome, quantidade)
            self.entrada_nome.delete(0, tk.END)
            self.entrada_quantidade.delete(0, tk.END)
            self.listar_produtos()
            self.estoque.salvar_em_arquivo()
        except ValueError:
            messagebox.showerror("Erro", "Quantidade deve ser um número inteiro.")

    def atualizar_quantidade(self):
        try:
            selecionado = self.texto_lista.curselection()
            if not selecionado:
                messagebox.showerror("Erro", "Selecione um produto para atualizar.")
                return
            produto_nome = self.texto_lista.get(selecionado[0]).split(":")[0].strip()
            try:
                quantidade = int(self.entrada_quantidade.get())
                self.estoque.atualizar_quantidade(produto_nome, quantidade)
                self.entrada_nome.delete(0, tk.END)
                self.entrada_quantidade.delete(0, tk.END)
                self.listar_produtos()
                self.estoque.salvar_em_arquivo()
            except ValueError:
                messagebox.showerror("Erro", "Digite uma quantidade válida.")
        except ValueError:
            messagebox.showerror("Erro", "Erro ao atualizar quantidade.")

    def excluir_produto(self):
        try:
            selecionado = self.texto_lista.curselection()
            if not selecionado:
                messagebox.showerror("Erro", "Selecione um produto para excluir.")
                return
            produto_nome = self.texto_lista.get(selecionado[0]).split(":")[0].strip()
            if produto_nome in self.estoque.produtos:
                del self.estoque.produtos[produto_nome]
                self.listar_produtos()
                self.estoque.salvar_em_arquivo()
                messagebox.showinfo("Sucesso", f"Produto '{produto_nome}' excluído com sucesso.")
            else:
                messagebox.showerror("Erro", "Produto não encontrado no estoque.")
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao excluir o produto: {e}")

    def listar_produtos(self):
        self.texto_lista.delete(0, tk.END)
        produtos = self.estoque.listar_produtos()
        for produto in produtos:
            self.texto_lista.insert(tk.END, f"{produto.nome}: {produto.quantidade}")

    def pesquisar_produto(self):
        nome_pesquisa = self.entrada_pesquisa.get()
        produtos_pesquisados = [produto for produto in self.estoque.produtos.values() if produto.nome.lower().startswith(nome_pesquisa.lower())]
        self.texto_lista.delete(0, tk.END)
        for produto in produtos_pesquisados:
            self.texto_lista.insert(tk.END, f"{produto.nome}: {produto.quantidade}")

if __name__ == "__main__":
    root = tk.Tk()
    app = ControleEstoque(root)
    root.mainloop()
