import datetime

def cria_conta(numero, titular, saldo, limite):
  conta = {
    "numero" : numero,
    "titular" : titular,
    "saldo" : saldo,
    "limite" : limite,
    "transacoes" : list()
  }
  return conta

def deposita(conta, valor):
  if valor > 0:
    conta["saldo"] += valor 
    valor_impressao = f"R$ {valor}"
    add_transacao(conta, "Deposito", valor_impressao)
    print("Deposito realizado com sucesso!")
  else:
    print("Não e possivel realizar depositos com valores negativos.")

def saca(conta, valor):
  if conta['saldo'] >= valor:
    conta["saldo"] -= valor
    valor_impressao = f"R$ {valor}"
    add_transacao(conta, "Saque", valor_impressao)
    print("saque realizado com sucesso.")
  else:
    print("Saldo insuficiente para saque.")

def add_transacao(conta, operacao, valor):
  data_hoje = str(datetime.datetime.now())
  nova_transacao = (data_hoje, operacao, valor)
  conta["transacoes"].append(nova_transacao)
  
def extrato(conta):
  print(f"Numero: {conta['numero']} \n Titular: {conta['titular']}")
  for transacao in conta["transacoes"]:
    print(f"{transacao[0]} \n Titular: {conta['titular']}")
    for transacao in conta['transacoes']:
  
      print("Conta criada com sucesso!")
nova_conta = cria_conta('123-7', 'Yan Gabriel', 200.99, 500.00)

deposita(nova_conta, 100.00)
extrato(nova_conta)

saca(nova_conta, 200)
extrato(nova_conta)