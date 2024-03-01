# #variables y tipos de datos
# import random
# #1.conversor de temparatura
# Celcius=int(input("ingrese un valor"))#declaramos variables
# Farenheirt=int(input("ingrese un valor"))

# conversion = ((Celcius * 9/5) + 32 )#formula para convertir a Fahrenheit
# print ("la conversion a Fahrenheit es: ", conversion)

# viseversa=((Farenheirt - 32) * 5/9)#formula para volver a Celsius

# print( "La conversion a Celsius es: ", viseversa)#impresion de la misma


# #2.conversor IMC

# print("programa  que calcula e l indice  de masa corporal")


# peso=float(input("ingrese su peso"))
# altura=float(input("ingrese su altura "))#declaracion de variables


# Indicedemasacorporal=(peso/altura)#formula IMC

# print(f"su imc es ",Indicedemasacorporal)#impresion del resultado

# #3.generador de nombres basico

# print("ingrese sus datos personales")
# nombre=str(input("ingrese nombre completo "))#consulta de datos personales 
# apellido=str(input("ingrese apellido "))
# fecha_nacimiento=input("ingrese fecha de nacimiento en formato")


# contraseña=nombre+apellido+fecha_nacimiento#generacion de contraseña
# print("su contraseña sera", contraseña)#impresion de la misma

# #Estructuras de Control

# #numero aleatorio

# numero=random.randint(1,10)

# numuser=int(input("ingresee un numero"))

# for i in range  (0,3): #el rango se va a repetir 3 veces


#     if numuser > numero :    
#         print("el numero es demasiado grande vuelva a intentarlo")
#     elif numuser < numero:
#         print("el numero es demasiado pequeño vuelva a intentarlo")
#     elif numuser==numero :
#         print("felicidades adivino el numero correcto")

# print("el numero de veces q se demoro en acertar el numero fue de ",i)


#Calculadora de Factorial
# def factorial(n):
#     if n == 0 and n==1:
#         return 1
#     else:
#         i=0
#         resultado=1
#         while i <n:
#             resultado=resultado*i
#             i+=1
#         return resultado
# print(
#     factorial(5)
# )



lista = []
# n = int(input("Ingrese un número de elementos: "))

# for i in range(1, n + 1):
#     valor = str(input("Ingrese un elemento: "))
    
#     if valor not in lista:
#         lista.append(valor)

# print("Lista sin duplicados:", lista)

#diccionario de sinonimos

# diccionario={"perro":"canino","gato":"felino","persona":"Homo sapiens","pajaro":"aves_lineaeus"}
# clave=str(input("ingrese uyna clave"))
# if clave in diccionario:
#     valor=diccionario[clave]
#      print(f"El valor asociado con la clave '{clave}' es '{valor}'")
# else:
#     print(f"La clave '{clave}' no está en el diccionario")
# print("el diccionario es ",diccionario)

# lista=[]
# n=int(input("ingrese un numero"))
# for i in range(1,n+1):
#     valor=int(input("ingrese un numero"))
#     lista.append(valor)

# maxnum=max(lista)
# minnum=min(lista)

# print(maxnum)
# print(minnum)

# lista1=[]
# lista2=[]
# n=int(input("ingrese un numero"))

# for i in range (1,n+1):
#     valor1=int(input("ingrese un numero"))
#     lista1.append(valor1)

# for i in range (1,n+1):
#     valor2=int(input("ingrese un numero"))
#     lista2.append(valor2)

# print("la cocatenacionnes "lista1+lista2)

# tupla=(1,2,3,4,5,6,7,8,9,10)


# tupla_invertida=tupla[::-1]


# print("la tupla invertidfa e s",tupla_invertida)


   