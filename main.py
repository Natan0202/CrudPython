import func
from func import Cadastrar

if __name__ == "__main__":
    cadastrar = Cadastrar()

    op = 0
    while (op != 2):

        nomear = input(str("Nome: ")) 
        cadastrar.setNome(nomear)

        print(" ---------- ")

        op = int(input("Digite 2 ou 0\nPara printar: "))
        if op == 2:
           print(cadastrar)
           #dele = int(input("Deletar algum nome? "))
           #cadastrar.deletar(dele)

           mod = int(input("Modificar algum nome? "))
           newNome = input("Novo nome: ")
           cadastrar.update(newNome, mod)
           print(cadastrar)
