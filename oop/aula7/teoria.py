class Pessoa: #CLASSE MÃE, TODAS AS CLASSES FILHAS VÃO TEM OS ATRIBUTOS NOME E IDADE E O METODO FAZER_ANIVERSARIO()
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    
    def fazer_aniversario(self):
        self.idade += 1 

class Aluno(Pessoa): # Classe filha, vai herdar tudo da mãe + os atributos e metodos dela
    def __init__(self, nome, idade, curso, turma):
        super().__init__(nome, idade) # METODO PARA CHAMAR O __INIT__ DA MÃE PARA O FILHO HERDAR OQ ELA TEM
        self.curso = curso
        self.turma = turma
    
    def fazer_matricula(self):
        print(f"O aluno {self.nome} fez matricula kkkk")

class Professor(Pessoa): # Classe filha, vai herdar tudo da mãe + os atributos e metodos dela
    def __init__(self, nome, idade, especialidade, nivel):
        super().__init__(nome, idade) # METODO PARA CHAMAR O __INIT__ DA MÃE PARA O FILHO HERDAR OQ ELA TEM
        self.especialidade = especialidade
        self.nivel = nivel
    
    def dar_aula(self):
        print(f"O professor {self.nome} deu aula kkkkk")

class Funcionario(Pessoa): # Classe filha, vai herdar tudo da mãe + os atributos e metodos dela
    def __init__(self, nome, idade, cargo, setor):
        super().__init__(nome, idade) # METODO PARA CHAMAR O __INIT__ DA MÃE PARA O FILHO HERDAR OQ ELA TEM
        self.cargo = cargo
        self.setor = setor
    
    def bater_ponto(self):
        print(f"O funcionario {self.nome} bateu o ponto KKKKKKKKKKKKKKK")

a1 = Aluno("Cleyton", 20, "TI", "3DSINSTB")    
a1.fazer_aniversario()
print(a1.__dict__)

p1 = Professor("Lindomar", 45, "Mobile e Excel", "Senior")
p1.fazer_aniversario()
print(p1.__dict__)

f1 = Funcionario("Cleyton", 20, "Auxiliar de Montagem", "Tesla1")

