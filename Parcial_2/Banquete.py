def totalReal(p_numPersonas, p_tipoMenu):
    if(p_tipoMenu == 1):
        return p_numPersonas*150;
    else:
        return p_numPersonas*200;

def totalDescuento(p_numPersonas, p_tipoMenu):
    descuento = 0;
    if (p_tipoMenu == 2):
        descuento += (totalReal(p_numPersonas, p_tipoMenu))*0.1;

    if (p_numPersonas > 100):
        descuento += (totalReal(p_numPersonas, p_tipoMenu)-descuento)*0.05;
    return descuento;        

def totalAPagar(p_numPersonas, p_tipoMenu):
    totalR = totalReal(p_numPersonas, p_tipoMenu);
    descuento = totalDescuento(p_numPersonas, p_tipoMenu);
    resultado = totalR-descuento;
    return resultado;

cliente = "Diana García";
numPersonas = 100;
tipoMenu = 1;
cuenta = totalReal(numPersonas, tipoMenu);
descuento = totalDescuento(numPersonas, tipoMenu);
pago = totalAPagar(numPersonas, tipoMenu);

row1Format = "BANQUETES LINCE";
print(row1Format.center(46));
row2Format = "PRESUPUESTO PARA: "+cliente+"\n";
print(row2Format);
row3Format = "N0.PERSONAS TIPO MENU  CUENTA DESCUENTO A PAGAR";
print(row3Format.center(46));
row4Format = str(numPersonas).center(20)+str(tipoMenu).center(11)+str(cuenta)+str(descuento).center(12)+str(pago).center(8);
print(row4Format);