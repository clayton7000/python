from aluno import Aluno

def main():
    aluno= Aluno("Maria",5,6,7,6)
    aluno.exibir_dados()

    if aluno.precisa_recuperacao():
        aluno.aplicar_recuperacao(7.0)
        print("\nApós recuperação:")
        aluno.exibir_dados()

if __name__ == "__main__":
    main()