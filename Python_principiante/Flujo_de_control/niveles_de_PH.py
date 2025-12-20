#Cree un programa que verifique si un nivel de pH es básico, ácido o neutro
pH = int(input("Proporciona un numero entre 0 y 14: "))

if (pH > 7) and (pH < 15):
  print("Basico")
elif (pH < 7) and (pH >= 0):
  print("Ácido")
else:
  print("Neutral")