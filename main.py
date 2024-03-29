import menu
import operacions_basiques.suma as suma
import operacions_basiques.resta as resta
import operacions_basiques.multiplicacio as multiplicacio
import operacions_basiques.divisio as divisio
import operacions_extra.divisio_entera as divisio_entera
import operacions_extra.factorial as factorial
import operacions_extra.mitjana as mitjana
import operacions_extra.primer as primer

print("Iniciando calculadora...")
menu.menu()

while True:
    caracter = input("Introduzca la operacion a realizar: ")

    if caracter != "salir":
        try:
            def operador(caracter):
                if caracter == "+":
                    numero1 = int(input("Introduzca el primer numero: "))
                    numero2 = int(input("Introduzca el segundo numero: "))
                    return suma.suma(numero1, numero2)
                elif caracter == "-":
                    numero1 = int(input("Introduzca el primer numero: "))
                    numero2 = int(input("Introduzca el segundo numero: "))
                    return resta.resta(numero1, numero2)
                elif caracter == "*":
                    numero1 = int(input("Introduzca el primer numero: "))
                    numero2 = int(input("Introduzca el segundo numero: "))
                    return multiplicacio.multiplicacio(numero1, numero2)
                elif caracter == "/":
                    numero1 = int(input("Introduzca el primer numero: "))
                    numero2 = int(input("Introduzca el segundo numero: "))
                    return divisio.divisio(numero1, numero2)
                elif caracter == "%":
                    numero1 = int(input("Introduzca el primer numero: "))
                    numero2 = int(input("Introduzca el segundo numero: "))
                    return divisio_entera.divisio_entera(numero1, numero2)
                elif caracter == "!":
                    numero = int(input("Introduzca un numero: "))
                    return factorial.factorial(numero)
                elif caracter == "?":
                    numero = int(input("Introduzca un numero: "))
                    return primer.primer(numero)
                elif caracter == "@":
                    lista = []
                    while True:
                        numero = input("Introduzca un numero: ")
                        if numero != "fin":
                            lista.append(int(numero))
                        else:
                            break
                    return mitjana.mitjana(lista)
                else:
                    print("Introduzca una operacion valida")
                    raise ValueError("Operación no válida")
        except ValueError as valErr:
            print(f"Error: {valErr}")
        except ZeroDivisionError:
            print("Error: No se puede dividir por cero")
        except Exception as e:
            print(f"Error inesperado: {e}")
    else:
        break

print(operador(caracter))
