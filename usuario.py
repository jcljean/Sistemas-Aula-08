class Usuario:
    def __init__(self, nome, matricula):
        if not nome:
            raise ValueError("O nome é obrigatório.")
        self.nome = nome
        self.matricula = matricula

    def __str__(self):
        return f"Usuário: {self.nome}, Matrícula: {self.matricula}"