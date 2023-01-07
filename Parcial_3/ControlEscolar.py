
from datetime import date, datetime

#Obtener fecha y hora
fecha = date.today()
fechaFormato = fecha.strftime("%d/%m/%Y")
hora = datetime.now()
horaFormato = str(hora.strftime("%H:%M:%S"));
horaFormato = horaFormato[0:5];

row1Format = "TECNOLÓGICO LINCE";
print(row1Format.center(52));
row2Format = "REPORTE DE INSCRIPCIONES";
print(row2Format.center(52));
row3Format = "FECHA: dd/mm/aaaa HORA: hh:mm";
print(row3Format.center(52));
row4Format = " NOMBRE PROMEDIO % CRÉDITOS APROB. SEM. MENSAJE DÍA ";
print(row4Format.center(52));

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
alumno = {
        "nombre": "Juán López",
        "promedio": 75,
        "credsAprobs": 90,
        "semestre": 6
    }
alumno2 = {
        "nombre": "Vicente Álvarez",
        "promedio": 49,
        "credsAprobs": 30,
        "semestre": 2
    };
alumno3 = {
        "nombre": "Luis Soto",
        "promedio": 79,
        "credsAprobs": 80,
        "semestre": 13
    };
alumno4 = {
        "nombre": "Vicente Álvarez",
        "promedio": 82,
        "credsAprobs": 60,
        "semestre": 4
    };

alumnosRegistro = [alumno, alumno2, alumno3, alumno4];
print(alumnosRegistro[0].get("nombre")); #Así acccedo al "key" nombre de

for i in alumnosRegistro:
    nombre = alumnosRegistro[i].get("nombre");
    credsAprobs = alumnosRegistro[i].get("credsAprobs");
    semestre = alumnosRegistro[i].get("semestre");
    promedio = alumnosRegistro[i].get("promedio");
    mensaje = inscritoObaja(credsAprobs, semestre);
    if(mensaje == "BAJA"):
        dia = 0;
    else:
        dia = diaInscripcion(promedio, semestre);
    #rowAlumnoFormat = alumnosRegistro[i].get("nombre");
    pass;

