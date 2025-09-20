meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", 
         "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]

fecha = input("Ingresa una fecha (ejemplo: 9/8/1636 o Septiembre 8, 1636): ")

if "/" in fecha:
    partes = fecha.split("/")
    mes, dia, año = partes
else:
    partes = fecha.replace(",", "").split()
    mes_nombre = partes[0]
    mes = str(meses.index(mes_nombre) + 1)
    dia = partes[1]
    año = partes[2]

fecha_formato = f"{año}-{mes.zfill(2)}-{dia.zfill(2)}"
print(fecha_formato)