''' Escribir un programa que pida al usuario su peso (en kg) y estatura (en metros), 
calcule el índice de masa corporal y lo almacene en una variable, y muestre
 por pantalla la frase Tu índice de masa corporal es <imc> donde <imc> es el índice 
 de masa corporal calculado redondeado con dos decimales. '''



	#Pregunta al usuario su peso y altura
peso = input('Escribe tu peso (kg): ')
estatura = input('Escribe tu estatura (m): ')

imc = round(float(peso)/float(estatura) **2,2)
print('Su imc es:' + str(imc))