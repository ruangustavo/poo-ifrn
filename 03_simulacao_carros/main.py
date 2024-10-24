from typing import List
import time
from datetime import datetime, timedelta


class CarroDeCorrida:
    def __init__(
        self,
        marca: str,
        modelo: str,
        velocidade_maxima: float,
        capacidade_tanque: float,
        consumo_combustivel: float,
    ):
        self.marca = marca
        self.modelo = modelo
        self.velocidade_maxima = velocidade_maxima
        self.capacidade_tanque = capacidade_tanque
        self.consumo_combustivel = consumo_combustivel
        self.velocidade_atual = 0.0
        self.tanque_combustivel = capacidade_tanque
        self.quilometragem = 0.0
        self.em_movimento = True

    def acelerar(self, quantidade: float) -> None:
        if not self.em_movimento:
            print(
                f"{self.marca} {self.modelo} está sem combustível e não pode acelerar!"
            )
            return

        nova_velocidade = self.velocidade_atual + quantidade
        self.velocidade_atual = min(nova_velocidade, self.velocidade_maxima)

    def frear(self, quantidade: float) -> None:
        self.velocidade_atual = max(0, self.velocidade_atual - quantidade)

    def abastecer(self, litros: float) -> None:
        espaco_disponivel = self.capacidade_tanque - self.tanque_combustivel
        litros_abastecidos = min(litros, espaco_disponivel)
        self.tanque_combustivel += litros_abastecidos
        print(f"{self.marca} {self.modelo} abastecido com {litros_abastecidos:.2f}L")

    def dirigir(self, distancia: float) -> float:
        if not self.em_movimento:
            return 0.0

        consumo_total = distancia * self.consumo_combustivel

        if self.tanque_combustivel < consumo_total:
            distancia_possivel = self.tanque_combustivel / self.consumo_combustivel
            self.quilometragem += distancia_possivel
            self.tanque_combustivel = 0
            self.em_movimento = False
            print(f"{self.marca} {self.modelo} ficou sem combustível!")
            return distancia_possivel

        self.tanque_combustivel -= consumo_total
        self.quilometragem += distancia
        return distancia

    def verificar_combustivel(self) -> float:
        return self.tanque_combustivel

    def status(self) -> str:
        return (
            f"\nStatus do {self.marca} {self.modelo}:\n"
            f"Velocidade atual: {self.velocidade_atual:.2f} km/h\n"
            f"Combustível: {self.tanque_combustivel:.2f}L\n"
            f"Quilometragem: {self.quilometragem:.2f} km\n"
            f"Em movimento: {'Sim' if self.em_movimento else 'Não'}"
        )


class Corrida:
    def __init__(self, distancia_total: float):
        self.carros: List[CarroDeCorrida] = []
        self.distancia_total = distancia_total
        self.vencedor = None
        self.tempo_inicio = None
        self.tempo_fim = None

    def adicionar_carro(self, carro: CarroDeCorrida) -> None:
        self.carros.append(carro)
        print(f"{carro.marca} {carro.modelo} adicionado à corrida!")

    def iniciar_corrida(self) -> None:
        if not self.carros:
            raise ValueError("Não há carros na corrida!")

        self.tempo_inicio = datetime.now()

        while not self._corrida_finalizada():
            for carro in self.carros:
                if (
                    not carro.em_movimento
                    or carro.quilometragem >= self.distancia_total
                ):
                    continue

                if carro.velocidade_atual < carro.velocidade_maxima:
                    carro.acelerar(10)

                distancia_ciclo = carro.velocidade_atual / 3600  # km/s
                carro.dirigir(distancia_ciclo)

                if (
                    carro.quilometragem >= self.distancia_total
                    and not self.vencedor
                    and carro.em_movimento
                ):
                    self.vencedor = carro
                    self.tempo_fim = datetime.now()

            time.sleep(0.1)

        print("\nCorrida finalizada!")

    def _corrida_finalizada(self) -> bool:
        return all(
            not carro.em_movimento or carro.quilometragem >= self.distancia_total
            for carro in self.carros
        )

    def resultado_corrida(self) -> None:
        print("\n=== RESULTADO DA CORRIDA ===")
        if self.vencedor:
            tempo_total = self.tempo_fim - self.tempo_inicio
            print(f"Vencedor: {self.vencedor.marca} {self.vencedor.modelo}")
            print(f"Tempo total: {tempo_total.total_seconds():.2f} segundos")
        else:
            print("Nenhum carro completou a corrida!")

        print("\nPosições finais:")
        carros_ordenados = sorted(
            self.carros, key=lambda carro: carro.quilometragem, reverse=True
        )

        for i, carro in enumerate(carros_ordenados, 1):
            print(f"{i}º lugar: {carro.marca} {carro.modelo}")
            print(f"Distância percorrida: {carro.quilometragem:.2f} km")
            print(f"Combustível restante: {carro.tanque_combustivel:.2f}L")


def main():
    ferrari = CarroDeCorrida("Ferrari", "F40", 320, 100, 0.5)
    porsche = CarroDeCorrida("Porsche", "911", 300, 80, 0.4)
    lamborghini = CarroDeCorrida("Lamborghini", "Aventador", 350, 90, 0.6)

    corrida = Corrida(10.0)

    corrida.adicionar_carro(ferrari)
    corrida.adicionar_carro(porsche)
    corrida.adicionar_carro(lamborghini)

    corrida.iniciar_corrida()
    corrida.resultado_corrida()

    for carro in corrida.carros:
        print(carro.status())


if __name__ == "__main__":
    main()
from typing import List
import time
from datetime import datetime, timedelta


class CarroDeCorrida:
    def __init__(
        self,
        marca: str,
        modelo: str,
        velocidade_maxima: float,
        capacidade_tanque: float,
        consumo_combustivel: float,
    ):
        self.marca = marca
        self.modelo = modelo
        self.velocidade_maxima = velocidade_maxima
        self.capacidade_tanque = capacidade_tanque
        self.consumo_combustivel = consumo_combustivel
        self.velocidade_atual = 0.0
        self.tanque_combustivel = capacidade_tanque
        self.quilometragem = 0.0
        self.em_movimento = True

    def acelerar(self, quantidade: float) -> None:
        if not self.em_movimento:
            print(
                f"{self.marca} {self.modelo} está sem combustível e não pode acelerar!"
            )
            return

        nova_velocidade = self.velocidade_atual + quantidade
        self.velocidade_atual = min(nova_velocidade, self.velocidade_maxima)

    def frear(self, quantidade: float) -> None:
        self.velocidade_atual = max(0, self.velocidade_atual - quantidade)

    def abastecer(self, litros: float) -> None:
        espaco_disponivel = self.capacidade_tanque - self.tanque_combustivel
        litros_abastecidos = min(litros, espaco_disponivel)
        self.tanque_combustivel += litros_abastecidos
        print(f"{self.marca} {self.modelo} abastecido com {litros_abastecidos:.2f}L")

    def dirigir(self, distancia: float) -> float:
        if not self.em_movimento:
            return 0.0

        consumo_total = distancia * self.consumo_combustivel

        if self.tanque_combustivel < consumo_total:
            distancia_possivel = self.tanque_combustivel / self.consumo_combustivel
            self.quilometragem += distancia_possivel
            self.tanque_combustivel = 0
            self.em_movimento = False
            print(f"{self.marca} {self.modelo} ficou sem combustível!")
            return distancia_possivel

        self.tanque_combustivel -= consumo_total
        self.quilometragem += distancia
        return distancia

    def verificar_combustivel(self) -> float:
        return self.tanque_combustivel

    def status(self) -> str:
        return (
            f"\nStatus do {self.marca} {self.modelo}:\n"
            f"Velocidade atual: {self.velocidade_atual:.2f} km/h\n"
            f"Combustível: {self.tanque_combustivel:.2f}L\n"
            f"Quilometragem: {self.quilometragem:.2f} km\n"
            f"Em movimento: {'Sim' if self.em_movimento else 'Não'}"
        )


class Corrida:
    def __init__(self, distancia_total: float):
        self.carros: List[CarroDeCorrida] = []
        self.distancia_total = distancia_total
        self.vencedor = None
        self.tempo_inicio = None
        self.tempo_fim = None

    def adicionar_carro(self, carro: CarroDeCorrida) -> None:
        self.carros.append(carro)
        print(f"{carro.marca} {carro.modelo} adicionado à corrida!")

    def iniciar_corrida(self) -> None:
        if not self.carros:
            raise ValueError("Não há carros na corrida!")

        self.tempo_inicio = datetime.now()

        while not self._corrida_finalizada():
            for carro in self.carros:
                if (
                    not carro.em_movimento
                    or carro.quilometragem >= self.distancia_total
                ):
                    continue

                # Simula aceleração gradual
                if carro.velocidade_atual < carro.velocidade_maxima:
                    carro.acelerar(10)

                # Calcula a distância percorrida neste ciclo (em 1 segundo)
                distancia_ciclo = carro.velocidade_atual / 3600  # km/s
                carro.dirigir(distancia_ciclo)

                # Verifica se este carro venceu
                if (
                    carro.quilometragem >= self.distancia_total
                    and not self.vencedor
                    and carro.em_movimento
                ):
                    self.vencedor = carro
                    self.tempo_fim = datetime.now()

            time.sleep(0.1)  # Pequena pausa para não sobrecarregar o CPU

        print("\nCorrida finalizada!")

    def _corrida_finalizada(self) -> bool:
        return all(
            not carro.em_movimento or carro.quilometragem >= self.distancia_total
            for carro in self.carros
        )

    def resultado_corrida(self) -> None:
        print("\n=== RESULTADO DA CORRIDA ===")
        if self.vencedor:
            tempo_total = self.tempo_fim - self.tempo_inicio
            print(f"Vencedor: {self.vencedor.marca} {self.vencedor.modelo}")
            print(f"Tempo total: {tempo_total.total_seconds():.2f} segundos")
        else:
            print("Nenhum carro completou a corrida!")

        print("\nPosições finais:")
        carros_ordenados = sorted(
            self.carros, key=lambda carro: carro.quilometragem, reverse=True
        )

        for i, carro in enumerate(carros_ordenados, 1):
            print(f"{i}º lugar: {carro.marca} {carro.modelo}")
            print(f"Distância percorrida: {carro.quilometragem:.2f} km")
            print(f"Combustível restante: {carro.tanque_combustivel:.2f}L")


def main():
    ferrari = CarroDeCorrida("Ferrari", "F40", 320, 100, 0.5)
    porsche = CarroDeCorrida("Porsche", "911", 300, 80, 0.4)
    lamborghini = CarroDeCorrida("Lamborghini", "Aventador", 350, 90, 0.6)

    corrida = Corrida(10.0)

    corrida.adicionar_carro(ferrari)
    corrida.adicionar_carro(porsche)
    corrida.adicionar_carro(lamborghini)

    corrida.iniciar_corrida()
    corrida.resultado_corrida()

    for carro in corrida.carros:
        print(carro.status())


if __name__ == "__main__":
    main()
