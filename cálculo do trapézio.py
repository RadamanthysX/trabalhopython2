def message(msg):
  print("---------------------------------------------------------")
  print(msg)
  print("---------------------------------------------------------")


def calcAreaTrap(bmaior, bmenor, h):
  area = ((bmaior + bmenor) * h) / 2
  message("O valor da area é igual a %s" % (area))


message("Bem vindo ao Sistema Trap")
bmaior = float(input("Entre com o valor da base maior: "))
bmenor = float(input("Entre com o valor da base menor: "))
h = float(input("Entre com o valor da altura: "))
calcAreaTrap(bmaior, bmenor, h)
message("Fim")
