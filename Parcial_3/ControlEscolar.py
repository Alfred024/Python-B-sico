
from datetime import date, datetime

#Obtener fecha y hora
fecha = date.today()
fechaFormato = fecha.strftime("%d/%m/%Y")
hora = datetime.now()
horaFormato = str(hora.strftime("%H:%M:%S"));
horaFormato = horaFormato[0:5];

def diaInscripcion(p_promedio, p_semestre):
    if(p_semestre < 13 and p_semestre > 0):
        if(p_promedio >= 90 and p_promedio <= 100):
            return 1;
        elif(p_promedio >= 80 and p_promedio <= 89):
            return 2;
        elif(p_promedio >= 70 and p_promedio <= 79):
            return 3;
        else:
            return 4;
    else:
        return 0;

def inscritoObaja(p_credsAprobs, p_semestre):
    if(p_semestre == 13 or p_credsAprobs < 50):
        return "BAJA"
    else:
        return "INSCRIBIR"

#Datos de alumno X
nombre;
promedio;
credsAprobs;
semestre;


row1Format = "TECNOLÓGICO LINCE";
print(row1Format.center(52));
row2Format = "REPORTE DE INSCRIPCIONES";
print(row2Format.center(52));
row3Format = "FECHA: dd/mm/aaaa HORA: hh:mm";
print(row3Format.center(52));
row4Format = " NOMBRE PROMEDIO % CRÉDITOS APROB. SEM. MENSAJE DÍA ";
print(row4Format.center(52));

# Los datos para cada alumno son: nombre, promedio, porcentaje de créditos aprobados y 
# semestre al que se van a inscribir. Ejemplo: