#Cree un programa que pueda responder a cualquier pregunta de Sí o No 
# con una respuesta diferente cada vez que se ejecute.

import random
input("Hola usuario, haga su pregunta por favor: ")
bola8 = ["Yes - definitely", "It is decidedly so.", "Without a doubt.", "Reply hazy, try again.", "Ask again later.", "Better not tell you now.", "My sources say no.", "Outlook not so good.", "Very doubtful.""Sí, definitivamente", "Decididamente así", "Sin duda", "Respuesta confusa, inténtalo de nuevo", "Pregunta más tarde", "Mejor no te lo digo ahora", "Mis fuentes dicen que no", "Las perspectivas no son muy buenas", "Muy dudoso"]
random = random.randint(0, 7)

print(bola8[random])