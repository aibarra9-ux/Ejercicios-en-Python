#Cree un programa que verifique si una calificación es superior o inferior a 55.
#Si la calificación es mayor o igual a 55, entonces escriba "Aprobó".
#De lo contrario, escriba "Falló".

cal = int(input("Cuanta es su calificación?:  "))

if cal >= 55:
  print("Pasaste")
else:
  print("No pasaste")