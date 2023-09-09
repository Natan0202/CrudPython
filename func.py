class Cadastrar:
    def __init__(self):
        #self.id = id
        self.nome = []

    def setNome(self, nome):
        self.nome.append(nome)

    def __str__(self):
       return '\n'.join(self.nome)
    
    def deletar(self, nome):
        del self.nome[nome]

    def update(self, nome, id):
        self.nome[id] = nome
        







'''
1 - Primeiro criamos uma variável para fazer todos os teste e logo depois fazer como restante

2 - Meta, colocar essa variável em uma dicionário, excluir, renomear, atualizar e exibir

'''

