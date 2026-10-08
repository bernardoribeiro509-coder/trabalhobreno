from abc import ABC, abstractmethod


class Quarto(ABC):

    def __init__(self, numero, tipo, preco_diaria):
        self._numero = numero
        self._tipo = tipo
        self._preco_diaria = preco_diaria
        self._ocupado = False

    @property
    def numero(self):
        return self._numero

    @property
    def tipo(self):
        return self._tipo

    @property
    def ocupado(self):
        return self._ocupado

    @ocupado.setter
    def ocupado(self, status):
        self._ocupado = status

    @property
    def preco_diaria(self):
        return self._preco_diaria

    @preco_diaria.setter
    def preco_diaria(self, valor):
        if valor >= 0:
            self._preco_diaria = valor
        else:
            print("Erro: O preço da diária não pode ser negativo.")

    @abstractmethod
    def mostrar_informacoes(self):
        """Método abstrato a ser implementado pelas subclasses."""
        pass


class QuartoSimples(Quarto):

    def __init__(self, numero, preco_diaria=50.0):
        super().__init__(numero, "Simples", preco_diaria)

    def mostrar_informacoes(self):
        status = "Ocupado" if self._ocupado else "Livre"
        print(f"Quarto {self._numero} ({self._tipo}) | Preço/Diária: {self._preco_diaria:.2f}€ | Status: {status}")


class QuartoLuxo(Quarto):

    def __init__(
        self,
        numero,
        preco_diaria=120.0,
        inclui_jacuzzi=True,
    ):
        super().__init__(numero, "Luxo", preco_diaria)
        self._inclui_jacuzzi = inclui_jacuzzi

    def mostrar_informacoes(self):
        status = "Ocupado" if self._ocupado else "Livre"
        jacuzzi = "Com Jacuzzi" if self._inclui_jacuzzi else "Sem Jacuzzi"
        print(f"Quarto {self._numero} ({self._tipo} - {jacuzzi}) | Preço/Diária: {self._preco_diaria:.2f}€ | Status: {status}")