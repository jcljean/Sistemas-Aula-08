class Livro:
    def __init__(self, titulo, autor, ano):
        if not titulo:
            raise ValueError("O título do livro não pode ser vazio.")
        if ano < 1450 or ano > 2026:
            raise ValueError("Ano invalido. O ano deve estar entre 1450 e 2026.")

        self.titulo = titulo
        self.autor = autor
        self.ano = ano

    @property
    def ano(self):
        return self._ano

    @ano.setter
    def ano(self, valor):
        if valor < 1450 or valor > 2026:
            raise ValueError("Ano invalido. O ano deve estar entre 1450 e 2026.")
        self._ano = valor



    def desctricao(self):
        return f"{self.titulo} - {self.autor} ({self.ano})"

    def __str__(self):
        return self.desctricao()