numClientes = int(input("Número de clientes: "));

totalClientes = 0; 
totalCostoGas = 0;
totalCostoLavado = 0;
total_aPagar = 0;

#Objeto cliente
# def cliente(nombre, topGas, litrosGas, lavado):
#     self.nombre = nombre;
#     pass;

def precioPorLitro(p_tipoGas):
    if(p_tipoGas == "P"):
        costoLitro = 20.3;
    elif(p_tipoGas == "E"):
        costoLitro = 19.5;
    elif(p_tipoGas == "D"):
        costoLitro = 21.1;
    else:
        costoLitro = 0;
    
    return costoLitro;

def costoGasolina(p_litrosGas, p_tipoGas):
    gasolinaTotal = p_litrosGas*precioPorLitro(p_tipoGas);
    return gasolinaTotal;

def costoLavado(p_lavado):
    if(p_lavado == "S"):
        return 50;
    else:
        return 0;

def costoTotal(p_litrosGas, p_tipoGas, lavado):
    costoTotal = costoGasolina(p_litrosGas, p_tipoGas);

    if(lavado == "S"):
        if(costoTotal >= 500 and costoTotal < 700):
            return costoTotal+45;
        elif(costoTotal >= 700):
            return costoTotal+40;
        else:
            return costoTotal;
    else:
        return costoTotal;
    
#AQUÍ VA EL PEDIDO DE LOS DATOS DE X CANTIDAD DE CLIENTES, LOS CUALES SE GUARDARÁN EN UN DICCIONARIO

row1Format = "AUTOSERVICIO LINCE";
print(row1Format.center(81));
row2Format = "REPORTE SEMANAL DE GASOLINA Y LAVADO ";
print(row2Format.center(81));
row3Format = "       NOMBRE       TIPO GAS PRECIO/lt. CANT.(lts) COSTO GAS COSTO LAV  A PAGAR  ";
print(row3Format.center(81));

cliente = 0;
while cliente < numClientes:

    nombreCliente = input("Nombre: ");
    tipoGasolina = input("Tipo de gasolina:  ");
    litrosGasolina = int(input("Cuántos litros: "));
    lavado = input("Lavado de auto: ");
    precioLitro = precioPorLitro(tipoGasolina);
    costoGas = costoGasolina(litrosGasolina, tipoGasolina);
    costoLav = costoLavado(lavado);
    totalPago = costoTotal(litrosGasolina, tipoGasolina, lavado);
    cliente += 1;

    totalClientes = cliente; 
    totalCostoGas += costoGas;
    totalCostoLavado += costoLav;
    total_aPagar += totalPago;

    row4Format = nombreCliente.center(20)+tipoGasolina.center(8)+(str(precioLitro)).center(11)+(str(litrosGasolina)).center(11)+(str(costoGas)).center(11)+(str(costoLav)).center(9)+(str(totalPago)).center(11);
    print(row4Format+"\n");

print();
row5Format = print("TOTAL CLIENTES:   "+str(totalClientes));
row6Format = print("TOTAL COSTO GAS:   "+str(totalCostoGas));
row7Format = print("TOTAL COSTO LAVADO:   "+str(totalCostoLavado));
row8Format = print("TOTAL A PAGAR:   "+str(total_aPagar));
