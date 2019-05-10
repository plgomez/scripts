"""
script que calcula el reparto de bancas por sitema d'hont
'"""

import string

A = 5000
B = 3000
C = 1400

ELECTORES = 5

votos = [A, B, C]
listas = list(string.ascii_uppercase)


#inicializamos la lista de elegios y cociente en 0
cociente = []
elegidos = []
for j in range(len(votos)):
	elegidos.append(0)
	cociente.append(0)
	

#formula = votos/(elegidos + 1)

for i in range(ELECTORES):
	print("Iteración ", i+1), 
	for j in range(len(votos)):
		cociente[j] = votos[j]/(elegidos[j]+1)
	maxpos = cociente.index(max(cociente))
	print("Seleccionado el candidato de la lista ", listas[maxpos])
	elegidos[maxpos] += 1
	print(cociente)
	print(elegidos)
	print()
print(elegidos)
