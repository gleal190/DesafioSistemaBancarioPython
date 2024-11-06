#Criação da Classe/Objeto que possui os metodos das operações
class SistemaBancario:
    def __init__(self):
        self.saldo = 0.0
        self.extrato = []
        self.limite_saque = 500.0
        self.saques_diarios = 0
        self.limite_saques_diarios = 3
    #Metodo Depositar
    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            self.extrato.append(f"Depósito: R$ {valor:.2f}")
            print(f"Depósito de R$ {valor:.2f} realizado com sucesso!")
        else:
            print("Valor de depósito inválido.")
    #Metodo Sacar
    def sacar(self, valor):
        if valor > self.limite_saque:
            print("Limite de saque é R$ 500,00 por operação.")
        elif self.saques_diarios >= self.limite_saques_diarios:
            print("Limite de saques diários atingido.")
        elif valor > self.saldo:
            print("Saldo insuficiente.")
        else:
            self.saldo -= valor
            self.saques_diarios += 1
            self.extrato.append(f"Saque: R$ {valor:.2f}")
            print(f"Saque de R$ {valor:.2f} realizado com sucesso!")
    #Metodo Extrato
    def mostrar_extrato(self):
        if not self.extrato:
            print("Não foram realizadas movimentações.")
        else:
            print("\nExtrato:")
            for operacao in self.extrato:
                print(operacao)
            print(f"\nSaldo atual: R$ {self.saldo:.2f}\n")


def main():
    banco = SistemaBancario() #Instancia do objeto que possui os metodos das operações
    while True:
        print("\n--- Sistema Bancário ---")
        print("1. Depositar")
        print("2. Sacar")
        print("3. Extrato")
        print("4. Sair")
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == "1":
            valor = float(input("Informe o valor do depósito: "))
            banco.depositar(valor)
        
        elif opcao == "2":
            valor = float(input("Informe o valor do saque: "))
            banco.sacar(valor)
        
        elif opcao == "3":
            banco.mostrar_extrato()
        
        elif opcao == "4":
            print("Obrigado por usar o sistema bancário. Até logo!")
            break
        
        else:
            print("Opção inválida. Tente novamente.")

# Executa o sistema bancário
main()
