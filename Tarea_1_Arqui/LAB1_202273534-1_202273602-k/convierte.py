def entero_bin(entero):
    '''
    Parametros:
    * entero Tipo: int
    Descripcion:
    *Toma el numero y lo divide en 2.Para luego guardar su modulo
    *Con el objetivo de transformarlo a binario y este retornarlo
    Retorno:
    * bin_entero Tipo: list
    '''
    bin__entero = []
    while entero != 0:
        bin__entero.append(entero % 2)
        entero = entero // 2
    bin__entero.reverse()

    return bin__entero

def decimal_bin(decimal,limite):
    '''
    Parametros:
    * decimal Tipo: float
    * limite Tipo: int
    Descripcion:
    * Toma el numero lo multiplica por 2. Para luego guardar la parte entera
    * Con el objetivo de transformarlo a binario y este retornarlo.
    * Se detiene al llegar al limite o hasta 0
    Retorno:
    * bin_decimal Tipo: list
    '''
    bin_decimal = []
    contador = 0
    while contador < (23 - limite):
        if decimal == 0.0 or decimal == 1.0:
            break
        if (decimal*2.0 >= 1.0):
            bin_decimal.append(1)
            decimal = decimal*2.0 - 1.0
        elif(decimal*2.0 < 1.0):
            bin_decimal.append(0)
            decimal = decimal*2.0
        contador +=1

    return bin_decimal

def int_to_binary(numero):
    '''
    Parametros:
    * numero Tipo: float
    Descripcion:
    * Recibe un float y lo transforma a binario, guardandolo en una lista
    * Retorna lista de el numero en binario y su signo
    Retorno:
    * entero Tipo: list
    * es_negativo Tipo: bool
    '''
    es_negativo = False
    numero = float(numero)
    entero = int(numero)
    if entero <0:
        es_negativo= True
        entero = entero *-1

    decimal = round((abs(numero) - entero),10)
    entero= entero_bin(entero)
    decimal= decimal_bin(decimal,len(entero)-1)
    entero.append('.')
    entero = entero + decimal

    return(entero,es_negativo)

def suma_bin(num1,num2):
    '''
    Parametros:
    * num1 Tipo: List
    * num2 Tipo: list
    Descripcion:
    * Hace la suma de la mantissa de dos numeros en binario
    * Retorna la suma junto con el orden
    Retorno:
    * resultado Tipo: list
    * orden Tipo: int
    '''
    signo = num1[0]
    if signo == 0:
        signo = False
    elif signo == 1:
        signo = True
   
    exponente1 = num1[1:9]
    exponente1 = binary_to_int(exponente1)
    mantissa1 = num1[9:]
    mantissa1.insert(0,'.')
    mantissa1.insert(0,1)

    exponente2 = num2[1:9]
    exponente2 = binary_to_int(exponente2)
    mantissa2 = num2[9:]
    mantissa2.insert(0,'.')
    mantissa2.insert(0,1)

    shift = exponente1 - exponente2
    if shift < 0:
        i = 0
        while i != abs(shift):
            mantissa1.pop(1)
            mantissa1.insert(0,'.')
            mantissa1.insert(0,0)
            i += 1
        orden = exponente2 - 127

    elif shift > 0:
        i = 0
        while i != shift:
            mantissa2.pop(1)
            mantissa2.insert(0,'.')
            mantissa2.insert(0,0)
            i += 1
        orden = exponente1 - 127
   
    mantissa1.remove('.')
    mantissa2.remove('.')
    mantissa1.reverse()
    mantissa2.reverse()

    suma =[]
    contador = 0
    carri = 0

    while len(mantissa1) != len(mantissa2):
        if len(mantissa1) > len(mantissa2):
            mantissa2.insert(0,0)
        elif len(mantissa1) < len(mantissa2):
            mantissa1.insert(0,0)
   

    while contador<len(mantissa1) or contador<len(mantissa2):
        if (mantissa1[contador] == 0)and(mantissa1[contador] == mantissa2[contador]):
            if carri == 1:
                suma.append(1)
                carri = 0
            elif carri == 0:
                suma.append(0)
        elif (mantissa1[contador] == 1)and(mantissa1[contador] == mantissa2[contador]):
            if carri == 1:
                suma.append(1)
            elif carri == 0:
                suma.append(0)
                carri = 1
        else:
            if carri == 1:
                suma.append(0)
            elif carri == 0:
                suma.append(1)
        contador +=1
   
    if mantissa1[-1] == 1 and mantissa2[-1] == 1:
        suma.append(0)
        suma.append(1)
    suma.reverse()
   
    if mantissa1[-1] == 1 and mantissa2[-1] == 1:
        suma.insert(2,'.')
    else:
        suma.insert(1,'.')

    i = 0
    while i < len(suma):
        if suma[i] == 1:
            break
        else:
            suma.pop(0)
    resultado = list(suma[:23])

    return resultado,orden

def binary_to_32bits(numero):
    '''
    Parametros:
    * numero Tipo: string
    Descripcion:
    * Recibe un numero en binario y lo transforma a 32 bits
    * Retorna el numero, como lista, en 32bits
    Retorno:
    * numero_final Tipo: list
    '''
    numero,signo = int_to_binary(float(numero))
    numero,pos_primer_1,orden = modo_cientifico(numero)
    numero_final=[]

    if signo == False:
        numero_final.append(0)
    else:
        numero_final.append(1)
    exponent,y = int_to_binary(float(127+ orden))
    exponent.remove('.')
    while len(exponent)<8:
        exponent.insert(0,0)
    numero_final= numero_final + exponent

    mantissa = numero[pos_primer_1+2:]
    while len(mantissa)< 23:
        mantissa.append(0)
    numero_final =numero_final +mantissa

    return numero_final 

def sum_to_32bits(numero,orden,es_negativo):
    '''
    Parametros:
    * numero Tipo: list
    * orden Tipo: int
    * es_negativo Tipo: bool
    Descripcion:
    * Recibe la suma de dos numeros en binario y lo transforma a base de 32 bits
    * Retorna el numero, como lista, en 32bits
    Retorno:
    * numero_final Tipo: list
    '''
    numero_final=[]

    if es_negativo == False:
        numero_final.append(0)
    else:
        numero_final.append(1)
    exponent,y = int_to_binary(float(127+ orden))
    exponent.remove('.')

    while len(exponent)<8:
        exponent.insert(0,0)
    numero_final= numero_final + exponent

    i = 0
    pos_punto = 0
    while i < len(numero):
        if numero[i] == '.':
            pos_punto = i
            break
        i += 1

    mantissa = numero[pos_punto+1:]
    while len(mantissa)< 23:
        mantissa.append(0)
    numero_final =numero_final + mantissa

    return numero_final

def modo_cientifico(numero):
    '''
    Parametros:
    * numero Tipo: list
    Descripcion:
    * Recibe un numero binario con punto y mueve el punto a la derecha del primer uno hacia la izquierda
    * Retorna un numero como lista, la posicion del primer 1 y el orden
    Retorno:
    * numero Tipo: list
    * pos_primer_1 Tipo: int
    * orden Tipo: int
    '''
    i = 0
    pos_punto_inicial = -1

    while i <len(numero):
        if numero[i] == '.':
            pos_punto_inicial = i
            break
        i += 1
    i = 0
    pos_primer_1 =-1

    while i <len(numero):
        if numero[i] == 1:
            pos_primer_1 = i
            break
        i += 1
    orden = 0
    if pos_punto_inicial != -1:
        if pos_punto_inicial > pos_primer_1:
            orden= pos_punto_inicial-pos_primer_1-1
            numero.pop(pos_punto_inicial)
            numero.insert(pos_primer_1+1,'.')

        elif pos_punto_inicial < pos_primer_1:
            orden= pos_punto_inicial-pos_primer_1
            numero.pop(pos_punto_inicial)
            numero.insert(pos_primer_1,'.')
           
    return (numero,pos_primer_1,orden)

def binary_to_int(binario):
    '''
    Parametros:
    * binario Tipo: list
    Descripcion:
    * Recibe un numero binario como lista y lo transforma a base decimal
    * Retorna el numero en base decimal
    Retorno:
    * decimal Tipo: int
    '''
    binario.reverse()
    i = 0
    decimal = 0
    while i < len(binario):
        decimal += binario[i]*(2**i)
        i += 1

    return decimal

def bits32_to_dec(numero):
    '''
    Parametros:
    * numero Tipo: list
    Descripcion:
    * Recibe un numero binario como lista y lo transforma a base decimal
    * Retorna el numero en base decimal redondeado al tercer decimal
    Retorno:
    * num_final Tipo: float
    '''
    signo = numero[0]
    exponente = numero[1:9]
    exponente = binary_to_int(exponente)
    orden = exponente - 127
    mantissa = numero[9:]
    mantissa_dec = 0
    i = 1

    while i <= len(mantissa):
        exp = -i
        mantissa_dec += mantissa[i-1] * (2**exp)
        i += 1

    num_final = ((-1)**signo) * (1 + mantissa_dec) * (2**orden)

    return round(num_final,3)

def distinto_signo(bin1,bin2):
    '''
    Parametros:
    * bin1 Tipo: list
    * bin2 Tipo: list
    Descripcion:
    * Recibe 2 numeros en binario, como lista, y los escribe en resultados.txt
    '''
    bin1 = "".join([str(elemento) for elemento in bin1])
    bin2 = "".join([str(elemento) for elemento in bin2])

    with open("resultados.txt" , "a") as arch_resultados:
        arch_resultados.write(linea[0]+'/'+bin1+';'+linea[1]+'/'+bin2+'\n')
   
def mismo_signo(bin1,bin2):
    '''
    Parametros:
    * bin1 Tipo: list
    * bin2 Tipo: list
    Descripcion:
    * Recibe 2 numeros en binario, como lista, los suma 
    * y despues escribe el resultado en resultados.txt
    '''
    suma,orden = suma_bin(bin1,bin2)
    resultado_bin_32 = sum_to_32bits(suma,orden,bin1[0])
    resultado_dec = bits32_to_dec(resultado_bin_32)
    resultado_bin_32 = "".join([str(elemento) for elemento in resultado_bin_32])

    with open("resultados.txt" , "a") as arch_resultados:
        arch_resultados.write(str(resultado_dec)+'/'+resultado_bin_32+'\n')


lineas_totales = 0
lineas_sum = 0
lineas_no_sum = 0
postivos = 0
negativos = 0

with open("operaciones.txt", "r") as archivo:
    for linea in archivo:
        lineas_totales +=1
        linea = linea.split(';')

        bin1 = binary_to_32bits(linea[0])
        bin2 = binary_to_32bits(linea[1])

        if bin1[0] != bin2[0]:
            distinto_signo(bin1,bin2)
            lineas_no_sum += 1
        else:
            mismo_signo(bin1,bin2)
            if bin1[0] == 0:
                postivos += 1
            elif bin1[0] == 1:
                negativos += 1
            lineas_sum +=1

print("\nSe procesaron "+ str(lineas_totales) + " lineas")
print("Fue posible hacer "+ str(lineas_sum) + " sumas")
print("No se pudo procesar "+ str(lineas_no_sum)+ " sumas")
print("Cantidad de numeros positivos: "+ str(postivos) + "\nCantidad de numeros negativos: " + str(negativos) + "\n")
