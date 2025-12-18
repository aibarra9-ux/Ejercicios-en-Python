#Crea un programa que pregunte al usuario el monto que tiene en pesos, soles y reales 
# y calcule el total en USD.

pesos = int(input("Cuantos pesos colombianos le quedan?:  "))
soles = int(input("Cuantos soles le quedan?:  "))
reales = int(input("Cuantos reales le quedan?:  "))
dolar_peso = pesos * 0.00024
dolar_soles = soles * 0.28 
dolar_reales = reales * 0.18
dolares_total = dolar_peso + dolar_soles + dolar_reales
print(dolares_total)