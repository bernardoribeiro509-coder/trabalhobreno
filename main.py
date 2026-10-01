from pessoas import Gerente, Hospede, Recepcionista, TecnicoManutencao, TecnicoRecepcao
from quartos import QuartoLuxo, QuartoSimples


def listar_quartos(quartos):
    print("\n--- QUARTOS ---")
    for q in quartos:
        q.mostrar_informacoes()
    print()


def registar_hospede(recepcionista, hospedes, quartos):
    print("\n--- REGISTAR HÓSPEDE ---")
    nome = input("Nome: ")
    idade = float(input("Idade: "))
    dias = int(input("Dias de estadia: "))

    hospede = Hospede(nome, idade, dias)
    recepcionista.registrar_hospede(hospede, hospedes)

    listar_quartos(quartos)
    numero = int(input("Número do quarto: "))

    encontrado = False
    for q in quartos:
        if q.numero == numero:
            hospede.atribuir_quarto(q)
            encontrado = True
    if not encontrado:
        print("Quarto não encontrado.")
    print()


def checkout(hospedes):
    print("\n--- CHECKOUT ---")
    if len(hospedes) == 0:
        print("Não há hóspedes registados.\n")
        return

    for i, h in enumerate(hospedes):
        print(f"{i + 1} - {h.nome}")

    escolha = int(input("Número do hóspede: "))
    if 1 <= escolha <= len(hospedes):
        hospedes[escolha - 1].checkout()
    else:
        print("Hóspede inválido.")
    print()


def main():
    # Quartos
    quartos = [
        QuartoSimples(101, 45.0),
        QuartoSimples(102, 45.0),
        QuartoLuxo(201, 120.0, True),
        QuartoLuxo(202, 100.0, False),
    ]

    # Funcionários
    gerente = Gerente("Carlos Silva", 45, 2500.0, 400.0)
    recepcionista = Recepcionista("Ana Martins", 101, 28, 1100.0, "manhã")
    tecnico = TecnicoManutencao("João Pereira", 38, 1250.0, "Eletricidade")
    tec_rec = TecnicoRecepcao("Rui Costa", 102, 1350.0, 31, "noite", "Climatização")

    funcionarios = [gerente, recepcionista, tecnico, tec_rec]
    hospedes = []

    print("=== SISTEMA DE GESTÃO HOTELEIRA ===\n")

    while True:
        print("1 - Listar quartos")
        print("2 - Registar hóspede")
        print("3 - Listar hóspedes")
        print("4 - Checkout")
        print("5 - Relatório de funcionários")
        print("6 - Registar reparo")
        print("7 - Técnico de Receção")
        print("8 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            listar_quartos(quartos)
        elif opcao == "2":
            registar_hospede(recepcionista, hospedes, quartos)
        elif opcao == "3":
            recepcionista.listar_hospedes(hospedes)
        elif opcao == "4":
            checkout(hospedes)
        elif opcao == "5":
            gerente.gerar_relatorio(funcionarios)
        elif opcao == "6":
            descricao = input("Descrição do reparo: ")
            tecnico.registrar_reparo(descricao)
            print()
        elif opcao == "7":
            tec_rec.mostrar_info()
            tec_rec.registrar_reparo("Manutenção no ar condicionado da suíte 201")
            print()
        elif opcao == "8":
            print("Encerrando programa...")
            break
        else:
            print("Opção inválida!\n")


if __name__ == "__main__":
    main()