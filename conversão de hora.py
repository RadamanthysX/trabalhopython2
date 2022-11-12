def message(msg):
  print("---------------------------------------------------------")
  print(msg)
  print("---------------------------------------------------------")
  
def converter_hora(hora):
	if hora > 12 and hora != 24:
		contador = 0
		for x in range(hora):
			if x >= 12:
				contador+=1
		return contador
	elif hora == 24:
		return 0
	else:
		return hora
    
controle = 0
a = "AM"
p = "PM"
periodo = a 
while controle >= 0:
  hora = int(input("Digite a hora a ser convertida: "))
  if hora <= -1 or hora >= 24:
    break
  minuto = int(input("Digite o minuto: "))
  if hora >= 12:
    periodo = p
  else:
    periodo = a
  message("Convertido: %i:%i %s" %(converter_hora(hora),minuto,periodo))
message("Obrigado até mais")