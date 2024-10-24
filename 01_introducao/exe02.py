class Conta:
    def __init__(self, numero, titular, saldo, limite, codigo_tipo, nome_tipo):
        self.numero = numero
        self.titular = titular
        self.saldo = saldo
        self.limite = limite
        self.codigo_tipo = codigo_tipo
        self.nome_tipo = nome_tipo

    def deposita(self, valor):
        self.saldo += valor

    def saca(self, valor):
        if self.saldo > valor:
            self.saldo -= valor
            return True
        return False

    def extrato(self):
        print(f"Saldo de {self.saldo} do titular {self.titular}")

    def transferir(self, destino):
        valor = self.saldo
        self.saldo -= valor
        destino.saldo += valor
