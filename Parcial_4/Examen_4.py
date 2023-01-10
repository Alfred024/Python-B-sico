
row1Format = "CONSTRUCTORA LINCE";
print(row1Format.center(61));
row2Format = "DEPARTAMENTO DE PERSONAL";
print(row2Format.center(61));
row3Format = "REPORTE DE EVALUACION DE SOLICITUDES";
print(row3Format.center(61));
row5Format = "   POSICION: GERENTE DE PROYECTOS ";
print(row5Format+"\n");
row4Format = "      NOMBRE      EXPERIENCIA     ESCOLARIDAD    DECISION    ";
print(row4Format.center(61));

def contratacion(p_experiencia, p_escolaridad):
    if(p_escolaridad == "BD"):
        return "RECHAZAR";

    if(p_escolaridad == "MD"):
        if(p_experiencia >= 4 and p_experiencia <= 6):
            return "CONSIDERAR C";
        elif(p_experiencia < 4):
            return "RECHAZAR";
        elif(p_experiencia > 6):
            return "CONSIDERAR B";
    
    if(p_escolaridad == "PHD"):
        if(p_experiencia > 3):
            return "ENTREVISTAR";
        elif(p_experiencia <= 3):
            return "CONSIDERAR A";

def tieneExperiencia(p_experiencia):
    if p_experiencia > 0:
        return True;
    else:
        return False;

candidato1 = {
    "nombre": "Tomas Reyes",
    "experiencia": 8,
    "escolaridad": "BD",
};
candidato2 = {
    "nombre": "Samuel Torres",
    "experiencia": 5,
    "escolaridad": "MD",
};
candidato3 = {
    "nombre": "Diana Sandoval",
    "experiencia": 3,
    "escolaridad": "MD",
};
candidato4 = {
    "nombre": "Carolina Vara",
    "experiencia": 8,
    "escolaridad": "MD",
};
candidato5 = {
    "nombre": "Arturo Herrera",
    "experiencia": 2,
    "escolaridad": "PHD",
};
candidato6 = {
    "nombre": "Andre Solis",
    "experiencia": 6,
    "escolaridad": "PHD",
};

candidatosRegistro = [candidato1, candidato2, candidato3, candidato4, candidato5, candidato6];

totalRechazados = 0;
totalConsA = 0;
totalConsB = 0;
totalConsC = 0;
totalEntrev = 0;

for candidatoX in candidatosRegistro:
    nombre = candidatoX.get("nombre");
    experiencia = candidatoX.get("experiencia");
    escolaridad = candidatoX.get("escolaridad");

    if(tieneExperiencia(experiencia)):
        decision = contratacion(experiencia, escolaridad);
    else:
        decision = "RECHAZAR";

    if decision == "RECHAZAR":
        totalRechazados += 1;
    elif decision == "CONSIDERAR A":
        totalConsA += 1;
    elif decision == "CONSIDERAR B":
        totalConsB += 1;
    elif decision == "CONSIDERAR C":
        totalConsC += 1;
    else:
        totalEntrev += 1;

    rowcandidatoFormat = nombre.center(18)+" "+(str(experiencia)).center(10)+" "+(str(escolaridad)).center(17)+" "+decision.center(10);
    print(rowcandidatoFormat);


print();
print("TOTAL RECHAZADOS   "+str(totalRechazados));
print("TOTAL CONSIDERAR A "+str(totalConsA));
print("TOTAL CONSIDERAR B "+str(totalConsB));
print("TOTAL CONSIDERAR C "+str(totalConsC));
print("TOTAL ENTREVISTAR  "+str(totalEntrev));