import func
from func import Cadastrar

if __name__ == "__main__":
    cadastrar = Cadastrar()
    cont = -1
    op = 0
    while (op != 2):
        cont += 1
        nomear = input(str("Nome: ")) 
        senha = input(str("Senha: ")) 
        cadastrar.setDados(nomear, senha, cont)

        print(20 * "-")

        op = int(input("Seleciona o valor:\nPrintar = 2\nContinuar a digitar = 0\n"))

        print(20 * "-")


        if op == 2:
           print(f'Contéudos da lista\n{cadastrar.mostrar()} \n')
           print(20 * "-")

           print('Opções:\n1 - Modificar nome por ID\n2 - Deletar dados por ID (Admin)')
           op2 = int(input("Opção: "))
           
           if(op2 == 1): 
                print(20 * "-")
                
                mod = int(input("Selecione o ID para modificar o nome e senha: "))
                newNome = str(input("Novo nome: "))
                newSenha = str(input("Nova senha: "))
                cadastrar.update(newNome, mod, newSenha)
                
                print(20 * "-")
                print(f'Dados atualizados:\n{cadastrar.mostrar()}')

           elif (op2 == 2):
                dele = int(input("Deletar dados:\nSelecione o ID: "))
                cadastrar.deletar(dele)

           

           #print(cadastrar.mostrar())
