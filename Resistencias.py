# Casos de prueba
# res1 = 25; res2 = 80; res3 = 120;

res1 = int(input("Valor de la resistencia 1: "));
res2 = int(input("Valor de la resistencia 2: "));
res3 = int(input("Valor de la resistencia 3: "));

def calcularResComb(p_res1, p_res2, p_res3):
    resComb = 1/((1/p_res1)+(1/p_res2)+(1/p_res3))
    return resComb;

resFinal = calcularResComb(res1, res2, res3);
resFinalRounded = ("%.2f" % resFinal);

row1Format = "REPORTE DE RESISTENCIAS COMBINADAS";
print(row1Format.center(67));
row2Format = "RESISTENCIA 1  RESISTENCIA 2  RESISTENCIA 3  RESISTENCIA COMBINADA";
print(row2Format.center(67));
row3Format = str(res1).center(15)+str(res2).center(15)+str(res3).center(15)+str(resFinalRounded).center(21);
print(row3Format);