from classes import Aluno, Professor, Funcionario

def main():
    a1 = Aluno("Cleyton", 20, "TI", "3DSINSTB")    
    a1.fazer_aniversario()

    p1 = Professor("Lindomar", 45, "Mobile e Excel", "Senior")
    p1.fazer_aniversario()

    f1 = Funcionario("Cleyton", 20, "Auxiliar de Montagem", "Tesla1")
    f1.fazer_aniversario()

if __name__ == "__main__":
    main()
    