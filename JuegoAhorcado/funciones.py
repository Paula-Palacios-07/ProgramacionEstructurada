import random

alfabeto = "a b c d e f g h i j k l m n ñ o p q r s t u v w x y z"

# Funcion para escojer una palabra random (aleatoria)
def seleccionarPalabra():
  lineas= open("frutas_verduras.txt").readlines()
  palabra = random.choice(lineas).rstrip()
  return palabra

# Funcion entrada del teclado
def entradaUsuario():
  letra = input("Ingrese una letra: ")
  return letra.lower()

# Funcion actualizar jugada
def actualizarJugada(palabra, letra, jugada):
  n_letras = len(palabra)

  for i in range(0, n_letras):
    if palabra[i] == letra:
      jugada[i] = letra
      
  return jugada
#palabra = seleccionarPalabra()
#letra = entradaUsuario()
#jugada = ["_"]*len(palabra)
#jugada = actualizarJugada(palabra, letra, jugada)



# Actalizar el alfabeto
def actualizarAlfabeto(letra,alfabeto):
  alfabeto = alfabeto.replace(letra, " ")
  return alfabeto

#alfabeto = actualizarAlfabeto(letra,alfabeto)
          
# Imprimir resultados de la jugada en pantalla 
def imprimirActualizacion(alfabeto, jugada):
  print(f"Jugada: {jugada}")
  print(f"Letras disponibles: {alfabeto}")

#imprimirActualizacion(alfabeto, jugada)

# Verificar jugada
def verificarJugada(suposicion, palabra):
  success = False
  if suposicion == palabra:
    success = True
  return success
#success = verificarJugada("tomate", palabra)
  