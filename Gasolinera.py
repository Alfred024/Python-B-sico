nombreCliente = "Manuel García";
tipoGasolina = "E";
litrosGasolina = 50;
lavado = "S";

#Objeto cliente
# def cliente(nombre, topGas, litrosGas, lavado):
#     self.nombre = nombre;
#     pass;

def costoGasolina(p_litrosGas, p_tipoGas):
    if(p_tipoGas == "P"):
        gasolinaTotal = p_litrosGas*20.3;
    elif(p_tipoGas == "E"):
        gasolinaTotal = p_litrosGas*19.5;
    elif(p_tipoGas == "D"):
        gasolinaTotal = p_litrosGas*21.1;
    
    return gasolinaTotal;

def costoTotal(p_litrosGas, p_tipoGas, lavado):
    if(lavado == "S"):
        costoTotal = costoGasolinaTotal(p_litrosGas, p_tipoGas)+50;
    else:
        costoTotal = costoGasolinaTotal(p_litrosGas, p_tipoGas);
    
    if(costoTotal >= 500 and costoTotal < 700):
        return costoTotal*0.9;
    elif(costoTotal >= 700):
        return costoTotal*0.8;
    else:
        return costoTotal;
        

costoGasolinaTotal = costoGasolina(litrosGasolina, tipoGasolina);



row1Format = "AUTOSERVICIO LINCE";
row2Format = "REPORTE SEMANAL DE GASOLINA Y LAVADO ";
row3Format = "NOMBRE TIPO GAS PRECIO/lt. CANT.(lts) COSTO GAS COSTO LAV A PAGAR";