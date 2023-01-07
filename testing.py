from datetime import date, datetime

#Obtener fecha y hora
fecha = date.today()
fechaFormato = fecha.strftime("%d/%m/%Y")
hora = datetime.now()
horaFormato = str(hora.strftime("%H:%M:%S"));
horaFormato = horaFormato[0:5];
print("ORAA: "+horaFormato);
