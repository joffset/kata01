# numero para resultado tabla multiplicar

tabla = int(input("Dime el valor a multiplicar? = "))

if(instance(tabla, int) in range(11)):
    
    for i in range(11):
      print(str(tabla) + " x " + str(i) + " = " + str((tabla*i)))
else:
    print("Solo puedes teclear numeros")
