import random
from datetime import date, datetime

#Obtener fecha y hora
fecha = date.today()
fechaFormato = fecha.strftime("%d/%m/%Y")
hora = datetime.now()
horaFormato = str(hora.strftime("%H:%M:%S"));
horaFormato = horaFormato[0:5];

totalEmpleados = 18;
bonoBoolean = False;

def dineroBono(numAleatorio):
    unidad = int((str(numAleatorio))[2]);
    decena = int((str(numAleatorio))[1]);
    centena = int((str(numAleatorio))[0]);

    if(unidad + decena == centena):
        return 10000;
    elif(decena+centena == unidad):
        return 8000;
    elif(centena+unidad == decena):
        return 6000;
    else:
        return 0;

def impuestoBono(bono):
    if(bono == 10000):
        return bono*0.1;
    elif(bono == 8000):
        return bono*0.075;
    elif(bono == 6000):
        return bono*0.05;
    else:
        return 0;

row1Format = "EMPRESAS LINCE";
print(row1Format.center(46));
row2Format = "RESULTADOS DE BONOS MENSUALES";
print(row2Format.center(46));
row3Format = "FECHA: "+ str(fechaFormato) +"         HORA: "+str(horaFormato);
print(row3Format.center(46));
row4Format = " NOMBRE  NÚMERO    BONO    IMPUESTO   RECIBE  ";
print(row4Format.center(46));

emp_cBono = 0;
bonosTotal = 0;
impuestosTotal = 0;
recibeTotal = 0;

for empleadoN in range(1, totalEmpleados+1):
    aleatorio = random.randint(100, 999);
    bono = dineroBono(aleatorio);
    impuesto = impuestoBono(bono);
    recibe = bono-impuesto;

    if(bono > 0):
        emp_cBono += 1;
    
    bonosTotal += bono;
    impuestosTotal += impuesto;
    recibeTotal += recibe;
    rowEmpleadoFormat = str(empleadoN).center(8)+" "+(str(aleatorio)).center(8)+" "+(str(bono)).center(10)+" "+(str(impuesto)).center(10)+" "+str(recibe).center(10);
    print(rowEmpleadoFormat);

print();
print("TOTAL EMPLEADOS           "+str(totalEmpleados));
print("TOTAL EMPLEADOS CON BONO  "+str(emp_cBono));
print("TOTAL BONOS              $"+str(bonosTotal));
print("TOTAL IMPUESTOS          $"+str(impuestosTotal));
print("TOTAL RECIBE             $"+str(recibeTotal));


