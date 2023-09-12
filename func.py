class Cadastrar:
    def __init__(self):
        #self.id = id
        self.nome = []
        self.senha = []
        self.id = []

    def setDados(self, nome, senha, id):
        self.nome.append(nome)
        self.senha.append(senha)
        self.id.append(id)

    def mostrar(self):
       #return '\n'.join(self.nome) + '\n'.join(self.senha) + '\n'.join(self.id)
        #return '\n'.join(self.nome), '\n'.join(self.senha)
        
        print(f'{self.id} {self.nome} {self.senha} \n')
    
    def deletar(self, nome):
        del self.nome[nome]
        #fazer uma lógica para apagar toda a linha que está o ID


    def update(self, nome, id, senha):
        self.nome[id] = nome
        self.senha[id] = senha

        







'''
1 - Primeiro criamos uma variável para fazer todos os teste e logo depois fazer como restante

2 - Meta, colocar essa variável em uma dicionário, excluir, renomear, atualizar e exibir

'''

