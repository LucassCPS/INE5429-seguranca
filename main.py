from tests.random_number_benchmark_test import generate_report as generate_random_report
from tests.prime_number_benchmark_test import generate_report as generate_prime_report
from tests.prime_number_gen_test import generate_primes

def display_menu():
    print("Escolha uma opção de teste:")
    print("1. Gerar relatório de benchmark de números aleatórios")
    print("2. Gerar relatório de benchmark de números primos")
    print("3. Gerar números primos")
    print("4. Sair")

def main():
    while True:
        display_menu()
        choice = input("Digite o número da opção desejada: ")

        if choice == "1":
            print("Gerando relatório de benchmark de números aleatórios...")
            generate_random_report()
            print(f"Relatório gerado com sucesso! O arquivo pode ser encontrado em: /tests/reports/random_number_generation_report.txt\n")
        elif choice == "2":
            print("Gerando relatório de benchmark de números primos...")
            generate_prime_report()
            print("Relatório gerado com sucesso! O arquivo pode ser encontrado em: tests/reports/prime_number_generation_report.txt\n")
        elif choice == "3":
            print("Gerando números primos...")
            generate_primes()
            print("Números primos gerados com sucesso! O arquivo pode ser encontrado em: tests/reports/prime_number_report.txt\n")
        elif choice == "4":
            print("Saindo do programa.\n")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
