from modulos import calculadora, ui

seguir = True
while seguir:    
    ui.clean()
    ui.screen()
  
    oper = int(input("Ingrese in tipo de operacion"))
    value1 =  int(input("Ingrese en primer valor"))
    value2 =  int(input("Ingrese en segundo valor"))
   
    resultado = calculadora.calcular(oper, value1, value2)

    print("El resultado es:", resultado)

    a = input("desea seguir (S/N)")
    if (a == "N"):
        seguir = False
