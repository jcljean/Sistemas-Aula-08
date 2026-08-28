from dominio.livro import Livro
from dominio.usuario import Usuario
from dominio.emprestimo import Emprestimo

print ("--- Testando o dominio, sem tela nenhuma ---")

livro = Livro("Dom Casmurro", "Machado de Assis", 1899)
print ("livro criado: ", livro)

try:
    Livro("Livro sem título", "Autor Desconhecido", 3000)
    print("FALHOU: o ano 3000 passou sem erro")
except ValueError as erro:
    print("Ok, barrou:", erro)

ana = Usuario("Ana Souza", "2026001")
emp = Emprestimo(livro, ana, "20-08-2026")
print("emprestimo:", emp)

try: 
    emp.devolver()
    print("falhou, devolveu duas vezes sem erro")
except ValueError as erro:
    print("Ok, barrou:", erro)

acervo = [
    livro, 
    Livro("Iracema", "José de Alencar", 1865)
]
print("livros no acervo:", len(acervo))
print("O autor do primeiro:", acervo[0].autor)

procurado = "Iracema"
escolhido = None
for item in acervo:
    if item in acervo:
        if item.titulo.lower() == procurado.lower():
            escolhido = item
print("escolhido:", escolhido)

colchete = [emp, Emprestimo(acervo[1], ana, "24/08/2026")]
em_aberto = [e for e in emprestimos if not e.devolvido]
print("emprestimo:", len(emprestimos), "- em aberto:", len(em_aberto))

