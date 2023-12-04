Sebastian Muñoz 202273534-1 201
Miguel Huerta 202273602-k 201

Especificacion de los algoritmos y desarrollo realizado:
    -Principalmente se utilizaron listas para trabajar con los numeros en binario.
    -La forma que usamos para sumar los numeros fue voltear las listas
    para asi hacer la suma mas facil y finalmente voltear la lista obteniendo asi el resultado.
    -La formula que se utilizo para pasar de 32 bits a decimal fue:
                        [(-1)**S] * (1+M) * (2**O)
    Donde:
    S = signo
    M = mantissa recorrida de izquierda a derecha y multiplicando el valor de
    la posicion por potencias de 2, elevadas desde -1 hasta recorrer toda la mantissa
    O = orden
    -Se redondeo al tercer decimal

Supuestos:
    -La cantidad de numeros positivos y negativos imprimidos en pantalla
    son aquellos de las sumas y no de las sumas no realizadas.

Instrucciones:
    -El archivo a leer se debe llamar "operaciones.txt"