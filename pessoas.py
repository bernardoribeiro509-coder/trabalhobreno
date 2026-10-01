from abc import ABC, abstractmethod


class Pessoa(ABC):

    def __init__(self, nome, idade):
        self._nome = nome
        self._idade = idade

    @property
    @abstractmethod
    def nome(self):
        pass

    @nome.setter
    @abstractmethod
    def nome(self, valor):
        pass

    @property
    @abstractmethod
    def idade(self):
        pass

    @idade.setter
    @abstractmethod
    def idade(self, valor):
        pass

    @abstractmethod
    def mostrar_informacoes(self):
        pass


class Hospede(Pessoa):

    def __init__(self, nome, idade, dias_estadia, quarto = None):
        super().__init__(nome, idade)
        self._dias_estadia = dias_estadia
        self._quarto = None
        if quarto is not None:
            self.quarto = quarto

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, valor):
        self._nome = valor

    @property
    def idade(self):
        return self._idade

    @idade.setter
    def idade(self, valor):
        if valor >= 0:
            self._idade = valor
        else:
            print("Erro: A idade não pode ser negativa.")

    @property
    def quarto(self):
        return self._quarto

    @quarto.setter
    def quarto(self, novo_quarto):
        if novo_quarto is not None and novo_quarto.ocupado:
            print(f"Erro: O quarto {novo_quarto.numero} já se encontra ocupado.")
        else:
            if self._quarto is not None:
                self._quarto.ocupado = False
            self._quarto = novo_quarto
            if novo_quarto is not None:
                novo_quarto.ocupado = True

    def atribuir_quarto(self, quarto):
        self.quarto = quarto

    def calcular_conta(self):
        if self._quarto is not None:
            return self._dias_estadia * self._quarto.preco_diaria
        return 0.0

    def mostrar_informacoes(self):
        num_quarto = (
            self._quarto.numero
            if self._quarto is not None
            else "Sem quarto atribuído"
        )
        print(f"Hóspede: {self._nome} | Idade: {self._idade} | Dias: {self._dias_estadia} | Quarto: {num_quarto}")

    def checkout(self):
        if self._quarto is not None:
            total = self.calcular_conta()
            print(f"Checkout efetuado para {self._nome}. Total a pagar: {total:.2f}€. Quarto {self._quarto.numero} libertado.")
            self._quarto.ocupado = False
            self._quarto = None
        else:
            print(f"{self._nome} não tem nenhum quarto atribuído para efetuar checkout.")


class Funcionario(Pessoa):

    def __init__(self, nome, idade, salario, id_func=0):
        super().__init__(nome, idade)
        self._salario = salario
        self._id_func = id_func

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, valor):
        self._nome = valor

    @property
    def idade(self):
        return self._idade

    @idade.setter
    def idade(self, valor):
        if valor >= 0:
            self._idade = valor
        else:
            print("Erro: A idade não pode ser negativa.")

    @property
    def salario(self):
        return self._salario

    @property
    def id_func(self):
        return self._id_func

    def mostrar_informacoes(self):
        print(f"Funcionário: {self._nome} | ID: {self._id_func} | Idade: {self._idade} | Salário: {self._salario:.2f}€")


class Gerente(Funcionario):

    def __init__(self, nome, idade, salario, bonus=200.0):
        super().__init__(nome, idade, salario)
        self._bonus = bonus

    def mostrar_informacoes(self):
        total = self._salario + self._bonus
        print(f"Gerente: {self._nome} | Idade: {self._idade} | Salário Base: {self._salario:.2f}€ | Bónus: {self._bonus:.2f}€ (Total: {total:.2f}€)")

    def gerar_relatorio(self, funcionarios):
        print("\n==========================================")
        print("    RELATÓRIO DE FUNCIONÁRIOS DO HOTEL    ")
        print("==========================================")
        for func in funcionarios:
            func.mostrar_informacoes()
        print("==========================================\n")


class Recepcionista(Funcionario):
    def __init__(self, nome, id_func, idade, salario, turno="manhã", **kwargs):
        super().__init__(nome=nome, idade=idade, salario=salario, id_func=id_func, **kwargs)
        self._turno = turno.lower()

    @property
    def turno(self):
        return self._turno

    @turno.setter
    def turno(self, novo_turno):
        validos = ["manhã", "tarde", "noite"]
        if novo_turno.lower() in validos:
            self._turno = novo_turno.lower()
        else:
            print("Erro: Turno inválido. Escolha entre: manhã, tarde, noite.")

    def mostrar_informacoes(self):
        print(f"Recepcionista: {self._nome} | ID: {self._id_func} | Idade: {self._idade} | Salário: {self._salario:.2f}€ | Turno: {self._turno}")

    def registrar_hospede(self, hospede, lista_hospedes: list):
        lista_hospedes.append(hospede)
        print(f"Hóspede {hospede.nome} registado com sucesso por {self._nome}.")

    def listar_hospedes(self, lista_hospedes: list):
        print("\n--- LISTA DE HÓSPEDES REGISTADOS ---")
        for h in lista_hospedes:
            h.mostrar_informacoes()
        print("------------------------------------\n")


class TecnicoManutencao(Funcionario):

    def __init__(self, nome, idade, salario, especialidade, id_func=0, **kwargs):
        super().__init__(nome=nome, idade=idade, salario=salario, id_func=id_func, **kwargs)
        self._especialidade = especialidade

    @property
    def especialidade(self):
        return self._especialidade

    def mostrar_informacoes(self):
        print(f"Técnico de Manutenção: {self._nome} | Idade: {self._idade} | Salário: {self._salario:.2f}€ | Especialidade: {self._especialidade}")

    def registrar_reparo(self, descricao):
        print(f"Reparação registada por {self._nome} ({self._especialidade}): {descricao}")


class TecnicoRecepcao(Recepcionista, TecnicoManutencao):

    def __init__(self, nome, id_fun, salario, idade, turno, especialidade):
        super().__init__(
            nome=nome,
            id_func=id_fun,
            idade=idade,
            salario=salario,
            turno=turno,
            especialidade=especialidade,
        )

    def mostrar_info(self):
        print(f"Técnico de Receção: {self._nome} | ID: {self._id_func} | Salário: {self._salario:.2f}€ | Turno: {self._turno} | Especialidade: {self._especialidade}")

    def mostrar_informacoes(self):
        self.mostrar_info()