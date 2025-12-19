#Simula el lanzamiento de una moneda utilizando if-else y la biblioteca random
import random

num = random.randint(0, 1)   # genera un numero random entre 0 y 1

if num > 0.5:
  print('cara')
else:
  print('cruz')