from pessoas import Gerente, Hospede, Recepcionista, TecnicoManutencao, TecnicoRecepcao
from quartos import QuartoLuxo, QuartoSimples

TURNOS_VALIDOS = ["manhã", "tarde", "noite"]

def ler_int(mensagem, minimo=None):
    while True:
        try:
            valor = int(input(mensagem))
            if minimo is not None and valor < minimo:
                print(f"Erro: o valor tem de ser pelo menos {minimo}.")
                continue
            return valor
        except ValueError:
            print("Erro: introduza um número inteiro válido.")

def ler_float(mensagem, minimo=None):
    while True:
        try:
            valor = float(input(mensagem).replace(",", "."))
            if minimo is not None and valor < minimo:
                print(f"Erro: o valor tem de ser pelo menos {minimo}.")
                continue
            return valor
        except ValueError:
            print("Erro: introduza um número válido.")

def ler_turno():
    while True:
        turno = input("Turno (manhã/tarde/noite): ").strip().lower()
        if turno in TURNOS_VALIDOS:
            return turno
        print("Erro: turno inválido. Escolha entre: manhã, tarde, noite.")

def ler_id_funcionario(funcionarios):
    while True:
        id_func = ler_int("ID do funcionário: ", 1)
        if any(f.id_func == id_func for f in funcionarios):
            print("Erro: já existe um funcionário com esse ID.")
        else:
            return id_func

def obter_recepcionista(funcionarios):
    for f in funcionarios:
        if isinstance(f, Recepcionista):
            return f
    return None

def obter_gerente(funcionarios):
    for f in funcionarios:
        if isinstance(f, Gerente):
            return f
    return None

def listar_quartos(quartos):
    print("\n--- QUARTOS ---")
    if len(quartos) == 0:
        print("Não há quartos registados.")
    for q in quartos:
        q.mostrar_informacoes()
    print()

def adicionar_quarto(quartos):
    print("\n--- ADICIONAR QUARTO ---")
    print("1 - Quarto Simples")
    print("2 - Quarto de Luxo")
    tipo = input("Tipo de quarto: ")

    if tipo not in ("1", "2"):
        print("Tipo inválido.\n")
        return

    numero = ler_int("Número do quarto: ", 1)
    if any(q.numero == numero for q in quartos):
        print(f"Erro: o quarto {numero} já existe.\n")
        return

    preco = ler_float("Preço por diária (€): ", 0)

    if tipo == "1":
        quarto = QuartoSimples(numero, preco)
    else:
        resposta = input("Inclui jacuzzi? (s/n): ").strip().lower()
        quarto = QuartoLuxo(numero, preco, resposta == "s")

    quartos.append(quarto)
    print(f"Quarto {numero} adicionado com sucesso.\n")

def adicionar_funcionario(funcionarios):
    print("\n--- ADICIONAR FUNCIONÁRIO ---")
    print("1 - Gerente")
    print("2 - Recepcionista")
    print("3 - Técnico de Manutenção")
    print("4 - Técnico de Receção")
    tipo = input("Tipo de funcionário: ")

    if tipo not in ("1", "2", "3", "4"):
        print("Tipo inválido.\n")
        return

    nome = input("Nome: ").strip()
    idade = ler_int("Idade: ", 0)
    salario = ler_float("Salário (€): ", 0)

    if tipo == "1":
        bonus = ler_float("Bónus (€): ", 0)
        funcionario = Gerente(nome, idade, salario, bonus)

    elif tipo == "2":
        id_func = ler_id_funcionario(funcionarios)
        turno = ler_turno()
        funcionario = Recepcionista(nome, id_func, idade, salario, turno)

    elif tipo == "3":
        especialidade = input("Especialidade: ").strip()
        funcionario = TecnicoManutencao(nome, idade, salario, especialidade)

    else:
        id_func = ler_id_funcionario(funcionarios)
        turno = ler_turno()
        especialidade = input("Especialidade: ").strip()
        funcionario = TecnicoRecepcao(nome, id_func, salario, idade, turno, especialidade)

    funcionarios.append(funcionario)
    print(f"Funcionário {nome} adicionado com sucesso.\n")

def relatorio_funcionarios(funcionarios):
    gerente = obter_gerente(funcionarios)
    if gerente is None:
        print("\nÉ necessário ter um gerente registado para gerar o relatório.\n")
        return
    gerente.gerar_relatorio(funcionarios)

def registar_reparo(funcionarios):
    print("\n--- REGISTAR REPARO ---")
    tecnicos = [f for f in funcionarios if isinstance(f, TecnicoManutencao)]

    if len(tecnicos) == 0:
        print("Não há técnicos de manutenção registados.\n")
        return

    for i, t in enumerate(tecnicos):
        print(f"{i + 1} - {t.nome} ({t.especialidade})")

    escolha = ler_int("Número do técnico: ")
    if not 1 <= escolha <= len(tecnicos):
        print("Técnico inválido.\n")
        return

    descricao = input("Descrição do reparo: ")
    tecnicos[escolha - 1].registrar_reparo(descricao)
    print()

def registar_hospede(funcionarios, hospedes, quartos):
    print("\n--- REGISTAR HÓSPEDE ---")

    recepcionista = obter_recepcionista(funcionarios)
    if recepcionista is None:
        print("É necessário ter um recepcionista registado.\n")
        return

    livres = [q for q in quartos if not q.ocupado]
    if len(livres) == 0:
        print("Não há quartos livres.\n")
        return

    nome = input("Nome: ").strip()
    idade = ler_int("Idade: ", 0)
    dias = ler_int("Dias de estadia: ", 1)

    print("\nQuartos livres:")
    for q in livres:
        q.mostrar_informacoes()

    numero = ler_int("Número do quarto: ")
    quarto = next((q for q in livres if q.numero == numero), None)
    if quarto is None:
        print("Quarto não encontrado ou ocupado. Hóspede não registado.\n")
        return

    hospede = Hospede(nome, idade, dias)
    recepcionista.registrar_hospede(hospede, hospedes)
    hospede.atribuir_quarto(quarto)
    print()

def listar_hospedes(funcionarios, hospedes):
    recepcionista = obter_recepcionista(funcionarios)
    if recepcionista is None:
        print("\nÉ necessário ter um recepcionista registado.\n")
        return
    recepcionista.listar_hospedes(hospedes)

def checkout(hospedes):
    print("\n--- CHECKOUT ---")
    if len(hospedes) == 0:
        print("Não há hóspedes registados.\n")
        return

    for i, h in enumerate(hospedes):
        print(f"{i + 1} - {h.nome}")

    escolha = ler_int("Número do hóspede: ")
    if 1 <= escolha <= len(hospedes):
        hospedes[escolha - 1].checkout()
    else:
        print("Hóspede inválido.")
    print()

def main():
    quartos = []
    funcionarios = []
    hospedes = []

    print("=== SISTEMA DE GESTÃO HOTELEIRA ===\n")

    while True:
        print("1 - Listar quartos")
        print("2 - Adicionar quarto")
        print("3 - Registar hóspede")
        print("4 - Listar hóspedes")
        print("5 - Checkout")
        print("6 - Adicionar funcionário")
        print("7 - Relatório de funcionários")
        print("8 - Registar reparo")
        print("9 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            listar_quartos(quartos)
        elif opcao == "2":
            adicionar_quarto(quartos)
        elif opcao == "3":
            registar_hospede(funcionarios, hospedes, quartos)
        elif opcao == "4":
            listar_hospedes(funcionarios, hospedes)
        elif opcao == "5":
            checkout(hospedes)
        elif opcao == "6":
            adicionar_funcionario(funcionarios)
        elif opcao == "7":
            relatorio_funcionarios(funcionarios)
        elif opcao == "8":
            registar_reparo(funcionarios)
        elif opcao == "9":
            print("Encerrando programa...")
            break
        else:
            print("Opção inválida!\n")

if __name__ == "__main__":
    main()