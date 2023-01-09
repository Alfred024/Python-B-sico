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

for candidatoX in candidatosRegistro:
    nombre = candidatoX.get("nombre");
    experiencia = candidatoX.get("experiencia");
    escolaridad = candidatoX.get("escolaridad");
    #decision = método();

    rowcandidatoFormat = nombre.center(18)+" "+(str(experiencia)).center(10)+" "+(str(escolaridad)).center(17)+" "+(str("Rechazar")).center(14);
    print(rowcandidatoFormat);