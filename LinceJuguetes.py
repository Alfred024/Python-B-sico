import math;
muñecas = int(input("Número de muñecas: "));
payasos = int(input("Número de payasos: "));
totalJuguetes = muñecas+payasos;

# Cada función debe calcular un valor individual para que podamos imprimirlo en cada sección correspondiente
def redondeo(numero):
    numRounded = float("%.2f" % numero);
    return numRounded;

def getCostoJuguetes(totalJuguetes):
    costo = (10+5*(math.sqrt(totalJuguetes)))*2.4;
    costoRounded = redondeo(costo);
    return costoRounded;

def getPrecioTotalVenta(totalJuguetes):
    precioxJuguete = (getCostoJuguetes(totalJuguetes)/totalJuguetes);
    precioTotalVenta = (precioxJuguete)*totalJuguetes;   
    precioTotalVentaRounded = redondeo(precioTotalVenta);
    return precioTotalVentaRounded;

def getPesoTotalJuguetes(muñecas, payasos):
    pesoTotalMuñecas = 75*muñecas;
    pesoTotalPayasos = 112*payasos;
    pesoTotal = pesoTotalPayasos+pesoTotalMuñecas;
    return pesoTotal;

def getCostoTotalPorPeso(muñecas, payasos):
    costo = getPesoTotalJuguetes(muñecas, payasos)*0.16;
    return costo;

def getTotalPedido(muñecas, payasos):
    precioFinal = getCostoTotalPorPeso(muñecas, payasos) + getPrecioTotalVenta(muñecas)+getPrecioTotalVenta(payasos);
    return precioFinal;


precioxMuñeca = str(redondeo(getCostoJuguetes(muñecas)/muñecas));
precioxPayaso = str(redondeo(getCostoJuguetes(payasos)/payasos));
precioTotalMuñecas = str(getPrecioTotalVenta(muñecas));
precioTotalPayasos = str(getPrecioTotalVenta(payasos));
pesoTotal = getPesoTotalJuguetes(muñecas, payasos);
costoEnvio = str(redondeo(pesoTotal*0.16));
costoTotal = str(redondeo(getTotalPedido(muñecas, payasos)));


row1Format = "JUGUETERÍA LINCE";
print(row1Format.center(34));
row2Format = "FACTURA DEL PEDIDO";
print(row2Format.center(34));
row3Format = "No. de muñecas: "+str(muñecas)+"  No. de payasos: "+str(payasos);
print(row3Format);
row4Format = "Precio por muñeca: $"+precioxMuñeca+"  Precio por payaso: $"+precioxPayaso+"\n";
print(row4Format);
row5Format = "Costo total muñecas: $"+precioTotalMuñecas+"\nCosto total payasos: $"+precioTotalPayasos+"\n";
print(row5Format);
row6Format = "Peso total del paquete: "+ str(pesoTotal)+" gramos";
print(row6Format);
row7Format = "Costo del envío:   $"+ costoEnvio;
print(row7Format);
row8Format = "Gran total del pedido: $"+ costoTotal;
print(row8Format.center(34));
