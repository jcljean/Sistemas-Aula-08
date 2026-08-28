from dominio.livro import Livro
from dominio.usuario import Usuario
from dominio.emprestimo import Emprestimo


acervo = []
emprestimos = []
usuario = Usuario("Aluno", "0000")

while True:
    print()
    print("=== BIBLIOTECA ====")
    print("1 - Cadastrar livro")
    print("2 - Listar Acervo")
    print("3 - Emprestar")
    print("0 - Sair")
    opcao = input("Opcao: ")

    if opcao == "1":
        titulo = input("Titulo: ")
        autor = input("Autor: ")
        ano = int(input("Ano: "))
        try:
            acervo.append(Livro(titulo, autor, ano))
            print("Livro cadastrada: ")
        except ValueError as erro:
            print("Não deu:", erro)
    elif opcao == 2:
        if not acervo:
            print("Acervo vazio.")
        for livro in acervo:
            print("-", livro)
    elif opcao == 3:
        procurando = input("Titulo:")
        escolhido = None

        for livro in acervo:
            if livro.titulo.lower() == procurando.lower():
                escolhido = escolhido

        if escolhido is None:
            print("Não está no acervo")
        else:
            emprestimos.append(Emprestimo(escolhido, usuario, "28/08/2026"))
            print ("Emprestado: ", emprestimos[-1])

    elif opcao == 0:
        print("Até logo")

    else:
        print("Opção Invalida !")