from funciones import *

def main():
  palabra = seleccionarPalabra()
  alfabeto = "a b c d e f g h i j k l m n ñ o p q r s t u v w x y z"
  jugada = ["_"]*len(palabra)

  for turno in range(5):
    print(f"\nTurno: {turno+1}")
    print("-"*20)
    #Imprimir alfabeto y jugada
    imprimirActualizacion(alfabeto, jugada)
    #Entrada usuario
    letra = entradaUsuario()
    #actualizar jugada y alfabeto
    jugada = actualizarJugada(palabra, letra, jugada)
    alfabeto = actualizarAlfabeto(letra, alfabeto)
    #imprimir Actualizacion
    imprimirActualizacion(alfabeto, jugada)
    #Preguntar al usuario si desea adivinar o no la palabra
    check = input("Desea adivinar la palabra? (s/n): ")
    if check.lower() == "s":
      suposicion = input("Introduzca su respuesta: ").lower()
      success = verificarJugada(suposicion, palabra)
    
      if success: 
        print("+"*20)
        print("GANASTE !!")
        print("+"*20)
        break
      else:
        print("+"*20)
        print("Incorrecto !!")
        print("+"*20)
    if turno == 4:
      print("-"*20)
      print("=( AHORCADOOO !")
      print("-"*20)

if __name__=="__main__":
  main()
